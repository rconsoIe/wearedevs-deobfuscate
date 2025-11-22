import re
import sys
import os

def solve_expr(expr):
    try:
        return eval(expr)
    except Exception as e:
        return 0

def decode_lua_string(s):
    def repl(m):
        if m.group(1): return chr(int(m.group(1)))
        return m.group(0)
    s = re.sub(r'\\(\d{1,3})', repl, s)
    escapes = {
        r'\n': '\n', r'\r': '\r', r'\t': '\t', r'\\': '\\', r'\"': '"', r"\'": "'", r'\0': '\0'
    }
    for k, v in escapes.items():
        s = s.replace(k, v)
    return s

def extract_strings_from_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='latin1') as f:
        content = f.read()

    # 1. Identify the main table variable name
    # Look for local var = { string, string, ... }
    # We expect the file to start with return(function(...)
    
    match_func = re.search(r'return\s*\(\s*function\s*\(\s*\.\.\.\s*\)', content)
    if not match_func:
        print("  Not a standard WeAreDevs obfuscated script (missing outer wrapper)")
        return

    start_idx = match_func.end()
    search_area = content[start_idx:start_idx+2000] # Look in the beginning

    # Find local VAR = {
    match_table_def = re.search(r'local\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\{', search_area)
    if not match_table_def:
        print("  Could not find string table definition")
        return

    table_var = match_table_def.group(1)
    print(f"  Table variable: {table_var}")

    # Extract the content of the table. It ends with }
    # Since strings can contain }, we need to be careful.
    # But usually the structure is local T = { "...", "..." }
    # We can parse valid lua strings until we hit a } that is not inside a string.
    
    # Let's find the start of the table content in 'content'
    table_start_idx = content.find('{', start_idx) + 1
    
    # Scanner to extract strings
    strings = []
    pos = table_start_idx
    
    while pos < len(content):
        # Skip whitespace
        while pos < len(content) and content[pos].isspace():
            pos += 1
        if pos >= len(content): break
        
        if content[pos] == '}':
            break # End of table
            
        if content[pos] == '"' or content[pos] == "'":
            quote = content[pos]
            # Parse string
            end_quote = pos + 1
            while end_quote < len(content):
                if content[end_quote] == quote and content[end_quote-1] != '\\':
                    break
                # Handle escaped backslash like \\"
                if content[end_quote] == quote and content[end_quote-1] == '\\':
                     # Check if it is actually escaped. \\" -> backslash then quote.
                     # Count backslashes
                     bk = 1
                     while content[end_quote - 1 - bk] == '\\':
                         bk += 1
                     if bk % 2 == 0: # even number of backslashes means quote is escaped
                         pass # continue
                     else:
                         break # end of string
                end_quote += 1
            
            str_content = content[pos+1:end_quote]
            strings.append(decode_lua_string(str_content))
            pos = end_quote + 1
            
            # Skip comma or semicolon
            while pos < len(content) and (content[pos].isspace() or content[pos] in ',;'):
                pos += 1
        else:
            # Maybe number or something else? Obfuscator usually puts strings.
            # Or empty string ""
            pos += 1

    print(f"  Found {len(strings)} encoded strings.")

    # 2. Extract shuffle loop
    # for I,l in ipairs({...})do
    # Use regex to find ipairs({...})
    # Note: variable names in loop might change.
    # for VAR1, VAR2 in ipairs
    
    match_shuffle = re.search(r'for\s+([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s+in\s+ipairs\s*\(\s*\{(.*?)\}\s*\)\s*do', content, re.DOTALL)
    if not match_shuffle:
        print("  Could not find shuffle loop")
        return

    shuffle_content = match_shuffle.group(3)
    
    pairs = []
    # extract pairs {expr; expr} or {expr, expr}
    for m in re.finditer(r'\{([^}]+)\}', shuffle_content):
        pair_str = m.group(1)
        parts = re.split(r'[;,]', pair_str)
        if len(parts) >= 2:
            s_val = solve_expr(parts[0])
            e_val = solve_expr(parts[1])
            pairs.append((s_val, e_val))
            
    # Apply shuffle
    for start, end in pairs:
        s = start - 1
        e = end - 1
        while s < e:
            if s < len(strings) and e < len(strings):
                strings[s], strings[e] = strings[e], strings[s]
            s += 1
            e -= 1

    # 3. Find Accessor Function to get offset
    # local function I(I)return D[I-(-80373-(-130783))]end
    # Pattern: local function VAR(ARG) return TABLE[ARG - (EXPR)] end
    # Or TABLE[ARG + (EXPR)]
    
    # Construct regex with table_var
    pattern_accessor = r'local\s+function\s+([a-zA-Z0-9_]+)\s*\([a-zA-Z0-9_]+\)\s*return\s+' + re.escape(table_var) + r'\[[a-zA-Z0-9_]+\s*([+\-])\s*\((.*?)\)\]\s*end'
    match_acc = re.search(pattern_accessor, content)
    
    offset = 0
    if match_acc:
        sign = match_acc.group(2)
        expr = match_acc.group(3)
        val = solve_expr(expr)
        if sign == '-':
            offset = val
        else:
            offset = -val
        # The lua code: D[I - offset].
        # strings[I - offset - 1] (0-based)
        # Usually the decrypt loop uses 1-based index iteration on strings table?
        # Let's check the loop.
    else:
        print("  Could not find accessor function offset. Assuming 0.")
    
    # 4. Extract Base64 Map
    # do local I=string.len local l={...}
    # The map variable is usually `l` or something else.
    # It is inside a `do ... end` block that contains the decrypt loop.
    
    # Find `do` block after the shuffle loop
    # Inside, there is `local [map] = { ... }`
    # And `for ... do ... end` loop
    
    match_do = re.search(r'do\s+local\s+[a-zA-Z0-9_]+\s*=\s*table\.concat', content)
    if not match_do:
        # Try another signature: `local function` definition of len?
        # `do local I=string.len`
        match_do = re.search(r'do\s+local\s+[a-zA-Z0-9_]+\s*=\s*string\.len', content)
        
    if match_do:
        # Search forward for map table
        start_do = match_do.start()
        search_area_do = content[start_do:start_do+5000]
        
        # local l = { ... }
        # We need to find the table that contains keys like "\054" or "e".
        # It's likely the first table defined in this block.
        match_map = re.search(r'local\s+([a-zA-Z0-9_]+)\s*=\s*\{', search_area_do)
        if match_map:
             map_var = match_map.group(1)
             # extract content
             map_start = search_area_do.find('{', match_map.end() - 1) + 1
             # find matching }
             # rudimentary parser
             cnt = 1
             map_end = map_start
             while map_end < len(search_area_do) and cnt > 0:
                 if search_area_do[map_end] == '{': cnt += 1
                 if search_area_do[map_end] == '}': cnt -= 1
                 map_end += 1
             map_content = search_area_do[map_start:map_end-1]
             
             # Parse map
             base64_map = {}
             # keys: ["..."] or var
             # values: expr
             # We can split by , or ;
             # But careful about expressions.
             # Using same scanner logic as before but adapted.
             
             pos = 0
             while pos < len(map_content):
                while pos < len(map_content) and map_content[pos].isspace(): pos += 1
                if pos >= len(map_content): break
                
                key = None
                if map_content[pos] == '[':
                    end_bracket = map_content.find(']', pos)
                    if end_bracket == -1: break
                    key_str = map_content[pos+1:end_bracket].strip('"')
                    key = decode_lua_string(key_str)
                    pos = end_bracket + 1
                else:
                    match_k = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)', map_content[pos:])
                    if match_k:
                        key = match_k.group(1)
                        pos += len(key)
                    else:
                        pos += 1
                        continue
                
                while pos < len(map_content) and (map_content[pos].isspace() or map_content[pos] == '='):
                    pos += 1
                
                # Value
                end_val = pos
                while end_val < len(map_content) and map_content[end_val] not in ',;}':
                    end_val += 1
                
                val_expr = map_content[pos:end_val]
                val = solve_expr(val_expr)
                base64_map[key] = val
                pos = end_val + 1
             
             # Verify we got a good map
             if len(base64_map) > 10:
                 # Decrypt
                 decoded_strings = []
                 for s_enc in strings:
                     if not s_enc or not isinstance(s_enc, str):
                         decoded_strings.append("")
                         continue
                     
                     # Verify it looks like "string"
                     # The obfuscator checks type(W)=="string"
                     # But we only extracted strings.
                     
                     res_bytes = bytearray()
                     a = 0
                     s = 0
                     for char in s_enc:
                         if char in base64_map:
                             val = base64_map[char]
                             a += val * (64**(3-s))
                             s += 1
                             if s == 4:
                                 b1 = (a >> 16) & 0xFF
                                 b2 = (a >> 8) & 0xFF
                                 b3 = a & 0xFF
                                 res_bytes.append(b1)
                                 res_bytes.append(b2)
                                 res_bytes.append(b3)
                                 a = 0
                                 s = 0
                         elif char == '=':
                             b1 = (a >> 16) & 0xFF
                             res_bytes.append(b1)
                             if s == 3:
                                 b2 = (a >> 8) & 0xFF
                                 res_bytes.append(b2)
                             break
                     
                     try:
                         decoded = res_bytes.decode('utf-8', errors='replace')
                         # Clean up null bytes if any?
                         decoded_strings.append(decoded)
                     except:
                         decoded_strings.append("<binary>")
                 
                 print("  Decrypted strings:")
                 for i, ds in enumerate(decoded_strings):
                     # Filter noise
                     if len(ds) > 3 and all(c.isprintable() for c in ds):
                         print(f"    [{i}] {ds}")
                     elif ds in ["game", "StarterGui", "SetCore", "Info", "Title", "Text", "Duration", "SendNotification"]:
                         print(f"    [{i}] {ds}")

             else:
                 print("  Failed to parse base64 map or map is too small")

def process_path(path):
    if os.path.isfile(path):
        extract_strings_from_file(path)
    elif os.path.isdir(path):
        for fname in os.listdir(path):
            if fname.endswith(".lua"):
                extract_strings_from_file(os.path.join(path, fname))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_path(sys.argv[1])
    else:
        print("Usage: python3 extract_strings.py <path>")

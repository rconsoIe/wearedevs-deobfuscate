import re
import sys
import os
import ast

def solve_expr(expr):
    """
    Safely evaluate a simple arithmetic expression.
    """
    try:
        expr = expr.strip()
        # Parse the expression into an AST
        node = ast.parse(expr, mode='eval')
        
        # Verify that the AST only contains safe nodes
        for subnode in ast.walk(node):
            if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp, 
                                        ast.Constant, ast.Num, ast.Add, ast.Sub, 
                                        ast.Mult, ast.Div, ast.Mod, ast.Pow, 
                                        ast.USub, ast.UAdd)):
                 # If we encounter anything unsafe (like Call, Attribute, Name, etc.), fail safely
                 return 0
        
        # Safe to evaluate using eval since we checked the structure,
        # but to be extra safe, we can limit the globals/locals.
        # Although ast.literal_eval is safer, it doesn't support operators.
        return eval(expr, {"__builtins__": None}, {})
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

def get_decrypted_strings(content):
    """
    Extract and decrypt strings from obfuscated Lua content.
    Returns a list of decrypted strings.
    """
    match_func = re.search(r'return\s*\(\s*function\s*\(\s*\.\.\.\s*\)', content)
    if not match_func:
        return []

    start_idx = match_func.end()
    search_area = content[start_idx:start_idx+2000]

    match_table_def = re.search(r'local\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\{', search_area)
    if not match_table_def:
        return []

    table_var = match_table_def.group(1)
    table_start_idx = content.find('{', start_idx) + 1
    
    strings = []
    pos = table_start_idx
    
    while pos < len(content):
        while pos < len(content) and content[pos].isspace():
            pos += 1
        if pos >= len(content): break
        
        if content[pos] == '}':
            break
            
        if content[pos] == '"' or content[pos] == "'":
            quote = content[pos]
            end_quote = pos + 1
            while end_quote < len(content):
                if content[end_quote] == quote and content[end_quote-1] != '\\':
                    break
                if content[end_quote] == quote and content[end_quote-1] == '\\':
                     bk = 1
                     while content[end_quote - 1 - bk] == '\\':
                         bk += 1
                     if bk % 2 == 0:
                         pass
                     else:
                         break
                end_quote += 1
            
            str_content = content[pos+1:end_quote]
            strings.append(decode_lua_string(str_content))
            pos = end_quote + 1
            
            while pos < len(content) and (content[pos].isspace() or content[pos] in ',;'):
                pos += 1
        else:
            pos += 1

    match_shuffle = re.search(r'for\s+([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s+in\s+ipairs\s*\(\s*\{(.*?)\}\s*\)\s*do', content, re.DOTALL)
    if not match_shuffle:
        return strings

    shuffle_content = match_shuffle.group(3)
    
    pairs = []
    for m in re.finditer(r'\{([^}]+)\}', shuffle_content):
        pair_str = m.group(1)
        parts = re.split(r'[;,]', pair_str)
        if len(parts) >= 2:
            s_val = solve_expr(parts[0])
            e_val = solve_expr(parts[1])
            pairs.append((s_val, e_val))
            
    for start, end in pairs:
        s = start - 1
        e = end - 1
        while s < e:
            if s < len(strings) and e < len(strings):
                strings[s], strings[e] = strings[e], strings[s]
            s += 1
            e -= 1

    # Look for the decoding block anchor (e.g., string.char, table.insert)
    match_anchor = re.search(r'local\s+[a-zA-Z0-9_]+\s*=\s*string\.char', content)
    if not match_anchor:
        match_anchor = re.search(r'local\s+[a-zA-Z0-9_]+\s*=\s*table\.insert', content)
        
    if match_anchor:
        start_do = match_anchor.start()
        search_area_do = content[start_do:start_do+8000] # Expanded search area
        
        # Find all table definitions in this area
        for match_map in re.finditer(r'local\s+([a-zA-Z0-9_]+)\s*=\s*\{', search_area_do):
             map_var = match_map.group(1)
             map_start = match_map.end() - 1 # Point to '{'
             
             # Extract table content
             cnt = 0
             map_end = map_start
             
             # Need to balance braces manually
             while map_end < len(search_area_do):
                 if search_area_do[map_end] == '{': cnt += 1
                 if search_area_do[map_end] == '}': cnt -= 1
                 if cnt == 0:
                     map_end += 1
                     break
                 map_end += 1
             
             map_content = search_area_do[map_start+1:map_end-1]
             
             base64_map = {}
             
             pos = 0
             valid_map = True
             while pos < len(map_content):
                while pos < len(map_content) and map_content[pos].isspace(): pos += 1
                if pos >= len(map_content): break
                
                key = None
                if map_content[pos] == '[':
                    end_bracket = map_content.find(']', pos)
                    if end_bracket == -1: 
                        valid_map = False
                        break
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
                
                end_val = pos
                while end_val < len(map_content) and map_content[end_val] not in ',;}':
                    end_val += 1
                
                val_expr = map_content[pos:end_val]
                val = solve_expr(val_expr)
                base64_map[key] = val
                pos = end_val + 1
             
             if valid_map and len(base64_map) > 50: # Base64 map should have around 64 entries
                 decoded_strings = []
                 for s_enc in strings:
                     if not s_enc or not isinstance(s_enc, str):
                         decoded_strings.append("")
                         continue
                     
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
                         decoded_strings.append(decoded)
                     except:
                         decoded_strings.append("<binary>")
                 
                 return decoded_strings

    return strings

def extract_strings_from_file(filepath):
    print(f"Credits: HUTAOSHUSBAND")
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='latin1') as f:
        content = f.read()

    decrypted = get_decrypted_strings(content)
    print(f"  Found {len(decrypted)} strings.")
    
    print("  Decrypted strings:")
    for i, ds in enumerate(decrypted):
        if len(ds) > 3 and all(c.isprintable() for c in ds):
            print(f"    [{i}] {ds}")
        elif ds in ["game", "StarterGui", "SetCore", "Info", "Title", "Text", "Duration", "SendNotification"]:
            print(f"    [{i}] {ds}")

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

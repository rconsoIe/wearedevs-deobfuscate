import os
import sys
import subprocess
import tempfile

def run_dumper(obfuscated_dir, tools_dir):
    dumper_template_path = os.path.join(tools_dir, "dumper.lua")
    if not os.path.exists(dumper_template_path):
        print(f"Error: {dumper_template_path} not found.")
        return

    # Read template as binary
    with open(dumper_template_path, 'rb') as f:
        template = f.read()

    files = [f for f in os.listdir(obfuscated_dir) if f.endswith(".lua")]
    files.sort()

    if not files:
        print(f"No .lua files found in {obfuscated_dir}")
        return

    print(f"Found {len(files)} lua files. Processing...")

    placeholder = b"-- PASTE YOUR OBFUSCATED SCRIPT HERE --"

    for fname in files:
        fpath = os.path.join(obfuscated_dir, fname)
        print(f"--- Processing {fname} ---")
        
        # Read obfuscated script as binary
        with open(fpath, 'rb') as f:
            obfuscated_content = f.read()
        
        # We need to ensure we don't break the Lua string delimiter `[[ ... ]]`
        # If the binary content contains `]]`, we need to change the delimiter in the template.
        
        # Find a safe delimiter
        level = 0
        while True:
            eq = b"=" * level
            # Lua delimiter: [=[ ... ]=]
            start_delim = b"[" + eq + b"["
            end_delim = b"]" + eq + b"]"
            if end_delim not in obfuscated_content:
                break
            level += 1
            
        # The template has `local OBFUSCATED_SCRIPT = [[` ... `]]`
        # We need to replace the whole block or just match the placeholder and surrounding brackets?
        # The template currently is:
        # local OBFUSCATED_SCRIPT = [[
        # -- PASTE YOUR OBFUSCATED SCRIPT HERE --
        # ]]
        
        # We can reconstruct the assignment line.
        # Find where OBFUSCATED_SCRIPT is defined.
        
        match_start = template.find(b"local OBFUSCATED_SCRIPT =")
        if match_start == -1:
            print("Template structure unexpected. Could not find OBFUSCATED_SCRIPT.")
            continue
            
        # Find the placeholder
        ph_start = template.find(placeholder)
        if ph_start == -1:
            print("Template structure unexpected. Could not find placeholder.")
            continue
            
        # We assume the template looks like: 
        # ... local OBFUSCATED_SCRIPT = [[ ... placeholder ... ]] ...
        
        # We will keep everything before `local OBFUSCATED_SCRIPT = `
        prefix = template[:match_start]
        
        # We will find the end of the Lua string after the placeholder.
        # It should be `]]`
        # But we need to be robust.
        # Let's just assume the placeholder is properly enclosed in the template and we replace the whole definition.
        
        # Let's search for the end of the assignment in the template.
        # It's hard to parse lua in binary without regex, but the template is simple.
        # It ends with `]]` followed usually by newline.
        
        # To be safe, let's just use string replacement on the placeholder IF `]]` is not in content.
        # If `]]` is in content, we need to replace the delimiters.
        
        if b"]]" not in obfuscated_content:
            # Simple case: just replace placeholder
            final_script = template.replace(placeholder, obfuscated_content)
        else:
            # Complex case: we need to replace the `[[` and `]]` in the template with `[=[` and `]=]`
            # Find the opening `[[` before placeholder
            open_bracket_pos = template.rfind(b"[[", 0, ph_start)
            # Find the closing `]]` after placeholder
            close_bracket_pos = template.find(b"]]", ph_start)
            
            if open_bracket_pos == -1 or close_bracket_pos == -1:
                print("Could not find delimiters in template.")
                continue
                
            # Construct new script
            # Prefix + `local OBFUSCATED_SCRIPT = ` + start_delim + content + end_delim + Suffix
            
            # Actually `local OBFUSCATED_SCRIPT = ` is before open_bracket_pos
            # So:
            part1 = template[:open_bracket_pos]
            part2 = template[close_bracket_pos+2:]
            
            final_script = part1 + start_delim + b"\n" + obfuscated_content + b"\n" + end_delim + part2

        # Write to temp file
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.lua', delete=False) as tmp:
            tmp.write(final_script)
            tmp_path = tmp.name
        
        try:
            # Run lua
            # capture_output handles bytes if we don't specify text=True, but we want text output for printing
            # However, if output contains garbage bytes, decoding might fail.
            # safe to use errors='replace'
            result = subprocess.run(['lua', tmp_path], capture_output=True)
            
            stdout = result.stdout.decode('utf-8', errors='replace')
            stderr = result.stderr.decode('utf-8', errors='replace')
            
            dumped_lines = []
            for line in stdout.splitlines():
                if "[DUMP]" in line:
                    print(line.replace("[DUMP] ", ""))
                    dumped_lines.append(line)
            
            if stderr:
                 # Check for errors
                 if "Error" in stderr or "stack traceback" in stderr:
                     print(f"Error output: {stderr}")
            
            if not dumped_lines and not stderr:
                print("(No SetCore calls intercepted)")
                
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        
        print("\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_dumper.py <obfuscated_dir>")
    else:
        # Assuming tools dir is where this script is
        tools_dir = os.path.dirname(os.path.abspath(__file__))
        run_dumper(sys.argv[1], tools_dir)

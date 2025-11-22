import os
import sys
import subprocess
import tempfile
import shutil
import time
import winsound
import base64

_a1 = base64.b64decode(b'TWFkZSBieQ==').decode()
_a2 = base64.b64decode(b'SFVUQU9TSFVTQkFORA==').decode()
_a3 = lambda: f"{_a1} {_a2}"
_verify_attr = lambda s: _a2.lower() in s.lower()

DUMPER_LUA_CONTENT = r"""
local OBFUSCATED_SCRIPT = [[
-- PASTE YOUR OBFUSCATED SCRIPT HERE --
]]

local LOG_CALLS = true

local RealEnv = getfenv()
local MockEnv = {}

local function Log(msg)
    for line in string.gmatch(msg, "[^\r\n]+") do
        print("[DUMP] " .. line)
    end
end

local function DebugLog(msg)
    print("[DEBUG] " .. msg)
end

local function FormatValue(val, depth)
    depth = depth or 0
    if depth > 2 then return "..." end
    
    if type(val) == "string" then
        return string.format("%q", val)
    elseif type(val) == "table" then
        return "{...}"
    elseif type(val) == "function" then
        return "function()"
    else
        return tostring(val)
    end
end

local function CreateProxy(name, path)
    local proxy = newproxy(true)
    local meta = getmetatable(proxy)
    
    meta.__index = function(t, k)
        local newPath = path .. "." .. tostring(k)
        
        if k == "StarterGui" and name == "game" then
            return CreateProxy("StarterGui", "game.StarterGui")
        end
        
        if k == "SetCore" then
            return function(self, method, args)
                if method == "SendNotification" then
                    local argsStr = "{"
                    if type(args) == "table" then
                        for ak, av in pairs(args) do
                            local valStr = tostring(av)
                            if type(av) == "string" then valStr = string.format("%q", av) end
                            argsStr = argsStr .. "\n    " .. tostring(ak) .. " = " .. valStr .. ";"
                        end
                    end
                    argsStr = argsStr .. "\n}"
                    Log(string.format('game.StarterGui:SetCore("SendNotification", %s)', argsStr))
                else
                    Log(string.format('%s:SetCore(%s, ...)', path, FormatValue(method)))
                end
            end
        end

        if RealEnv[k] then return RealEnv[k] end
        
        return CreateProxy(k, newPath)
    end
    
    meta.__newindex = function(t, k, v)
    end
    
    meta.__call = function(t, ...)
        local args = {...}
        return CreateProxy("Result", path .. "()")
    end
    
    meta.__tostring = function()
        return name
    end
    
    return proxy
end

local Bit32 = {}
function Bit32.band(a, b) return 0 end
function Bit32.bor(a, b) return 0 end
function Bit32.bxor(a, b) return 0 end
function Bit32.bnot(a) return 0 end
function Bit32.lshift(a, b) return 0 end
function Bit32.rshift(a, b) return 0 end

setmetatable(MockEnv, {
    __index = function(t, k)
        if k == "game" then return CreateProxy("game", "game") end
        if k == "script" then return CreateProxy("script", "script") end
        if k == "wait" then return function(n) end end
        if k == "spawn" then return function(f) f() end end
        if k == "delay" then return function(n, f) f() end end
        if k == "print" then return function(...) end end
        if k == "warn" then return function(...) end end
        if k == "bit" or k == "bit32" then return Bit32 end
        
        if RealEnv[k] then return RealEnv[k] end
        
        return nil
    end,
    __newindex = function(t, k, v)
        RealEnv[k] = v
    end
})

if not newproxy then
    function newproxy(u)
        local t = {}
        if u then
            local mt = {}
            setmetatable(t, mt)
        end
        return t
    end
end

local func, err = loadstring(OBFUSCATED_SCRIPT)
if func then
    setfenv(func, MockEnv)
    local status, err = pcall(func)
    if not status then
        print("Error running script: " .. tostring(err))
    end
else
    print("Failed to load script: " .. tostring(err))
end
"""

def beep():
    try:
        winsound.Beep(2000, 50)
    except:
        pass

def find_lua_executable():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        
    local_lua = os.path.join(base_path, "lua.exe")
    if os.path.exists(local_lua):
        return local_lua
        
    for cmd in ["lua5.1", "lua", "luajit"]:
        path = shutil.which(cmd)
        if path:
            return path
    return None

def _get_credit_line(idx=0):
    parts = [_a1, _a2]
    if not all(parts):
        return None
    return " ".join(parts)

def _display_credits(count=100):
    credit = _get_credit_line()
    if not credit or not _verify_attr(credit):
        return False
    for _ in range(count):
        print(credit)
    return True

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("file: ", end='', flush=True)
    try:
        target_path = input().strip()
    except EOFError:
        return

    if target_path.startswith('"') and target_path.endswith('"'):
        target_path = target_path[1:-1]
        
    if not os.path.exists(target_path):
        print("File not found!")
        time.sleep(3)
        return

    beep()

    lua_exec = find_lua_executable()
    if not lua_exec:
        print("Error: No Lua interpreter found. Please install lua5.1, lua, or luajit, or place lua.exe next to this executable.")
        time.sleep(5)
        return

    beep()

    template = DUMPER_LUA_CONTENT.encode('utf-8')
    
    try:
        with open(target_path, 'rb') as f:
            obfuscated_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        time.sleep(3)
        return

    beep()

    placeholder = b"-- PASTE YOUR OBFUSCATED SCRIPT HERE --"
    
    level = 0
    while True:
        eq = b"=" * level
        start_delim = b"[" + eq + b"["
        end_delim = b"]" + eq + b"]"
        if end_delim not in obfuscated_content:
            break
        level += 1
        
    match_start = template.find(b"local OBFUSCATED_SCRIPT =")
    ph_start = template.find(placeholder)
    
    if match_start == -1 or ph_start == -1:
        print("Internal Error: Template structure corrupted.")
        time.sleep(3)
        return

    if b"]]" not in obfuscated_content:
        final_script = template.replace(placeholder, obfuscated_content)
    else:
        open_bracket_pos = template.rfind(b"[[", 0, ph_start)
        close_bracket_pos = template.find(b"]]", ph_start)
        
        if open_bracket_pos == -1 or close_bracket_pos == -1:
            print("Internal Error: Could not find delimiters in template.")
            time.sleep(3)
            return
            
        part1 = template[:open_bracket_pos]
        part2 = template[close_bracket_pos+2:]
        
        final_script = part1 + start_delim + b"\n" + obfuscated_content + b"\n" + end_delim + part2

    beep()

    with tempfile.NamedTemporaryFile(mode='wb', suffix='.lua', delete=False) as tmp:
        tmp.write(final_script)
        tmp_path = tmp.name
    
    try:
        result = subprocess.run([lua_exec, tmp_path], capture_output=True)
        
        stdout = result.stdout.decode('utf-8', errors='replace')
        stderr = result.stderr.decode('utf-8', errors='replace')
        
        dumped_lines = []
        for line in stdout.splitlines():
            if "[DUMP]" in line:
                dumped_lines.append(line.replace("[DUMP] ", ""))
        
        if stderr:
             if "Error" in stderr or "stack traceback" in stderr:
                 print(f"Lua Error: {stderr}")
        
        if dumped_lines:
            base, ext = os.path.splitext(target_path)
            output_path = f"{base}_deobfuscated{ext}"
            
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write("\n".join(dumped_lines))
            
            print(f"Saved to {output_path}")
            beep()
        else:
            print("No deobfuscated content found.")
            
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    
    if not _display_credits(100):
        print(_a3())
    
    time.sleep(3)

if __name__ == "__main__":
    main()

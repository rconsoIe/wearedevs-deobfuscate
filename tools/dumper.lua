--[[
    WeAreDevs Deobfuscator / Dynamic Dumper
    Author: Jules
]]

local OBFUSCATED_SCRIPT = [[
-- PASTE YOUR OBFUSCATED SCRIPT HERE --
]]

-- Configuration
local LOG_CALLS = true

---------------------------------------------------------
-- Mock Environment Setup
---------------------------------------------------------

local RealEnv = getfenv()
local MockEnv = {}

local function Log(msg)
    -- Ensure every line starts with [DUMP] for easy parsing
    for line in string.gmatch(msg, "[^\r\n]+") do
        print("[DUMP] " .. line)
    end
end

local function DebugLog(msg)
    print("[DEBUG] " .. msg)
end

-- Helper to format values
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
        
        -- Intercept specific Roblox services
        if k == "StarterGui" and name == "game" then
            return CreateProxy("StarterGui", "game.StarterGui")
        end
        
        if k == "SetCore" then
            return function(self, method, args)
                if method == "SendNotification" then
                    -- Format the args table nicely
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
        
        -- DebugLog("Accessing " .. newPath)
        return CreateProxy(k, newPath)
    end
    
    meta.__newindex = function(t, k, v)
        -- DebugLog("Setting " .. path .. "." .. tostring(k) .. " = " .. FormatValue(v))
    end
    
    meta.__call = function(t, ...)
        local args = {...}
        -- DebugLog("Calling " .. path .. " with " .. #args .. " args")
        return CreateProxy("Result", path .. "()")
    end
    
    meta.__tostring = function()
        return name
    end
    
    return proxy
end

-- Polyfill bit32/bit
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

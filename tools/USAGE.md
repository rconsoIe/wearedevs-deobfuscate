# WeAreDevs Deobfuscator Tools

This folder contains tools to help you deobfuscate and dump strings/code from Lua scripts obfuscated with WeAreDevs Obfuscator (v1.0.0).

## Tools

1.  **`dumper.lua`**: A dynamic analysis tool written in Lua.
2.  **`extract_strings.py`**: A static analysis tool written in Python.

## Usage

### 1. Dynamic Dumper (`dumper.lua`)

This tool runs the obfuscated script in a mocked environment to intercept and log function calls, specifically `game.StarterGui:SetCore`.

**How to use:**

1.  Open `dumper.lua`.
2.  Copy the content of your obfuscated script.
3.  Paste it into the `OBFUSCATED_SCRIPT` variable inside `dumper.lua` (between `[[` and `]]`).
4.  Run `dumper.lua` using your preferred Lua executor (e.g., Roblox Studio, Synapse X, Krnl, or a standard Lua 5.1 interpreter).
5.  Check the console output. It will print dumped calls like:
    ```lua
    [DUMP] game.StarterGui:SetCore("SendNotification", {
        Title = "Info";
        Text = "Hallo, dies ist eine Notification!";
        Duration = 4;
    })
    ```

### 2. Static String Extractor (`extract_strings.py`)

This tool statically parses the obfuscated file and decrypts all strings found in the internal string table.

**How to use:**

1.  Ensure you have Python 3 installed.
2.  Run the script from the command line, passing the path to the obfuscated lua file:
    ```bash
    python3 extract_strings.py path/to/obfuscated_script.lua
    ```
3.  The tool will output all decrypted strings found in the file.

## Note

The `dumper.lua` script mocks `game`, `script`, and other Roblox globals. If the obfuscated script uses other specific globals that are not mocked, you might need to add them to the `MockEnv` in `dumper.lua`.

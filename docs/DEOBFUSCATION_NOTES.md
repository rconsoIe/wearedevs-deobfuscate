# Deobfuscation Findings

## Obfuscation Structure

The WeAreDevs obfuscator (v1.0.0) generally follows this structure:

1.  **String Table**: A large table (e.g., `local D={...}`) containing encrypted strings.
2.  **Shuffle Loop**: A loop that shuffles the string table based on a seed or algorithm.
3.  **VM / Decryption Loop**: The main code logic is often wrapped in a VM-like structure or uses a custom string decryptor function (e.g., `local function I(I) ... end`).
4.  **Base64 Variant**: Strings are often encoded using a custom Base64-like scheme with a dynamic alphabet map.
5.  **Environment Checks**: Some scripts contain "Tamper Detected!" strings, suggesting they check the environment integrity (e.g., `getfenv`, `debug` library).

## Tools Developed

### 1. Dynamic Dumper (`tools/dumper.lua`)

This tool mocks the Roblox environment (`game`, `script`, `StarterGui`, etc.) and polyfills missing libraries (`bit32`). It successfully intercepts calls to `game.StarterGui:SetCore("SendNotification", ...)` and prints the arguments.

**Key Features:**
*   Mocks `game.StarterGui:SetCore`.
*   Polyfills `bit/bit32` (returning 0 for operations, which seems sufficient for these scripts to run without crashing, or at least reach the notification part).
*   Handles `[DUMP]` prefix for easy parsing by the runner.

### 2. Static Extractor (`tools/extract_strings.py`)

This tool attempts to statically parse the Lua file to find the string table, shuffle logic, and decryption keys. It works for some variants but is less robust than the dynamic dumper because the variable names and shuffling logic can vary.

### 3. CLI Runner (`tools/run_dumper.py`)

A Python script that automates the process of injecting obfuscated scripts into the `dumper.lua` template and running them with the system's `lua` interpreter. It handles multiline output from the dumper.

## Success Verification

The dynamic dumper has been verified against the provided test files and successfully extracts the expected notification strings:
*   "Hallo, dies ist eine Notification!"
*   "Etwas wurde erfolgreich geladen."
*   "Script wurde ausgeführt."
*   "Loader / Starte Module..."

## Future Work

*   **Complete VM Decompilation**: Writing a full decompiler for the custom bytecode/VM used by WeAreDevs would require analyzing the opcodes in the main loop.
*   **Robust Polyfills**: The current `bit` polyfill just returns 0. If the script relies on actual bitwise logic for control flow, this might cause incorrect behavior. Implementing a proper `bit` library in pure Lua would improve accuracy.

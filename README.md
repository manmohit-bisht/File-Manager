# Python CLI File Manager

A lightweight command-line file manager built in Python. It provides basic file and directory operations through a custom command system with support for command-specific flags.
This is made to mimic the basic operations of a terminal file manager the core idea is to make tag based sorting available in file manager with strict tree based directory structure.
## Features

- Navigate between directories
- List files and folders
- Sort directory listings
- Show hidden files
- Create and delete files
- Create and delete directories
- Rename files and directories
- Open/execute files
- Clear the terminal
- Custom command registry using decorators
- Command and flag validation

## Project Structure

```text
project/
│
├── main.py          # CLI entry point and input handling
├── commands.py      # File-management commands
├── registry.py      # Command registry and decorator
└── README.md
```

## How It Works

The project uses a command registry to keep commands modular.

Commands are registered using the `@command` decorator:

```python
@command("cd", allowed_flags=[])
def cd(arguments, allowed_flags):
    ...
```

The registry stores the command function and its supported flags. When the user enters a command, `main.py` tokenizes the input, separates arguments from flags, validates them, and executes the corresponding registered function. fileciteturn1file2L1-L9 fileciteturn1file1L9-L40

## Running the File Manager

The CLI is started using:

```bash
python main.py -start
```

or:

```bash
python main.py --myp
```

The program then waits for commands.

Type:

```text
exit
```

or:

```text
quit
```

to close the file manager. fileciteturn1file1L9-L18

> **Note:** The current implementation is configured for Windows and starts from the path defined in `main.py`.

---

# Commands

| Command | Syntax | Flags | Description |
|---|---|---|---|
| `cd` | `cd <path>` | — | Change the current directory |
| `listdir` | `listdir [path]` | `-full`, `-asc`, `-desc`, `-hidden` | List files and directories |
| `rename` | `rename <old> <new>` | — | Rename a file or directory |
| `execute` | `execute <path>` | — | Open/execute a file |
| `mkdir` | `mkdir <path>` | — | Create a directory |
| `mkfile` | `mkfile <path>` | — | Create a new file |
| `delfile` | `delfile <path>` | — | Delete a file |
| `deldir` | `deldir <path>` | `-all` | Delete a directory |
| `cls` | `cls` | — | Clear the terminal |

---

## Command Examples

### `cd`

Change the current working directory:

```bash
cd "C:\Users\manmo\Documents"
```

The command validates that the supplied path exists and is a directory. fileciteturn1file0L7-L33

### `listdir`

List the contents of the current directory:

```bash
listdir
```

List another directory:

```bash
listdir "C:\Users\manmo\Documents"
```

Available flags:

```bash
listdir -full
listdir -asc
listdir -desc
listdir -hidden
```

- `-full` → display full paths
- `-asc` → ascending order
- `-desc` → descending order
- `-hidden` → include hidden files/directories

`-asc` and `-desc` cannot be used together. fileciteturn1file0L36-L69

### `rename`

```bash
rename old.txt new.txt
```

Renames a file or directory.

### `execute`

```bash
execute "program.exe"
```

Opens a file using the operating system. The current implementation uses Windows `os.startfile()`. fileciteturn1file0L102-L122

### `mkdir`

```bash
mkdir "New Folder"
```

Creates a directory, including missing parent directories when necessary. fileciteturn1file0L125-L142

### `mkfile`

```bash
mkfile "notes.txt"
```

Creates a new empty file. fileciteturn1file0L145-L164

### `delfile`

```bash
delfile "notes.txt"
```

Deletes a file. fileciteturn1file0L167-L183

### `deldir`

Delete an empty directory:

```bash
deldir "Old Folder"
```

Delete a directory recursively:

```bash
deldir "Old Folder" -all
```

The `-all` option requires additional confirmation before recursively deleting the directory and its contents. fileciteturn1file0L186-L230

### `cls`

```bash
cls
```

Clears the terminal screen. fileciteturn1file0L233-L238

---

# Command Validation

Before executing a command, the CLI:

1. Tokenizes the user's input.
2. Separates arguments and flags.
3. Checks whether the command exists.
4. Checks whether supplied flags are supported.
5. Executes the registered command.

For example:

```text
listdir -asc
```

is parsed into:

```text
Command:  listdir
Argument: none
Flag:     -asc
```

This allows every command to define its own supported flags through the registry. fileciteturn1file1L18-L40

---

# Future Work

### Batch Processing with Multithreading

Add support for performing operations on multiple files simultaneously.

For example:

```text
batch rename ...
batch execute ...
batch delete ...
```

Multithreading could be used to process independent file operations concurrently, improving performance when working with large numbers of files.

### Tag-Based Sorting

Add a flexible tagging system that allows users to organize and filter files using custom tags rather than relying only on filename or directory structure.

For example:

```text
tag project report
tag important
tag college
```

Files could then be searched or sorted using their tags.

---

## Tech Stack

- **Python**
- `pathlib` — file and directory operations
- `argparse` — command-line argument handling
- `shlex` — command tokenization
- `os` — operating-system operations
- `shutil` — recursive directory deletion

## Current Limitations

- The current implementation is primarily designed for **Windows**.
- The starting directory is currently configured directly in `main.py`.
- The interface is command-line based.
- Batch processing is not implemented yet.
- Tag-based file organization is not implemented yet.

# Python CLI File Manager

A lightweight command-line file manager built in Python. The project provides a custom command-line interface for performing common file and directory operations such as navigating directories, listing files, creating and deleting files, renaming items, and opening files. Instead of relying on separate `if-else` blocks for every command, the project uses a command registry so that commands can be registered and handled in a modular way.

⚠️⚠️ I haven't changed the default directory right now it's set to-:
```
C:
```
Please change it to accordingly to your computer in main.py line 59.

ℹ️ℹ️ after compiling the program use following command to run it from anywhere:
```
myp -start
```
## Project Structure

```text
File Manager/
│
├── .git/
├── .venv/
├── myparser.egg-info/
│
├── src/
│   └── myparser/
│       ├── __pycache__/
│       ├── commands.py
│       ├── main.py
│       └── registry.py
│
├── myparser.egg-info/
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

`main.py` is responsible for starting the file manager, reading user input, tokenizing commands, separating arguments and flags, validating the input, and executing the corresponding command. The actual file-management operations are implemented in `commands.py`, while `registry.py` provides the command registry and decorator used to register each command. fileciteturn1file1L1-L6 fileciteturn1file2L1-L9

## How It Works

The project uses a registry-based command system. Each command is registered using the `@command` decorator along with the flags that the command supports. For example, `listdir` is registered with flags such as `-full`, `-asc`, `-desc`, and `-hidden`, while commands such as `cd` do not accept any flags. The registry stores both the command function and its supported flags so that the main program can look them up when a user enters a command. fileciteturn1file0L36-L40 fileciteturn1file2L4-L7

When the user enters a command, `main.py` tokenizes the input using `shlex`, separates normal arguments from flags, checks whether the command exists in the registry, validates the supplied flags, and finally calls the corresponding function. This keeps the command-processing logic separate from the actual file operations and makes it easier to add new commands later. fileciteturn1file1L9-L40

## Running the File Manager

The CLI can be started with:

```bash
python main.py -start
```

or:

```bash
python main.py --myp
```

Once started, the program displays the current working directory and waits for commands. Typing either `exit` or `quit` terminates the command loop. The current implementation changes the working directory to a path configured directly inside `main.py`, so that path should be adjusted for a different system. fileciteturn1file1L44-L63

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

## Command Usage

The `cd` command changes the current working directory. It accepts exactly one path and checks that the supplied path exists and refers to a directory before changing into it.

```bash
cd "C:\Users\manmo\Documents"
```

The `listdir` command displays the contents of the current directory, or of a directory supplied as an argument. It can also modify how the results are displayed through its supported flags. The `-full` flag prints the complete paths, `-asc` sorts the results in ascending order, `-desc` sorts them in descending order, and `-hidden` includes hidden files and directories. The `-asc` and `-desc` flags cannot be used together. fileciteturn1file0L36-L69

```bash
listdir
listdir "C:\Users\manmo\Documents"
listdir -full
listdir -asc
listdir -desc
listdir -hidden
```

The `rename` command changes the name or path of a file or directory. It requires both the existing path and the new path.

```bash
rename old.txt new.txt
```

The `execute` command opens a file using the operating system. In the current implementation, this is handled through Python's Windows-specific `os.startfile()` function.

```bash
execute "program.exe"
```

The `mkdir` command creates a new directory. The implementation uses `Path.mkdir()` with parent creation enabled, which allows missing parent directories to be created when required.

```bash
mkdir "New Folder"
```

The `mkfile` command creates a new empty file at the specified path. It uses `Path.touch()` and will report an error if the file already exists.

```bash
mkfile "notes.txt"
```

The `delfile` command removes a file from the file system. It checks for conditions such as a missing file or insufficient permissions and reports the corresponding error.

```bash
delfile "notes.txt"
```

The `deldir` command removes a directory. By default, it removes an empty directory using `rmdir()`. The optional `-all` flag enables recursive deletion using `shutil.rmtree()`, but the implementation asks the user for additional confirmation before carrying out the operation. fileciteturn1file0L186-L230

```bash
deldir "Old Folder"
deldir "Old Folder" -all
```

Finally, the `cls` command clears the terminal screen and does not accept any arguments or flags.

```bash
cls
```

## Command Validation

The file manager validates commands before execution. After tokenizing the input, it checks whether the entered command exists in `COMMAND_REGISTRY`. It then compares the supplied flags against the flags registered for that command. If an invalid command or unsupported flag is detected, the command is rejected instead of being executed. fileciteturn1file1L18-L40

This approach also makes the system extensible. A new command can be added by defining a function in `commands.py` and registering it with the `@command` decorator in the same way as the existing commands. fileciteturn1file0L7-L8

## Future Work

One planned improvement is **batch processing with multithreading**. Instead of processing one file operation at a time, the file manager could accept a group of files and perform independent operations concurrently. This could be particularly useful when processing large numbers of files, where multiple operations can be handled at the same time.

Another planned feature is **tag-based sorting**. The current `listdir` command mainly works with directory structure and alphabetical sorting, but a tagging system could allow files to be associated with custom categories such as `project`, `college`, `important`, or `documents`. Users could then filter or organize files based on those tags, providing a more flexible way of managing files.

## Tech Stack

The project is written in **Python** and uses `pathlib` for file and directory operations, `argparse` for command-line startup options, `shlex` for parsing user input, `os` for operating-system operations, and `shutil` for recursive directory deletion.

## Current Limitations

The current implementation is primarily designed for Windows because the `execute` command uses `os.startfile()`, and the initial working directory is currently hard-coded in `main.py`. The file manager is also entirely command-line based, and features such as batch processing and tag-based organization are planned for future versions.

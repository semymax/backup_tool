# Backup Tool

This is a simple backup tool written in Python, using `tar` for archiving,
`zstandard` for compression, and optionally `rclone` to upload backups to a
cloud provider.

`rclone` must be installed and configured separately in order to be used.
More information is available on the
[rclone official website](https://rclone.org/).

---

## Features

- Backups using `tar`
- Compression using the Zstandard algorithm via the
  [python-zstandard library](https://python-zstandard.readthedocs.io/en/stable/)
- Command Line Interface (CLI) built with
  [Click](https://click.palletsprojects.com/en/stable/)
- Optional upload to cloud storage using `rclone`

---

## Requirements

This project depends on the following external libraries:

- `zstandard`
- `click`

### Virtual environment setup

It is recommended to run this project inside a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Safety Notes

At this point this is an unfinished tool, still in development and shouldn't be used as a safe tool for backups.
But if you still consider using it, it's recommendable to test restoring any backups before relying on it.
Always avoid running this tool as root, unless you know what you're doing.

## CLI (Command Line Interface)

This tool provides a CLI for creating and restoring backups.
`create`:

```md
python -m src.cli create [OPTIONS] [SOURCES]...

Options

-o, --output PATH            Output path (directory or file name)
-l, --level INTEGER RANGE    Compression level for the zstd algorithm [0–22]
                             (default: 3)
--rclone TEXT                Rclone destination (e.g. remote:backups)
-f, --force                  Overwrite output file if it already exists
--help                       Show this message and exit
```

`restore`:

```md
python -m src.cli restore [OPTIONS] BACKUP

Options:
  -o, --output PATH
  --no-checksum      Skip checksum verification
  -f, --force        Overwrite files in destination if they exist
  --help             Show this message and exit.
```

### Notes

When creating a backup:

- At least one source path must be provided.

- When `--rclone` is provided, the backup file is uploaded using the `rclone` CLI.

- If the output path does not include a file extension `.tar.zstd` willl be appended automatically.

In both cases:

- If the output file already exists and `--force` is not specified, the command will exit with an error.

### Examples

Create a backup of `/home/user/projects` and store it in `/home/user/backups`:

```bash
python -m src.cli create /home/user/projects \
  -o /home/user/backups/projects-backup.tar.zst
```

Create a backup and upload it to a cloud remote:

```bash
python -m src.cli create /home/user/projects \
  -o /home/user/backups/projects-backup \
  --rclone gdrive:backups
```

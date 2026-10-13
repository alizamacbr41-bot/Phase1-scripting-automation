# Phase 1 Internship — Scripting & Automation

Beginner-friendly Bash and Python projects focused on Linux system information and secure password generation.

## Projects

### 1. Linux System Information Tool

**File:** [`system_info.sh`](system_info.sh)

A Bash script that prints a concise report about the current Linux system.

**Features**
- Current date and time
- Hostname and operating-system details
- Kernel version and system architecture
- CPU information
- Memory usage
- Disk usage

**Requirements**
- Linux (Kali Linux or another compatible distribution)
- Bash and standard utilities such as `uname`, `df`, and `free`

**Run**
```bash
bash system_info.sh
```

### 2. Secure Password Generator

**File:** [`password_generator.py`](password_generator.py)

A command-line Python script that generates passwords using Python's `secrets` module.

**Features**
- Default password length of 16 characters
- Custom lengths from 8 to 128 characters
- Uses lowercase and uppercase letters, digits, and special characters
- Command-line help

**Requirements**
- Python 3
- No third-party packages required

**Run**
Generate a password with the default length:
```bash
python3 password_generator.py
```

Generate a 24-character password:
```bash
python3 password_generator.py --length 24
```

View available options:
```bash
python3 password_generator.py --help
```

## Screenshots

The screenshot files currently present in this repository appear to be incomplete, so they need to be uploaded again as valid image files before they can display correctly here.

- System information output: replace `system_info_output.jpg` with the actual terminal screenshot.
- Password generator output: replace `passwort_generator_output.png` with the actual terminal screenshot. The filename can optionally be corrected to `password_generator_output.png`, as long as the README path is updated to match.

After uploading valid screenshots, embed them here using the exact repository filenames, for example:

```markdown
![System information tool output](system_info_output.jpg)
![Password generator output](password_generator_output.png)
```

## Notes

- Output varies depending on the Linux system and available utilities.
- Generated passwords should be stored securely and never shared publicly.
- Do not include real passwords or other sensitive information in screenshots.
- These are learning projects and are not intended to replace full system-monitoring or password-management applications.

## Learning Objectives

- Practise Bash scripting and Linux command-line utilities
- Use Python modules and command-line arguments
- Generate random passwords using a security-focused standard-library module
- Document and organise small projects in GitHub

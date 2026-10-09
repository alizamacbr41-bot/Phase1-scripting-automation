Phase 1 Internship — Scripting & Automation

Overview

This repository contains two beginner-level scripting and automation projects developed using Bash and Python on Kali Linux.

Project 1: System Information Tool

File: "system_info.sh"

What it does

Displays useful information about the Linux system.

Features

- Displays the current date and time.
- Shows the hostname and operating system.
- Displays the kernel version and system architecture.
- Shows CPU information.
- Displays memory usage.
- Shows disk usage.

Technologies used

- Bash
- Linux command-line utilities

Requirements

- Kali Linux or another compatible Linux distribution
- Bash
- Standard Linux utilities such as "uname", "df", and "free"

Setup and execution

Open a terminal in the project directory and run:

bash system_info.sh

Expected output

The terminal displays a system information report containing operating system details, CPU information, memory usage, and disk usage.

Project 2: Secure Password Generator

File: "password_generator.py"

What it does

Generates random passwords using Python's "secrets" module.

Features

- Generates a password with a default length of 16 characters.
- Supports custom password lengths from 8 to 128 characters.
- Includes lowercase letters, uppercase letters, digits, and special characters.
- Uses Python's "secrets" module for secure random selection.
- Provides command-line help.

Technologies used

- Python 3
- "secrets"
- "string"
- "argparse"

Requirements

- Python 3
- No additional third-party packages required

Setup and execution

Generate a default password:

python3 password_generator.py

Generate a 24-character password:

python3 password_generator.py --length 24

Display available options:

python3 password_generator.py --help

Expected output

The program displays a generated password and its length. Do not publish real passwords in screenshots or documentation.

Screenshots

The repository includes screenshots demonstrating the tools running in the terminal:

- "system_info_output.png" — system information tool output.
- "password_generator_output.png" — password generator output.

Important notes and limitations

- System information depends on the Linux environment and available command-line utilities.
- The password generator accepts lengths from 8 to 128 characters.
- Generated passwords should be stored securely and not shared publicly.
- These projects demonstrate basic scripting and automation skills; they are not full system-monitoring or password-management applications.

Learning objectives

- Practice Bash scripting.
- Use Linux command-line utilities.
- Work with Python modules and command-line arguments.
- Generate random passwords securely.
- Document and organize projects using GitHub.

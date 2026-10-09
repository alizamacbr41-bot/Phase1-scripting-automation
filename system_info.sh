#!/usr/bin/env bash

# System Information Tool
# Displays basic Linux system information.

echo "===== SYSTEM INFORMATION REPORT ====="
echo "Date: $(date)"
echo "Hostname: $(hostname)"

echo
echo "===== OPERATING SYSTEM ====="
if [ -r /etc/os-release ]; then
    . /etc/os-release
    echo "${PRETTY_NAME:-Unknown Linux}"
else
    echo "Unknown Linux distribution"
fi

echo "Kernel: $(uname -r)"
echo "Architecture: $(uname -m)"

echo
echo "===== CPU INFORMATION ====="
if command -v lscpu >/dev/null 2>&1; then
    lscpu | grep -E '^(Model name|CPU\(s\)):' || true
fi

echo
echo "===== MEMORY INFORMATION ====="
free -h

echo
echo "===== DISK USAGE ====="
df -h

echo
echo "Report completed successfully."

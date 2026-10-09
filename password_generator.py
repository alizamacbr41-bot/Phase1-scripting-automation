#!/usr/bin/env python3

import argparse
import secrets
import string
import sys


def generate_password(length):
    if length < 8 or length > 128:
        raise ValueError("Length must be between 8 and 128.")

    categories = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+"
    ]

    password = [
        secrets.choice(category) for category in categories
    ]

    all_characters = "".join(categories)

    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure random password."
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Password length from 8 to 128 (default: 16)"
    )

    args = parser.parse_args()

    try:
        password = generate_password(args.length)
        print("Password generated successfully:")
        print(password)
        print(f"Password length: {len(password)}")
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

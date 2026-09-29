import subprocess
import re


def list_users():
    print("\n========== SYSTEM USERS ==========")

    with open("/etc/passwd", "r") as file:
        for line in file:
            username = line.split(":")[0]
            print(username)


def username_exists(username):
    with open("/etc/passwd", "r") as file:
        for line in file:
            existing_username = line.split(":")[0]

            if existing_username == username:
                return True

    return False


def create_user():
    username = input("Enter username to create: ").strip()

    # Check username format
    if not re.fullmatch(r"[a-z_][a-z0-9_-]*[$]?", username):
        print("Invalid username.")
        print("Use lowercase letters, numbers, '_' or '-'.")
        return

    # Check if user already exists
    if username_exists(username):
        print(f"User '{username}' already exists.")
        return

    try:
        subprocess.run(
            ["sudo", "useradd", "-m", username],
            check=True
        )

        print(f"User '{username}' created successfully.")

    except subprocess.CalledProcessError:
        print(f"Failed to create user '{username}'.")
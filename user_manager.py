import subprocess
import re
from logger import log_action


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

    if not re.fullmatch(r"[a-z_][a-z0-9_-]*[$]?", username):
        print("Invalid username.")
        print("Use lowercase letters, numbers, '_' or '-'.")
        return

    if username_exists(username):
        print(f"User '{username}' already exists.")
        return

    try:
        subprocess.run(
            ["sudo", "useradd", "-m", username],
            check=True
        )

        print(f"User '{username}' created successfully.")
        log_action(f"Created user '{username}'")

    except subprocess.CalledProcessError:
        print(f"Failed to create user '{username}'.")


def delete_user():
    username = input("Enter username to delete: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if not username_exists(username):
        print(f"User '{username}' does not exist.")
        return

    if username == "root":
        print("You cannot delete the root user.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{username}'? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("User deletion cancelled.")
        return

    try:
        subprocess.run(
            ["sudo", "userdel", username],
            check=True
        )

        print(f"User '{username}' deleted successfully.")
        log_action(f"Deleted user '{username}'")

    except subprocess.CalledProcessError:
        print(f"Failed to delete user '{username}'.")
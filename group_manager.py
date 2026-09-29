import subprocess
import re
from logger import log_action


def group_exists(group_name):
    with open("/etc/group", "r") as file:
        for line in file:
            existing_group = line.split(":")[0]

            if existing_group == group_name:
                return True

    return False


def user_exists(username):
    with open("/etc/passwd", "r") as file:
        for line in file:
            existing_user = line.split(":")[0]

            if existing_user == username:
                return True

    return False


def list_groups():
    print("\n========== SYSTEM GROUPS ==========")

    with open("/etc/group", "r") as file:
        for line in file:
            group_name = line.split(":")[0]
            print(group_name)


def create_group():
    group_name = input("Enter group name to create: ").strip()

    if not re.fullmatch(r"[a-z_][a-z0-9_-]*[$]?", group_name):
        print("Invalid group name.")
        print("Use lowercase letters, numbers, '_' or '-'.")
        return

    if group_exists(group_name):
        print(f"Group '{group_name}' already exists.")
        return

    try:
        subprocess.run(
            ["sudo", "groupadd", group_name],
            check=True
        )

        print(f"Group '{group_name}' created successfully.")
        log_action(f"Created group '{group_name}'")

    except subprocess.CalledProcessError:
        print(f"Failed to create group '{group_name}'.")


def delete_group():
    group_name = input("Enter group name to delete: ").strip()

    if not group_name:
        print("Group name cannot be empty.")
        return

    if not group_exists(group_name):
        print(f"Group '{group_name}' does not exist.")
        return

    protected_groups = {
        "root",
        "sudo",
        "adm",
        "users",
        "wheel",
        "docker"
    }

    if group_name in protected_groups:
        print(f"You cannot delete the protected group '{group_name}'.")
        return

    confirmation = input(
        f"Are you sure you want to delete group '{group_name}'? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Group deletion cancelled.")
        return

    try:
        subprocess.run(
            ["sudo", "groupdel", group_name],
            check=True
        )

        print(f"Group '{group_name}' deleted successfully.")
        log_action(f"Deleted group '{group_name}'")

    except subprocess.CalledProcessError:
        print(f"Failed to delete group '{group_name}'.")


def add_user_to_group():
    username = input("Enter username: ").strip()
    group_name = input("Enter group name: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if not group_name:
        print("Group name cannot be empty.")
        return

    if not user_exists(username):
        print(f"User '{username}' does not exist.")
        return

    if not group_exists(group_name):
        print(f"Group '{group_name}' does not exist.")
        return

    try:
        subprocess.run(
            ["sudo", "usermod", "-aG", group_name, username],
            check=True
        )

        print(
            f"User '{username}' added to group "
            f"'{group_name}' successfully."
        )

        log_action(
            f"Added user '{username}' to group '{group_name}'"
        )

    except subprocess.CalledProcessError:
        print(
            f"Failed to add '{username}' to group "
            f"'{group_name}'."
        )
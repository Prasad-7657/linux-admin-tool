import os
import stat


def get_permission_string(file_path):
    try:
        file_stat = os.stat(file_path)
        permissions = stat.filemode(file_stat.st_mode)

        return permissions

    except FileNotFoundError:
        print(f"File or directory '{file_path}' does not exist.")
        return None

    except PermissionError:
        print(f"Permission denied: '{file_path}'.")
        return None


def explain_permissions(permissions):
    if not permissions:
        return

    print("\n========== PERMISSION DETAILS ==========")
    print(f"Permission string: {permissions}")

    print("\nType:")

    if permissions[0] == "-":
        print("Regular file")
    elif permissions[0] == "d":
        print("Directory")
    elif permissions[0] == "l":
        print("Symbolic link")
    else:
        print("Other file type")

    print("\nOwner permissions:")
    print(f"Read    : {'Yes' if permissions[1] == 'r' else 'No'}")
    print(f"Write   : {'Yes' if permissions[2] == 'w' else 'No'}")
    print(f"Execute : {'Yes' if permissions[3] == 'x' else 'No'}")

    print("\nGroup permissions:")
    print(f"Read    : {'Yes' if permissions[4] == 'r' else 'No'}")
    print(f"Write   : {'Yes' if permissions[5] == 'w' else 'No'}")
    print(f"Execute : {'Yes' if permissions[6] == 'x' else 'No'}")

    print("\nOther permissions:")
    print(f"Read    : {'Yes' if permissions[7] == 'r' else 'No'}")
    print(f"Write   : {'Yes' if permissions[8] == 'w' else 'No'}")
    print(f"Execute : {'Yes' if permissions[9] == 'x' else 'No'}")


def check_file_permissions():
    file_path = input("Enter file or directory path: ").strip()

    if not file_path:
        print("Path cannot be empty.")
        return

    permissions = get_permission_string(file_path)

    if permissions:
        explain_permissions(permissions)

def change_file_permissions():
    file_path = input("Enter file or directory path: ").strip()

    if not file_path:
        print("Path cannot be empty.")
        return

    if not os.path.exists(file_path):
        print(f"'{file_path}' does not exist.")
        return

    permissions = input(
        "Enter permissions in numeric format (example: 755, 644, 700): "
    ).strip()

    if not permissions.isdigit() or len(permissions) != 3:
        print("Invalid permission format.")
        print("Use exactly three digits, such as 755 or 644.")
        return

    if any(digit not in "01234567" for digit in permissions):
        print("Invalid permissions.")
        print("Each digit must be between 0 and 7.")
        return

    print(f"\nYou are about to change:")
    print(f"Path        : {file_path}")
    print(f"Permissions : {permissions}")

    confirmation = input("Continue? (yes/no): ").strip().lower()

    if confirmation != "yes":
        print("Permission change cancelled.")
        return

    try:
        os.chmod(file_path, int(permissions, 8))

        print(
            f"Permissions for '{file_path}' "
            f"changed to {permissions}."
        )

    except PermissionError:
        print("Permission denied. You may need sudo privileges.")

    except OSError as error:
        print(f"Failed to change permissions: {error}")
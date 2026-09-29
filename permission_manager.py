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
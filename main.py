from user_manager import list_users, create_user, delete_user
from group_manager import (
    list_groups,
    create_group,
    delete_group,
    add_user_to_group
)
from user_info import get_user_info
from permission_manager import (
    check_file_permissions,
    change_file_permissions
)


def show_menu():
    print("\n" + "=" * 45)
    print("              LINUX ADMIN TOOL")
    print("=" * 45)

    print("\nUSER MANAGEMENT")
    print("  1. List users")
    print("  2. Create user")
    print("  3. Delete user")
    print("  4. Check user information")

    print("\nGROUP MANAGEMENT")
    print("  5. List groups")
    print("  6. Create group")
    print("  7. Delete group")
    print("  8. Add user to group")

    print("\nPERMISSION MANAGEMENT")
    print("  9. Check file permissions")
    print(" 10. Change file permissions")

    print("\n  0. Exit")
    print("=" * 45)


def main():
    while True:
        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("\nExiting Linux Admin Tool...")
            break

        elif choice == "1":
            list_users()

        elif choice == "2":
            create_user()

        elif choice == "3":
            delete_user()

        elif choice == "4":
            get_user_info()

        elif choice == "5":
            list_groups()

        elif choice == "6":
            create_group()

        elif choice == "7":
            delete_group()

        elif choice == "8":
            add_user_to_group()

        elif choice == "9":
            check_file_permissions()

        elif choice == "10":
            change_file_permissions()

        else:
            print("\nInvalid option.")
            print("Please choose a number between 0 and 10.")


if __name__ == "__main__":
    main()
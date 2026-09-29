from user_manager import list_users, create_user, delete_user
from group_manager import (
    list_groups,
    create_group,
    delete_group,
    add_user_to_group
)


def show_menu():
    print("\n================================")
    print("        LINUX ADMIN TOOL")
    print("================================")
    print("1. List users")
    print("2. Create user")
    print("3. Delete user")
    print("4. List groups")
    print("5. Create group")
    print("6. Delete group")
    print("7. Add user to group")
    print("8. Check user information")
    print("9. Check file permissions")
    print("10. Change file permissions")
    print("0. Exit")


while True:
    show_menu()

    choice = input("\nEnter your choice: ").strip()

    if choice == "0":
        print("Exiting...")
        break

    elif choice == "1":
        list_users()

    elif choice == "2":
        create_user()

    elif choice == "3":
        delete_user()

    elif choice == "4":
        list_groups()

    elif choice == "5":
        create_group()

    elif choice == "6":
        delete_group()
        
    elif choice == "7":
        add_user_to_group()

    else:
        print("That option is not implemented yet.")
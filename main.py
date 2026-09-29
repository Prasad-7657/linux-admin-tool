def show_menu():
    print("\n================================")
    print("        LINUX ADMIN TOOL")
    print("================================")
    print("1. List users")
    print("2. Create user")
    print("3. Delete user")
    print("4. List groups")
    print("5. Create group")
    print("6. Add user to group")
    print("7. Check user information")
    print("8. Check file permissions")
    print("9. Change file permissions")
    print("0. Exit")


while True:
    show_menu()

    choice = input("\nEnter your choice: ")

    if choice == "0":
        print("Exiting...")
        break

    print(f"You selected option {choice}")
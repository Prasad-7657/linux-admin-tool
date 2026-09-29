def list_users():
    print("\n========== SYSTEM USERS ==========")

    with open("/etc/passwd", "r") as file:
        for line in file:
            username = line.split(":")[0]
            print(username)
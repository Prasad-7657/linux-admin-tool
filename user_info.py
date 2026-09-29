import subprocess


def user_exists(username):
    result = subprocess.run(
        ["id", username],
        capture_output=True,
        text=True
    )

    return result.returncode == 0


def get_user_info():
    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if not user_exists(username):
        print(f"User '{username}' does not exist.")
        return

    print(f"\n========== USER INFORMATION: {username} ==========")

    try:
        result = subprocess.run(
            ["id", username],
            capture_output=True,
            text=True,
            check=True
        )

        print("\nIdentity:")
        print(result.stdout.strip())

        result = subprocess.run(
            ["getent", "passwd", username],
            capture_output=True,
            text=True,
            check=True
        )

        passwd_data = result.stdout.strip().split(":")

        if len(passwd_data) >= 7:
            print("\nAccount Information:")
            print(f"Username       : {passwd_data[0]}")
            print(f"UID            : {passwd_data[2]}")
            print(f"Primary GID    : {passwd_data[3]}")
            print(f"Description    : {passwd_data[4]}")
            print(f"Home Directory : {passwd_data[5]}")
            print(f"Login Shell    : {passwd_data[6]}")

        result = subprocess.run(
            ["groups", username],
            capture_output=True,
            text=True,
            check=True
        )

        print("\nGroups:")
        print(result.stdout.strip())

    except subprocess.CalledProcessError:
        print("Unable to retrieve user information.")
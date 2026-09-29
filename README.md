# 🐧 Linux Admin Tool

A basic and beginner-friendly command-line tool for managing Linux users, groups, and file permissions using Python.

The project is designed to help understand Linux administration concepts while learning Python system automation.

---

## 🚀 Features

### 👤 User Management

- List system users
- Create Linux users
- Delete Linux users
- Validate usernames
- Prevent deletion of the root account
- Display detailed user information

### 👥 Group Management

- List system groups
- Create groups
- Delete groups
- Add users to groups
- Protect important system groups

### 🔐 Permission Management

- Check file and directory permissions
- Explain Linux permission strings
- Change permissions using numeric modes
- Support common modes such as `755`, `644`, and `600`

---

## 🛠️ Technologies

- Python 3
- Linux
- Git
- GitHub
- Linux system utilities

Python modules used:

- `subprocess`
- `os`
- `stat`
- `re`

No external Python packages are currently required.

---

## 📁 Project Structure

```text
linux-admin-tool/
│
├── main.py
├── user_manager.py
├── group_manager.py
├── user_info.py
├── permission_manager.py
│
├── README.md
├── requirements.txt
└── .gitignore
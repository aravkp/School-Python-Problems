def login(username="Admin"):
    password = input("Enter password: ")
    if username == "Admin" and password == "password":
        print("Login successful!")
    else:
        print("Invalid username or password.")

login()


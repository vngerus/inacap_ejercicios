userSave = "admin"
userPass = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

# using while loop to validate user credentials if not correct just fix the error, i mean if you mistake the username or password just fix it and try again
while True:
    if userSave == username and password == userPass:
        print("Welcome to your account!")
        break
    elif userSave != username:
        print("Incorrect username, please try again.")
        userSave = input("Enter username: ")
    elif password != userPass:
        print("Incorrect password, please try again.")
        password = input("Enter password: ")

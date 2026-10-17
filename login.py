
password = "meowmeow"
logged_in = False

while logged_in == False:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Logged in")
        logged_in = True
    else:
        print("Wrong password. Try again.")
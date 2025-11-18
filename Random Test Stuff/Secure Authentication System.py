def Hash(password):
    n = ""
    for i in password:
        n += chr(ord(i)*5)
    return(n)

CorrectUsername = "ŅǴȡȍȦ"
CorrectPassword = "ŅǴȡȍȦõúÿĄ"

Username = input("What is your username?\n")
Password = input("What is your password?\n")

if(Username.isalnum() and Password.isalnum()):
    if(Hash(Username) == CorrectUsername and Hash(Password) == CorrectPassword):
        print("Access granted!")
    else:
        print("Access denied...")
else:
    print("Please only use alphanumeric characters.")
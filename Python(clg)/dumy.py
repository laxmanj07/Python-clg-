saved_usrname = input("Enter username: ")
saved_usrpassword = input("Enter password: ")
print("ID created successfully.")
print("Please login to continue.\n")

usrname = input("Enter username: ")
password = input("Enter password: ")

if usrname == saved_usrname and password == saved_usrpassword:
    print("Login successful")
    import random
    otp = random.randint(1000, 9999)
    print(f"Your OTP is: {otp}")
    attempts = 0
    while attempts < 3:
        user_otp = int(input("Enter OTP: "))
        if user_otp == otp:
            print("OTP verified. Access granted!")
            break
        else:
            attempts += 1
            if attempts == 3:
                print("Account blocked due to 3 incorrect OTP attempts.")
            else:
                print(f"Incorrect OTP. You have {3 - attempts} attempts left.")
elif usrname != saved_usrname and password != saved_usrpassword:
    print("Invalid username and password")
elif usrname != saved_usrname:
    print("Invalid username")
elif password != saved_usrpassword:
    print("Invalid password")
else:
    print("Login failed")

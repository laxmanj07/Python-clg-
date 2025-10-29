name_of_variable = 10
print(name_of_variable, id(name_of_variable))
name_of_variable = 20
print(name_of_variable, id(name_of_variable))

x=7
y=x
print(y+1, id(y))
print(x, id(x))
fname="Laxman"
print(fname[0])

# Conditional Statements using if
  #authenticate user using if statement

saved_usrname = input("enter username:")
saved_usrpassword = input("enter password:")
print("id created successfullty.")
print("please login to continue.")

usrname = input("enter username:")
password = input("enter password:")

if usrname == saved_usrname and password == saved_usrpassword:
    print("login successful")      
elif usrname != saved_usrname and password != saved_usrpassword:
        print("invalid password and username")
elif usrname != saved_usrname:
        print("invalid username")
elif password != saved_usrpassword:
        print("invalid password")
else:
        print("login failed")


    
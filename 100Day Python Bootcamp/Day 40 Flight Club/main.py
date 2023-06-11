import sheety

print("Welcome to Helen's Flight Club.\n We can find the best deal for you :)")
f_name = input("Please enter your first name: ")
l_name = input("Please enter your last name: ")
email1 = "e1"
email2 = "e2"

while email1 != email2:
    email1 = input("Please enter your email: ")
    email2 = input("Please enter your email again: ")
    if email1 != email2:
        print("Email do not match each other, please try again.")

print("Ok! We have your information on file!")
sheety.add_customer(f_name, l_name, email1)
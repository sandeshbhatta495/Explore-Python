#otp or code Genrator 
def menu():
    print("******************************")
    print("******************************")
    print("Welcome To OTP generation app")
    print("choose an option:")
    print("1.Want to generate code for facebook Login.")
    print("2.Want To genetrate code for Google Verification.")
    print("3.Want to Generate Code for Other Or Extra App verification")
    print("4.Exit This Program.")
    print("******************************")

    name=input("Enter Your Name:")

    def facebook():
        global name
        print(f"Welocme,{name} \n In Code Generator. ")
        print("you have chossen The Facebook Code Genetarion .")
        import random
        code= random.randint(100000,999999)
        print(f"Code for facebook,{code}\n")

    def google():
        global name
        import random
        code= random.randint(100000,999999)
        print(f"Code for google,{code}\n")


    def other():
        global name
        import random
        code= random.randint(100000,999999)
        print(f"Code for Other Apps ,{code}\n")


while True:
    menu()
    choice=int(input("Enter Your Choice(1-4):"))    

if choice == "1":
    facebook()

elif choice == "2":
    google()

elif choce =="3":
    other()

elif choice =="4":
    print("Exiting The Program Thank You For useing Our Product.")

else:
    print("Invalid choice!, Please Enter Valid Choice ")
    print("\n")


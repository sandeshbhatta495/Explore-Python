
#scissor paper And Rock Game 
#program
import random
item_list=["Scissor","Paper","Rock"]
name =input("Enter the name of player :")
user_choice = input("Enter your Choice(Scissor,paper,Rock)**choose any one:")
comp_choice=random.choice(item_list)
print(f"Users choice ={user_choice}\n Computer Choice ={comp_choice}")
    
def menu():
    global name
    print("****************")
    print(f"Welcome,{name} to Scissor ,Paper & Rock Game!")
    print("**************************************")
    print(" your Choice(Scissor,paper,Rock:)**choose any one.")
    print("1.Scissor")
    print("2.Paper ")
    print("3.Rock")
    print("4.I Dont want to play with You !")


    def scissor():
        print("You have chossen The Scissor.")

    def computer():
        import random
        comp_choice=random.choice(item_list)
        print(f"Computer Has Choseen ,{comp_choice}.") 

    def paper():
        print("You have Chossen the Paper.")

    def rock():
        print("You Have Chossen The Rock.")

def result():
     global user_choice
     global comp_choice

     #The condition for user both has same choices
     if comp_choice =="Scissor" and user_choice =="Scissor":
         print("Its Become Drawn.")

     elif comp_choice =="Paper" and user_choice =="Paper":
          print("Its Become Drawn.")

     elif comp_choice =="Rock" and user_choice =="Rock":
         print("Its Become Drawn.")

     # the Condition that computer choses scissor
     elif comp_choice =="Scisssor" and user_choice =="Paper":
          print("Its Become win goes to Bot.")
     elif comp_choice =="Scisssor" and user_choice =="Rock":
         print(f"Its Become  win Goes to {name}")
     #The Condition that computer chosse Paper
     elif comp_choice =="Paper" and user_choice =="Scissor":
         print(f"Its Become  win Goes to {name}")
   
     elif comp_choice =="Paper" and user_choice =="Rock":
         print("Its Become win goes to Bot.")

     #the condition That Computer Choose Rock
     elif comp_choice =="Rock" and user_choice =="Scissor":
         print("Its Become win goes to Bot.")
      
     elif comp_choice =="Rock" and user_choice =="Paper": 
         print(f"Its Become  win Goes to {name}")
         breakpoint
    
     else:
         print("Defult choice.")
         exit()
   
while True:
    result()
    print("\n")




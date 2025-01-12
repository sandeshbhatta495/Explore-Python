
#scissor paper And Rock Game 
#program
import random
user_score =0
comp_score =0
ties =0
name =input("Enter the name of player :")
comp_choice=random.choice(["Scissor","Paper","Rock"])
item_list=(["Scissor","Paper","Rock"])

def menu():
    global name
    print("****************")
    print(f"Welcome,{name} to Scissor ,Paper & Rock Game!")
    print("**************************************")
    print("User Have Three Coices.")
    print("Type Scissor,Paper,Rock(any one):")

def computer():
    global comp_choice
    print(f"Bot Has Choseen,{comp_choice}.") 

#in that condition where Users and Computer Chosse Same Element or s,p,r
def winner(user_choice,comp_choice):
    if user_choice == comp_choice:
     return"Ties"
    
    elif (user_choice =="scissor" and  comp_choice =="paper") or \
         (user_choice =="paper" and  comp_choice =="rock") or \
         (user_choice =="rock" and  comp_choice =="scissor"):#having users wins conditions respectively
         return "Human Wins."
    else:
       return "Bot Wins."

while True:
   user_choice = input("Enter or Type Scissor,Paper,Rock(any one):")  .lower()
   
   if user_choice == "exit":
      
      print("Thanks For Playing.My Games! ")
      print("Your Score Looks Like:")
      print(f"You score {user_score} points, Bot Score {comp_score} points,Ties become {ties} times")
      break
   elif user_choice not in item_list:
      print("Invalid Choice")
      
comp_choice =computer()
print(f"Bot Has Choosen :{comp_choice}")

result = winner(user_choice,comp_choice)
print (result)

if result =="Human Wins.":
   user_score +=1
elif result =="Bot Wins.":
   comp_score +=1
else:
    ties +=1


print("Current Scores:")
print(f"You Score {user_score} and Bot Score {comp_score}")
print("="*30)
menu()


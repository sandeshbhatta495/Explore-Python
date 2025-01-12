
import random
name=input("Enter The Name of The Player:")
choice_list=["scissor","paper","rock"]
user_choice=input("Enter Your Choice(scissor,paper,rock):")
comp_choice=random.choice(choice_list)


#The cndition for user both has same choices
if comp_choice =="scisssor" and user_choice =="Scissor":
    print("Its Become Drawn.")

elif comp_choice =="paper" and user_choice =="paper":
    print("Its Become Drawn.")

elif comp_choice =="rock" and user_choice =="rock":
    print("Its Become Drawn.")

# the Condition that computer choses scissor
elif comp_choice =="scisssor" and user_choice =="Paper":
    print("Its Become win goes to Bot.")
elif comp_choice =="scisssor" and user_choice =="Rock":
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
     print(f"Users choice ={user_choice}\n computer Choice ={comp_choice}")
     breakpoint
else:
    print("Defult choice.")
    exit()
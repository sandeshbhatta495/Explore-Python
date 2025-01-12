name = input("Enter your name: ")
age = int(input("Enter your age: ")) 

if age > 18:
    print(f"Congratulations, {name}! You are above 18!")
elif age == 18:
    print(f"Congrats, {name}! You just became 18!")
else:
    print(f"Oh no, {name}! You are less than 18.")

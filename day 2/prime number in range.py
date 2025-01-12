#prime Number in Range 
# Input the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Loop through the range
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):  # Iterate through each number in the range
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to √num
            if num % i == 0:  # If divisible, it's not prime
                is_prime = False
                break
        if is_prime:  # If no divisors are found, the number is prime
            print(num)



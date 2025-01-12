count = 0

while count < 10:
    count += 1
    if count == 5:
        continue  # Skip when count is 5
    if count == 8:
        break  # Stop the loop when count is 8
    print(count)

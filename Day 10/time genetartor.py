import time
from datetime import datetime

while True:
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Clear the terminal screen (optional)
    print("\033c", end="")  # Works on most terminals to clear the screen
    
    # Display the current time
    print("Current Time:", current_time)
    
    # Wait for 1 second before updating
    time.sleep(1)

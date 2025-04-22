import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"  # Format time as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("Time's up! 🚨")

# Timer Start
try:
    user_time = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_time)
except ValueError:
    print("Please enter a valid number.")

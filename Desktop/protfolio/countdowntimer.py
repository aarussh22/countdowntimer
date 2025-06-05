import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Time's Up!\n")

while True:
    try:
        t = int(input("Enter the time in seconds: "))
        if t == 0:
            print("Exiting countdown.")
            break
        countdown(t)
    except ValueError:
        print("Please enter a valid number.")

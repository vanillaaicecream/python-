import time

seconds = int(input("Enter seconds: "))

while seconds:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")

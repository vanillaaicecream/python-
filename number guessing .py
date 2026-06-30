import random

secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! Took {tries} tries")
        break

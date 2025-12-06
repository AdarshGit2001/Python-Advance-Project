import random

guess = random.randint(1, 100)

# print(guess)   # remove this to make the game real

Your_num = int(input("Guess the number between 1 - 100: "))

while True:
    if Your_num == guess:
        print("Correct! 🎉")
        break

    elif Your_num < guess:
        print("Try a larger number.")
        
    else:
        print("Try a smaller number.")

    Your_num = int(input("Guess again: "))

import random

user_wins = 0
computer_wins = 0
game_tie = 0

while True:
    user = int(input("Enter 1 for Rock, 2 for paper, 3 for scissor: "))
    computer = random.randint(1, 3)
    print("Computer chose ",computer)

    if (user not in [1, 2, 3]):
        print("Please enter a valid number to play!")
        continue

    if (user == computer):
        print("Its a tie!")
        game_tie +=1

    elif(user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2):
            print("You Win.")
            user_wins +=1

    else:
        print("Computer Wins.")
        computer_wins +=1

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print(f"Match got tie {game_tie} times.")
print("Good Bye")


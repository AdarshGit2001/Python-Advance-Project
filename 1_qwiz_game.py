print("Welcome to the qwiz")

play = input("Do you want to play?  ").lower()

if (play != "yes"):
    quit()

print("Okay. Lets Go...")

score = 0

answer = input("\nQ1. Name a laptop company that start with 'S': ").lower()
if answer == "samsung":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is Samsung")

answer = input("\nQ2. What is 'A' stands for in USA?  ").lower()
if answer == "america":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is America")

answer = input("\nQ3. Who is the third richest person in the world?  ").lower()
if answer == "larry page":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is Larry Page")

answer = input("\nQ4. What is the parent company of Google and Pixel Phones.  ").lower()
if answer == "alphabet":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is Alphabet.")

answer = input("\nQ5. Which is the largest cloud service provider in the World?  ").lower()
if answer == "aws":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is aws.")

answer = input("\nQ6. Which company has largest smartphone share in india?  ").lower()
if answer == "vivo":
    print("Correct. You got 1 point")
    score +=1
else:
    print("Wrong. The answer is Vivo.")

print("\n")
print("Great. " + str(score) + " Score")
print(f"Your Total scores are {score}\n")


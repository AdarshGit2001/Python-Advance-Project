print("Welcome to the qwiz")

play = input("Do you want to play?  ").lower()

if (play != "yes"):
    quit()

print("Okay. Lets Go...")

score = 0

questions = [
    ("Q1. Name a laptop company that start with 'S': ", "samsung"),
    ("Q2. What is 'A' stands for in USA?  ", "america"),
    ("Q3. Who is the third richest person in the world?  ", "larry page"),
    ("Q4. What is the parent company of Google and Pixel Phones.  ", "alphabet"),
    ("Q5. Which is the largest cloud service provider in the World?  ", "aws"),
    ("Q6. Which company has largest smartphone share in india?  ", "vivo")
]

for q, correct in questions:
    answer = input(q).lower()
    if answer == correct:
        print("Correct. You got 1 Point.")
        score +=1
    else:
        print(f"Wrong. The correct answer is {correct.capitalize()}.")

print("\nGreat Job.")
print(f"Your total score is {score}/{len(questions)}")


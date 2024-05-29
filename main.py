# Python quiz
# checks users enter yes (y) no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks users response, question
        # repeats if users don't  enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

# print instructions
def instructions():
    print('''
These are the instructions

This quiz is a Science related quiz and will ask you some basic knowledge question.

There 5 question and it will be a multiple answer quiz for example: A. 1 B. 2 C. 3 D. 4

This is what its gonna look like when you do the quiz

Good luck :)
    ''')


# these are the questions for the user
questions = ("How many elements are in the periodic table?: ",
             "Which animals lays the largest eggs?: ",
             "What is the most abundant gas in the atmosphere?: ",
             "How many bones are in the human body?: ",
             "which planet in the solar system is the hottest?: ")

# this is the mutliple choice for the user
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen ", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
# this is the answers for each question in order
answers = ("C", "D", "A", "A", "B",)
guesses = []
score: int = 0
question_num = 0
# Main Routine

# todo introduce the game, ask the user if they want to see the instructions

instructions_wanted = yes_no("do you want to read the instruction?")
# instructions coding
if instructions_wanted == "yes":
    instructions()

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
# End Quiz
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
# If you get all answers right you get 100% score
score = int (score / len (questions)* 100)
print(f"Your score is: {score}%")

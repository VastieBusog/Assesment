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

There 5 question and it will be a multiple answer quiz for example: 1. Mercury 2. Earth 3. Mars 3. Venus

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
options = (("1. 116", "2. 117", "3. 118", "4. 119"),
           ("1. Whale", "2. Crocodile", "3. Elephant", "4. Ostrich"),
           ("1. Nitrogen ", "2. Oxygen", "3. Carbon-Dioxide", "4. Hydrogen"),
           ("1. 206", "2. 207", "3. 208", "4. 209"),
           ("1. Mercury", "2. Venus", "3. Earth", "4. Mars"))
# this is the answers for each question in order
answers = ("3", "4", "1", "1", "2",)
guesses = []
score: int = 0
question_num = 0
# Main Routine


instructions_wanted = yes_no("do you want to read the instruction?")
# instructions coding
if instructions_wanted == "yes":
    instructions()

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (1, 2, 3, 4): ").upper()
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

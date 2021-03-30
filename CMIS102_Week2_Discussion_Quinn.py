# Import dependencies
import random
import time

# Define constants
PURPLE = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"
MAGIC_8_BALL_ANSWERS = [
    {"answer": "As I see it, yes.", "color": GREEN},
    {"answer": "Ask again later.", "color": YELLOW},
    {"answer": "Better not tell you now.", "color": YELLOW},
    {"answer": "Cannot predict now.", "color": YELLOW},
    {"answer": "Concentrate and ask again.", "color": YELLOW},
    {"answer": "Don’t count on it.", "color": RED},
    {"answer": "It is certain.", "color": GREEN},
    {"answer": "It is decidedly so.", "color": GREEN},
    {"answer": "Most likely.", "color": GREEN},
    {"answer": "My reply is no.", "color": RED},
    {"answer": "My sources say no.", "color": RED},
    {"answer": "Outlook not so good.", "color": RED},
    {"answer": "Outlook good.", "color": GREEN},
    {"answer": "Reply hazy, try again.", "color": YELLOW},
    {"answer": "Signs point to yes.", "color": GREEN},
    {"answer": "Very doubtful.", "color": RED},
    {"answer": "Without a doubt.", "color": GREEN},
    {"answer": "Yes.", "color": GREEN},
    {"answer": "Yes – definitely.", "color": GREEN},
    {"answer": "You may rely on it.", "color": GREEN}]

#Display welcome message
print(BOLD + PURPLE + "Welcome to the Virtual Magic 8 Ball" + END + "\n")

# Input name and question
name = input("What is your name? ")
question = input("What is your question? ")

# calculate number of loop iterations
iterate = len(name) + len(question)

# Ouput response
print("")
for i in range(iterate):
    n = random.randint(0, len(MAGIC_8_BALL_ANSWERS) - 1)
    answer = MAGIC_8_BALL_ANSWERS[n]["answer"]
    color = MAGIC_8_BALL_ANSWERS[n]["color"]
    response = color + answer
    print("\r" + BOLD + name + ", my answer is: " + response + END, end = "")
    time.sleep(.1)

"""
Decide for me
# Goal: Your program should allow the user to a question and your program should show on the screen that is thinking... for a few seconds, and then your program should respond to the user, within 10 possibilities that you have given it. Then you should ask the user if he wants to make a new question. If it answers yes, allow the user to ask a new question, otherwise, terminate the program.
"""

from random import choices, randint
from time import sleep

class DecideForMe:
    def __init__(self):
        self.answers = [
            "I haven't idea",
            "I think it's better to ask this to Google",
            "In this you surprised me, i don't know the answer",
            "Do you think I'm 'Siri'?",
            "Don't ask this for me, You've got to trust in your heart of hearts",
            "Do you believe that? Go ahead, keep going",
            "You better think calmly",
            "Again this question? I already answered"
        ]

    def start(self):
        self.MakeQuestion()

    def MakeQuestion(self):
        question = str(input("Ask the computer a question: "))
        print("Thinking...")
        sleep(2)
        print(choices(self.answers)[0])
        new_question = \
            str(input("Do you want to like a new question? [Y/N] ")).strip().upper()[0]
        while new_question not in "YN":
            print("Please, type Y or N")
            new_question = \
                str(input("Do you want to like a new question? [Y/N] ")).strip().upper()[0]
        if new_question == "Y":
            self.MakeQuestion()
        elif new_question == "N":
            print("Thanks for using our program!")


decide_for_me = DecideForMe()
decide_for_me.start()

# questions = []
# number = 0
# while True:
#     question = str(input("Ask the computer a question: "))
#     print("Thinking...")
#     sleep(2)
#     if question in questions:
#         print(answers[7])
#     else:
#         print(f"Answer → {answers[number]}")
#         questions.append(question)
#     number = randint(0, 6)



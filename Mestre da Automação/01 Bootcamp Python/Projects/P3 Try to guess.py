from random import randint

number = randint(0, 100)

while True:
    attempt = int(input("Try to guess the number between 1 and 100: "))
    if attempt > number:
        print("Too high...try again")
    elif attempt < number:
        print("Too low...Try again")
    else:
        print("Yas, congrats! You guessed the number.")
        break

# Or

class GuessTheNumber:
    def __init__(self):
        self.range = randint(0, 100)

    def start(self):
        self.TryToGuess()

    def TryToGuess(self):
        try:
            attempt = int(input("Try to guess the number between 0 and 100: "))
            while attempt < 0 or attempt > 100:
                print("Type numbers between 0 and 100")
                attempt = int(input("Try to guess the number between 0 and 100: "))
            if attempt > self.range:
                print("Too high...try again")
                self.TryToGuess()
            elif attempt < self.range:
                print("Too low...Try again")
                self.TryToGuess()
            else:
                print("Yas, congrats! You guessed the number.")
        except ValueError:
            print("Type just numbers between 0 and 100")
            self.TryToGuess()


guess_the_number = GuessTheNumber()
guess_the_number.start()
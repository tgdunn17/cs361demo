import random

random.seed()

def guessingGame():
    """ Function that will prompt the user to guess an integer between 0 and 10 """
    ans = random.randint(0, 10)
    userVal = int(input("Guess an integer!\n"))
    while ans != userVal:
        if ans < userVal:
            userVal = int(input("Too high! Try again!\n"))
        elif ans > userVal:
            userVal = int(input("Too low! Try again!\n"))
    print("Good job guessin'!")

guessingGame()
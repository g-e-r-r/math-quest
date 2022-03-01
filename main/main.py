#Importing necessary moodules and libraries
from time import sleep
import random

#Global
calculatorLink = "(google drive link)"
firstNum = 0
secondNum = 0
result = 0
field = 1

#Functions
def welcome():
    print("Welcome to the math test")
    print("If you have to do some operation you can use mine")
    print("You can download it at this link")
    print(calculatorLink)

def checkAnswer():
    pass

def generateNumber():
    firstNum = random.randrange(100)
    if field == 1:
        secondNum = "X"
        result = random.randrange(100)
    elif field == 2:
        secondNum = random.randrange(100)
        result = "X"    

def guessNumber():
    pass
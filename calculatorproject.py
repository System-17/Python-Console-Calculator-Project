# Project 1 - Basic Calculator
# input gives a prompt

import re   # imports regex library

print("Our Magical Calculator!")
print("Type 'quit' to exit\n")

previous = 0        # Going to store our current result
run = True          # Program loop


def performMath():

    global run   # givss access to non static non local vars
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye!")
        run = False
    elif equation == 'c':
        previous = 0

    else:
        equation = re.sub('[a-zA-Z,.(): "]', '', equation)     # Do some regex to eliminate bad values - code safety

        if previous == 0:
            previous = eval(equation)          # Evaluate function nice and useful! but can execute code so bad!
        else:
            previous = eval(str(previous)+equation)
        print(previous)


while run:          # Keep program running until exit
    performMath()


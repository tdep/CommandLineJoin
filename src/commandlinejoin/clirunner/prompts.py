"""
CLI Runner [CommandLineJoin]
Author: Trevor DePew

This is where the prompt functions live.
"""

import pyinputplus as pyip


def inputPrompt():
    print(('Welcome to CommandLineJoin!\n'
           'This is a command line interface to join two .csv files in a specified way.\n'
           'Please follow the prompts or type "quit" at any point to exit the program.'))
    while True:
        prompt = 'Hello World?'
        response = pyip.inputYesNo(prompt)

        if response == "yes":
            print("Hello World!")
            break
        elif response == "no":
            print("Goodbye World!")
            break
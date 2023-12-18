#.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-. To-Do List:
#|                                                                       | 1. Add Special characters
#|                 # Pass Phrase Generator                               | 2. Add input option to choose amount of items in pass phrase
#|                 # Created By Sebastiaan                               | 3. Use safe random module
#|                                                                       | 4. Use JSON files for items in lists
#|                Intended for educational use only                      | 5. Add input option for item language
#!          do NOT use as a real life Pass Phrase Generator              ! 6. Add a function for something
#:                                                                       :
#`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-etf-'

# Import random module for generating random numbers
# Import pyperclip for copying pass phrase to clipboard automatically (https://pypi.org/project/pyperclip/)
import random
import pyperclip

# Define list, define random number to use in print statement starting at 0 ending at list length -1.
kleur = ["Rood", "Wit", "Blauw", "Groen", "Geel", "Paars"]
number = random.randint(0, len(kleur) -1 )

dier = ["Aap", "Capybara", "Koe", "Giraffe"]
number2 = random.randint(0,3)

number3 = random.randint(0,99)
str_number = str(number3)

# Create a list with the variables
variables = [kleur[number], dier[number2], str(str_number)]

# Shuffle the order of variables
random.shuffle(variables)

# Concatenate the variables and print the result
result = "".join(variables)
print("Copied to clipboard:", result)

pyperclip.copy(result)

#print((kleur[number])+(dier[number2])+str_number)
#pyperclip.copy((kleur[number])+(dier[number2])+str_number)











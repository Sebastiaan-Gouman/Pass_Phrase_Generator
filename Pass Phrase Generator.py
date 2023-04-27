#.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-. To-Do List:
#|                                                                       | 1. Add Special characters
#|                 # Pass Phrase Generator                               | 2. Make order of items random (ie. not start with a color every time)
#|                 # Created By Sebastiaan                               | 3. Add input option to choose amount of items in pass phrase
#|                                                                       | 4. Use safe random module
#|                Intended for educational use only                      | 5. Use JSON files for items in lists
#!          do NOT use as a real life Pass Phrase Generator              ! 6. Copy Pass Phrase to clipboard automatically
#:                                                                       : 7. Add input option for item language
#`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-etf-'

# Import random module for generating random numbers
import random

# Define list, define random number to use in print statement starting at 0 ending at list length -1.
kleur = ["Rood", "Wit", "Blauw", "Groen", "Geel", "Paars"]
number = random.randint(0, len(kleur) -1 )

dier = ["Aap", "Capybara", "Koe", "Giraffe"]
number2 = random.randint(0,3)

number3 = random.randint(0,99)
str_number = str(number3)


print((kleur[number])+(dier[number2])+str_number)




import random as r 

def madlib_game():
    noun1 = input("A type of animal: ")
    verb1 = input("Give me verb: ")
    adjective1 = input("Give me an adjective: ")
    noun2 = input("Name a fruit: ")
    verb2 = input("Give me a verb: ")

    madlib1 = (f"Madlib 1 Story... {noun1},{verb1},{adjective1},{noun2},{verb2}")
    madlib2 = (f"Madlib 2 Story... {noun1},{verb1},{adjective1},{noun2},{verb2}")
    madlib3 = (f"Madlib 3 Story... {noun1},{verb1},{adjective1},{noun2},{verb2}")

    randomNumber =r.randint(1,3)

    print(randomNumber)

    if randomNumber <=1:
        print(madlib1)
    elif randomNumber <=2:
        print(madlib2)
    elif randomNumber <=3:
        print(madlib3)

madlib_game()
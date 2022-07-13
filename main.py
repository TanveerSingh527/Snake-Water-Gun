# We imported random module to give computer brain and choose something
import random

# This is the logic behind winning, loosing or tie in the game, like if you choose snake computer choose water then you win. (Just like that)
def gameWin(comp, you):
    # It declares tie when you and computer's choice is same
    if comp == you:
        return None

    # Checks for all posibilities except tie when computer chooses s
    if comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    # Checks for all posibilities except tie when computer chooses w
    if comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

    # Checks for all posibilities except tie when computer chooses g
    if comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

turns = int(input("How many times you want to play (example: 5): "))

for i in range (0, turns):
    # Here we use random module to help computer play his turn
    print("Computer's turn: Snake(s) water(w) or gun(g)? ") # It tells the user that computer has choosen something
    randomNum = random.randint(1, 3) # It gives computer a range to choose between
    if randomNum == 1: # Here we convert computer's number choice into snake, water or gun
        comp = "s" # It converts it into snake
    elif randomNum == 2:
        comp = "w" # It converts it into water
    elif randomNum == 3:
        comp = "g" # It converts it into gun
    you = input("Your turn: Snake(s) water(w) or gun(g)? ") # It takes the input from the user about his/her turn

    print(f"Computer chose {comp}") # It tells what computer has choosen
    print(f"You chose {you}") # It tells what you have choosen


    a = gameWin(comp, you) # Here we call the function and get a value in None, True or False
    if a == None: # It tells that game is a tie because function returns None
        print("The game is a tie! :|")
    elif a: # By default value if True so we didn't tell computer that a == True. If a == True then it will automatically understand this thing and run this elif
        print("You have won the game! :)")
    else: # We ran out of every choice except False, so obviously if none of the above statement executed, the value of a will be == False
        print("You loose the game. :(")
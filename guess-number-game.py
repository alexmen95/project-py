import random
from colored import fore, style
from goto_py import goto

print(fore.BLUE + "Welcome to game 'Guess the number'! You have 3 tries to guess the right number, which is between 1 and 10!" + style.RESET)
guess = 1
number = random.randint(1, 10)
# Player must enter some number between 1 and 10
user = int(input("# What is the number?:"))

# The while loop so it can go on.
while user != number:

    if user > number:
        print(fore.BLUE + "Lower" + style.RESET)

    elif user < number:
        print(fore.BLUE + "Higher" + style.RESET)

    user = int(input("What is the number?: "))
    guess += 1
    if guess == 3:
        print("#################################################################")
        print("#" + fore.RED + "Sorry,You did not guess the number! THE GUESSING NUMBER WAS" + style.RESET, number, "#")
        print("#################################################################")
        break
else:
    print("#####################################################################")
    print("#" + fore.GREEN + "You guessed it right! The number is", number, "and it only took you ", guess,
          "tries" + style.RESET + "#")
    print("#####################################################################")

print("Do you want to play again!? Y = yes, N = no?")
answer = input(": ")
if answer == 'Y' or answer == 'y':
    goto(1, once_only=False)
elif answer == 'N' or answer == 'n':
    print(fore.BLUE + "It was a nice game! Thank you and goodbye!" + style.RESET)
else:
    print(fore.RED + "You entered something different! Try again, but properly" + style.RESET)
    goto(33, once_only=False)

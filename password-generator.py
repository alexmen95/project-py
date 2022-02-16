import string
import random
from goto_py import goto
from colored import fore, style

print(fore.BLUE + "Welcome to password generator" + style.RESET)
print(fore.BLUE + "Please enter the length for password" + style.RESET)
length = int(input(":"))

numb = string.digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = string.punctuation

print("What kind of password do you want: Numeric = 1, Combined = 2, Symbolic = 3, Letters and numbers = 4")
choice = int(input(":"))

if choice == 1:
    comb = numb
    temp = random.sample(comb, length)
    password = "".join(temp)
    print(fore.BLUE + "Your password is: " + style.RESET + password)
    file = open("password.txt", "w")
    file.write("Your password is: ")
    file.write(password)
    file.close()
elif choice == 2:
    comb = numb + lower + upper + symbols
    temp = random.sample(comb, length)
    password = "".join(temp)
    print(fore.BLUE + "Your password is: " + style.RESET + password)
    file = open("password.txt", "w")
    file.write("Your password is: ")
    file.write(password)
    file.close()
elif choice == 3:
    comb = symbols
    temp = random.sample(comb, length)
    password = "".join(temp)
    print(fore.BLUE + "Your password is: " + style.RESET + password)
    file = open("password.txt", "w")
    file.write("Your password is: ")
    file.write(password)
    file.close()
elif choice == 4:
    comb = numb + lower + upper
    temp = random.sample(comb, length)
    password = "".join(temp)
    print(fore.BLUE + "Your password is: " + style.RESET + password)
    file = open("password.txt", "w")
    file.write("Your password is: ")
    file.write(password)
    file.close()
else:
    print("You entered something different. Try again!")
    goto(13)

print("Do you want to generate new password? Y = yes, N = no")
a = input(":")

if a == 'Y' or a == 'y':
    goto(1)
elif a == 'N' or a == 'n':
    print("Thank you and goodbye!")
else:
    print("You entered something different. Try again")
    goto(36)

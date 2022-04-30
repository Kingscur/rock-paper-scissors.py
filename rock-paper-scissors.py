from random import randint
from colorama import Fore, Back, Style

choice = ["Schere", "Stein", "Papier"]

computer = choice[randint(0,2)]

print(Fore.BLUE + "Willkommen bei Schere, Stein, Papier!")
print()
player = input(Fore.YELLOW + "Deine Wahl: ")
print()
print (Fore.BLUE + "Der Computer hat " + computer + " gewählt")
print()

if player == computer:
    print(Fore.YELLOW + "Unentschieden!")
elif player == "Schere" and computer == "Stein":
    print (Fore.RED + "Der Computer gewinnt!")
elif player == "Schere" and computer == "Papier":
    print (Fore.GREEN + "Du gewinnst!")
elif player == "Stein" and computer == "Papier":
    print (Fore.RED + "Der Computer gewinnt!")
elif player == "Stein" and computer == "Schere":
    print (Fore.GREEN + "Du gewinnst!")
elif player == "Papier" and computer == "Schere":
    print (Fore.RED + "Der Computer gewinnt!")
elif player == "Papier" and computer == "Stein":
    print (Fore.GREEN + "Du gewinnst!")


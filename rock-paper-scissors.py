from random import randint
from colorama import Fore, Back, Style

choice = ["Rock", "Paper", "Scissors"]

computer = choice[randint(0,2)]

print(Fore.BLUE + "Welcome to Rock, Paper, Scissors!")
print()
player = input(Fore.YELLOW + "Your choice: ")
print()
print (Fore.BLUE + "Computer choosed" + computer)
print()

if player == computer:
    print(Fore.YELLOW + "Draw!")
elif player == "Scissors" and computer == "Rock":
    print (Fore.RED + "Computer wins!")
elif player == "Scissors" and computer == "Paper":
    print (Fore.GREEN + "You win!")
elif player == "Rock" and computer == "Paper":
    print (Fore.RED + "Computer wins!")
elif player == "Rock" and computer == "Scissors":
    print (Fore.GREEN + "You win!")
elif player == "Paper" and computer == "Scissors":
    print (Fore.RED + "Computer wins!")
elif player == "Paper" and computer == "Rock":
    print (Fore.GREEN + "You win!")


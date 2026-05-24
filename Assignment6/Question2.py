import random

choices = ["Rock", "Paper", "Scissors"]

print("""
      Availible choices:
      Rock
      Paper
      Scissors
      """)

tries = int(input("How many tries? "))
uscore = 0
cscore = 0

for i in range(tries):
    uchoice = input("Enter your choice: ")
    cchoice = random.choice(choices)

    if uchoice == cchoice:
        print("Draw")
    elif (uchoice == "Rock" and cchoice == "Scissors") or (uchoice == "Scissors" and cchoice == "Paper") or (uchoice == "Paper" and cchoice == "Rock"):
        print("User wins")
        uscore = uscore + 1
    else:
        print("Computer wins")
        cscore =cscore + 1

print("Final Score: ")
print("User Score:", uscore)
print("Computer Score:", cscore)

if uscore == cscore:
    print("Draw")
elif uscore > cscore:
    print("User wins")
else:
    print("Computer wins")

import random;

def printRock():
# Rock
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)

def printPaper():
# Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)

def printScissors():
# Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)

def printImage(selection):
    if selection == 1:
        printRock()
    if selection == 2:
        printPaper()
    if selection == 3:
        printScissors()


def choicePrint(userSel, compSel):
    print("Your Selection: \n")
    printImage(userSel)

    print("Computer Selection: \n")
    printImage(compSel)

def playGame():
    userSel = int(input("Select 1 for Rock, 2 for Paper, 3 for Scissor"))
    compSel = random.randint(1,3)

    choicePrint(userSel,compSel)

    if(userSel == compSel ):
        print("Draw!!!")
    else:
        if ((userSel == 1 and compSel ==2) or (userSel == 2 and compSel == 3) or (userSel == 3 and compSel == 1)):
            print("You lose, Computer wins!!!")
        else:
            print("You Win!!!")

playGame()
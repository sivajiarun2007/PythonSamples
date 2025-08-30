import random

def replaceWord(blankStr, selectedWord, userInput):
        selectedWordList = list(blankStr)
        for index in range(0, len(selectedWord)):
            if selectedWord[index].lower() == userInput.lower():
                selectedWordList[index] = userInput.lower()
        return "".join(selectedWordList)    



def startGame():
    listOfWords = ["Arun", "Siaara", "Svetha"]
    selectedWord = random.choice(listOfWords)
    totalLife = 5
    incorrectCount = 0
    selectedWordLength = len(selectedWord)
    blankStr = ""

    for letter in selectedWord:
        blankStr += "_"

    print(f"You have total of {totalLife} life to guess the word")

    while incorrectCount < 5:
        print(f"Total lives available is {totalLife - incorrectCount}")
        userInput = input(f"Guess the letter in the word: {blankStr} \n Enter your input: ")
        
        if userInput.lower() in selectedWord.lower():
             blankStr = replaceWord(blankStr, selectedWord, userInput)
             if blankStr.lower() == selectedWord.lower():
                  break
        else:
             incorrectCount += 1
    
    if(incorrectCount < 5):
         print(f"You Won!! The Word is {blankStr.upper()}")
    else:
         print("Game Over")


startGame()
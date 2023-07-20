import math
from random import *
wordpool = ["nice", "cool", "cat", "cheese", "dictionary", "bruh", "dog", "pneumonoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialidocious", "floccinaucinihilipilification"]
randomWord = wordpool[randint(0, len(wordpool)-1)]
guessedWord = ""
correctLetters = ""
failedLetters = ""
triedLetters = ""
failedTries = 0
maxFail = 10
def load_words():
    global wordpool
    with open('words_alpha.txt') as word_file:
        wordpool = word_file.read().split()
def isInString(s, t):
    for x in s:
        if x == t:
            return True
    return False

def refreshGuessedWord():
    global guessedWord
    guessedWord = ""
    for x in randomWord:
        if isInString(correctLetters,x):
            guessedWord = guessedWord + x
        elif x == " ":
            guessedWord = guessedWord + " "
        else:
            guessedWord = guessedWord + "_"
def draw():
    print("==================================")
    print("Tries: " + str(failedTries) + "/" + str(maxFail))
    print("")
    print("Correct letters: " + correctLetters)
    print("")
    print("Incorrect letters: " + failedLetters)
    print("")
    print("")
    print(guessedWord)
    print("")
    print("")
    print("==================================")
    if guessedWord == randomWord:
        print("You win!")
        print("==================================")
    if failedTries >= maxFail:
        print("You lose :(")
        print(randomWord)
        print("==================================")
def tryInput(let):
    global triedLetters
    global failedLetters
    global failedTries
    global correctLetters
    if len(let) > 1:
        return
    let = let.lower()
    if isInString(triedLetters, let):
        return
    if isInString(randomWord, let):
        correctLetters = correctLetters + let
        triedLetters = triedLetters + let
        #positionsForLetter = getStringPositions(randomWord,let)
        refreshGuessedWord()
        return
    failedLetters = failedLetters + (let)
    triedLetters = triedLetters + (let)
    failedTries = failedTries + 1
    
if __name__ == '__main__':
    load_words()
    while True:
        triedLetters = ""
        failedLetters = ""
        correctLetters = ""
        failedTries = 0
        randomWord = wordpool[randint(0, len(wordpool)-1)]
        refreshGuessedWord()    
        while guessedWord != randomWord:
            draw()
            if failedTries >= maxFail:
                print("You lose L")
                break
            tryInput(input("Type a letter: "))
        draw()
        input("Press any key to restart")
        
        

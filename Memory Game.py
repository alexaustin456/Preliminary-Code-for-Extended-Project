import random #random is required for randomising list indexes
import time #Allowing time.sleep() to be used
import sys #Enabling sys.exit to work
def clearScreen (): #Function allow screen to move up 50 lines
    menu = 0
    while menu < 50:
        time.sleep(0.1)
        print()
        menu = menu + 1
    return(clearScreen)
print("Welcome to Memory Trainer! \n \n")
mode = input("Would you like easy, hard or exit?:").upper()#Mode selection
if mode == 'EASY':
    print("You have chosen the easy option, you will now be shown the 3x3 grid"'\n','\n')
    print("You will need to study the grid and find the word \nthat has been removed and that has been substituted to\nreplaced it, when shown the second grid.\n\n")
    words = open("words.txt")#Opening file
    wordsList = []
    for word in words:
        wordsList.append(word.strip())#Adding words to wordsList
    words.close
    subWord = wordsList[random.randint(0,9)]#Selecting substitute word
    wordsList.remove(subWord)#removing substitute word from wordsList
    random.shuffle(wordsList)#Randomly shuffling wordsList
    print(wordsList[0], wordsList[1], wordsList[2])#Displaying first grid
    print(wordsList[3], wordsList[4], wordsList[5])
    print(wordsList[6], wordsList[7], wordsList[8])
    subWordback = wordsList[random.randint(0,9)]#Removed word
    wordsList = [i.replace(subWordback, subWord) for i in wordsList]#swapping substitute word for removed word
    random.shuffle(wordsList)
    time.sleep(30)#30 second wait
    clearScreen()#clearscreen function
    print(wordsList[0], wordsList[1], wordsList[2])#Displaying second grid
    print(wordsList[3], wordsList[4], wordsList[5])
    print(wordsList[6], wordsList[7], wordsList[8])
    def substituteWord ():#substitute function
        rem_guess = 3 #beginning guesses
        while rem_guess > 0: #while loop for guesses
            subsWord = input("Please input substitute word:").upper()#substitute word guess
            if subsWord == subWord:
                print("Well Done! You Win!")#message when user is correct
                sys.exit(2)
            else:
                rem_guess = rem_guess -1 #-1 guess when user is wrong
                print("You have", rem_guess, "guesses remaining")
                if rem_guess == 0:
                    print("You lose")#user loses when 0 guesses left
                    sys.exit(2)
        return(substituteWord)
    def removedWord ():#remove function
        rem_guess = 3
        while rem_guess > 0:
            removeWord = input("Please input removed word:").upper()
            if removeWord == subWordback:
                print("Well Done! Please proceed to the substituted word.")
                substituteWord()
                sys.exit(2)
            else:
                rem_guess = rem_guess -1
                print("Please guess again")
                print("You have", rem_guess, "guesses remaining")
                if rem_guess == 0:
                    print("You Lose")
                    sys.exit(2)
        return(removedWord)
    removedWord()#removed function called
    substituteWord()#substituted function called
if mode == 'HARD':#user selection hard
    print("You have chosen the hard option, you will now be shown the 4x4 grid"'\n','\n')
    print("You will need to study the grid and find the word that has been removed and that has replced it, when shown the second grid, you will be given 1 minute to study it.")
    words = open("wordsEXT.txt")#opens extended word file
    wordsExtList = []#list for 4x4 words
    for word in words:
        wordsExtList.append(word.strip())
    words.close
    subWord = wordsExtList[random.randint(0,16)]
    wordsExtList.remove(subWord)
    random.shuffle(wordsExtList)
    print(wordsExtList[0], wordsExtList[1], wordsExtList[2], wordsExtList[3])#displaying first 4x4 grid
    print(wordsExtList[4], wordsExtList[5], wordsExtList[6], wordsExtList[7])
    print(wordsExtList[8], wordsExtList[9], wordsExtList[10], wordsExtList[11])
    print(wordsExtList[12], wordsExtList[13], wordsExtList[14], wordsExtList[15])
    subWordback = wordsExtList[random.randint(0,16)]
    wordsExtList = [i.replace(subWordback, subWord) for i in wordsExtList]
    random.shuffle(wordsExtList)
    time.sleep(60)
    clearScreen()
    print(wordsExtList[0], wordsExtList[1], wordsExtList[2], wordsExtList[3])#displaying second 4x4 grid
    print(wordsExtList[4], wordsExtList[5], wordsExtList[6], wordsExtList[7])
    print(wordsExtList[8], wordsExtList[9], wordsExtList[10], wordsExtList[11])
    print(wordsExtList[12], wordsExtList[13], wordsExtList[14], wordsExtList[15])
    def substituteWordExt ():#4x4 substitute function
        rem_guess = 3
        while rem_guess > 0:
            subsWord = input("Please input substitute word:").upper()
            if subsWord == subWord:
                print("Well Done! You Win!")
            else:
                rem_guess = rem_guess -1
                print("You have", rem_guess, "guesses remaining")
                if rem_guess == 0:
                    print("You lose")
        return(substituteWord)
    def removedWordExt ():#4x4 removed function
        rem_guess = 3
        while rem_guess > 0:
            removeWord = input("Please input removed word:").upper()
            if removeWord == subWordback:
                print("Well Done! Please proceed to the substituted word.")
                substituteWordExt()
                sys.exit(2)
            else:
                rem_guess = rem_guess -1
                print("You have", rem_guess, "guesses remaining")
                if rem_guess == 0:
                    print("You Lose")
                    sys.exit(2)
        return(removedWord)
    removedWordExt()#4x4 removed function called
    substituteWordExt()#4x4 substitute function called
if mode == 'EXIT':
    sys.exit()#exit module
# Imports
import random

# Project Selection
print('What project do you wanna test? ')
x = int(input("\n"))

#Project Select #1
if x == 1:
    
    #Project Title
    print("\nProject Title: Greet Project")
    
    # Functions for the Project
    def greet(usrName, birthDate):
        return print("Your name is " + usrName + ' and you were born on ' + birthDate + '. ' + 'Nice to meet you!')

    #User-Program Interaction
    userName = str()
    userBday = str()

    userName = input('\nWhat is your name?\n')
    userBday = input('\nWhen were you born?\n')
    
    greet(userName, userBday)
    
#Project Select #2
elif x == 2:
    
    #Project Title
    print("\nProject Title: Number Guessing Game")

    # 1. rolls a random number from 1 to 3
    # 2. Sets 3 lives
    # 2. Checks whether guess matches random number
    # 3. if it doesn't match, re-roll number to guess and deduct lives
    # WIN CONDITION: match and random number matches before lives finish
    # LOSE CONDITION: run out of lives before guessing
    
    
    keepTrying = True
    
    while keepTrying is True:
        
        ranNum = random.randint(1,3)
        messageBox = ["\nGame over :(\n", "\nWrong again :) 1 life left.\n", "\nOops, wrong guess. You got 2 lives left.\n",  "\nCongrats, you won and survived my torture! :)\n"]
        heartLeft = 3
        print("\nGame's easy, guess the correct number that ranges from 1 - 3.\nAn incorrect guess changes the number to guess, and you've only got 3 tries :)\n")
    
        while heartLeft > 0:
            userGuess = int(input("Type your guess here: "))
            if userGuess == ranNum:
                print(messageBox[3])
                heartLeft = 0
            elif userGuess != ranNum:
                heartLeft = heartLeft - 1
                print(messageBox[heartLeft])
                ranNum = random.randint(1,3)
        
        endTry = input("Do you want to keep trying? Y/N\n")
        
        if endTry == 'n' or 'N':
            print('\nSee you next time! :)')
            keepTrying = False
        
#Project Select #3 
elif x == 3:
    
    # 1. Receive a random set of number
    # 2. Transfer into an array
    # 3. Set variables for highest and lowest numbers, initial value is set to none
    # 4. Value of the first item in the array will be set as the highest or lowest value at the start of iteration.
    # 5. Variables will be updated if the array item is smaller or bigger than current values
    # 6. Print highest and lowest numbers.
    
    #Project Title
    print("\nProject Title: HIGHEST and LOWEST number project")
    
    #Functions of the project
    def giveRandomSet(fiveSetRand):
        p = int(0)
        while p < 5:
            fiveSetRand.append(random.randint(1,100))
        p = p + 1
        
    numSet = []
    giveRandomSet(numSet)
    print(numSet)
    
    lowestNumber = None
    highestNumber = None
    
    for number in numSet:
        if highestNumber is None or number > highestNumber:
            highestNumber = number
    
    for number in numSet:
        if lowestNumber is None or number < lowestNumber:
            lowestNumber = number

    print("\nthe lowest number is ",lowestNumber)
    print("\nthe highest number is ",highestNumber)
    
#Project Select #4    
elif x == 4:
    
    # 1. Receive a word
    # 2. Find the length of the word (how many characters total)
    # 3. Set a variable to represent index number
    # 4. Print each letter accompanied by their index placement
    # 5. Print word length
    
    #Project Title
    print("\nProject Title: String Character Counter and Index Coded Character Print")
    
    wordInput = input('\nType a word: ')
    wordLen = len(wordInput)  
    indNum = 0  
    print('\n')
    for letter in wordInput:
        print(indNum," - ",wordInput[indNum])
        indNum += 1
    print("\nWord length is ", wordLen," characters")
    
#Project Select #5
elif x == 5:
    
    # 1. Receive a sentence
    # 2. Break into words (ignore numbers or special characters) 
    # 3. Place into array
    # 4. Check length of each word
    # 5. Print longest word
    
    #Project Title
    print("\nProject Title: Finding the longest word in the sentence")
    
    #Input Sentence and Variables Declaration
    inputSentence = input("Type a sentence\n")
    wordList = []
    wordList = inputSentence.split()
    wordListClean = []
    longestWord = ''
    
    #Cleans wordList of non-alpha characters
    for word in wordList:
        cleanWord = ''
        if word.isalpha():
            wordListClean.append(word)
        elif not word.isalpha():
            for letter in word:
                if letter.isalpha():
                    cleanWord = cleanWord + letter
            wordListClean.append(cleanWord)
            
    #Finds longest word and prints all words with their character count
    for word in wordListClean:
        if len(word) > len(longestWord):
            longestWord = word
        print('\n', word, " - ", len(word), " characters")
    print("\nThe longest word is ", longestWord, " with ", len(longestWord), " characters")
    
#Project Select #6
elif x == 6:
    
    # 1. Receive input sentence
    # 2. Put into array (ignore special characters, numbers, and spaces)
    # 3. Print words with number code
    # 4. Offer choice to select a word of their choice using number code
    
    print('\nProject Title: Word Selection')
    inputSentence = input('\nType a sentence: ')
    wordList = []
    aWord = ''
    
    for letter in inputSentence:
        if letter.isalpha():
            aWord = aWord + letter
        elif not letter.isalpha():
            if aWord != '':
                wordList.append(aWord)
                aWord = ''
                
    if aWord != '':
            wordList.append(aWord)
            
    for word in wordList:
        print('\n', wordList.index(word), " - ", word)
    
    wordSelect = int(input("\nSelect a word by typing their number code: "))
    print('\nYou have selected the word', '"', wordList[wordSelect], '"')
    
elif x == 7:
    
    #Project Title
    print("\nProject Title: Word Flipper")
    
    #Function for the project
    def backward_string(val):
        newVal = ''
        counterVal = int((len(val) - 1))
        while counterVal > -1:
            newVal += val[counterVal]
            counterVal -= 1
        return newVal.strip()
    
    #User-Program Interaction Segment
    userIn = input("\nInput the word you want to FLIP: ")
    print(">", backward_string(userIn))
    
#Project Select Fail
else:
    print("Project not found, please try again.")
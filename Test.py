# Imports
import random

# Functions
def greet(usrName, birthDate):
    return print("Your name is " + usrName + ' and you were born on ' + birthDate + '. ' + 'Nice to meet you!')

def giveRandomSet(fiveSetRand):
    p = int(0)
    while p < 5:
        fiveSetRand.append(random.randint(1,100))
        p = p + 1

# Project Selection
print('What project do you wanna test? ')
x = input()
x = int(x)

#Project Select #1
if x == 1:
    
    #Project Title
    print("Project Title: Greet Project")
    
    userName = str()
    userBday = str()

    userName = input('What is your name? ')
    userBday = input('When were you borN? ')
    
    greet(userName, userBday)
    
#Project Select #2
elif x == 2:
    
    #Project Title
    print("Project Title: Number Guessing Project")

    # 1. Input a number between 1 - 100
    # 2. Check if it's lower or higher than 50
    # 3. Check if it's higher or lower than 25/75
    # 4. Increase or decrease count check while printing the iterations
    
    countCheck = int(50)
    print("Ill guess your number, give me a number between 1 - 100: ")
    numberIn = input()
    numberIn = int(numberIn)
    
    if numberIn == countCheck:
        print("Your number is neither above or below 50, so it's ", countCheck)
        
    elif numberIn < countCheck:
        print('Lower than ', countCheck)
        countCheck = countCheck - 25
            
        if numberIn > countCheck:
            print('Higher than ', countCheck)
            
            while numberIn != countCheck:
                print("It's not ", countCheck)
                countCheck = countCheck + 1
            print("Your number is ", countCheck)
                
        elif numberIn < countCheck:
            print('Lower than ', countCheck)
            
            while numberIn != countCheck:
                print("It's not ", countCheck)
                countCheck = countCheck - 1 
            print("Your number is ", countCheck)
            
    elif numberIn > countCheck:
        print('Higher than', countCheck)
        countCheck = countCheck + 25.
        
        if numberIn < countCheck:
            print('Lower than ', countCheck)
            
            while numberIn != countCheck:
                print("It's not ", countCheck)
                countCheck = countCheck - 1
            print('Your number is ', countCheck)
        
        elif numberIn > countCheck:
            print('Higher than ', countCheck)
            
            while numberIn != countCheck:
                print("It's not ", countCheck)
                countCheck = countCheck + 1
                
            print('Your number is ', countCheck) 

#Project Select #3 
elif x == 3:
    
    # 1. Receive a random set of number
    # 2. Transfer into an array
    # 3. Set variables for highest and lowest numbers, initial value is set to none
    # 4. Value of the first item in the array will be set as the highest or lowest value at the start of iteration.
    # 5. Variables will be updated if the array item is smaller or bigger than current values
    # 6. Print highest and lowest numbers.
    
    #Project Title
    print("Project Title: HIGHEST and LOWEST number project")
    
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

    print("the lowest number is ",lowestNumber)
    print("the highest number is ",highestNumber)
    
#Project Select #4    
elif x == 4:
    
    # 1. Receive a word
    # 2. Find the length of the word (how many characters total)
    # 3. Set a variable to represent index number
    # 4. Print each letter accompanied by their index placement
    # 5. Print word length
    
    #Project Title
    print("Project Title: String Character Counter and Index Coded Character Print")
    
    wordInput = input('Type a word: ')
    wordLen = len(wordInput)  
    indNum = 0  
    for letter in wordInput:
        print(indNum," - ",wordInput[indNum])
        indNum = indNum + 1
    print("Word length is ", wordLen," characters")
    
#Project Select #5
elif x == 5:
    
    # 1. Receive a sentence
    # 2. Break into words (ignore numbers or special characters) 
    # 3. Place into array
    # 4. Check length of each word
    # 5. Print longest word
    
    #Project Title
    print("Project Title: Finding the longest word in the sentence")
    
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
        print(word, " - ", len(word), " characters")
    print("The longest word is ", longestWord, " with ", len(longestWord), " characters")
    
#Project Select Fail
else:
    print("Project not found, please try again.")
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
    print("Greet Project")
    
    userName = str()
    userBday = str()

    userName = input('What is your name? ')
    userBday = input('When were you borN? ')
    
    greet(userName, userBday)
    
#Project Select #2
elif x == 2:
    
    #Project Title
    print("Number Guessing Project")
    
    countCheck = int(50)
    print("Ill guess your number, try me: ")
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
    
    #Project Title
    print("BIGGEST and LOWEST number project")
    
    numSet = []
    giveRandomSet(numSet)
    print(numSet)
    
    lowestNumber = None
    biggestNumber = None
    
    for number in numSet:
        if biggestNumber is None or number > biggestNumber:
            biggestNumber = number
    
    for number in numSet:
        if lowestNumber is None or number < lowestNumber:
            lowestNumber = number

    print("the lowest number is ",lowestNumber)
    print("the biggest number is ",biggestNumber)
    
#Project Select #4    
elif x == 4:
    
    #Project Title
    print("String Character Counter and Index Coded Character Print")
    
    wordInput = input('Type a word: ')
    wordLen = len(wordInput)  
    indNum = 0  
    for letter in wordInput:
        print(indNum," - ",wordInput[indNum])
        indNum = indNum + 1
    print("Word length is ", wordLen," characters")
    
#Project Selection Failure
else:
    print("hatdog")
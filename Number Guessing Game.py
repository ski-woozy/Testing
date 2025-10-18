import random
    
#Project Title
print("\nProject Title: Number Guessing Game")

# 1. rolls a random number from 1 to 3
# 2. Sets 3 lives
# 2. Checks whether guess matches random number
# 3. if it doesn't match, re-roll number to guess and deduct lives
# WIN CONDITION: match and random number matches before lives finish
# LOSE CONDITION: run out of lives before guessing

#Keep playing loop
keepTrying = True

#Main Game Loop
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
        print('\nSee you next time! :)\n')
        keepTrying = False
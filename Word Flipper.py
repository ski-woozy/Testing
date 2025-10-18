#Project Title
print("\nProject Title: Word Flipper")

#Function for the project
def revWord(val):
    return val[::-1]

#User-Program Interaction
userIn = input("\nInput the word you want to FLIP: ")
print(">", revWord(userIn),'\n')
#Project Title
print("\nProject Title: Word Flipper")

#Function for the project
def backward_string(val):
    return val[::-1]

#User-Program Interaction Segment
userIn = input("\nInput the word you want to FLIP: ")
print(">", backward_string(userIn),'\n')
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
print(">", backward_string(userIn),'\n')
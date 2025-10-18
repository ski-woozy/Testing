#Project Title
print("\nProject Title: Sum of Numbers In String")

#Function to sum all numbers in a string
def sum_numbers(text: str) -> int:

    numArr = []
    textArr = text.split()
    
    for word in textArr:
        letP = False
        numP = False
        for letter in word:
            if letter.isalpha():
                letP = True
            if letter.isnumeric():
                numP = True
                
        if numP & letP is True:
            continue
        elif numP is True and letP is False:
            numArr.append(word)
            
    sumOfNum = int(0)
    
    for num in numArr:
        sumOfNum += int(num)
            
    return print("\n",sumOfNum)

#User-Program Interaction
userIn = input("\nTo test the program, input any string with numbers\n\n>")
sum_numbers(userIn)
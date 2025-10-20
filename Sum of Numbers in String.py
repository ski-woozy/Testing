#Project Title
print("\nProject Title: Sum of Numbers In String")

#Function to sum all numbers in a string
def sum_numbers(text: str) -> int:

    numArr = []
    textArr = text.split()
    numCount = int(0)
    
    for word in textArr:
        letP = False
        numP = False
        for letter in word:
            if letter.isalpha():
                letP = True
            if letter.isnumeric():
                numCount += 1
                numP = True
                
        if numP & letP is True:
            continue
        elif numP is True and letP is False:
            numArr.append(word)
            
    sumOfNum = int(0)
    
    for num in numArr:
        sumOfNum += int(num)

    return print("\nThe sum of numbers without letters is: ", sumOfNum, '\n\nWith a total number count of: ', numCount, '\n')

#User-Program Interaction
userIn = input("\nTo test the program, input any string with numbers\n\n>")
sum_numbers(userIn)
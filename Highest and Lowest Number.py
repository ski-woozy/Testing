import random

#Functions of the project
def giveRandomSet(fiveSetRand):
    p = int(0)
    while p < 5:
        fiveSetRand.append(random.randint(1, 100))
        p = p + 1
    return fiveSetRand

#Project Title
print("\nProject Title: HIGHEST and LOWEST number")

# 1. Receive a random set of number
# 2. Transfer into an array
# 3. Set variables for highest and lowest numbers, initial value is set to none
# 4. Value of the first item in the array will be set as the highest or lowest value at the start of iteration.
# 5. Variables will be updated if the array item is smaller or bigger than current values
# 6. Print highest and lowest numbers.

#User-Program Interaction
numSet = []
giveRandomSet(numSet)
print('\nThe random set of numbers is: ', numSet, '\n')

print("The HIGHEST number is: ", max(numSet))
print("The LOWEST number is: ", min(numSet), '\n')
#Project Title
print("\nProject Title: String Char and Index Counter")

# 1. Receive a word
# 2. Find the length of the word (how many characters total)
# 3. Set a variable to represent index number
# 4. Print each letter accompanied by their index placement
# 5. Print word length

#User-Program Interaction
wordInput = input('\nType a word: ')
wordLen = len(wordInput)  
indNum = 0  
print('\n')
for letter in wordInput:
    print(indNum," - ",wordInput[indNum])
    indNum += 1
print("\nWord length is ", wordLen," characters\n")
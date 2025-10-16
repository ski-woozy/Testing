#Project Title
print('\nProject Title: Word Selection')

# 1. Receive input sentence
# 2. Put into array (ignore special characters, numbers, and spaces)
# 3. Print words with number code
# 4. Offer choice to select a word of their choice using number code

inputSentence = input('\nType a sentence: ')
wordList = []
aWord = ''

for letter in inputSentence:
    if letter.isalpha():
        aWord = aWord + letter
    elif not letter.isalpha():
        if aWord != '':
            wordList.append(aWord)
            aWord = ''
            
if aWord != '':
    wordList.append(aWord)
        
for word in wordList:
    print('\n', wordList.index(word), " - ", word)

wordSelect = int(input("\nSelect a word by typing their number code: "))
print('\nYou have selected the word', '"', wordList[wordSelect], '"\n')
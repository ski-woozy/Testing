#Project Title
print("\nProject Title: Find Longest Word\n")

# 1. Receive a sentence
# 2. Break into words (ignore numbers or special characters) 
# 3. Place into array
# 4. Check length of each word
# 5. Print longest word

#Input Sentence and Variables Declaration
inputSentence = input("Type a sentence\n")
wordList = []
wordList = inputSentence.split()
wordListClean = []
longestWord = ''

#Cleans wordList of non-alpha characters
for word in wordList:
    cleanWord = ''
    if word.isalpha():
        wordListClean.append(word)
    elif not word.isalpha():
        for letter in word:
            if letter.isalpha():
                cleanWord = cleanWord + letter
        wordListClean.append(cleanWord)
        
#Finds longest word and prints all words with their character count
for word in wordListClean:
    if len(word) > len(longestWord):
        longestWord = word
    print('\n', word, " - ", len(word), " characters")
print("\nThe longest word is ", longestWord, " with ", len(longestWord), " characters\n")
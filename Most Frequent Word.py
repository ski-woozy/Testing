#Project Title
print("\nProject Title: Most Frequent Word")

#Function to find the most frequent word in a string
def most_frequent(strData):
    strData = str(strData)
    arrData = strData.split()
    
    for word in arrData:
        wordClean = ''
        for char in word:
            if char.isalpha():
                wordClean += char
        inRep = int(arrData.index(word))
        arrData.pop(inRep)
        arrData.insert(inRep, wordClean)
        
    arrDataComp = []
    highCount = 0
    highWord = ''
        
    for word in arrData:
        wordCount = 0
        wordHold = ''
        noCopy = True
        for comp in arrDataComp:
            if word == comp:
                noCopy = False
                break
        if noCopy is True:
            wordHold = word
            for word in arrData:
                if wordHold == word:
                    wordCount += 1
                arrDataComp.append(wordHold)
                if highCount < wordCount:
                    highCount = wordCount
                    highWord = wordHold
                    
    return print("The word ", '"', highWord, '"', " appeared ", highCount, " times.\n")

#User-Program Interaction
userIn = input("\nInput the sentence you want to test.\n\n>")
most_frequent(userIn)
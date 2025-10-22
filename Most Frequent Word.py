#Project Title
print("\nProject Title: Most Frequent Word")
print('\n1. Version 1.0')
print('\n2. Version 2.0\n')

#Selection of version to run
version = input("Select the version to run (1 or 2): ")

if version == '1':
    print("\n\nYou have selected Version 1.0\n")
    
    #Function to clean string and find most frequent word
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
        freqWord = ''
            
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
                        freqWord = wordHold

        return print("\nThe word ", '"', freqWord, '"', " appeared ", highCount, " times.\n")

    #User-Program Interaction
    userIn = input("Input the sentence you want to test.\n\n>")
    most_frequent(userIn)

#Selection of version to run
elif version == '2':
    print("\n\nYou have selected Version 2.0\n")
    
    #Function that asks to clean or keep non-alpha characters (removes special characters automatically) and find most frequent word
    def most_frequent(strData, action):
        
        strData = str(strData)
        arrData = strData.split()
        highCount = 0
        freqWord = []
        
        #Clean words if action is 'clean'
        if action == 'clean':
            for word in arrData:
                wordClean = ''
                for char in word:
                    if char.isalpha():
                        wordClean += char
                inRep = int(arrData.index(word))
                arrData.pop(inRep)
                arrData.insert(inRep, wordClean)
        
        elif action == 'keep':
            for word in arrData:
                wordClean = ''
                for char in word:
                    if char.isalnum():
                        wordClean += char
                inRep = int(arrData.index(word))
                arrData.pop(inRep)
                arrData.insert(inRep, wordClean)
                        
        #Count occurrences of each word
        counts = {}
        for word in arrData:
            counts[word] = counts.get(word, 0) + 1
        
        #Determine most frequent word
        for word in counts:
            if highCount is None or counts[word] > highCount:
                highCount = counts[word]
                freqWord = [word]
                
        #Check for multiple words with same highest count
        for word in counts:
            if counts[word] == highCount and word not in freqWord:
                freqWord += [word]

        return print("\nThe word(s)", '"', freqWord[:], '"', "appeared ", highCount, " times.\n")

    #User-Program Interaction
    userIn = input("Input the sentence you want to test.\n\n>")
    print("\nWould you like to clean non-alpha characters from words before processing?")
    action = input("Type 'clean' to remove non-alpha characters or 'keep' to retain them:\n\n>").lower()

    if action not in ['clean', 'keep']:
        while action not in ['clean', 'keep']:
            action = input("Invalid input. Please type 'clean' or 'keep':\n\n>")
    elif action in ['clean', 'keep']:
        most_frequent(userIn, action)
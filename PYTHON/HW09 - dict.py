#CS100-019
#HW09 - dictionaries


#Problem 1:

def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = 1
        else:
            d[word[0]] += 1

    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']


#Problem 2:

def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = [word]
        elif word not in d[word[0]]:
            d[word[0].append(word)]

    return d

print(initialLetters(horton))
            
#Problem 3:

def shareALetter(wordList):
    d = {}
    for word in wordList:
        for c in  word:
            for wd in wordList:
                if c in wd:
                    if word not in d:
                        d[word] = [wd]
                    elif wd not in d[word]:
                        d[word].append(wd)
    return d
print(shareALetter(horton))
    

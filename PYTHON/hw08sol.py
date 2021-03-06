#HW 08

#Problem 1
def file_copy(in_file, out_file):

    cFrom = open(in_file,'r')
    cTo = open(out_file,'w')

    for lines in cFrom:  
        cTo.write(lines)

    cFrom.close()
    cTo.close()

#Problem 2
def file_stats(in_file):
    lines = 0
    w = 0
    c = 0
    for i in in_file:
        lines += 1
        w += len(i.split())
        c += len(i)
    print("Lines: " + str(lines) + "\nWords: " + str(w) + "\nCharacters: " +str(C))

#Problem 3
def repeat_words(input_file, output_file):
    inF = open(input_file)
    outF = open(output_file,'w')
    lineList = inF.readlines()
    for line in lineList:
        wordList = line.split()
        cleanList = []
        for word in wordList:
            cleanList.append(word.strip(string.punctuation))
        for word in cleanList:
            if cleanList.count(word) >1:
                outF.write(word + " ")
        outF.write("\n")
        

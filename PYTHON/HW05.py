#HW 05
# CS 100- 0019

def hasFinalLetter(strList,letters):
    returnList=[]
    for word in strList:
        if word[-1] in letters:
            returnList.append(word)
    return returnList
                


# Test Case 1:
strList=['hello', 'jello', 'cat']
letters = ('a','e','i','o','u','c','t')

print(hasFinalLetter(strList,letters))


# Test Case 2

strList=['BillY', 'mANDy' , 'cooL']
letters = ('X','d','b','y','L')

print(hasFinalLetter(strList,letters))


# Test Case 3

strList=['delL','AET','ber']
letters = ('a','e','i','o','u','c','t')

print(hasFinalLetter(strList,letters))


  
#2
def isDivisible(maxInt,twoInts):
    returnList=[]
    count=0
    for number in range(0,maxInt):
        if number % twoInts[0] ==0 and number % twoInts[1]==0:
            returnList.append(number)
    return returnList




# Test Case 1:

maxInt = 30

twoInts = (5,10)

print(isDivisible(maxInt,twoInts))


#Test Case # 2
maxInt = 64

twoInts = (4,8)

print(isDivisible(maxInt,twoInts))

#Test Case 3

maxInt = 0

twoInts = (1,2)

print(isDivisible(maxInt,twoInts))
      

#HW 06

#Problem 1
def twoWords(length, firstLetter):
    while True:
        wordLength = input("Enter a "+str(length)+"-letter word please")
        if len(wordLength) == length:
            break
        
    while True:
        word = input("Enter a word beginning with "+firstLetter+ " please")
        if word[0] == firstLetter.upper() or word[0] == firstLetter.lower():
            break
    return [wordLength,word]
       

print(twoWords(4, 'B'))


#Problem 2
def twoWordsV2(length, firstLetter):
    wordLength = input("Enter a "+str(length)+"-letter word please")
    while len(wordLength) != length: 
        wordLength = input("Enter a "+str(length)+"-letter word please")

    word = input("Enter a word beginning with "+firstLetter+ " please")        
    while  word[0] != firstLetter.upper() and word[0] != firstLetter.lower():
        word = input("Enter a word beginning with "+firstLetter+ " please") 
    return [wordLength,word]
        

print(twoWordsV2(4, 'B'))



#Problem3
def enterNewPassword():

    while True:    
        password = input("Enter password: ")
                                 
        if 15 < len(password) < 8 or sum(str.isdigit(p) for p in password) < 1:
            print("Password must be 8-15 characters long and must contain at least one number:")
            continue
        else:
            print("Successfully entered password.")
            break

enterNewPassword()


#Problem 4
import random
print("Im thinking of a number in the range 0-50. You have five tries to guess it.")
values = range(0,51)
number = random.choice(values)
i = 0

while i in range(5):
    guess = int(input("Guess "+str(i+1))+"?")
    if number == guess:
        print("You are right! ")
        break
    elif number < guess:
        print(guess," is too high")
        i += 1
        continue
    elif number > guess:
        print(guess," is too low")
        i += 1
        continue
print("I was thinking of ",+number)


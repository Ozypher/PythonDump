#Exercise 1
months = ["January", "February", "March", "April", "May", "June", "July",
             "August","September", "October", "November", "December"]
for i in months:
    if i[0] == "J":
        print(i)


#Exercise 2
for i in range(100):
    if i % 5 == 0 and i % 2 == 0:
        print(i)

#Exercise 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for l in horton:
    if l in vowels:
        print(l)

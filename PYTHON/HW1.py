"""
Sherwin Rahimi
CS100 2017F Section 017
HW 1,  September 19, 2017
"""
#Q2;
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

print('grades =', grades)
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print('frequency =',frequency)

#Q3:

#a
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print('Dog breeds:', dog_breeds)

#b
herding_dogs = dog_breeds[0:2]
print('Herding dog:', herding_dogs)

#c
tiny_dogs = [dog_breeds[-1]]
print('Tiny dogs:', tiny_dogs)

#d
print('Persian in dogs?', 'Persian' in dog_breeds)

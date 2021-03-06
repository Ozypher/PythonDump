#Sherwin Rahimi
#CS 100-23

#1
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

#Equilateral Triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

#move turtle
t.up()
t.left(120)
t.forward(150)
t.down()

#Square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

#move turtle
t.up()
t.forward(180)
t.left(90)
t.down()

#Pentagon

t.forward(100)
t.right((180-(5-2)*180)/5)
t.forward(100)
t.right((180-(5-2)*180)/5)
t.forward(100)
t.right((180-(5-2)*180)/5)
t.forward(100)
t.right((180-(5-2)*180)/5)
t.forward(100)

#move turtle
t.up()
t.right(108)
t.forward(300)
t.right(90)
t.forward(100)
t.down()


#2

#Concentric Circles

t.circle(50)
t.right(90)

t.up()
t.forward(50)
t.left(90)
t.down()

t.circle(100)
t.right(90)

t.up()
t.forward(50)
t.left(90)
t.down()

t.circle(150)
t.right(90)

t.up()
t.forward(50)
t.left(90)
t.down()

t.circle(200)
t.right(90)

#3
#A
print("100! = " + str(math.factorial(100)))


#B
print("The log(base 2) of 1,000,000 = " +str(math.log(1000000, 2)))
print(" ")

#C
answerC = str(math.gcd(63,49))
print("GCD of 63 and 49 is = " +str(math.gcd(63,49)))
print(" ")




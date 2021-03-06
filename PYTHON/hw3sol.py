#1
a = 3
b = 4
c = 5
if a < b:
    print('OK')
elif c < b:
    print('OK')
elif a + b == c:
    print('OK')
elif a**2 + b**2 == c**2:
    print('OK')
#2
else:
    print('NOT OK')
    
#3
import math
import turtle
color = input("Pick a color: ")
width = int(input("Pick a line width: "))
length = int(input("Pick a line length: "))
shape = input("Pick a shape: ")
s = turtle.Screen()
t = turtle.Turtle()

t.color(color)
t.width(width)

if shape.lower() == "line":
    t.fd(length)
elif shape.lower() == "triangle":
    t.fd(length)
    t.left(120)
    t.fd(length)
    t.left(120)
    t.fd(length)
elif shape.lower() == "square":
    t.fd(length)
    t.left(90)
    t.fd(length)
    t.left(90)
    t.fd(length)
    t.left(90)
    t.fd(length)
else:
    print("Invalid shape")

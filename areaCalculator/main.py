#alec george raid: area calculator

#might need to import math
import math

#function for square, takes side length and squares it
def square(side_length):
    return float(side_length)**2

#function for rectangle, takes length and width and multiplies them
def rectangle(length, width):
    return float(length)*float(width)

#function to calculate triangle with the base and height, multiplies them together and divides the result by 2
def bh_triangle(base, height):
    return float(base)*float(height)/2

#function to calculate area of a circle, multiplies the radius squared by pi, rounds to a decimal
def circle(radius, decimal):
    return round(math.pi*float(radius)**2, int(decimal))

#function to calculate area of trapezoid, adds bases together and divides by two, multiplies by height
def trapezoid(base1, base2, height):
    return (float(base1)+float(base2))*float(height)/2

#function to calculate area of a triangle, but with three sides and using trigonometry
#   C
#a / \ c
# /   \
#A-----B
#   b
def trig_triangle(side1, side2, side3):
    angle_A = 

#put functions in a loop to use it repeatedly
while True:
    #needs to be able to calculate area of square, rectangle, triangle, circle, and trapezoid
    shape = input("""\nwhat would you like to calculate the area of?
type
  1 to calculate a square
  2 to calculate a rectangle
  3 to calculate a triangle (with base and height)
  4 to caclulate a circle
  5 to calculate a trapezoid
  6 to calculate a triangle (with three sides)
type your answer here: """)
    if shape == "1":
        print(square(input("what are the side lengths?")))
    elif shape == "2":
        print(rectangle(input("what is the length? "),input("what is the width? ")))
    elif shape == "3":
        print(bh_triangle(input("what is the base (bottom side) width? "),input("what is the height? ")))
    elif shape == "4":
        print(circle(input("what is the radius? "),input("to how many decimals? ")))
    elif shape == "5":
        print(trapezoid(input("what is the width of one base (bottom side)? "),input("what is the width of the other base (top side)? "),input("what is the height ")))
    elif shape == "6":
        print(rectangle(input("what is the length? "),input("what is the width? ")))
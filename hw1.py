# Name: Richard Castro
# CSE 160
# Autumn 2020
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and then copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all of the problems given.

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1
print("Problem 1 solution follows:")

# Quadratic Equation 3x^2 - 5.86x + 2.5408
a = 3
b = -5.86
c = 2.5408
bigger = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
smaller = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
print('Root 1: ' + str(smaller))
print('Root 2: ' + str(bigger))
print()
# Problem 2
print("Problem 2 solution follows:")

for i in range(2, 11):
    num = print('1/' + str(i) + ': ' + str(1/i))
print()

# Problem 3
print("Problem 3 solution follows:")

n = 10
triangular = 0
for i in range(triangular, n + 1):
    triangular = i + triangular
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)
print()
# Problem 4
print("Problem 4 solution follows:")

factorial_ten = 1
for k in range(2, n + 1):
    factorial_ten = k * factorial_ten
print('10!: ' + str(factorial_ten))
print()
# Problem 5
print("Problem 5 solution follows:")

factorial = 1
for z in range(10, 0, -1):
    for t in range(1, z + 1):
        factorial = t * factorial
    print(str(z) + '!: ' + str(factorial))
    factorial = 1
print()

# Problem 6
print("Problem 6 solution follows:")
total = 0
fact = 1
for z in range(10, 0, -1):
    for t in range(1, z + 1):
        fact = t * fact
    total = total + (1/fact)
    fact = 1

print("e: " + str(fact + total))
# Collaboration

# No one helped me with my code

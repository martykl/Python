# Program to generate a random number between user specified number range
range1 = int(input("Enter first number range "))
range2 = int(input("Enter second number range "))
# import the random module
import random

print(random.randint(range1,range2))

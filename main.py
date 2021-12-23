from Story import *

name = input("What's your chracter name: ")
age = input("What's your chracter age: ")
mother = input("What's your chracter mother's name: ")
mothermood = input(
    "What's your chracter mother's mood: is his mother happy or sad: ")

s1 = Story(name, age, mother, mothermood)
print("Genrated Story: ")
print()
s1.printstory()

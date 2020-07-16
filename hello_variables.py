# a = 5
# b = 2
# c = "Hello"
# d = 0.25
# e = True
#
#
# print(a)
# print(b)
# print(c)
#
# a = (2, 3, 4)
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print("what is your name")
#
# name = input()
# print("Hello", name)


# name = input("What is your name?")
# age = int(input("What is your age?"))
# DOB = input("What is your DOB?")
#
# print("Hi", name, "you are", age, "years old, your birthday is", DOB)

# Numbers
# String
# Boolean

# print(1+1)
# print(1-1)
# print(14 % 3)
# print(2*2)
# print(12/4)
# print(3 > 5)

# >, <, >=, <=, ==, !=
# print(2 == 4)
# print(2 != 4)

# NUMBERS
# a = 3 + 2j
# b = 3.23
# c = 3
#
# print(type(a), type(b), type(c))
# # STRINGS
#
# single = 'Single Quotes'
# double = "Double Quotes"
#
# singleInside = "single ' quotes in a string "
# slash = 'I\'m using single quotes'
# help = "i'm saying \"help\""
#
# print(single, double, singleInside, slash, help)

# hw = "Hello World!"
# print(hw)
# print(hw[4])
#
# print(hw[3:7])
# print(hw[4:])
# print(hw[:8])
# print(hw[-2])
# print(hw[-5:])
# print(len(hw))

# STING METHODS
#
# whiteSpace = "     Spaces String      "
# print(len(whiteSpace))
# print(whiteSpace.strip())
# print(whiteSpace.lstrip())
# print(whiteSpace.rstrip())
#
# print(whiteSpace.count("spaces"))
# print(whiteSpace.lower())
# print(whiteSpace.upper())
# print(whiteSpace.capitalize())
# print(whiteSpace.replace("e", "ooooo"))
# print(whiteSpace.strip().capitalize().replace("s", "ooooo").count("o"))

# a = "Ardvark"
# b = "Bat"
# c = "Cat"
# d = 5
#
# print(a + "," + b + "," + c + " " + str(d))
# num = "5"
# print(int(num))
#
# print(f"{a}, {b}, {c} {d}")
#
# name = "Jade"
# print(f"Hello my name is " + name + "!")

#Name, age, number of siblings, fave decimal, fave animal

name = input("What is your name?")
try:
    age = int(input("How old are you?"))
except:
    age =int(input("please enter a integer"))

numSib = int(input("How many siblings do you have?"))
faveDec = float(input("What is your favourite decimal?"))
faveAni = input("What is your favourite animal?")

print(f"Hi", name, "you are", age,
      "years old, you have", numSib,
      "siblings, your favourite decimal is", faveDec,
      "and your favourite animal is a", faveAni)

# a = True
# b = False
# age = 19
# weather = "sunny"
# print(True and True)
# print(False and False)
#
# print(True or False)
#
# print(age > 18 and weather == "sunny")

# hw = "Hello World!"
#
# print(hw.isalpha())
# print(hw.islower())
# print(hw.isupper())
# print(hw.endswith("x"))
# print(hw.startswith("x"))

# LISTS (ARRAYS)
# shoppingList = ["eggs", "sausages", "cheese", "bread", 5, 2.5, True, [1, 2, 5]]
# print(shoppingList)
# print(type(shoppingList))
# print(shoppingList[-1])
# print(len(shoppingList))
# shoppingList.append("mushrooms")
# print(shoppingList)
# shoppingList.append("coffee")
# print(shoppingList)
# shoppingList.remove("cheese")
# print(shoppingList)
# popReturn = shoppingList.pop()
# print(shoppingList)
# print(popReturn)
# print(shoppingList.pop(0))
# print(shoppingList)

#TUPLES
# colours = ("blue", "purple", "turqouise")
# print(colours)
# print(type(colours))
# print(colours[-1])
#
# #IMMUTABLE
# print(colours.count("orange"))
# print(colours.index("purple"))
#
# shoppingList = ["eggs", "bacon"]
# shoppingList[1] = "quorn"
# print(shoppingList)

#DICTIONARIES

# myDict = {"key": "value", "key2": 2}
# print(myDict)
# print(type(myDict))
#
# biggerDict = {
#     "key1": "value1",
#     "key2": 2,
#     "key3": [1, 2, 3, 4]
# }
# print(biggerDict)
#
# infoDict = {
#     "name": "Jade",
#     "age": 22,
#     "numberOfSiblings": 4,
#     "faveColour": "Purple",
#     "myNumbers": [7, 13, 19]
# }
#
# print(infoDict)
# print(infoDict["faveColour"])
# infoDict["newKey"] = "newKeyValue"
# print(infoDict)
# del infoDict["newKey"]
# print(infoDict)
#
# print(myDict.keys())
# print(myDict.values())
#
# data14Dict = {
#     "stream": "Data14",
#     "course": "Data Engineering",
#     "number of people": 11,
#     "location": "Birmingham",
#     "week": 4,
#     "trainer": "David",
#     "trainees": ["Alex", "Anthony", "Ben", "Charlie", "Charlotte", "Danvir",
#                  "Evie", "Jade", "Joe", "Juxhen", "Katie"]
#
# }
#
# print(data14Dict)

#SETS
#
# carParts = {"wheels", "doors", "steering wheel"}
# print(carParts)
#
# carParts.add("pedals")
# print(carParts)
#
# carParts.discard("doors")
# print(carParts)
#
# #FROZEN SETS
# fs = frozenset([1, 2, 3, 4])
# fs2 = frozenset([3, 4, 5, 6])
# print(fs)
# print(fs2)
# print(fs.difference(fs2))
# print(fs.intersection(fs2))
# print(fs.issubset(fs2))
# print(fs.union(fs2))

#CONTROL

# age = 18
# x = 1
# if age > 18:
#     print("You can see the scary file")
#     x = 2
# elif age == 18:
#     print("you are only just old enough")
# else:
#     print("your too young, go away")
#
# print("everyone can be here")
# print(x)

# filmRating = "pg"
#
# if filmRating == "U":
#     print("Suitable for all ages")
# elif filmRating.upper() == "PG":
#     print("Suitable with parental guidence")
# elif filmRating == "12A" or filmRating == "12":
#     print("Suitable for ages 12 and over")
# elif filmRating == "15":
#     print("suitable for ages 15 and over")
# elif:
#     print("Suitable for ages 18 and over")
# else:
#     print("enter a valid film rating")

#FOR LOOPS
# shoppingList = ["eggs", "bacon", "bread"]
# colours = ["yellow", "purple", "turquoise"]
# for item in shoppingList:
#     for colour in colours:
#         print(item, colour)
#
# dictData = {
#     1: {"name": "Alex", "animal": "all dogs"},
#     2: {"name": "Ben", "animal": "flamingo"},
#     3: {"name": "Evie", "animal": "gorilla"},
#     4: {"name": "Charlotte", "animal": "giraffe"}
# }
#
# for key in dictData:
#     for innerKey in dictData[key]:
#         print(dictData[key][innerKey])

# chineseMenu = {
#     101: {"dish": "egg fried rice", "price": 3.50},
#     102: {"dish": "chow mein", "price": 2.60},
#     103: {"dish": "chicken fried rice", "price": 6.20},
#     104: {"dish": "sweet and sour chicken", "price": 8.40}
# }

# for key in chineseMenu:
#     print(chineseMenu[key])
#
# for key in chineseMenu:
#     for value in chineseMenu[key]:
#         print(chineseMenu[key][value])

# for key in chineseMenu:
#     for value in chineseMenu[key]:
#         print(f"{chineseMenu[key]} has the price {chineseMenu[key][value]['price']:.2f}")

# counter = 0
# while counter < 10:
#     print(f"still counting! {counter}")
#     counter += 1
#     if counter == 6:
#         break
#     counter += 1
#
# print("We've escaped the while loop")

# age = ""
# while not age.isnumeric():
#     age = input("Enter your age:\n")
#     if age.isnumeric():
#         age = int(age)
#         break
#     else:
#         print("Thats not a number, try again please")
#
# print("you are "+ str(age))
#

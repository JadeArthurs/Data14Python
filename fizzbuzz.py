#ORIGINAL TASK

# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#USER INPUT FOR 1 NUMBER
#
# number = int(input("pick a number between 1&100?"))
# for value in range(number, number+1):
#     if (value % 3 == 0) and (value % 5 == 0):
#         print("FizzBuzz")
#     elif value % 3 == 0:
#         print("Fizz")
#     elif value % 5 == 0:
#         print("Buzz")
#     else:
#         print(value)

# def check(input):
# value = input
# if value is not value.isnumeric():
#     value = print(input("Please enter a numeric value?"))




#USER INPUTS FOR START FINISH INCREMENT & WORD VALUES

def num_check(num):
    while not num.isnumeric():
        num = input("Please enter a valid number?\n")
    if num.isnumeric:
        return int(num)


start_value = num_check(input("Choose a number to start from?\n"))
end_value = num_check(input("Choose a number to end at?\n"))
divide3and5 = input("Choose a word for values divisable by 3 and 5\n")
divide3 = input("Choose a word for values divisable by 3\n")
divide5 = input("Choose a word for values divisable by 5\n")
increment = num_check(input("Choose a number to increment by?\n"))


for number in range(int(start_value), int(end_value)+1, int(increment)):
    if (number % 3 == 0) and (number % 5 == 0):
        print(divide3and5)
    elif number % 3 == 0:
        print(divide3)
    elif number % 5 == 0:
        print(divide5)
    else:
        print(number)



# ZeroDivision error
# Indentation error
# Name error
# ModuleNotFound error
# Syntax error
# Type error
# Key error
# Attribute error
# Index error
# Assertion error
# Recursion Error

#TRY EXCEPT

# try:
#     print("Trying to open the file....")
#     file = open("order.txt")
#     print("File success")
# except FileNotFoundError as errmsg:
#     print("error")
#     print(errmsg)
#     raise
# finally:
#     print("Finished handling errors")

# MODES
# r - read mode
# w - write mode
# c - create mode
# a - append mode
# t - text mode
# b - binary mode
# + - reading and writing

def open_and_print(filename):
    try:
        with open(filename, "r") as open_file:
            file_line_list = open_file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        open_file.close()

    except FileNotFoundError:
        print("File can no be found, check filename")
        raise


# file = open("order.txt")
# print(1, file.readline())
# print(2, file.readline())
# print(3, file.readline())
# print(4, file.readline())
# print(5, file.readline())

with open("order.txt", "w") as open_file:
    write_to = input("What would like in your file?\n")
    open_file.write(write_to)

with open("order.txt", "a") as open_file:
    write_to = input("Would you like to add anything else to the file?\n")
    open_file.write(f"\n{write_to}")

print(open_file)
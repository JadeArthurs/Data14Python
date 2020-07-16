# MAPPING

# data14 = ["Katie", "Juxhen", "Joe"]
#
# data14_upper = map(lambda x: x.upper(), data14)
#
# print(list(data14_upper))
#
# num = [1]

# numbers = [1, 2, 3]
# adds = [10, 100, 1000]
#
# def square_add(num, add):
#     return num**2 + add
#
# num_sq3 = map(square_add, numbers, adds)
# print(list(num_sq3))
#
# FILTERING
# students = ["DAVID", "lee", "RICHARD"]
# result = filter(str.isupper, students)
# print(list(result))
#
# def even3(num):
#     return num % 6 == 0
#
# numbers = list(range(1,100))
#
# even3filter = filter(even3, numbers)
# print(list(even3filter))
# words ["Cat", "Bird", "Bread"]





# LAMBDAS
# def add(n1, n2):
#     return n1 + n2
#
# add_lambda = (lambda n1, n2: n1 + n2)
#
# print(add_lambda(2, 2))

# numbers = [181, 2834, 2, 283, 2]
# result = map(lambda x: x * x + 3, numbers)
# print(list(result))

# savings = [234.00, 555.00, 674.00, 78.00]
# # bonus = list(map(lambda x: round(x*1.1, 2), savings))
# # print(bonus)
#
# even_savings = list(filter(lambda x: x % 2 == 0, savings))
# print(even_savings)

# Ternary Operators

age = 17

# if age >= 18:
#     print("Go Ahead")
# else:
#     print("Go Away")
#
# print("Go Ahead" if age >= 18 else "Go Away")
# print(("Go Away", "Go Ahead")[age >= 18])  # Dont do this

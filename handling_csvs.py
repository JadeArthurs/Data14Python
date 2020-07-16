import csv

#
# scores = []
# with open("data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader))
#
# data_to_write =[["David", 5], ["Paula", 6], ["Nish", 7]]
#
# with open("new_data.csv", "w") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     # for row in data_to_write:
#     #     csv_writer.writerow(row)
#     csv_writer.writerows(data_to_write)

def open_iris():
    with open("iris.csv") as csvfile:
        csvreader = list(csv.reader(csvfile))

        return csvreader

def means():
    sepal_length = []
    sepal_width = []
    petal_lenth = []
    petal_width = []
    values = (open_iris()[1:])
    for row in values:
        sepal_length.append(float(row[0]))
        sepal_width.append(float(row[1]))
        petal_lenth.append(float(row[2]))
        petal_width.append(float(row[3]))
    sepal_length_mean = sum(sepal_length)/len(sepal_length)
    sepal_width_mean = sum(sepal_width) / len(sepal_width)
    petal_length_mean = sum(petal_lenth) / len(petal_lenth)
    petal_width_mean = sum(petal_width) / len(petal_width)

    return print(f" sepal length mean = {round(sepal_length_mean, 4)}, \
           sepal width mean = {round(sepal_width_mean, 4)}, \
           petal length mean = {round(petal_length_mean, 4)},\
           petal width mean = {round(petal_width_mean, 4)}")

print(means())
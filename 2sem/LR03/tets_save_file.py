import csv

field = ["Col-1", "Col2", "Col3", "Col4"]
data = [
    ["Value", 23, 24, 25],
    ["Value", 24, 25, 26],
    ["Value", 25, 26, 27],
    ["Value", 26, 27, 28],
]

with open("my_file.csv", "w") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\n")
    writer.writerow(field)
    writer.writerows(data)




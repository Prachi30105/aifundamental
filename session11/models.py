import csv

with open("students.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Grade"])
    writer.writerow(["Alice",20,"A"])
    writer.writerow(["Bob",21,"B"])
    writer.writerow(["Charlie",22,"C"])



with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

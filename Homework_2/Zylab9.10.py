# Justino Cortez ID 1615245
import csv

amount = {}
filename = input()
with open(filename, 'r') as words:
    reader = csv.reader(words)
    row = next(reader)
    for word in row:
        if word in amount:
            amount[word] = amount[word] + 1
        else:
            amount[word] = 1

for i in amount:
    print(i, amount[i])

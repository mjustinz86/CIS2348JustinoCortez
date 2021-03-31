# Justino Cortez ID 1615245
numbers = input()
my_list = [int(i) for i in numbers.split() if int(i) >= 0]
my_list.sort()

for x in my_list:
    print(x, end=' ')

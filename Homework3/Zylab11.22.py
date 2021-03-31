# Justino Cortez ID 1615245
words = input().split()
for x in words:
    frequency = 0
    for y in words:
        if y == x:
            frequency = frequency + 1
    print(x, frequency)

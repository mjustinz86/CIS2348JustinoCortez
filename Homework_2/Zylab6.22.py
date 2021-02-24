# Justino Cortez ID 1615245
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

for x in range(-11,10):
    for y in range(-11,10):
        if (a*x+b*y==c) and (d*x+e*y==f):
            print("\n\nx = ",x," y = ",y)
            quit()
print("\nThere is no solution")   

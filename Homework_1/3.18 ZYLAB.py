# Justino Cortez  ID:1615245

length = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))

area = (length * width)
paint = (area / 350)
can = round(paint)
color = {'red': 35, 'blue': 25, 'green': 23}

print('Wall area:', area, 'square feet')
print('Paint needed:', '{:.2f}'.format(paint), 'gallons')
print('Cans needed:', can, 'can(s)\n')

choice = input('Choose a color to paint the wall:\n')
price = '${}'.format(color[choice] * can)

print('Cost of purchasing', choice, 'paint:', price)

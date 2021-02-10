# Justino Cortez ID:1615245
(input('Enter amount of lemon juice (in cups):\n'))
(input('Enter amount of water (in cups):\n'))
(input('Enter amount of agave nectar (in cups):\n'))
(input('How many servings does this make?\n'))

print(end='\n')

print('Lemonade ingredients - yields 6.00 servings')
print('2.00 cup(s) lemon juice')
print('16.00 cup(s) water')
print('2.50 cup(s) agave nectar')

print(end='\n')

servings = int(input('How many servings would you like to make?'))

juice = (servings / 6) * 2
water = (servings / 6) * 16
nectar = (servings / 6) * 2.5

print(end='\n')
print(end='\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar')

print(end='\n')

juice_G = ((servings / 6) * 2) / 16
water_G = ((servings / 6) * 16) / 16
nectar_G = ((servings / 6) * 2.5) / 16

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(juice_G), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_G), 'gallon(s) water')
print('{:.2f}'.format(nectar_G), 'gallon(s) agave nectar')

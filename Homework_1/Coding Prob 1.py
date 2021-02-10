# Justino Cortez ID:1615245
print('Birthday Calculator', '\n Current day')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
print('Birthday')
B_month = int(input('Month: '))
B_day = int(input('Day: '))
B_year = int(input('Year: '))

age = year - B_year
if (month + day) > (B_month + B_day):
    age = age
else:
    age = (year - B_year) - 1
print('You are', age, 'years old')

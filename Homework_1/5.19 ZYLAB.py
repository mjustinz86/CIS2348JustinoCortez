# Justino Cortez ID:1615245
print("Davy's auto shop services")
print('Oil change --', '${}'.format(35))
print('Tire rotation --', '${}'.format(19))
print('Car wash --', '${}'.format(7))
print('Car wax --', '${}'.format(12) + '\n')

service = (input('Select first service:\n'))
service2 = (input('Select second service:'))
print("\n")
cost = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
price = '${}'.format(cost[service])
price2 = '${}'.format(cost[service2])
t_price = '${}'.format(cost[service] + cost[service2])

print("Davy's auto shop invoice")
print('\n')
print('Service 1:', service + ",", price)
print('Service 2:', service2 + ",", price2)
print('\n')
print('Total:', t_price)

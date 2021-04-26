# Justino Cortez ID 1615245
import csv
import datetime

# creating lists

Date = datetime.datetime.now()
Date = Date.strftime("%m/%d/%Y")
Date2 = datetime.datetime.strptime(Date, '%m/%d/%Y')
Man1 = []
Price1 = []
Service1 = []
Laptop = []
Phone = []
Manufacturer = []
Tower = []
Damaged = []
Past = []
LDate = []
Date3 = []
Query = []
Query2 = []

# opening csv files and joining together to create full inventory

with open('FinalProjectManufacturerList.csv') as Man_file:
    words = csv.reader(Man_file, delimiter=',')
    for word in words:
        Man1.append(word)

Man2 = sorted(Man1)

with open('FinalProjectPriceList.csv') as Man_file:
    words = csv.reader(Man_file, delimiter=',')
    for word in words:
        Price1.append(word)

Price2 = sorted(Price1)

with open('FinalProjectServiceDatesList.csv') as Man_file:
    words = csv.reader(Man_file, delimiter=',')
    for word in words:
        Service1.append(word)
Service2 = sorted(Service1)

# Attach lists together

for data in range(0, len(Man2)):
    Man2[data].append(Price2[data][1])
    Man2[data].append(Service2[data][1])

Full_Inventory = sorted(Man2)

# Creating the full-inventory output file

with open('FullInventory.csv', 'w') as F_Inventory:
    FI_Data = csv.writer(F_Inventory)

    for data in range(0, len(Full_Inventory)):
        FI_Data.writerow(Full_Inventory[data])

# Laptop Inventory
for data in range(0, len(Man2)):
    if Man2[data][2] == "laptop":
        Laptop.append(Man2[data])

Laptop = sorted(Laptop)

with open('LaptopInventory.csv', 'w') as L_Inventory:
    Lap_Data = csv.writer(L_Inventory)

    for data in range(0, len(Laptop)):
        Lap_Data.writerow(Laptop[data])

# Tower Inventory
for data in range(0, len(Man2)):
    if Man2[data][2] == "tower":
        Tower.append(Man2[data])

with open('TowerInventory.csv', 'w') as T_Inventory:
    Tow_Data = csv.writer(T_Inventory)

    for data in range(0, len(Tower)):
        Tow_Data.writerow(Tower[data])

# Phone inventory

for data in range(0, len(Man2)):
    if Man2[data][2] == "phone":
        Phone.append(Man2[data])

with open('PhoneInventory.csv', 'w') as P_Inventory:
    Pho_Data = csv.writer(P_Inventory)

    for data in range(0, len(Phone)):
        Pho_Data.writerow(Phone[data])

# Past service inventory
for data in range(0, len(Man2)):
    if datetime.datetime.strptime(Man2[data][5], '%m/%d/%Y') < Date2:
        Past.append(Man2[data])

with open('PastServiceInventory.csv', 'w') as Past_Inventory:
    PDate_Data = csv.writer(Past_Inventory)

    for data in range(0, len(Past)):
        PDate_Data.writerow(Past[data])

# Damaged Data

for data in range(0, len(Man2)):
    if Man2[data][3] == "damaged":
        Damaged.append(Man2[data])

with open('DamagedInventory.csv', 'w') as D_Inventory:
    Dam_Data = csv.writer(D_Inventory)

    for x in range(0, len(Damaged)):
        Dam_Data.writerow(Damaged[x])

    # Part 2
    # Create user input code

    manufacturer_type = str(input('Enter Manufacturer type(q to exit): '))
    item_type = str(input('Enter item type: '))

# code checks if entered string value matches string value within file
# If there is a match of values it is appended to a new list "query"
    while manufacturer_type != 'q':
        for data in range(0, len(Full_Inventory)):
            if manufacturer_type in Full_Inventory[data]:
                if item_type in Full_Inventory[data]:
                    Query.append(Full_Inventory[data])
        # second query that outputs the same item type from all manufacturers
            if item_type in Full_Inventory[data]:
                Query2.append(Full_Inventory[data])

# If there is no match for entered string within file
# If Query list is empty then that must mean no match was found

        if len(Query) != 0:
            print('Your item is: ', Query)
            print('You may also consider: ', Query2)
        else:
            print('no such item in inventory')

    # once again ask for user input to continue code until q is entered

        manufacturer_type = str(input('Enter Manufacturer type: '))
        item_type = str(input('Enter item type: '))

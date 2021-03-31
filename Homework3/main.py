# Justino Cortez ID 1615245
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity,
                                         self.item_price, (self.item_price * self.item_quantity)))


if __name__ == "__main__":
    print("Item 1")
    item_1 = ItemToPurchase()
    item_2 = ItemToPurchase()

    item_1.item_name = input('Enter the item name:\n')
    item_1.item_price = int(input('Enter the item price:\n'))
    item_1.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')

    item_2.item_name = input('Enter the item name:\n')
    item_2.item_price = int(input('Enter the item price:\n'))
    item_2.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')

    item_1.print_item_cost()
    item_2.print_item_cost()

    total = ((item_1.item_price * item_1.item_quantity) +
             (item_2.item_price * item_2.item_quantity))

    print('\nTotal: ${}'.format(total))

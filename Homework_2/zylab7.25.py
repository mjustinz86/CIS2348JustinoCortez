# Justino Cortez ID 1615245

def exact_change(user_total):
    num_dollars = int(user_total / 100)
    user_total = user_total % 100
    num_quarters = int(user_total / 25)
    user_total = user_total % 25
    num_dimes = int(user_total / 10)
    user_total = user_total % 10
    num_nickels = int(user_total / 5)
    user_total = user_total % 5
    num_pennies = int(user_total / 1)
    user_total = user_total % 1
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == "__main__":
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val < 1:
        print('no change')
    else:
        if num_dollars > 1:
            print(num_dollars, 'dollars')
        elif num_dollars == 1:
            print(num_dollars, 'dollar')
        if num_quarters > 1:
            print(num_quarters, 'quarters')
        elif num_quarters == 1:
            print(num_quarters, 'quarter')
        if num_dimes > 1:
            print(num_dimes, 'dimes')
        elif num_dimes == 1:
            print(num_dimes, 'dime')
        if num_nickels > 1:
            print(num_nickels, 'nickels')
        elif num_nickels == 1:
            print(num_nickels, 'nickel')
        if num_pennies > 1:
            print(num_pennies, 'pennies')
        elif num_pennies == 1:
            print(num_pennies, 'penny')

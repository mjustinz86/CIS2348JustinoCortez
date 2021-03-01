# Justino Cortez ID 1615245
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
user_inputs = 0
while user_inputs != -1:
    try:
        user_input = input("Enter the month day, year: ")
    except IndentationError:
        continue
    try:
        date = user_input.split()
        amount = len(date)
        if amount != 3:
            continue
        month = date[0]
        day = date[1]
        year = date[2]
        day, comma = day.split(',')

        for x in range(12):
            if user_input.find(months[x]) >= 0:
                month = str(x + 1)
                ans = month + '/' + day + '/' + year
                print(ans)
                break
    except ValueError:
        continue

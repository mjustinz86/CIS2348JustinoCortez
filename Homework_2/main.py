# Justino Cortez ID 1615245
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
import_file = open(str(input()), 'r')
info_file = import_file.readline()
user_inputs = 0

for info_file in import_file:
    if info_file != -1:
        try:
            date = info_file.split()
            amount = len(date)
            if amount != 3:
                continue
            month = date[0]
            day = date[1]
            year = date[2]
            day, comma = day.split(',')

            for x in range(12):
                if info_file.find(months[x]) >= 0:
                    month = str(x + 1)
                    ans = month + '/' + day + '/' + year
                    print(ans)
                    break
        except ValueError:
            continue
    else:
        break

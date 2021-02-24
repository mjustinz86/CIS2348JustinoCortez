# Justino Cortez ID 1615245
def new_password(password):
    password = password.replace('i', '!')
    password = password.replace('a', '@')
    password = password.replace('m', 'M')
    password = password.replace('B', '8')
    password = password.replace('o', '.')
    password = password + 'q*s'
    return password


word = str(input())
print(new_password(word))

# Justino Cortez ID 1615245
def get_age() -> object:
    age = int(input())
    if 18 <= age <= 75:
        return age
    else:
        raise ValueError('Invalid age')


def fat_burning_heart_rate(age):
    heart_rate = .70 * (220 - age)
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        print('Fat burning heart rate for a', age, 'year-old:',
              fat_burning_heart_rate(age), 'bpm')
    except ValueError:
        print('Invalid age.')
        print('Could not calculate heart rate info.\n')

# Justino Cortez ID 1615245
def string_check(word):
    word1 = word.replace(' ', '')
    r_word = "".join(reversed(word1))
    if word1 == r_word:
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')


x = str(input())
string_check(x)

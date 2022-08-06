def reverse(text):
    return text[::-1]


def is_palindrome(text):
    if text == reverse(text):
        print('This is a palindrome!')
    else:
        print('This is not a palindrome!')


something = input('Please input a word: ')
is_palindrome(something)

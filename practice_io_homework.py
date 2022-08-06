def reverse_and_check(text):
    check = (',', '.', ' ')
    ans = ''
    text = text.lower()
    for i in text[::1]:
        # check if the word(referred as x) is in the tuple called check
        if i not in check:
            ans = ans + i
    ans_reverse = ans[::-1]
    if ans_reverse == ans:
        print('This is a palindrome!')
    else:
        print('This is not a palindrome!')


something = input('Please input a word: ')
reverse_and_check(something)

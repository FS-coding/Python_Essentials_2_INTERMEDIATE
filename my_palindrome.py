def palindrome(text):
    pal = False
    text = text.strip().replace(" ", "").lower()
    hlf = len(text) // 2
    if len(text) % 2 == 1:
        # check if first half equals second half reversed
        # ignore middle
        if text[:hlf] == text[-1:hlf:-1]:
            pal = True
    else:
        # check if first half equals second half reversed
        # move half for second part
        if text[:hlf] == text[-1:hlf-1:-1]:
            pal = True

    if pal:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


#palindrome("    I am legend")
palindrome("Ten animals I slam in a net")
palindrome("Eleven animals I slam in a net")

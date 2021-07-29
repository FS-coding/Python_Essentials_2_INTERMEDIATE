
def caesar_complex(cipher, value):

    #cipher = input('Enter your text: ')
    #value = int(input('Enter cypher shift: '))
    if not (value > 0 and value <= 25):
        print('Enter a number (1-25)')
        return
    text = ''
    for char in cipher:
        if not char.isalpha():
            text += char
            continue

        char_c = ord(char)

        # 65-90 A-Z
        if char_c <= ord('Z'):
            code = char_c + value
            if code > ord('Z'):
                code = code-26

        # 97-122 a-z
        if char_c >= ord('a'):
            code = char_c + value
            if code > ord('z'):
                code = code-26

        #print(char + " " + str(char_c) + " " + str(code))
        text += chr(code)

    print(text)


caesar_complex("abc xyz ABC xyz 123", 2)
# cde zab CDE zab 123

caesar_complex("The die is cast", 25)
# Sgd chd hr bzrs
# 83 103 100

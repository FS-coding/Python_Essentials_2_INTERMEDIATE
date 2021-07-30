def digi(number):
    if isinstance(number, int):
        life = 0
        number = str(number)
        # format can be YYYYMMDD, DDDMMYYY, MMDDYYYY
        # Don't use leading 0 for MM or DD: 07 -> 7
        if len(number) == 8 or len(number) == 7:
            for digit in [int(i) for i in number]:
                life += digit

    else:
        print("Enter a valid date")

    print(life)


digi(30072021)
digi(20210730)

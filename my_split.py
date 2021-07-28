# 2.3.1.18 Your own split

def mysplit(st):
    split_string = []

    if st == "":
        return []

    spaces = []

    for k, ch in enumerate(st):
        if ch.isspace():
            spaces.append(k)
    spaces.append(len(st))

    i = 0
    for space in range(len(spaces)):
        j = spaces[space]
        #print("i: " + str(i) + ", j: " + str(j))
        if i != j:
            word = st[i:j]
            split_string.append(word)
        i = j+1
    return split_string


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit("abc"))
print(mysplit(""))

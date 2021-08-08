# 4.3.1.15 LAB: Character frequency histogram
# 4.3.1.16 LAB: Sorted character frequency histogram

#  write a program which:

# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
# prints a simple histogram in alphabetical order (only non-zero counts should be presented)
# Create a test file for the code, and check if your histogram contains valid results.

# the output histogram will be sorted based on the characters' frequency
# (the bigger counter should be presented first)
# the histogram should be sent to a file with the same name as the input one,
# but with the suffix '.hist' (it should be concatenated to the original name)

# Use a lambda to change the sort order.
from os import strerror

dic = {}


def dic_add(dic, key):
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] = dic.get(key) + 1


def dic_sort(dic):
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return sorted_dic


def get_base(file):
    base_i = file.find(".txt")
    base = file[:base_i]
    return base


def out_file(f_base, data):
    try:
        o = open(f_base + ".hist.txt", 'wt')
        for d in data:
            d = str(d).replace("(", "")
            d = str(d).replace(")", "")
            d = str(d).replace(",", ":")
            o.write(str(d) + "\n")
        o.close()
        print("File written")

    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))


try:
    #f_in = input("Enter file name: ")
    f_in = 'samplefile.txt'
    f_base = get_base(f_in)

    # read
    s = open(f_in, 'rt')
    lines = s.readlines()
    # while line != '':
    for line in lines:
        for ch in line:
            # print(ch) # debug
            if ch.isalpha():
                dic_add(dic, ch.lower())
    s.close()

    # output
    s_d = dic_sort(dic)
    print(s_d)
    out_file(f_base, s_d)

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

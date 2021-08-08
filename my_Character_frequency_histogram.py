# 4.3.1.15 LAB: Character frequency histogram

#  write a program which:

# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
# prints a simple histogram in alphabetical order (only non-zero counts should be presented)
# Create a test file for the code, and check if your histogram contains valid results.


from os import strerror

dic = {}


def dic_add(dic, key):
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] = dic.get(key) + 1


try:
    f_in = input("Enter file name: ")
    #f_in = 'samplefile.txt'
    s = open(f_in, 'rt')
    lines = s.readlines()
    # while line != '':
    # for i in range(1):
    for line in lines:
        for ch in line:
            # print(ch) # debug
            if ch.isalpha():
                dic_add(dic, ch.lower())
    s.close()
    print(dic)

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# 4.3.1.17 LAB: Evaluating students' results
# Each line of the file contains three elements:
# the student's first name,
# the student's last name, and
# the number of point the student received during certain classes.

# The elements are separated with white spaces. Each student may appear more than once

# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew Cox	1.5

# write a program which:

# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report Name Points:

# program must be fully protected against all possible failures:
# the file's non-existence,
# the file's emptiness,
# or any input data failures;
# encountering any data error should cause immediate program termination, and
# the erroneous should be presented to the user;

# implement and use your own exceptions hierarchy
# Use a dictionary to store the students' data.

from os import strerror
import errno


class StudentsDataException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("Error: ", strerror(e.errno))
        exit(e.errno)


class BadLine(StudentsDataException):
    pass


class FileEmpty(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)
        self.err = err


dic = {}


def dic_add(dic, key, val):
    if key not in dic:
        dic[key] = val
    else:
        dic[key] = dic.get(key) + val


def dic_sort(dic):
    sorted_dic = sorted(dic.items(), key=lambda x: x[0], reverse=False)
    return sorted_dic


def get_base(file):
    base_i = file.find(".txt")
    base = file[:base_i]
    return base


def out_file(f_base, data):
    try:
        o = open(f_base + ".report.txt", 'wt')
        for d in data:
            # print(d)
            d = str(d).replace("'", "")
            d = str(d).replace("(", "")
            d = str(d).replace(")", "")
            print(d)
            o.write(str(d) + "\n")
        o.close()
        print("** File written **")

    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))


try:
    #f_in = input("Enter file name: ")
    f_in = 'samplefile.txt'
    s = open(f_in, 'rt')

except IOError as e:
    raise StudentsDataException

try:
    f_base = get_base(f_in)
    lines = s.readlines()
    if lines == []:
        raise FileEmpty("File is empty!")

    for line in lines:
        words = line.split()
        name = ""
        points = 0
        for word in words:
            if word.isalpha():
                name = name + " " + word
                name = name.lstrip()
            else:
                points += float(word)

        dic_add(dic, name, points)
    s.close()

    # output
    s_d = dic_sort(dic)
    # print(s_d)
    out_file(f_base, s_d)


except FileEmpty as e:
    print(e)

except ValueError as e:
    print("Bad line!")

except IOError as e:
    print("Error: ", strerror(e.errno))
    exit(e.errno)

def my_sudo(list_i):
    sudok = True
    # check rows

    def check_row(list, n_i):
        rws = True
        n = str(n_i)
        for row in list:
            count = 0
            for col in row:
                if col == n:
                    count += 1
            if count != 1:
                rws = False
        return rws

    # check cols
    def check_col(list, n_i):
        n = str(n_i)
        cls = True
        for i in range(9):
            count_2 = 0
            for row in list:
                if row[i] == n:
                    count_2 += 1
            if count_2 != 1:
                cls = False
        return cls

  # blocks
    def check_blocks(list, n_i):
        blcks = True
        n = str(n_i)
        for rows in range(0, 9, 3):
            for cols in range(0, 9, 3):
                count_3 = 0
                for j in range(3):
                    for i in range(3):
                        x = list[rows+j][cols+i]
                        if x == n:
                            count_3 += 1
                if count_3 != 1:
                    blcks = False
        return blcks

    # main
    list = []
    for row in list_i:
        list.append(str(row))

    # call functions
    for i in range(1, 10):
        if not check_row(list, i) or not check_col(list, i) or not check_blocks(list, i):
            sudok = False
            break

    if sudok:
        print("Yes")
    else:
        print("No")


my_sudo([295743861, 431865927, 876192543, 387459216,
         612387495, 549216738, 763524189, 928671354, 154938672])
my_sudo([195743862, 431865927, 876192543, 387459216,
         612387495, 549216738, 763524189, 928671354, 254938671])

def reading():
    f = open(r'C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\poem(my mother at sixty six).txt', 'r')

    first_line = f.readline()
    sec_line = f.readline()
    entire_file = f.read(10)
    line_by_line = f.readlines()

    print(first_line, end='')
    print(sec_line)
    print()
    print(entire_file)
    print()
    print(line_by_line)


def prob_5_1():
    f = open(r"C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\poem(my mother at sixty six).txt", 'r')

    file = f.read()
    print("File size = ", len(file))


def prob_5_2():
    f = open(r"C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\poem(my mother at sixty six).txt", 'r')

    lines = f.readlines()
    print("The number of the lines = ", len(lines))


# reading()
# prob_5_1()
# prob_5_2()

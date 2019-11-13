def print_rectangle(rows,columns):
    for i in range(0,rows):
        line_to_be_printed = ""
        for j in range(0,columns):
            line_to_be_printed += "*"
        print(line_to_be_printed)

print_rectangle(6,5)
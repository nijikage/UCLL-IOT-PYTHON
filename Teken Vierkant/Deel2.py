def print_rectangle(rows,columns):
    for i in range(0,rows):
        line_to_be_printed = ""
        for j in range(0,columns):
            if(i == 0 or i == (rows-1) or j == 0 or j == (columns-1)):
                line_to_be_printed += "*"
            else:
                line_to_be_printed += " "
        print(line_to_be_printed)

print_rectangle(6,5)
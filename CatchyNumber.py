def char_to_num(chunk):
    i = len(chunk)
    dex = 0
    while i > 0:
        if chunk[dex] == 'A' or chunk[dex] == 'B' or chunk[dex] == 'C':
            print('2', end='')
        elif chunk[dex] == 'D' or chunk[dex] == 'E' or chunk[dex] == 'F':
            print('3', end='')
        elif chunk[dex] == 'G' or chunk[dex] == 'H' or chunk[dex] == 'I':
            print('4', end='')
        elif chunk[dex] == 'J' or chunk[dex] == 'K' or chunk[dex] == 'L':
            print('5', end='')
        elif chunk[dex] == 'M' or chunk[dex] == 'N' or chunk[dex] == 'O':
            print('6', end='')
        elif chunk[dex] == 'P' or chunk[dex] == 'Q' or chunk[dex] == 'R' or chunk[dex] == 'S':
            print('7', end='')
        elif chunk[dex] == 'T' or chunk[dex] == 'U' or chunk[dex] == 'V':
            print('8', end='')
        elif chunk[dex] == 'W' or chunk[dex] == 'X' or chunk[dex] == 'Y' or chunk[dex] == 'Z':
            print('9', end='')
        dex += 1
        i -= 1
        


catchy_number = input("Enter your catchy phone number in this format XXX-XXX-XXXX:\n")

num_chunks = catchy_number.split('-')

print(num_chunks[0] + '-', end ='')
char_to_num(num_chunks[1])
print('-', end='')
char_to_num(num_chunks[2])

full_name = input("Please enter your full name:\n")
print()

name_pieces = full_name.split(' ')
print("%1s. %1s. %1s." % (name_pieces[0][0], name_pieces[1][0], name_pieces[2][0]))

arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))


if arrow_base_width >= arrow_head_width:
    while arrow_base_width >= arrow_head_width:
        arrow_head_width = int(input('Enter arrow head width:\n'))
print('')

# Draw arrow base (height = 3, width = 2)
while arrow_base_height > 0:
    for num in range(arrow_base_width):
        print('*', end = '')   
    arrow_base_height -= 1
    print()

# Draw arrow head (width = 4)
while arrow_head_width > 0:
    for num in range(arrow_head_width):
        print('*', end = '')
    arrow_head_width -= 1
    print()
    


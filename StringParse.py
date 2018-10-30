#defines the variable user_string with a blank space
user_string = ' '

#begins a while loop that can be exited with 'q'
while user_string != 'q':

    #prompts user to input a sting
    user_string = input("Enter input string:\n")

    #if the user's string is q, break the loop
    if user_string == 'q':
        break

    #prints error if there is no comma in the user's string
    elif user_string.count(',') < 1:
        print("Error: No comma in string.")
        print()

    #Else the string is processed and split.
    else:
        user_string = user_string.replace(' ', '')
        split_string = user_string.split(',')
        print("First word:", split_string[0])
        print("Second word:", split_string[1])
        print()

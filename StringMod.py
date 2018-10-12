#Defines the get_num_characters() function, which counts the characters in a string.
def get_num_of_characters(inputStr):
    char_count = 0
    for char_num in inputStr: 
        char_count += 1
    return char_count

#defines the output_without_whitespace() function which replaces spaces and tabs with no space.
def output_without_whitespace(inputStr):
    inputStrFirst = inputStr.replace(' ', '')
    no_space_string = inputStrFirst.replace('\t', '')
    return no_space_string
    
if __name__ == '__main__':
    # Type your code here
    usr_str = input("Enter a sentence or phrase:\n")
    print()
    print('You entered:', usr_str)
    print()
    print('Number of characters:', get_num_of_characters(usr_str))
    print('String with no whitespace:', output_without_whitespace(usr_str))

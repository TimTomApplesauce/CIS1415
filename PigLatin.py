def to_pig_latin(usr_str):
    split_str = usr_str.split(' ')
    for word in split_str:
        first_letter = word[0]
        word = word[1:]
        print(word + first_letter + 'ay', end =' ')
    print()
    return
        

user_string = input("Please enter a sentance to convert to Pig Latin:\n")


print("English:", user_string)
pig_latin = to_pig_latin(user_string)

def num_vowels(usr_str):
    vowels = 'aAeEiIoOuU'
    num = 0

    for char in usr_str:
        for v in vowels:
            if char == v:
                num += 1
            else:
                num += 0
    return num

def num_consonants(usr_str):
    cons = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
    num = 0

    for char in usr_str:
        for c in cons:
            if char == c:
                num += 1
            else:
                num += 0
    return num

user_string = input("Please enter a string:\n")
print()
vowel_num = num_vowels(user_string)
cons_num = num_consonants(user_string)
print("Number of vowels:", vowel_num)
print("Number of consonants:", cons_num)

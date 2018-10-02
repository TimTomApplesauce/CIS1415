#importing random
import random

#declaring a dictionary storage for dice roll totals
roll_totals = {
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,
    11 : 0,
    12 : 0
}

#Declaring dice and dice total variables
die1 = 0
die2 = 0
dice_total = 0

#prompting user for number of dice rolls
roll_num = int(input('How many dice rolls?'))
print()

#start loop if user input is greater than or equal to 1
while roll_num >= 1:

    #nested loop that loops user determined times
    for num in range(roll_num):

        #rolls dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)

        #totals dice
        dice_total = die1 + die2

        #increments dict with dice total value by 1
        roll_totals[dice_total] += 1
    #prompts user to input number of dice rolls again
    roll_num = int(input('How many dice rolls?'))
    print()

#begin dice roll histogram printing
print('Dice roll histogram:')
print()

#prints '*' for value range stored in roll_totals[2]
print('2s:', end = '  ')
for num in range(roll_totals[2]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[3]
print('3s:', end = '  ')
for num in range(roll_totals[3]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[4]
print('4s:', end = '  ')
for num in range(roll_totals[4]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[5]
print('5s:', end = '  ')
for num in range(roll_totals[5]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[6]
print('6s:', end = '  ')
for num in range(roll_totals[6]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[7]
print('7s:', end = '  ')
for num in range(roll_totals[7]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[8]
print('8s:', end = '  ')
for num in range(roll_totals[8]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[9]
print('9s:', end = '  ')
for num in range(roll_totals[9]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[10]
print('10s:', end = ' ')
for num in range(roll_totals[10]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[11]
print('11s:', end = ' ')
for num in range(roll_totals[11]):
    print('*', end ='')
print()

#prints '*' for value range stored in roll_totals[12]
print('12s:', end = ' ')
for num in range(roll_totals[12]):
    print('*', end ='')
print()

        
    
            
    

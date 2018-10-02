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

while roll_num >= 1:
    for num in range(roll_num):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice_total = die1 + die2
        roll_totals[dice_total] += 1
    roll_num = int(input('How many dice rolls?'))
    print()

print('Dice roll histogram:')
print()

print('2s:', end = '  ')
for num in range(roll_totals[2]):
    print('*', end ='')
print()

print('3s:', end = '  ')
for num in range(roll_totals[3]):
    print('*', end ='')
print()

print('4s:', end = '  ')
for num in range(roll_totals[4]):
    print('*', end ='')
print()

print('5s:', end = '  ')
for num in range(roll_totals[5]):
    print('*', end ='')
print()

print('6s:', end = '  ')
for num in range(roll_totals[6]):
    print('*', end ='')
print()

print('7s:', end = '  ')
for num in range(roll_totals[7]):
    print('*', end ='')
print()

print('8s:', end = '  ')
for num in range(roll_totals[8]):
    print('*', end ='')
print()

print('9s:', end = '  ')
for num in range(roll_totals[9]):
    print('*', end ='')
print()

print('10s:', end = ' ')
for num in range(roll_totals[10]):
    print('*', end ='')
print()

print('11s:', end = ' ')
for num in range(roll_totals[11]):
    print('*', end ='')
print()

print('12s:', end = ' ')
for num in range(roll_totals[12]):
    print('*', end ='')
print()

        
    
            
    

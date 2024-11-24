numbOfBottles = int(input("Enter number of bottles: "))

while numbOfBottles >0:
    totalBottlesOnTheWall = numbOfBottles - 1
    print (f'{numbOfBottles} bottles of beer on the wall, {numbOfBottles} bottles of beer.')
    print (f'Take one down and pass it around, {totalBottlesOnTheWall} bottle(2) of beer on the wall.')
    numbOfBottles = numbOfBottles - 1

print('Time to buy more bottles of beer.')
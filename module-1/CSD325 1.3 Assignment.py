# Weihao
#11/24/2024
#CSD325-T301 1.3 Assignment
#The purpose of the code is to utilize the song "100 bottles of beer on the wall" game to practice my python code

#Input the Number Of Bottles
numbOfBottles = int(input("Enter number of bottles: "))

#While Number of Bottles are greater than 0, the game continues, else game ends.
while numbOfBottles >0:
    totalBottlesOnTheWall = numbOfBottles - 1
    print (f'{numbOfBottles} bottles of beer on the wall, {numbOfBottles} bottles of beer.')
    print (f'Take one down and pass it around, {totalBottlesOnTheWall} bottle(2) of beer on the wall.')
    numbOfBottles = numbOfBottles - 1

print('Time to buy more bottles of beer.')
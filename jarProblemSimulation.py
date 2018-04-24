#Claire Yegian and Lea Adams-Blackmore
#4/24/18
#jarProblemSimulation.py - simulations to test jar problem answers

from random import randint

guess = input('Enter your guess (red or green: ')
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))
red = randint(1,N)
green = N - red

marbleList = []
item = 0
while item <= red:
    marbleList.append(1)
    item += 1

item2 = 0
while item2 <= green:
    marbleList.append(2)
    item2 += 1

print(marbleList)

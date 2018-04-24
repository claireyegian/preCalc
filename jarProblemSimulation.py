#Claire Yegian and Lea Adams-Blackmore
#4/24/18
#jarProblemSimulation.py - simulations to test jar problem answers

from random import randint

"""guess = input('Enter your guess (red or green): ')
if guess == 'red':
    guess = 1
elif guess == 'green':
    guess = 2
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))"""

guess = 1
N = 10
W = 10

runs = 0
while runs <= 50:
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
    
    pick = randint(0,N-1)
    marblePicked = marbleList[pick]
    
    print(marblePicked)
    
    wins = 0
    if guess != marblePicked:
        wins += 1
    runs += 1

print(wins)
#Claire Yegian and Lea Adams-Blackmore
#4/24/18
#jarProblemSimulation.py - simulations to test jar problem answers

from random import randint

runs = 0
while runs <= 50:
    guess = input('Enter your guess (red or green): ')
    if guess == 'red':
        guess = 1
    elif guess == 'green':
        guess = 2
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
    
    pick = randint(0,N-1)
    marblePicked = marbleList[pick]
    
    wins = 0
    if guess == marblePicked:
        wins += 1

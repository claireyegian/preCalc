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
W = int(input('Enter the monetary prize: '))

runs = 0
wins = 0
while runs <= 1000:
    red = randint(0,N)
    green = N - red
    
    marbleList = []
    item = 0
    while item < green:
        marbleList.append(2)
        item += 1
    
    item2 = 0
    while item2 < red:
        marbleList.append(1)
        item2 += 1
    
    pick = randint(0,N-1)
    marblePicked = marbleList[pick]
    
    if guess == marblePicked:
        wins += 1
    runs += 1

print(wins)"""


N = 20
W = 10
wins1 = 0
runs1 = 0
while runs1 <= 1000:
    red1 = randint(0,N)
    green1 = N - red1
      
    marbleList1 = []
    item1 = 0
    while item1 < green1:
        marbleList1.append(2)
        item1 += 1
        
    item3 = 0
    while item3 < red1:
        marbleList1.append(1)
        item3 += 1
    
    pick1 = randint(0,N-1)
    guess1 = marbleList1[pick1]
    
    pick2 = randint(0,N-1)
    marblePicked1 = marbleList1[pick2]
    
    if guess1 == marblePicked1:
        wins1 += 1
    
    runs1 += 1
print(wins1)

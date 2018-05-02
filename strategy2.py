#Claire Yegian and Lea Adams-Blackmore
#4/30/18
#strategy2.py - finds exact value for D and creates simulation for strategy 2 (guess green)

from random import randint

#Exact value
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))

subtractN = 0
sumValues = 0
while subtractN <= N:
    sumValues += (((N - subtractN)/N)*W)
    subtractN += 1

print('The game will cost',sumValues/(N + 1),'dollars to play if you guess green')
print('D equals $',sumValues/(N + 1))

#Simulation
guess = 2
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

print(wins)

#Claire Yegian and Lea Adams-Blackmore
#4/23/18
#strategy1.py - finds exact value for D and creates simulation for strategy 1 (guess red)

from random import randint

N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))

subtractN = 0
sumValues = 0
while subtractN <= N:
    sumValues += (((N - subtractN)/N)*W)
    subtractN += 1

print(' ')
print('Theoretical:')
print('The game will cost',sumValues/(N + 1),'dollars to play if you guess red.')
print('D equals $',sumValues/(N + 1),'(',((sumValues/(N + 1))/W)*100,'% of the monetary prize)')

#Simulation
guess = 1
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

print(' ')
print('Simulation:')
print('You won',wins,'times out of 1000 or',wins/10,'percent of the time.')

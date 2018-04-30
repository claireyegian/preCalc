#Claire Yegian and Lea Adams-Blackmore
#4/23/18
#jarProblem.py - calculates fair costs for different strategies of jar game

from random import randint

#Strategy 1: Guess red
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))

subtractN = 0
sumValues = 0
while subtractN <= N:
    sumValues += (((N - subtractN)/N)*W)
    subtractN += 1

print('The game will cost',sumValues/(N + 1),'dollars to play if you guess red')
print('The game will cost',sumValues/(N + 1),'dollars to play if you guess green')

D = sumValues/(N + 1)
Nsubtract = 0
sumNValues = 0
while Nsubtract < N:
    sumNValues += ((N - Nsubtract)/N)
    Nsubtract += 1
print((sumNValues/N))

sumprobred = 0
sumprobgreen = 0
red = randint(0,N)
green = N - red
Rruns = 0
Gruns = 0
while Rruns < red:
    sumprobred += (red/N)
    Rruns += 1

while Gruns < green:
    sumprobgreen += (green/N)
    Gruns += 1

print(((sumprobred)**2 + (sumprobgreen)**2))

"""Nsubtract1 = 0
sumProbability = 0
while Nsubtract1 < N:
    sumProbability += ((Nsubtract1/N)^2 + (((Nsubtract1/N)^2)*(N - Nsubtract1)/N))
    Nsubtract1 += 1

print(sumProbability)"""

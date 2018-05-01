#Claire Yegian and Lea Adams-Blackmore
#4/23/18
#jarProblem.py - calculates fair costs for different strategies of jar game

from random import randint

"""#Strategies 1 and 2: Guess red/green
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
print((sumNValues/N)*W)"""

"""#Strategy 3: pay P above D
N = 10
W = 10
sumprobred = 0
sumprobgreen = 0
Rruns = 0
Rsubtract = 0
Gruns = 0
Gsubtract = 0
while Rruns < N:
    sumprobred += (((N - Rsubtract)/N)**2)
    print((N - Rsubtract)/N)
    Rruns += 1
    Rsubtract += 1

while Gruns < N:
    sumprobgreen += (((N - Gsubtract)/N)**2)
    Gruns += 1
    Gsubtract += 1

print((sumprobred/N) + (sumprobgreen/N))"""

"""#Strategy 4: pay R above D
N = 10
W = 10
marbleList = []
runs = 0
while runs <= N:
    marbleList.append([runs, N - runs])
    runs += 1
sumProb = 0
for item in marbleList:
    red = item[0]
    green = item[1]
    sumProb += ((red/N)**3 + (green/N)**3 + 2*(((red/N)**3)*(green/N)) + 2*(((red/N)**3)*(green/N)))
print(sumProb/(N + 1))"""

#Strategy 5: pay S above D
N = 10
W = 10
marbleList = []
runs = 0
while runs <= N:
    marbleList.append([runs, N - runs])
    runs += 1
sumProb = 0
for item in marbleList:
    red = item[0]
    green = item[1]
    if red >= 3 and green >= 3:
        sumProb += (((red/N)*((red-1)/(N-1))*((red-2)/(N-2))) + ((green/N)*((green-1)/(N-1))*((green-2)/(N-2))) + 2*((red/N)*((red-1)/(N-1))*((red-2)/(N-2)))(green/(N-3))) + 2*((green/N)*((green-1)/(N-1))*((green-2)/(N-2)))(red/(N-3)))
print(sumProb/(N + 1))







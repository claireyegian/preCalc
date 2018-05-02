#Claire Yegian and Lea Adams-Blackmore
#4/30/18
#strategy4.py - finds exact value for R and D and creates simulation for strategy 4 (pay R above D)

from random import randint

#Exact value
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))
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
print('You will pay',(sumProb/(N + 1))*W - (W/2),'dollars extra.')
print('P equals $',(sumProb/(N + 1))*W - (W/2),', and D equals $',(W/2))

#Simulation
wins2 = 0
runs2 = 0
while runs2 <= 1000:
    red2 = randint(0,N)
    green2 = N - red2
    
    marbleList2 = []
    item4 = 0
    while item4 < green2:
        marbleList2.append(2)
        item4 += 1
        
    item5 = 0
    while item5 < red2:
        marbleList2.append(1)
        item5 += 1
    
    guess2 = marbleList2[randint(0,N-1)]
    guess3 = marbleList2[randint(0,N-1)]
    if guess2 == guess3:
        finalGuess = guess2
    elif guess2 != guess3:
        finalGuess = marbleList2[randint(0,N-1)]
    marblePicked2 = marbleList2[randint(0,N-1)]
    
    if finalGuess == marblePicked2:
        wins2 += 1

    runs2 += 1
print(wins2)

print('You won',wins2,'times out of 1000 or',wins2/10,'percent of the time.')

#Claire Yegian and Lea Adams-Blackmore
#4/30/18
#strategy5.py - finds exact value for S and D and creates simulation for strategy 5 (pay S above D)

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
    if red >= 3 and green >= 3:
        sumProb += (((red/N)*((red-1)/(N-1))*((red-2)/(N-2))) + ((green/N)*((green-1)/(N-1))*((green-2)/(N-2))) + ((red/N)*((green)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))) + ((red/N)*((green)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))) + ((green/N)*(red/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))) + ((green/N)*(red/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))))
    elif red < 3 and red >= 1:
        sumProb += (((green/N)*((green-1)/(N-1))*((green-2)/(N-2))) + ((red/N)*((green)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))) + ((green/N)*(red/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))))
    elif red <1:
        sumProb += ((green/N)*((green-1)/(N-1))*((green-2)/(N-2)))
    elif green < 3 and green >= 1:
        sumProb += (((red/N)*((red-1)/(N-1))*((red-2)/(N-2))) + ((red/N)*((green)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))) + ((green/N)*(red/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))))
    elif red <1:
        sumProb += ((red/N)*((red-1)/(N-1))*((red-2)/(N-2)))
print('You will pay',(sumProb/N)*W - (W/2),'dollars extra.')
print('P equals $',(sumProb/N)*W - (W/2),', and D equals $',(W/2))

#Simulation
w5ins = 0
r5uns = 0
while r5uns <= 1000:
    r5ed = randint(0,N)
    g5reen = N - r5ed
    
    m5arbleList = []
    i1tem = 0
    while i1tem < g5reen:
        m5arbleList.append(2)
        i1tem += 1
        
    i2tem = 0
    while i2tem < r5ed:
        m5arbleList.append(1)
        i2tem += 1
    
    g1uess = m5arbleList[randint(0,2)]
    
    g2uess = m5arbleList[randint(6,9)]
    if g1uess == g2uess:
        f5inalGuess = g1uess
    elif g1uess != g2uess:
        f5inalGuess = m5arbleList[randint(3,5)]
    m5arblePicked = m5arbleList[randint(0,N-1)]
    
    if f5inalGuess == m5arblePicked:
        w5ins += 1

    r5uns += 1
print('You won',w5ins,'times out of 1000 or',w5ins/10,'percent of the time.')
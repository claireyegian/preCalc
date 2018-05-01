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


"""N = 8
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
    
    guess1 = marbleList1[randint(0,N-1)]
    marblePicked1 = marbleList1[randint(0,N-1)]
    
    if guess1 == marblePicked1:
        wins1 += 1

    runs1 += 1
print(wins1)"""

"""N = 10
W = 10
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
print(wins2)"""

N = 10
W = 10
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
    
    g1uess = m5arbleList[randint(0,N-1)]
    g2uess = m5arbleList[randint(0,N-1)]
    if g1uess == g2uess:
        f5inalGuess = g1uess
    elif g1uess != g2uess:
        f5inalGuess = m5arbleList[randint(0,N-1)]
    m5arblePicked = m5arbleList[randint(0,N-1)]
    
    if f5inalGuess == m5arblePicked:
        w5ins += 1

    r5uns += 1
print(w5ins)
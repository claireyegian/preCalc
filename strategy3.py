#Claire Yegian and Lea Adams-Blackmore
#4/30/18
#strategy3.py - finds exact value for D and P and creates simulation for strategy 3 (pay P above D)

from random import randint

#Exact value
N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))
sumprobred = 0
sumprobgreen = 0
Rruns = 0
Rsubtract = 0
Gruns = 0
Gsubtract = 0
while Rruns < N:
    sumprobred += (((N - Rsubtract)/N)**2)
    Rruns += 1
    Rsubtract += 1

while Gruns < N:
    sumprobgreen += (((N - Gsubtract)/N)**2)
    Gruns += 1
    Gsubtract += 1
P = ((sumprobred/N) + (sumprobgreen/N))*W - (W/2)
D = (W/2)

print(' ')
print('Theoretical: ')
print('You will pay',((sumprobred/N) + (sumprobgreen/N))*W - (W/2),'dollars extra.')
print('P equals $',P,', and D equals $',D, 'The total cost is', (P + D) , 'or', ((P + D)/W)*100, 'percent of the total monetary prize')

#Simulation
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

print(' ')
print('Simulation: ')
print('You won',wins1,'times out of 1000, or',(wins1/10),'percent of the time')
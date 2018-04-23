#Claire Yegian and Lea Adams-Blackmore
#4/23/18
#jarProblem.py - calculates fair costs for different strategies of jar game

N = int(input('Enter the number of marbles: '))
W = int(input('Enter the monetary prize: '))

subtractN = 0
sumNvalues = 0
while subtractN <= N:
    sumNvalues += (N - subtractN)
    subtractN += 1

print(sumNvalues)
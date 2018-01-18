#Claire Yegian
#1/18/18
#loopDemo.py - how to use a loop

"""for i in range(1,101):
    if '7' in str(i) or i%7==0:
        print('Buzz')
    else:
        print(i)"""

i = 1
while i <= 100:
    if '7' in str(i) or i%7==0:
        print('Buzz')
    else:
        print(i)
    i += 1
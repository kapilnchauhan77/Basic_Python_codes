import random
a=random.randint(1,21)
b=int(input('How many chances You want?:'))
for i in range(0,b):
    c=int(input('Guess from 1 to 20:'))
    if c==a:
        print('You win')
        break
    else:
        print('Sorry try guessing again')
        i=i+1
if i==b:
    print('You lose, the number is',a)

a=input('Height:')
while a=='':
    a=input("Enter a valid number:")
b=int(a)
for i in range(0,b):
    for j in range(0,b-i):
        print(' ',end='')
    for k in range(0,2*i+1):
        print('0',end='')
    print('')
    

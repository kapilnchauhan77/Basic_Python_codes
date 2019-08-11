a=0
b=1
print(a,end='')
print(' ',b,end='')
for i in range(1,19):
    a=a+b
    b=a+b
    print(' ',a,end='')
    print(' ',b,end='')

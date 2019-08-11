a=input('Word:')
b=0
c=len(a)-1
while b<=c:
    if a[b]!=a[c]:
        break
    b=b+1
    c=c-1
if b>=c:
    print('palindrome')
else:
    print('sorry')

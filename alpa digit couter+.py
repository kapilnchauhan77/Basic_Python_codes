a=input('Line:')
b=c=0
d=e=0
for i in a:
    if i.islower():
        b=b+1
    elif i.isupper():
        c=c+1
    if i.isalpha():
        d=d+1
    elif i.isdigit():
        e=e+1
print('No. of lowercase alphabets:',b)
print('No. of uppercase alphabets:',c)
print('No of alphabets:',d)
print('No of digits:',e)

def binary_search(l, n):
    if len(l)==0 and l!=n:
        print(q, 'is not in the array')
    else:
        r=0
        lt=len(l)-1
        while r<=lt:
           m=(r+lt)//2
           if l[m]>n:
               lt=m-1
           elif l[m]<n:
               r=m+1
           elif l[m]==n:
               print(q, 'is in the array at', m+1)
               break
        else:
            print('sad')


a=[i for i in range(1,11)]
for j in range(10):
    q=int(input('Number='))
    binary_search(a,q)
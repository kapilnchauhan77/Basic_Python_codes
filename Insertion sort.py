def insort(l):
    for i in range(1,len(l)):
        v=l[i]
        j=i
        while l[j-1]>v and j>=1:
            l[j]=l[j-1]
            j-=1
        l[j]=v
lt=[7,9,8,4,1,4,7,7,9,2]
insort(lt)
print(lt)
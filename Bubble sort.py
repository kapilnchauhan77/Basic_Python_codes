def bs(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
lt=[7,9,8,4,1,4,7,7,9,2]
bs(lt)
print(lt)
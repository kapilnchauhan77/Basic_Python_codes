def st(l):
    for i in range(len(l)):
        cp = i
        for j in range(i+1, len(l)):
            if l[cp] > l[j]:
                cp = j
        l[i], l[cp] = l[cp], l[i]


lt = [7, 9, 8, 4, 1, 4, 7, 7, 9, 2]
st(lt)
print(lt)

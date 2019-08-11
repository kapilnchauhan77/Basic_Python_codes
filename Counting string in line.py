line=input('Line:')
Word=input('Word:')
lengthline=len(line)
lengthword=len(Word)
start=count=0
while 1>0:
    positionword=line.find(Word,start,lengthline)
    if positionword!=-1:
        count=count+1
        start=positionword+1
    else:
        break
print('The word occurs',count,'times.')
    

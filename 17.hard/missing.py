def findmissing(lis):
    originallis=[i for i in range(lis[0],lis[len(lis)-1])]

    lis=set(lis)
    print(lis)
    print(set(originallis))
     
    return list(lis ^ set(originallis))

lis=[1,2,3,4,6,8,8,999,111]
print(findmissing(lis))
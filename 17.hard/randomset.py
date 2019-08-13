import random as magic

def randomset(originallist,pickup,n):
    if(n+1 == pickup):
        print('Base Condition Satisfied! \n')
        return originallist[:pickup]
    elif(n+1 > pickup):
        print('Lowering down to Base Condition \n',n)
        subset = randomset(originallist,pickup,n-1)
        print('Upstream to Aggregate to pickup! \n',n,subset)

        k=magic.randint(0,n)
        if(k<pickup):
            subset[k]=originallist[n]
        return subset
    else:
        return None

originallist=[1,2,3,4,5,6,7,8,9,0]
n=len(originallist)-1
pickup=4
print(randomset(originallist,pickup,n))

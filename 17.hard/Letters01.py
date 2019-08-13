# Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
# an equal number of letters and numbers

# solution: O(N)
def deltaarray(lis):
    deltaarray=[]
    delta=0
    x=str(lis)
    for i in x:
        if i.isalpha():
            delta += 1
        elif i.isdigit():
            delta -=1
        deltaarray.append(delta)
    return deltaarray

def findlongestmatch(deltaarray):
    x=dict()
    max_map = [0,0]
    for i in range(0,len(deltaarray)):
        if(deltaarray[i] not in x):
            x[deltaarray[i]]=i
        else:
            match = x[deltaarray[i]]
            print(match)
            distanc = i-match
            longest = max_map[1]-max_map[0]
            if(distanc>longest):
                max_map[1]=i
                max_map[0]=match
    return max_map

lis=[1,'a',1,'a',2,3,2,2,3,'a',3,'a',3,'a','a','a',3,'a',3,3]
a= findlongestmatch(deltaarray(lis))
print(a)
print(lis[a[0]:a[1]]) 
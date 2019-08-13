# Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
# an equal number of letters and numbers

# solution O(N^2)
def checkequality(lis,st,en):
    equ=0
    lis=str(lis[st:en])
    for i in lis:
        if i.isalpha():
            equ += 1
        elif i.isdigit():
            equ -= 1
    return equ == 0 # return true or false over equ check to 0

def findlongest(lis):
    for i in range(len(lis),1,-1):
        for j in range(0,len(lis)-i):
            if (checkequality(lis,j,j+i-1)):
                return lis[j:j+i-1]
    return None
lis=[1,'a',1,'a',2,3,2,2,3,'a',3,'a',3,'a','a','a',3,'a',3,3]
print(findlongest(lis))
import random as magic
def sufflelist(mylist,n):
    if n==0:
        print('base condition satisfied!')
        return mylist
    x=n-1
    print("getting in >> ",x)
    sufflelist(mylist,x)
    print('getting out >> ',x)
    print("\n{0} >> {1}".format(mylist,x))
    k = magic.randint(0,n)
    temp = mylist[k]
    mylist[k]=mylist[n]
    mylist[n]=temp
    return mylist
mylist=[1,2,3,4,5,6,7,8]
n=len(mylist)-1
yourlist=sufflelist(mylist,n)
print(yourlist)
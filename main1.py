def printnumber(n):
    itr=0
    print("the total number entered by user is ",n)
    itr+=1
    print("the total iteration for n is ",itr)
printnumber(10)
printnumber(15)
#for every n the time taken will not change
#time complexit=O(1)
#best case scenario

def print2(n):
    itr=0
    for i in range(1,n+1):
        itr+=1
    print("for total n=",n,"the total iteration ",itr)
print2(10)
print2(100)

#time complexit=O(n)
#avg case scenario
#for every n the time taken increase linearly

def print3(n):
    itr=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            itr+=1
        print(" ")
    print("for total n=",n,"the total iterations",itr)
print3(6)
print3(4)

#time complexit=O(n^2)
#worst case scenario
#for every n the time taken increases quadrately
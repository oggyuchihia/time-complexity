def func1(n):
    return n*(n+1)/2
print(func1(11))
#time complaxcity=1

def func2(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    return sum
print(func2(11))
#time complaxcity=n

def func3(n):
    sum=0
    for i in range (1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
print(func3(11))
#time complaxcity=n^2
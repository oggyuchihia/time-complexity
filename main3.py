def sum(n):
    return n*(n+1)/2
print(sum(5))
#spacecomplexity=1

def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum

a=[12,3,4,1]
print(arraysum(a))

#space complexity=n
#space complexity will increase here due to array
def recursion(n):
    if (n<=0):
        return n
    print("codingal")
    recursion(n/2)
    recursion(n/2)

recursion(4)
#timecomplextiy=O(nlogn)with base 2


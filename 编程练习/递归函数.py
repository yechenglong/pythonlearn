# import sys
# sys.setrecursionlimit(1000000)
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,producet):
    if num == 1:
        return producet
    return fact_iter(num-1,num*producet)
print(fact_iter(1000,1))
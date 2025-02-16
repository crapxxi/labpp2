def gen(N):
    i = 1
    while (N >= i):
        yield (i**2)
        i+=1
N = int(input())
ctr = gen(N)
for n in ctr:
    print(n)

def gen(N):
    i = 1
    while (N >= i):
        if i%2==0 and (i+1 == N or i==N):
            yield str(i)
        elif i%2==0:
            yield str(i) + ','
        i+=1
N = int(input())
ctr = gen(N)
for n in ctr:
    print(n,end=" ")

def gen(N):
    for i in range(N):
        if i%3==0 and i!=0:
            yield i
        elif i%4==0 and i!=0:
            yield i
N = int(input())
ctr = gen(N)
for n in ctr:
    print(n,end=" ")


def gen(a,b):
    for i in range(a,b+1):
        yield (i**2)
a = int(input())
b = int(input())
ctr = gen(a,b)
for n in ctr:
    print(n,end=" ")


def gen(N):
    while(N>=0):
        yield N
        N-=1
N = int(input())

ctr = gen(N)
for n in ctr:
    print(n,end=" ")
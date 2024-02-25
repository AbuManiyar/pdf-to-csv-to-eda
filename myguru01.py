
''' Program 1
'''
L = [1]

for i in range(len(L)):
    j = i
    while(j<len(L)):
        if L[j]<L[i]:
            L[i],L[j] = L[j],L[i]
        j +=1
            
print(L)      

''' Program 2
Removing non-int Values from the heterogenous list
'''
L=['hello', 1, 2.2, 2,'Y']
for i in L:
    if (int != type(i)):
        L.remove(i)
    
print(L)      

''' Program 3
Calculating the average of the list elements
'''

L = [2,2.3, 23,11,23,20.5, 2.6]
if len(L)!=0 : print(sum(L)/len(L))
Sum = 0
for i in L :
    Sum += i
    
if len(L)!=0 : print(Sum/len(L))


''' Program 4
List of first N prime numbers
'''
import time
time1 = time.time()

N = 5 #int(input('N = '))
counts = 0
primes = []
i = 2
while(counts != N):
    j = 2
    isprime = True
    while(j<i):
        if i%j == 0:
            isprime = False
            break
        j += 1
        
    if isprime:
        primes.append(i)
        counts+=1
        print(counts)
    
    i += 1

time1 = time.time() - time1

print(primes)



#N = int(input('N = '))
time2 = time.time()
counts = 0
primes = []
i = 2
while(counts != N):
    isprime = True
    for j in primes: 
        if i%j == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
        counts+=1
        print(counts)
    
    i += 1

time2 = time.time() - time2
print(primes)

print('time1 = ', time1)
print('time2 = ', time2)


''' Program 5
List of first N terms of fibonacci series'''

N = int(input('N = '))

# 0  1  1  2  3  5  8  ....

a,b = 0,1
if N==1:
    print(0)
elif N==2:
    print(0,1)
else:
    print(0,1, end=' ')
    for i in range(N-2):
        term = a+b
        a = b
        b = term
        print(term, end=' ')

# Method 1: recursive
# Time: O(2^n)
# Space: O(n)
# set base cases: (n==1, n==2), then return fib(n-1) and fib(n-2)
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Method 2: recursive, Memorization/Caching
# Time: O(n)
# Space: O(n)
# set the base cases (1 & 2) in the hash table (memoize), calculate each fib once and stores it in the hash table,
# when retriving the value from hash table is a constant operation [O(1)]
def fib(n,  memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
        return memoize[n]

# Method 3: iterative
# Time: O(n)
# Space: O(1)
#
def fib(n):
    lastTwo = [0, 1] # initialize base case, store last 2 Fib values in the array
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]  # calculate next Fib
        lastTwo[0] = lastTwo[1]  # throw away value at lastTwo[0], replace it with lastTwo[1]
        lastTwo[1] = nextFib # replace lastTwo[1] with next value lastTwo[2] (nextFib) 
        counter +=1
    return lastTwo[1] if n > 1 else lastTwo[0] # edge case: n = 1, return lastTow[0]
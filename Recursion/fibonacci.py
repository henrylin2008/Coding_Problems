
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
# retriving the value from hash table is a constant operation [O(1)]
def fib(n,  memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
        return memoize[n]

# Method 3: iterative
# Time: O(n): runs through all values once
# Space: O(1): only stores lastTwo/base case values [0, 1]
# Concept: initialized first 2 base cases and a counter, next Fib = sum of lastTwo[0] and lastTwo[1], ex: 0 1 => 1(nextFib)
# then lastTwo[1] replaces lastTwo[0], and next Fib replaces lastTwo[1]
# count: [1,2,3,4,5,6,7,8,9,10]
# Value: [0,1,1,2,3,5,8,13,21,34]
def fib(n):
    lastTwo = [0, 1] # initialize base case, store last 2 Fib values in an array
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]  # next Fib = sum of previous 2 values
        lastTwo[0] = lastTwo[1]  # replace lastTwo[0] with lastTwo[1]
        lastTwo[1] = nextFib # replace lastTwo[1] with nextFib
        counter +=1 # increment the counter
    return lastTwo[1] if n > 1 else lastTwo[0] # edge case: n = 1, return lastTow[0]

# fib(30s
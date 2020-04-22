#Naive Recursion:
#Time: O(2^n)
#Inefficient in time
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

# Memoized
# Time: O(n)
def fib_2(n, memo):
    if memo[n] is not None: # if memo[n] != null
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return fib_2(n, memo)

# Bottom-Up Approach:
# Time: O(n)
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)#new int[n+1]
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i from range(3, n+1): #3 upto n:
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

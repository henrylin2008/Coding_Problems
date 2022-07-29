# Memoization
# https://algo.monster/problems/memoization_intro

# Memoization is a fancy word for a simple concept (so is the case for a lot of things we learn at school). It means
# saving the previous function call result in a dictionary and reading from it when we do the exact same call again.
# And no I didn't spell it wrong. The word is meant to mean writing down on a "memo".


# Fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

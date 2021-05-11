# recursion: it needs the base case, and recursive calls on same function of last 2 positions
# Fibonacci Sequence
def get_fib(position):
    if position == 0 or position == 1:  # base case
        return position
    return get_fib(position - 1) + get_fib(position - 2)

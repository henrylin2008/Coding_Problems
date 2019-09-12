# 70. Climbing Stairs

def climbstairs(n):
    previous, current = 0, 1
    for i in range(n):
        previous, current = current, previous + current
        # print("round",i)
        # print("previous:", previous)
        # print("current:", current)
        # print()
    return current

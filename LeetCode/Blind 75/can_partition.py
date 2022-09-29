def can_partition(nums):
    target = sum(nums) // 2
    if sum(nums) % 2 == 0:
        first = []
        second = []
        done = False
        for i in range(len(nums)):
            if not done:
                first.append(nums[i])
                if sum(first) == target:
                    print(first)
                    # i += 1
                    done = True
                    continue
            second.append(nums[i])
            if sum(second) == target:
                print(second)
        print('True')
        return True
    else:
        print("False")
        return False


can_partition([5, 2, 2, 3, 2])



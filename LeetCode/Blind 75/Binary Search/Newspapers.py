# Newspapers
# Link: https://algo.monster/problems/newspapers_split

# You've begun working in the one and only Umbristan, and it is part of your job duty to organize newspapers. Every
# morning, your fellow coworkers will diligently read through the newspapers to examine its contents. It is your job
# to organize the newspapers into piles and hand them out to your coworkers to read through.
#
# Each newspaper is marked with the time it would take to read through its contents. The newspapers are carefully
# laid out in a line in a particular order that must not be broken when assigning the newspapers. You cannot pick and
# choose newspapers randomly from the line to assign to a co-worker. Instead, you must take newspapers from a
# particular subsection of the line, make a pile and give that to a co-worker.
#
# What is the minimum amount of time it would take to have your coworkers go through all the newspapers?
#
# Constraints
# 1 <= newspapers_read_times.length <= 10^5
#
# 1 <= newspapers_read_times[i] <= 10^5
#
# 1 <= num_coworkers <= 10^5
#
# Examples
# Example 1:
# Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
# Output: 18
# Explanation:
# Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3
# newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.
#
# Example 2:
# Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
# Output: 7
# Explanation:
# Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.

from typing import List


# Logic: use binary search on possible time values (min: max(read_times), max: sum(read_times)), checking if each time
#        limit is enough to finish the work.
# We check if a particular time works by trying to split the work among the coworkers and see if the total time
# taken exceeds the given time limit. We do so by moving from left to right in the newspapers array while keeping
# track of the time that the current coworker spent. When the time that the current coworker spent exceeds the given
# time limit, we reset the current time tracker and add 1 to our coworker count. When we finish checking the
# newspapers array, we check if the required coworker count exceeds the one we are given. If it does, then we know
# that the given time limit doesn't work and we must try a higher value. Otherwise, we want to try a lower value to
# look for the minimum time limit that works.

# Time: O(n log(n)); O(n): find low and high values; binary search is O(log(n)), feasible function: O(n)
# Space: O(1)
def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers_read_times, num_coworkers, mid):
            high = mid - 1
        else:
            low = mid + 1
    return high + 1


def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    # time to keep track of the current worker's time spent, num_workers to keep track of the number of coworkers used
    time, num_workers = 0, 0
    for read_time in newspapers_read_times:
        # check if current time exceeds the given time limit
        if time + read_time > limit:
            time = 0
            num_workers += 1
        time += read_time
    # edge case to check if we needed an extra worker at the end
    if time != 0:
        num_workers += 1
    # check if the number of workers we need is more than what we have
    return num_workers <= num_coworkers


if __name__ == '__main__':
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)

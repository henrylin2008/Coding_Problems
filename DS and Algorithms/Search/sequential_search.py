# Sequential search: search through the list via index values in sequence.
# Best case: matched item at position 0; O(1)
# Worst case: not find the item after search all n items; O(n)
# Average case: n/2 for finding the item, only if it is in the list; O(n/2)
#                   Best Case       Worst Case      Average Case
# item is present       1               n               n/2
# item is missing       n               n                n
def sequentialSearch(alist, item):
    i = 0
    while i < len(alist):
        if alist[i] == item:
            return True
        i += 1
    return False


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


# Sequential Search on ordered data
# ex: [2, 3, 5, 12, 26, 33, 43, 91, 98]
#                   Best Case       Worst Case      Average Case
# item is present       1               n               n/2
# item is missing       1               n               n/2
def seqSearchOrdered(alist, item):
    i = 0
    pos = 0
    while pos < len(alist):
        if alist[i] == item:
            return True
        if alist[i] > item:
            return False
        pos += 1
    return False

# # zip()
x = [1,2,3,4]
y = [1,2,4,8,9]

for i, j in zip(x, y):
    if i == j:
        print("same")
    else:
        print("not same")


# enumerate
# myList = ["one", "two", "three", "four"]
#
# for i, j in enumerate(myList):
#     print(i, j)

# List Comprenhension

# x = [i for i in range(10) if i%2 == 0 ]
# x = [[5 for j in range(5)] for i in range(5)]
# print(x)
#

# Help and dir functions:

# print(dir(int))

# more detail of each method
# print(help(str))

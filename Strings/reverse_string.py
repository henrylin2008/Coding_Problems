# Option 1: using for loop

inputStr = 'Hello'

#initalize empty string
result = ''

# run a loop from 'len(inputStr)-1' to 0
# one by one
for i in range(len(inputStr)-1, -1, -1):
    result += inputStr[i]

#print reversed string
print(result)



# Option 2: using reversed() function

# inputStr = 'Hello'
#
# # use inbuilt function reversed()
# # it will return list of characters of input string
# # in reversed order
#
# reversedChars = reversed(inputStr)
#
# # now join list of characters without space
# print(''.join(reversedChars))


# Option 3: using extended slicing
#
# inputStr = 'Hello'
#
# print(inputStr[::-1])
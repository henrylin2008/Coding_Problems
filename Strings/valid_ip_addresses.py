# Link: https://www.algoexpert.io/questions/Valid%20IP%20Addresses
# Valid Ip Addresses
# Difficulty: Medium
# You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible
# IP addresses that can be created by inserting three .s in the string.
# An IP address is a sequence of four positive integers that are separated by .s, where each individual integer is
# within the range 0-255, inclusive.
# An IP address isn't valid if any of the individual integers contains leading 0s. For example, "192.168.0.1" is a valid
# IP address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and 01, respectively. Another
# example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.
# Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can
# be created from the string, your function should return an empty list.
# Note: check out our Systems Design Fundamentals on SystemsExpert to learn more about IP addresses!

# Sample Input:
# string = "1921680"

# Sample Output: // The IP Addresses could be ordered differently
# [
#   "1.9.216.80",
#   "1.92.16.80",
#   "1.92.168.0",
#   "19.2.16.80",
#   "19.2.168.0",
#   "19.21.6.80",
#   "19.21.68.0",
#   "19.216.8.0",
#   "192.1.6.80",
#   "192.1.68.0",
#   "192.16.8.0"
# ]


# Time: O(1); ip address is 32 (8*4) bits, at most 2^32 addresses to check, constant upper bound, O(2^32) -> O(1)
# Space: O(1); list at most 2^32 ip addresses, absolute upper bound, thus constant upper bound
# Solution: check the location of each period (3 periods), loop through different combinations of numbers, then validate
# each combination is <255; last to append all valid octets and joins it with a '.' in between octets.
def validIPAddresses(string):
    ipAddressesFound = []   # array to store all the valid IP addresses that have been found

    for i in range(1, min(len(string), 4)):     # first period; min(len(string)): length of 1, 2, 3
        currentIPAddressParts = ['', '', '', '']  # a list of strings to represent 4 parts of IP address

        currentIPAddressParts[0] = string[:i]   # first octet = everything up to i
        if not isValidPart(currentIPAddressParts[0]):   # validate first octet; if it's not valid, move to the next loop
            continue    # move to next octet

        for j in range(i + 1, i + min(len(string) - i, 4)):  # second octet; starting from i+1, at most 3 digits
            currentIPAddressParts[1] = string[i: j]     # second octet of IP address (not including j)
            if not isValidPart(currentIPAddressParts[1]): # validate second octet
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):   # third octet
                currentIPAddressParts[2] = string[j:k]  # third octet
                currentIPAddressParts[3] = string[k:]   # fourth octet

                # if third and fourth octet are valid, then join all octets with a '.'
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append(".".join(currentIPAddressParts))

    return ipAddressesFound


def isValidPart(string):    # Check if input string is valid, in between 0 and 255
    stringAsInt = int(string)   # int(string) removes leading 0; ex: 00 -> 0, 01 -> 1
    if stringAsInt > 255:   # return False if number is > 255
        return False

    return len(string) == len(str(stringAsInt))    # check for leading 0, remove any leading 0s


# validIPAddresses(string)

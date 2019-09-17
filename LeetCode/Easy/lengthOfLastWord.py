def lengOfLastWord(s):
    count = 0
    local_count = 0

    for i in range(len(s)):
        if s[i] == ' ':
            local_count = 0
            # print()
            # print("empty space:", s[i])
            # print()
        else:
            local_count += 1
            # print("local count: ", local_count)
            # print("Word so far: ", s[i])
            count = local_count
            # print("count: ", count)
    return count
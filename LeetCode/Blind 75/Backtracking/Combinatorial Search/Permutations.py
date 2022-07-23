# Permutations
# Given a string of unique letters, find all of its distinct permutations.
#
# Input
# letters: a string of unique letters
# Output
# all of its distinct permutations
#
# Example 1:
# Input:
# letters = `abc`
# Output:
# ```` abc acb bac bca cab cba


from typing import List


def permutations(letters):
    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(letters), res)
    return res


if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)

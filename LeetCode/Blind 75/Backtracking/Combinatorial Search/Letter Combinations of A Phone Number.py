# Letter Combinations of A Phone Number
# Link: https://algo.monster/problems/letter_combinations_of_phone_number

# Given a phone number that contains digits 2-9, find all possible letter combinations the phone number could translate
# to.
#       1       2       3
#             A B C   D E F
#       4       5       6
#     G H I   J K L   M N O
#       7       8       9
#    P Q R S  T U V   W X Y Z
#
# Input:
# "56"
#
# Output:
# ["jm","jn","jo","km","kn","ko","lm","ln","lo"]


from typing import List

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(path, res):
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        next_number = digits[len(path)]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path, res)
            path.pop()

    res = []
    dfs([], res)
    return res


if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))

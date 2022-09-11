# Divisor Game
# https://algo.monster/problems/divisor_game

# James and Oliver take turns playing a game, with James starting first.
#
# Initially, there is a number N on the chalkboard. On each player's turn, that player makes a move consisting of:
#
# Choosing any x with 0 < x < N and N % x == 0 where 1 <= N <= 1000.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
#
# Return True if and only if James wins the game, assuming both players play optimally.
#
# Example 1:
# Input: 2
# Output: true
# Explanation:
# James chooses 1, and Oliver has no more moves.
#
# Example 2:
# Input: 3
# Output: false
# Explanation:
# James chooses 1, and Oliver chooses 1, and James has no more moves.

# Solution
# Winning and losing states
# A winning state is a state where the player will win the game if they play optimally, and a losing state is a state
# where the player will lose the game if the opponent plays optimally. We can classify all states of a game so that
# each state is either a winning state or a losing state.
#
# State 1 is clearly a losing state, because the player cannot make any moves. States 2 is winning state, because we
# can remove one stick and force the opponent into the losing state of 1 and win the game. State 3, in turn,
# is a losing state, because any move leads to a state that is a winning state for the opponent.
#
# More generally, if there is a move that leads from the current state to a losing state, the current state is a
# winning state, and otherwise the current state is a losing state. Using this observation, we can classify all
# states of a game starting with losing states where there are no possible moves.
#
# State 1 is a losing state. For each states from 2..N, we try all the possible x we can choose and see if it results
# in a losing state for the opponent. The state transitions for the first 8 numbers are illustrated here:

# Dynamic programming
# Now we fill the table where each entry dp[i] represents whether the current state is a winning state.
#
# Time Complexity: O(n^2)

def divisor_game(n: int) -> bool:
    dp = [False] * (n + 1)

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = dp[i] or not dp[i - j]

    return dp[-1]


if __name__ == '__main__':
    n = int(input())
    res = divisor_game(n)
    print('true' if res else 'false')

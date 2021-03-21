# Algoexpert: https://www.algoexpert.io/questions/Tournament%20Winner
# Difficulty: Easy
# Tournament Winner
# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve
# algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other
# teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home
# team, while the other team is the away team. In each competition there's always one winner and one loser; there
# are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team
# that receives the most amount of points.
# Given an array of pairs representing the teams that have competed against each other and an array containing the
# results of each competition, write a function that returns the winner of the tournament. The input arrays are named
# competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where
# each team is a string of at most 30 characters representing the name of the team. The results array contains
# information about the winner of each corresponding competition in the competitions array. Specifically, results[i]
# denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding
# competition won and a 0 means that the away team won.
# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams
# exactly once. It's also guaranteed that the tournament will always have at least two teams.

# Sample Input:
# competitions = [
#     ["HTML", "C#"],  # [homeTeam, awayTeam]
#     ["C#", "Python"],
#     ["Python", "HTML"],
# ]
# results = [0, 0, 1]  # 0: awayTeam won; 1: homeTeam won


# Sample Output:
# "Python"
# // C# beats HTML, Python Beats C#, and Python Beats HTML.
# // HTML - 0 points
# // C# - 3 points
# // Python - 6 points


# Time: O(n); n is the number of competitions
# Space: O(k); k is the number of teams
# Solution: loop through competitions array, get the result of each competition (index) fro the results array (match
# index of competition and index of results), then store the score in a hash table(scores); when a better score is
# presented, update the currentBestTeam and the best score in hash table (scores). Last return the currentBestTeam
def tournamentWinner(competitions, results):
    Home_Team_Won = 1
    currentBestTeam = ""  # current Best team (empty string)
    scores = {currentBestTeam: 0}  # Hash table to keep track of scores

    for idx, competition in enumerate(competitions):  # loop through entire competitions array
        # ex: idx: 0; competition: ['HTML', 'C#']
        result = results[idx]  # result of competition between homeTeam/awayTeam at current index
        homeTeam, awayTeam = competition  # decompose competition into homeTeam and awayTeam;
        # ex: homeTeam:'HTML', awayTeam:'C#'
        # check the winning team (homeTeam or awayTeam)
        winningTeam = homeTeam if result == Home_Team_Won else awayTeam  # return winningTeam if result==1 else awayTeam
        updateScores(winningTeam, 3, scores)  # update score by adding 3 to the score of the winning Team
        if scores[winningTeam] > scores[currentBestTeam]:  # if score of winning team > score of current best team:
            currentBestTeam = winningTeam  # update the current best team
    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:  # if team is not in scores hash table
        scores[team] = 0  # store it to scores table

    scores[team] += points  # add points to the (winning) team


# tournamentWinner(competitions, results)

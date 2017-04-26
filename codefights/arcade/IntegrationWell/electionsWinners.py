def electionsWinners(votes, k):
    w = max(votes)
    if k:
        return sum([1 for i in votes if i + k > w])
    elif votes:
        return sum([1 for i in votes if i == w]) > 1
    else:
        return 0


print electionsWinners([2,3,5,2], 3)
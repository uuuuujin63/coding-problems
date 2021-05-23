from itertools import combinations
def solution(board, r, c):
    answer = 0
    turn = []
    n = max(board)
    way = combinations(range(1, n+1), n)
    return answer
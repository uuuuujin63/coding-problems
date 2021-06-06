def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        popped = board.pop(0)
        board.append([p for p in popped])
    while 1:
        check = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i][j+1]:
                    if board[i][j] == board[i+1][j+1] and board[i][j] == board[i+1][j]:
                        check.append((i, j))
                        check.append((i, j+1))
                        check.append((i+1, j))
                        check.append((i+1, j+1))
        if len(check) == 0:
            break
        else:
            answer += len(set(check))
            for c in check:
                board[c[0]][c[1]] = '0'
            for c in reversed(check):
                check_n = c[0]-1
                put_n = c[0]
                while check_n >= 0:
                    if board[put_n][c[1]]=='0' and board[check_n][c[1]]!='0':
                        board[put_n][c[1]] = board[check_n][c[1]]
                        board[check_n][c[1]] = '0'
                        put_n -= 1
                    check_n -= 1
    return answer

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
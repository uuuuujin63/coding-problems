def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(1, rows+1):
        arr.append(list(columns*(i-1)+j for j in range(1, columns+1)))
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        for i in range(rows):
            print(arr[i])
        minn = rows*columns
        tmp = arr[y1][x1]
        for nx in range(x1, x2):
            arr[y1][nx] = arr[y1][nx+1]
            minn = min(arr[y1][nx], minn)
        for ny in range(y1, y2):
            arr[ny][x2] = arr[ny+1][x2]
            minn = min(arr[ny][x2], minn)
        for nx in range(x2, x1, -1):
            arr[y2][nx] = arr[y1][nx-1]
            minn = min(arr[y2][nx], minn)
        for ny in range(y2, y1, -1):
            arr[ny][x1] = arr[ny-1][x1]
            minn = min(arr[ny][x1], minn)
        arr[ny][x1+1] = tmp
        for i in range(rows):
            print(arr[i])
        answer.append(minn)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(1, rows+1):
        arr.append(list(columns*(i-1)+j for j in range(1, columns+1)))
    for y1, x1, y2, x2 in queries:
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
       
        minn = rows*columns
        
        y1x2 = arr[y1][x2]
        for nx in range(x2, x1, -1):
            arr[y1][nx] = arr[y1][nx-1]
            minn = min(arr[y1][nx], minn)
        
        y2x2 = arr[y2][x2]
        for ny in range(y2, y1+1, -1):
            arr[ny][x2] = arr[ny-1][x2]
            minn = min(arr[ny][x2], minn)
        arr[y1+1][x2] = y1x2
        
        y2x1 = arr[y2][x1]
        for nx in range(x1, x2):
            arr[y2][nx] = arr[y2][nx+1]
            minn = min(arr[y2][nx], minn)
        arr[y2][x2-1] = y2x2
        
        for ny in range(y1, y2):
            arr[ny][x1] = arr[ny+1][x1]
            minn = min(arr[ny][x1], minn)
        arr[y2-1][x1] = y2x1
        
        answer.append(minn)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
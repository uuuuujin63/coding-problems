def dfs(i, res, numbers, target):
    global answer
    if i != len(numbers)-1:
        dfs(i+1, res+numbers[i+1], numbers, target)
        dfs(i+1, res-numbers[i+1], numbers, target)
    if i == len(numbers)-1 and res == target:
        answer = answer + 1
        return
    return
    
def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers[0], numbers, target)
    dfs(0, -numbers[0], numbers, target)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

def solution(numbers):
    answer = ''
    n = list(map(str, numbers))
    n.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 2]))
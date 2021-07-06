from collections import deque
def solution(numbers, target):
    answer = 0
    s = deque()
    s.append(0)
    for number in numbers:
        for _ in range(len(s)):
            n = s.popleft()
            s.append((n+number))
            s.append((n-number))
    answer = s.count(target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
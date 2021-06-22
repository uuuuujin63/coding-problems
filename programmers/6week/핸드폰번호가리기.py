def solution(phone_number):
    answer = ''
    n = len(phone_number)-4
    answer = '*'*n + phone_number[n:]
    return answer
print(solution("01033334444"))
print(solution("027778888"))
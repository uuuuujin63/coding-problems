def solution(nums):
    answer = 0
    s_nums = set(nums)
    if (len(s_nums)>=(len(nums)//2)):
        answer = len(nums)//2
    else:
        answer = len(s_nums)
    return answer

nums = [3,1,2,3]
print(solution(nums))
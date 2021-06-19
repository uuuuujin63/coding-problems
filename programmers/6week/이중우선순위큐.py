import heapq
def solution(operations):
    hq = []
    for oper in operations:
        num = int(oper[2:])
        if oper[0] =='I':
            heapq.heappush(hq, num)
        else:
            if len(hq) == 0:
                continue
            elif num == 1:
                hq = heapq.nlargest(len(hq), hq)[1:]
                heapq.heapify(hq)
            else:
                print(heapq.heappop(hq))
        print(hq)
    if len(hq)==0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, hq)[0], heapq.nsmallest(1, hq)[0]]
#print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
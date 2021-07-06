def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    route = dict()
    for t1, t2 in tickets:
        if t1 in route:
            route[t1].append(t2)
        else:
            route[t1] = [t2]
    print(route)
    start = ['ICN']
    while start:
        t = start[-1]
        print(start)
        if t not in route or len(route[t])==0:
            answer.append(start.pop())
            print(answer[-1])
        else:
            start.append(route[t].pop())
        print(route)
    answer.reverse()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
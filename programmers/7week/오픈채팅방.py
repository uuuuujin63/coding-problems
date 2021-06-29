def solution(record):
    answer = []
    stack = []
    dic = {}
    for r in record:
        if r[:5] == 'Leave':
            c, u_id = r.split()
            stack.append((u_id, '0'))
        else:
            c, u_id, nick = r.split()
            if c == 'Enter':
                dic[u_id] = nick
                stack.append((u_id, '1')) #1이 들어온 것
            else:
                dic[u_id] = nick
    for u_id, c in stack:
        if c == '1':
            answer.append((dic[u_id]+"님이 들어왔습니다."))
        else:
            answer.append((dic[u_id]+"님이 나갔습니다."))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
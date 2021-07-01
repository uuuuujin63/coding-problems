#정확성만 통과 ㅠ..
def solution(info, query):
    answer = []
    que = []
    inform = []
    for i in range(len(info)):
        info[i] = info[i].split()
        inform.append(info[i])
    for i in range(len(query)):
        query[i] = query[i].split(' and ')
        que.append(query[i][:3]+query[i][3].split())
    for q in que:
        cnt = 0
        for inf in inform:
            if ((q[0]=='-' or q[0]==inf[0]) and (q[1]=='-' or q[1]==inf[1]) and (q[2]=='-' or q[2]==inf[2]) and (q[3]=='-' or q[3]==inf[3]) and (int(q[4])<=int(inf[4]))):
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
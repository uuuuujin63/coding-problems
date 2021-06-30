def change(m):
    m = m.replace("C#", "H")
    m = m.replace("D#", "I")
    m = m.replace("F#", "J")
    m = m.replace("G#", "K")
    m = m.replace("A#", "L")
    return m

def solution(m, musicinfos):
    answer = '(None)'
    t = 0
    m = change(m)
    for info in musicinfos:
        music = ''
        info = info.split(',')
        info[3] = change(info[3])
        time = (int(info[1][:2])-int(info[0][:2]))*60+(int(info[1][3:])-int(info[0][3:]))
        i = -1
        flg = 0
        while (flg == 0):
            i += 1
            music += info[3][i%len(info[3])]
            if m in music:
                if t<time:
                    answer = info[2]
                    t = time
                flg = 1
            if i == time:
                flg = 1
    return answer

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
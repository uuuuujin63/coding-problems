def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            idx = cache.index(city)
            if idx != len(cache)-1:
                cache = cache[:idx]+cache[idx+1:]
                cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache = cache[1:]
                cache.append(city)
            else:
                cache.append(city)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
def solution(cacheSize, cities):
    answer = 0

    cacheList = []
    if cacheSize==0:
        answer = 5*len(cities)
        return answer

    for city in cities:
        city = city.lower()
        if city in cacheList:
            answer+=1
            cacheList.remove(city)
            cacheList.append(city)
        else:
            if len(cacheList) <cacheSize:
                cacheList.append(city)
            else:
                cacheList.remove(cacheList[0])
                cacheList.append(city)
            answer+=5
    print(answer)
    return answer


if __name__ == '__main__':
    cache = 0
    cityList = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    solution(cache,cityList)

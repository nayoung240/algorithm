def solution(sticker):
	# 리스트에 원소가 한 개면 아래 코드를 진행할 수 없다.
    if len(sticker) == 1:
        return sticker[0]
    
    # 처음과 마지막은 연결되어 있다고 했으니, 처음 원소를 제외했을 때와 마지막 원소를 제외했을 때로 나눈다.
    a = sticker[1:]
    b = sticker[:-1]

    i = 1
    while i < len(sticker)-1:
    	# 인덱스가 1이면 앞 원소와 현재 원소 비교
        if i == 1:
            a[i] = max(a[i-1], a[i])
            b[i] = max(b[i-1], b[i])
        # 인덱스가 2이상이면 앞 원소와 여태까지 합에 현재 원소를 더한 값 비교
        else:
            a[i] = max(a[i-1], a[i-2]+a[i])
            b[i] = max(b[i-1], b[i-2]+b[i])
        i += 1

	# 최종적으로 두 리스트의 마지막 원소가 최대합이기 때문에 둘 중 더 큰 값을 리턴
    return max(a[-1], b[-1])

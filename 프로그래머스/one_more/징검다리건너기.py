def solution(stones, k):
    answer = 0
    _min, _max = 1, 200_000_000
    

    while _min <= _max:
        mid = (_min + _max) // 2

        max_continuous_zero = -1
        continuous_zero = 0
        for stone in stones:
            if stone-mid <= 0:
                continuous_zero += 1
                if continuous_zero > max_continuous_zero:
                    max_continuous_zero = continuous_zero
                # max_continuous_zero = max(continuous_zero, max_continuous_zero)
            else:
                continuous_zero = 0
                
        # 0 이하의 값이 연속 k개 이하인지 확인
        if max_continuous_zero < k:
            _min = mid + 1
        else:
            _max = mid - 1
            answer = mid
        
    return answer

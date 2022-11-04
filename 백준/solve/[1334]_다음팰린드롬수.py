"""
    1. 대칭변환 수행
    2. 대칭변환 수행 후 값을 비교 => 클 경우 Return
    3. 작을 경우
        3-1. 중앙에 존재하는 값들을 1씩 증가
        3-2. 10일 경우는 left, right point를 한 칸씩 이동 한 후 3-1을 수행.
        3-3. 길이를 벗어날 경우 => 다음 자리수로 넘어감 => 101, 1001, 10001, 100001, 1000001 등이 정답
"""

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, list(str(n))))

def solution(original_num_list):

    def convert(num_list):
        mid = len(num_list) // 2
        front = num_list[:mid]
        # back = num_list[:mid]
        # back.reverse() 
        back = num_list[:mid][::-1]

        if len(num_list) % 2 == 0:
            num_list = front + back
        else:   
            num_list = front + [num_list[mid]] + back

        return num_list

    next_num_list = convert(original_num_list)

    # 대칭변환을 수행하였을 때, 기존값 보다 클 경우 Return
    if int(''.join(list(map(str, next_num_list)))) > int(''.join(list(map(str, original_num_list)))):
        return int(''.join(list(map(str, next_num_list))))

    # 대칭변환을 수행하였을 때, 기존값 보다 작을 경우, 추가 변환 수행
    else:
        mid = len(original_num_list) // 2

        if len(original_num_list) % 2 == 0:
            left, right = mid-1, mid
        else:
            left, right = mid, mid
        
        while left >= 0 and right < len(original_num_list):

            # 홀 수일 때
            if left == right:
                next_num_list[mid] += 1

                if next_num_list[mid] == 10:
                    next_num_list[mid] = 0

                    right += 1
                    left -= 1
                else:
                    return int(''.join(list(map(str, next_num_list))))

            # 그 외
            else:
                next_num_list[left] += 1
                next_num_list[right] += 1
                
                if next_num_list[left] == 10 or next_num_list[right] == 10: # 무조건 left와 right 값은 같음
                    next_num_list[left] = 0
                    next_num_list[right] = 0
                    
                    right += 1
                    left -= 1
                else:
                    return int(''.join(list(map(str, next_num_list))))
        
        # 밖으로 빠져나올 경우 => 자리수가 변했기 때문.
        answer_list = [1] + [0] * (len(next_num_list) - 1) + [1]
        return int(''.join(list(map(str, answer_list))))
    
print(solution(num))

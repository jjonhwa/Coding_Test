from itertools import combinations

def solution(orders, course):
    answer = []
    
    check = []
    for c in course:
        check_dict = {}
        for order in orders:
            # combination을 사용하기 위하여, order를 정렬. (XY, YX)를 없애주기 위해
            order = list(order)
            order.sort()
            for comb in combinations(order, c):
                # c개의 조합을 모두 구해서 개수 저장
                check = ''.join(comb)
                if check in check_dict.keys():
                    check_dict[check] += 1
                else:
                    check_dict[check] = 1
                    
        if check_dict: # c개 이상의 메뉴를 먹었을 경우에만 (안먹었으면 어차피 생길 수 없으므로)
            max_value = max(check_dict.values()) # 가장 많이 먹은 조합의 개수 저장
            if max_value >= 2: # 2번 이상일 경우에만 후보군으로 저장
                answer += [k for k, v in check_dict.items() if v == max_value]
            
    # 오름차순 정렬
    answer.sort()
    return answer
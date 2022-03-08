# 첫 제출 - 시간초과
# `enroll.index(child)`에서 O(n) 소모
def solution(enroll, referral, seller, amount):
    def dfs(child, price):
        if child == '-': # center까지 들어갔을 경우 return
            return
        idx = enroll.index(child)
        parent = referral[idx]

        upper_price = price // 10
        answer[idx] += price - upper_price

        if upper_price:
            dfs(parent, upper_price)
            
    answer = [0] * len(enroll)
    
    for seller_name, count in zip(seller, amount):
        price = count * 100
        dfs(seller_name, price)
    return answer
  
# 수정 후 제출 - 통과
def solution(enroll, referral, seller, amount):
    def dfs(child, price):
        if child == '-': # center까지 들어갔을 경우 return
            return
        idx = name_idx_pair[child]
        parent = referral[idx]

        upper_price = price // 10
        answer[idx] += price - upper_price

        if upper_price:
            dfs(parent, upper_price)
            
    answer = [0] * len(enroll)
		
		# 이름 - index pair
    name_idx_pair = {}
    for i in range(len(enroll)):
        name_idx_pair[enroll[i]] = i
        
    for seller_name, count in zip(seller, amount):
        price = count * 100
        dfs(seller_name, price)
    return answer

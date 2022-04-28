def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])
  
  
# dfs 활용할 경우, 속도 측면에서 비효율적
answer = 0
def solution(numbers, target):
    
    def dfs(num_list, k):
        global answer

        if len(num_list) == len(numbers):
            if sum(num_list) == target:
                answer += 1
            return
        
        for i in [-1, 1]:
            num_list.append(i*numbers[k])
            k += 1
            dfs(num_list, k)
            k -= 1
            num_list.pop()
            
    num_list = []
    dfs(num_list, 0)  
        
    return answer

# bfs 풀이 
https://programmers.co.kr/questions/16222

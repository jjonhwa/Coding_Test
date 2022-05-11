from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque([(begin, 0)])
    
    visits = {}
    for w in words:
        visits[w] = 0
    
    while queue:
        word, count = queue.popleft()
        visits[word] = count
        
        for w in words:
            cnt = 0
            for a, b in zip(word, w):
                if a != b:
                    cnt += 1
            if cnt == 1:
                if visits[w] == 0 or visits[word] < visits[w]:
                    visits[w] = count + 1
                    queue.append((w, count + 1))
     
    if target not in visits:
        return 0
    else:
        return visits[target]
        
from collections import defaultdict, deque

def solution(begin, target, words):
    answer = float("inf")
    if target not in words:
        return 0
    
    visited = defaultdict(int)
    visited[begin] = 1
    queue = deque([(begin, 0)])
    while queue:
        check, cnt = queue.popleft()
        if check == target:
            answer = min(answer, cnt)
        for i in range(len(check)):
            tmp = check[:i] + check[i+1:]
            for word in words:
                tmp_word = word[:i] + word[i+1:]
                if tmp == tmp_word and not visited[word]:
                    visited[word] = 1
                    queue.append((word, cnt + 1))
    
    return answer

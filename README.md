# Coding_Test
Practice about Conding_Test

## Algorithm Study
- [BackTracking](#BackTracking)

## Module 사용법
- [heapq](#heapq)
- [Counter](#Counter)

## BackTracking

<details>
    <summary><b>설명</b></summary>

- 해를 찾는 도중 해가 아닐 경우, 다시 돌아가서 해를 찾는 기법
- 최적화 문제, 결정 문제
### DFS vs BackTracking

#### DFS
- 가능한 모든 경로(후보)를 탐색
- 불필요한 경로를 사전 차단하지 못한다.
- 시간복잡도가 N!일 경우, DFS로 해결하기 힘들다.

#### BackTracking
- 해를 찾는 도중, 지금 경로가 최적의 해가 되지 않을 것이라고 판단하면 되돌아간다.
- 반복문의 횟수를 줄일 수 있으므로, 보다 효율적이다.
- 시간복잡도 O(N!)의 문제일 경우, 최악의 경우 지수함수의 시간을 필요로 하여 처리가 불가능할 수도 있다. 여기서, 가지치기를 얼마나 잘 하느냐가 효율성을 결정하게 된다.

### Core Idea
- 모든 경우의 수 중에서 **특정한 조건을 만족하는 경우**만 살펴보는 방법
- 답이 될지 판단하며, 되지 않는다면 그만하고 되돌아가는 방법
- DFS와 같이, 모든 경우의 수를 탐색하는 과정에서 if문을 추가하여 해가 되지 않는 경우를 정의하고, 이럴 경우에 break 혹은 더 이상 진행하지 않게 구현할 수 있다.
</details>

<details>
    <summary><b>대표예제</b></summary>

### N-Queen (백준 9663)

#### 문제
크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없도록 말을 놓게하는 문제.

입력: N (1 <= N <= 15)
출력: N개가 서로 공격할 수 없게 놓는 경우의 수 출력

#### code

```python
import sys
input = sys.stdin.readline

N = int(input())

ans = 0
row = [0] * N # N=4: row = [0,0,0,0]

def is_promising(x):
    """x가 유망한지 판단"""
    for i in range(x): # 퀸을 위에서 부터 놓는다 => x이전까지만 i를 탐색
        # 행이 같은 경우는 있을 수 없다. => i는 x보다 작으므로
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            # 열 체크: x의 열, i의 열을 비교했을 때 같은 열에 놓여져 있는지: row[x] == row[i]
            # 대각선 체크: 열의 차이와, 행의 차이의 절대값이 같은지: abs(row[x] - row[i]) == abs(x-i)
            return False
    return True

def dfs(x):
    global ans

    if x == N: # 마지막 행까지 전부 유망할 경우 1추가
        ans += 1
    else:
        # 각 행, 열에 놓는다.
        for i in range(N): # x행 1열부터 ~ x행 N열까지
            row[x] = i # x행 i열
            if is_promising(x):
                dfs(x+1) # x+1행 삽입

dfs(0)
print(ans)
```

</details>

## heapq

<details>
    <summary><b>설명</b></summary>

- Binary tree 기반의 최소힙 자료구조를 제공한다.
- 최소힙 자료구조를 사용할 경우, 원소들이 항상 정렬된 상태로 추가 및 삭제된다.
    - 주의해야할 점은 정렬이 될 경우, 최소값을 보장해주지만 오름차순 혹은 내림차순의 정렬을 보장해주지는 않는다.
- `heappush()`, `heappop()`는 O(logN)의 시간복잡도를 가진다.
- `heapify()`는 O(NlogN)의 시간복잡도를 가진다.

#### 원소 추가 (heappush)
```python
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1) ...
```

#### 원소 삭제 및 꺼내기 (heappop)
```python
heapq.heappop(heap)
```

- 위의 코드를 활용할 경우, heap 배열에서 최솟값을 꺼내게 된다.
- heapq의 경우 맨 앞에 최소값을 보장해주기 때문에 `heapq[0]`을 활용하여 값을 제거하지 않으면서 꺼내올 수도 있다.

#### 힙 변환
```python
heap = [6,2,5,4,3,1,7]
heapq.heapify(heap)
```

- `heapify()`의 경우, 기존 배열에서의 원소들이 힙 구조에 맞게 재배치되면서 최소값을 0번째 인덱스에 위치하도록 한다.
- 비어있는 배열을 생성하고, heappush()를 활용하여 하나씩 추가한 효과가 나타나며, 시간복잡도는 원소의 수에 비례하여 O(NlogN)을 가진다.
#### 최대힙 (응용)
- heap에 tuple을 원소로 추가하거나 삭제한다.
    - tuple을 활용할 경우 tuple의 0번째 index를 기준으로 최소힙이 구성된다.
- `(우선순위, 값)` 구조의 튜플을 heap에 삽입 및 삭제를 해줄 경우, 우선순위 기준으로 최소힙 정렬이 진행된다.
- 즉, **우선순위를 음수로 넣어주고, 값을 본래의 값**을 넣어주고 최소힙 정렬을 하게되면, 가장 큰 값을 0번째에 위치하도록 보장한다.

```python
for num in nums:
    heapq.heappush(heap, (-num, num))
heapq.heappop(heap)[1]
```

#### K번째 최소, 최대값 (응용)
- K번째 값을 추출할 경우, 힙 정렬을 한 후 `heappop()`을 k번 호출하면 할 수 있다.

```python
k_th = None
heapq.heapify(heap)
for _ in range(k):
    k_th = heapq.heappop(heap)
print(k_th)
```

</details>

<details>
    <summary><b>대표예제</b></summary>

### 최대힙 (백준 11279)

#### 문제
- 배열에 자연수 x를 넣는다.
- 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

- 입력 
    - N (1 <= N <= 100000)
    - N개의 줄에 연산 정보 x 입력.
    - x가 자연수일 경우 배열에 추가, 0일 경우 가장 큰 값 출력 및 제거
- 출력
    - 0이 주어진 회수만큼 답 출력
    - 비어있는 배열인데 0이 주어질 경우 0을 출력

#### code

```python
import sys
import heapq
input = sys.stdin.readline

N = int(input())
number_list = []
for _ in range(N):
    insert = int(input())
    if insert == 0:
        if number_list:
            pop_number = heapq.heappop(number_list)[1]
            print(pop_number)
        else:
            print(0)
    else:
        heapq.heappush(number_list, (-insert, insert))
```

</details>

## Counter 클래스 사용법

<details>
    <summary><b>설명</b></summary>

- 데이터의 개수를 셀 때 유용한 모듈
- `from collections import Counter`
- `Counter`는 파이썬의 기본 자료구조인 dictionary를 확장하고 있기 때문에, dictionary에서 제공하는 API를 그대로 사용할 수 있다.

### Dictionary vs Counter

#### Dictionary

```python
word = "hello world"

counter = {}
for w in word:
    if w not in counter:
        counter[w] = 1
        continue
    counter[w] += 1
print(counter)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

#### Counter

```python
from collections import Counter
Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

### 데이터의 개수가 많은 순 정렬

- Basic Code

```python
from collections import Counter

word = "hello world"

counter = Counter(word)
max_count = -1

for key in counter.keys():
    if counter[key] > max_count:
        max_count = counter[key]
        max_letter = letter
print((letter, max_letter)) # ('l', 3)
```

- Code with Counter

```python
from collections import Counter
common = Counter("hello world").most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

print(common[0])
```

</details>

## 양방향 링크드 리스트

<details>
    <summary><b>설명</b></summary>

### 사용법 및 사용할 경우
- head node부터 탐색하는 것은 O(n)의 시간복잡도를 가진다.
- O(n)의 시간복잡도가 너무 큰 경우, 더욱 빠르게 해결하기 위하여 양방향 링크드 리스트를 활용한다.
- 양방향 링크드 리스트는 3개의 구성요소를 갖는다.
    - **Node 값인 Key**와 **2개의 Link**
    - **첫번째 링크는 앞 노드의 주소 링크**
    - **두번째 링크는 이전 노드의 주소 링크**

- 시간 측면에서는 좋을 수 있으나, 메모리 측면에서는 손해가 있다. (즉, 메모리를 손해보면서 더욱 빠르게 실행할 수 있는 알고리즘이다.)

### 알고리즘
- Linked List: 길이가 정해져있지 않은 Data에 연결된 집합
- 단방향 Linked List
    - Data를 저장한 Node에 다음 Node의 주소를 가지고 있는 형태

- 양방향 Linked List
    - Data를 저장한 Node의 다음 Node, 이전 Node의 주소를 가지고 있는 형태

    - **새로운 Node 삽입**
        - **이전 Node가 가지고 있던 다음 Node 주소를 새로운 Node에 삽입**
        - **이전 Node의 주소를 새로운 Node의 이전 주소로 삽입**
        - **다음 Node가 가지고 있던 이전 Node의 주소를 새로운 Node의 주소로 삽입**

    - **기존 Node 삭제**
        - **기존 Node가 가지고 있는 다음 Node 주소를 이전 Node의 다음 주소에 삽입**
        - **기존 Node가 가지고 있는 이전 Node 주소를 다음 Node의 이전 주소에 삽입**

- **삭제 및 삽입을 통한 풀이가 아니다!** (일반적으로)
- **`prev`와 `next`를 활용하여 index를 움직여주면서 삽입, 삭제를 표시해주는 방식으로 풀이를 진행한다.**

<details>
    <summary><b>대표예제</b></summary>

### 표 편집 (프로그래머스 81303)

#### 문제
[링크 참고](https://programmers.co.kr/learn/courses/30/lessons/81303)

#### Code

```python
def solution(n, k, cmd):
    answer = ''
    
    name_list = []
    for i in range(n):
        name_list.append([max(0,i-1), 'O', min(i+1,n-1)])
        # [[0,'O',1], [0,'O',2], [1,'O',3], [2,'O',4], ..., [5,'O',7], [6,'O',7]]
    
    delete_stack = []     # 삭제할 name & row
    now = k               # 현재 행
    for command in cmd:

        if "D" in command:
            move = command.split()[-1]
            for i in range(int(move)):
                now = name_list[now][2] # _next로 움직인 결과값

        elif 'U' in command:
            move = command.split()[-1]
            for i in range(int(move)):
                now = name_list[now][0] # prev로 움직인 결과값

        elif command == "C":
            name_list[now][1] = 'X'
            prev, _, _next = name_list[now]
            delete_stack.append([now, prev, _next])   

            # 주소 변환
            if now == name_list[now][2]: # 마지막 행일 경우
                name_list[prev][2] = prev 
                now = prev
            elif now == name_list[now][0]: # 첫 행일 경우
                name_list[_next][0] = _next
                now = _next
            else:
                name_list[prev][2] = _next
                name_list[_next][0] = prev
                now = _next

        elif command == 'Z':
            idx, prev, _next = delete_stack.pop()

            # 삽입 행
            name_list[idx][0] = prev
            name_list[idx][2] = _next
            name_list[idx][1] = 'O'

            # 이전 행 => 첫번째 행이 복구되는 경우에는 prev를 조작하지 않는다.
            if prev != idx:
                name_list[prev][2] = idx

            # 다음 행 => 마지막 행이 복구되는 경우에는 next를 조작하지 않는다.
            if _next != idx:
                name_list[_next][0] = idx
                
    for i in range(n):
        answer += name_list[i][1]
    return answer
```

</details>

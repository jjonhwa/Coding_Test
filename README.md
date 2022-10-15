# Coding_Test
Practice about Conding_Test

## Algorithm Study
- [BackTracking](#BackTracking)
- [양방향 링크드 리스트](#양방향-링크드-리스트)
- [분리집합](#분리집합)
- [위상정렬](#위상정렬)
- [플로이드 워셜](#플로이드-워셜)
- [최장 증가 부분 수열(LIS) 알고리즘](#최장-증가-부분-수열LIS-알고리즘)
- [크루스칼 알고리즘](#크루스칼-알고리즘)
- [LRU 알고리즘](#LRU-알고리즘)
- [다익스트라](#다익스트라)
- [밸만포드](#밸만포드)
- [최소 스패닝 트리](#최소-스패닝-트리)
## Module 사용법
- [heapq](#heapq)
- [Counter](#Counter)

## Study

- Python 명명 규칙
    - Python 명명 규칙 ([https://mentha2.tistory.com/186](https://mentha2.tistory.com/186))
    - Pythonic → PEP8 ([https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/))
- heapq vs deque
    - heapq가 필수적으로 필요할 경우가 아닌 이상 deque 사용 권장
    - heapq의 경우, multihtread -> wait()를 사용하기 때문세 속도가 조금 더 느리다고 한다.
    - deque: 선입선출, BFS
    - heapq: 최소힙, 최대힙, 다익스트라 (시간복잡도: O(logN))
- **List Indexing의 Time Complexity: O(n)**
- **Combination의 Time COmplexity: n개 중 2개 -> O(2^n) / n개 중 3개 -> O(3^n) ...**

~~- `while q` vs `while len(q)`~~
    ~~- 결론부터 말하자면, **`while len(q)`를 활용했을 경우 속도가 조금 더 빠르다.**~~
    ~~- `while q`의 경우, 시간이 q만큼 소모. 즉, 시간복잡도 O(q)~~
    ~~- `while len(q)`의 경우, 시간은 상수의 시간복잡도를 가진다. 즉, 시간복잡도 O(1)~~
- `while q` vs `while len(q)` (참고, 확실하진 않다.)
    - `while q`를 활용하는 것이 시간적으로 더욱 효율적이다.
    - `while len(q)`는 list 참조변수가 가리키는 주소로 접근해서 list 객체 안에 있는 len 변수까지 접근하기 때문에 총 2번의 연산을 하는 반면, `while q`는 list 참조변수가 가리키는 주소로 가서 한 번의 연산만 하면 종료된다.
- "다익스트라 + 왕복 경로"를 해결할 때, 결로를 뒤집어주는 방식을 활용하는 것도 좋은 방법이 될 수 있다.
- **`if something in [1,2,...]` 과 같은 조건문을 활용할 경우, Time Complexity는 O(N)이므로, 이를 상수 시간복잡도로 만들어주기 위하여 visited와 같은 정보를 미리 저장해놓고 사용하도록 한다.**
- `if something in set([1,2,...])`과 같은 조건문을 사용하게 되면, Time Complexity는 O(1)이 된다.
- `global` 변수의 경우 참조 시간이 더 오래 걸린다.
- Python의 경우, 전역 변수에 접근하는 것은 시간이 오래걸리기 떄문에 **지역 변수로 선언하여 사용하는 것이 더 효율적**이다.
- 원형으로 생긴 문제를 해결할 경우, 직선 구간을 *2를 해주게되면, 원형을 선형문제로 해결할 수 있다.
- `defaultdict`를 사용할 경우, `dict`에 빈 리스트 혹은 int, str 등등의 값을 사전에 정의하지 않아도 append 혹은 추가에 대한 실행을 할 수 있다.
- `Counter`는 집합 연산을 지원한다.
    - 반면, `dictionary`는 집합 연산을 지원하지 않는다.
    - 즉, Counter는 intersection(&), union(|)을 사용할 수 있다.
    - 이 때, intersection의 경우 key 기준 교집합 연산을 수행하며, value의 경우 더 작은 값을 택한다.
    - union의 경우 key 기준 합집합 연산을 수행하며, value의 경우 더 큰 값을 택한다.    
- 경우의 수가 많아서 어떤 큰 값으로 나누어 주어야 할 경우, 중간중간에 나누어준 값을 리턴해야 시간초과를 회피할 수 있다.
    - 메모이제이션의 경우, 다시 사용할 값만을 저장해둔다! 라는 것을 기억하며 필요한 값이 나머지 값이라면 나머지 값만 저장해두고 사용하도록 한다.  
- for loop를 돌 때, 바로 꺼내쓸 수 있다면
    - `for i in range(len(stones))` 보다는
    - `for stone in stones` 사용하기
- 2가지 값을 비교할 경우,
    - `max(a,b)` 보다는
    - `if a>b: a=b` 사용하기
     
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
- `heapify()`는 O(N)의 시간복잡도를 가진다.
- `heapq`는 tuple 형태로 값을 넣어줄 때, 0번째 index를 기준으로 정렬되며, 0번째 index가 같을 경우에는 1번째 index 순서대로 정렬된다.
    
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

</details>


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

## 분리집합

<details>
    <summary><b>설명</b></summary>

### 분리집합이란?
- Union-Find 집합이라고도 하며, Disjoint-Set (서로소 집합 혹은 분리 집합)이라고 한다.
- 흔히, 배열에서 Index를 Node로 나타내여 각각의 index에 대한 값에 해당 index의 parent node 정보를 저장한다.
- 주로 그래프 문제에 적용할 수 있으며, 순수히 Node간의 연결 관계를 파악할 때, 유용하다.

### 알고리즘
- Union (서로 다른 두 집합을 합치는 연산)
- Find (Root Node를 찾는 연산)

#### Union
- 서로 다른 두 집합을 합치는 연산
- 각 tree의 root node를 비교하여 둘 중 작은 root node를 기준으로 합친다. (큰 node를 기준으로 합쳐서 상관없으나, 흔히 이렇게 한다고 한다.)
- Union 연산을 하기 위해서는 반드시 find 연산을 필요로한다.

#### Find
- 어떤 인자를 주었을 때, 해당 node의 root node를 반환하는 연산
- 임의의 두 node가 연결되어있는지 확인할 때 사용한다.
- 흔히, 재귀 형태로 구현한다.
- 시간복잡도의 효율을 높이기 위해, 경로 압축 최적화를 한다. (자식 노드들이ㅡ 값을 모두 root node로 변경하여, Skewed Tree를 방지한다.)

</details>


<details>
    <summary><b>대표예제</b></summary>

### 집합의 표현 (백준 1717)

#### 문제
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

#### Code

```python
import sys

sys.setrecursionlimit(10**6)                # 재귀 한도 늘려주기
input = sys.stdin.readline

n, m = list(map(int, input().split()))
parent = [i for i in range(n+1)]            # Parent Node 정의

def find(x):
    """부모 Node를 찾는 함수"""
    if parent[x] == x:                      # 부모가 자기 자신을 경우 그대로 반환
        return x
    
    parent[x] = find(parent[x])             # 부모가 다른 값일 경우
    return parent[x]

def union(parent_a, parent_b):
    """
    두 집합을 합쳐주는 함수
    
    Args:
        parent_a: a의 부모 node
        parent_b: b의 부모 node
    """
    if parent_a < parent_b:                 # 더 작은 값을 기준으로 합쳐준다.
        parent[parent_b] = parent_a
    else:
        parent[parent_b] = parent_b

for _ in range(m):
    cal, a, b = list(map(int, input().split()))
    parent_a = find(a)
    parent_b = find(b)

    if cal == 0:
        union(parent_a, parent_b)
    else:
        if parent_a == parent_b:
            print('YES')
        else:
            print('NO')

```

</details>

## 위상정렬

<details>
    <summary><b>설명</b></summary>

### 위상정렬이란?
- 어떤 일을 하는 순서를 찾는 알고리즘
- 정점들의 선행순서를 위배하지 않으면서 모든 정점을 나열하는 것

### 위상정렬의 특징
- 한 방향 그래프에서는 여러 위상 정렬이 가능
- 선택되는 정점의 순서를 위상 순서라고 한다.
- 남아있는 정점 중 진입 차수가 0인 정점이 없다면 알고리즘이 중단되고 실행불가능하다.
Cycle이 발생하는 경우, 위상 정렬을 수행할 수 없다.

### 알고리즘
- 우선 위상정렬 알고리즘이 적용 가능한지 확인한다.
    - Cycle이 존재하지 않는가?
    - 시작점이 존재하는가?
- 위의 조건을 만족한다면, 마지막으로 결과가 있는지 확인한다.

</details>


<details>
    <summary><b>대표예제</b></summary>

### 문제 (백준 14567)

올해 Z대학 컴퓨터공학부에 새로 입학한 민욱이는 학부에 개설된 모든 전공과목을 듣고 졸업하려는 원대한 목표를 세웠다. 어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수할 수 있게 되어 있다. 공학인증을 포기할 수 없는 불쌍한 민욱이는 선수과목 조건을 반드시 지켜야만 한다. 민욱이는 선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수할 수 있는지 궁금해졌다. 계산을 편리하게 하기 위해 아래와 같이 조건을 간소화하여 계산하기로 하였다.

- 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
- 모든 과목은 매 학기 항상 개설된다.

### Code

```python
from collections import deque
import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))          # node와 간선의 개수 입력
indegree = [0] * (n+1)                          # 모든 Node에 대한 진입차수를 0으로 초기화
graph = [[] for _ in range(n+1)]                # 각 Node에 연결된 간선 정보를 담기 위한 graph 초기화
answer = [0] * (n+1)                            # 해당 Node의 수강학기를 담기 위한 List
for _ in range(m):                              # Graph에서 모든 간선 정보 입력
    a, b = list(map(int, input().split()))
    graph[a].append(b)                          # a에서 b로만 이동 가능
    indegree[b] += 1                            # b의 진입차수 1 증가

queue = deque()
for i in range(1, len(indegree)):               # 맨 처음 수강정보를 queue에 삽입
    if indegree[i] == 0:                        # 진입차수가 없는 경우에만 추가 (맨 처음이므로)
        queue.append(i)
        answer[i] = 1

while len(queue):                               # queue가 빌 때 까지, 반복
    target = queue.popleft()
    for _next in graph[target]:
        indegree[_next] -= 1                    # 진입차수 -1

        if indegree[_next] == 0:                # 진입차수가 0일 경우에만 answer update
            queue.append(_next)
            answer[_next] = answer[target] + 1  # 이전 answer에 + 1

# 출력
for i in range(1, len(answer)):
    print(answer[i], end=' ')
```

</details>

## 플로이드 워셜

<details>
    <summary><b>설명</b></summary>

### 플로이드 워셜 알고리즘이란?
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.

### 작동 원리
- 다익스트라 알고리즘과 마찬가지로 단계별로 **거쳐가는 노드를 기준으로 알고리즘을 수행**한다.
- 2차원 테이블에 최단 거리 정보를 저장한다.
- 이전 값을 활용한다는 점에서 다이나믹 프로그래밍 유형에 속한다.
- 시간복잡도 O(N^3)이기 때문에, 노드의 개수가 적을 경우에 유용하게 사용할 수 있으며, 노드와 간선의 개수가 많아지면 플로이드워셜보다는 다익스트라를 활용해야 해결할 수 있다.

### 점화식
- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인한다.
- **a에서 b로 가는 최단 거리**보다 **a에서 k를 거쳐 b로 가는 거리**가 더 짧은지 검사한다.
- 점화식
**$D_{ab}$ = $min(D_{ab}, D_{ak} + D_{kb})$**

### 과정
- 2차원 List를 만든다. 이 때, 행은 출발 Node를, 열은 도착 Node를 의미한다.
- 초기 상태
    - **자기 자신에서 자기 자신으로 가는 값은 0이다.**
    - **인접한 Node만을 확인하면서 인접한 Node까지의 거리를 2차원 List에 삽입한다.**
- 알고리즘 수행
    - **점화식에 따라, a to b와 a to k + k to b를 비교하면서 더 짧은 거리의 값으로 update**

</details>


<details>
    <summary><b>코드</b></summary>

```python
INF = int(1e9) # 무한을 의미하는 값을 설정

n = int(input()) # node의 개수 입력
m = int(input()) # 간선의 개수 입력
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 list 형태로 graph 초기화

# 자기 자신에서 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 직접 연결된 node 사이의 거리 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    # 양방향일 경우
    # graph[b][a] = c

# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[i][j], end=' ')
```

</details>

## 최장 증가 부분 수열(LIS) 알고리즘

<details>
    <summary><b>설명</b></summary>

### LIS란?
- 가장 긴 증가하는 부분 수열을 의미한다.
- 예를 들어, `[6, 2, 5, 1, 7, 4, 8, 3]`가 있을 경우, LIS는 `[2, 5, 7, 8]`이 된다.

### 작동 원리
- LIS를 풀기 위한 가장 일반적인 방법은 DP를 이용하는 것이다.

```python
dp = [1] * n
for i in range(n):
    # 첫번째 요소부터 i번째 요소까지 비교
    for j in range(i):
        if arr[i] > arr[j]:
            # 값의 크기에 따른 index를 가지게 된다.
            dp[i] = max(dp[i], dp[j]+1)
```

- 하지만, DP로 접근하는 것은 `O(n^2)`을 갖게 된다.
- 시간복잡도를 개선하기 위해 `이분탐색`을 활용한다.
- 다음의 방법을 활용하여 시간복잡도 `O(N logN)`으로 개선시킬 수 있다.

```python
memoization = [0]
arr = [0] + original_array

for case in cases:
    
    # 기존 최댓값보다 큰 값이 들어올 경우, 조건 없이 삽입 
    if memoization[-1] < case:
        memoization.append(case)
    
    # 최댓값보다 작은 값일 경우, 이분탐색으로 삽입될 위치를 탐색 후 변경하여 삽입
    else:
        left = 0
        right = len(memoization)
        
        while left < right:
            mid = (left + right) // 2

            if memoization[mid] < case:
                left = mid + 1
            else:
                right = mid
        memoization[right] = case
```

- `[6, 2, 5, 1, 7, 4, 8, 3]`가 있을 경우
    - `[6]`
    - `[2]`
    - `[2, 5]`
    - `[1, 5]`
    - `[1,5,7]`
    - `[1,4,7]`
    - `[1,4,7,8]`
    - `[1,3,7,8]`
- 즉, 이분탐색을 이용하여 LIS를 구하게 되면, **가장 긴 증가하는 수열을 만드는 것은 아니다.** 단지, 가장 긴 증가하는 수열의 길이만을 올바르게 출력한다는 것을 알 수 있다.

</details>

## 크루스칼 알고리즘

<details>
    <summary><b>설명</b></summary>

### 크루스칼 알고리즘이란?
- 최소신장트리을 찾는 알고리즘
- 최소신장트리: 무방향 가중치 그래프에서 간선의 가중치 합이 최소인 것
- 항상 욕심내서 최솟값을 선택하여 가중치의 합이 최소인 것을 찾기 때문에 그리디 알고리즘으로 볼 수 있다.


### 작동 원리
- 간선이 사이클을 만드는지 확인: Union-Find 알고리즘 활용
- 그래프의 가중치를 기준으로 오름차순 정렬
- 가중치가 낮은 간선부터 선택하면서, 사이클을 만들면 제외

### 과정
- 그래프의 가중치를 기준으로 오름차순 정렬 `(node, node, weight)
- 정렬된 순서대로 간선을 선택한다.
- 이 때, 사이클을 형성할 경우(Union-Find), 선택하지 않는다. (이미 낮은 간선이 먼저 선택되었으므로, 사이클을 형성하는 높은 간선은 선택하지 않는다.)


</details>


<details>
    <summary><b>코드</b></summary>

```python
n = 6
graph = [(1,2,13), (1,3,5), (2,4,9), (3,4,15), (3,5,3),
         (4,5,1), (4,6,7), (5,6,2)]
graph.sort(key = lambda x: x[2]) # 가중치 기준으로 정렬

# parent node를 담는 list 생성 => 노드가 1번부터 시작하므로, 0을 채워준 채로 시작
parent = [0]
for i in range(1, n+1):
    parent.append(i)

# find 함수
def find(x):
    if parent[x] == x:
        return x
    
    # 타고 들어가면서 부모가 자기 자신일 때 까지 반복
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

minimum_tree = [] # 최소신장트리
tree_edges = 0 # 간선의 개수
weight_sum = 0 # 가중치 합
while True:
    # 모든 그래프를 순회하였을 경우 break
    if tree_edges == n-1:
        break
    
    a, b, weight = graph.pop(0)
    # 서로 다른 집합이라면 추가 (즉, 사이클이 생성되지 않는다면)
    if find(a) != find(b):
        union(a, b)
        minimum_tree.append((a, b))
        tree_edges += 1
        weight_sum += weight
```

</details>

## LRU 알고리즘

<details>
    <summary><b>설명</b></summary>

### LRU 알고리즘이란?
- 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
- 컴퓨터의 자원은 한정적이며, 한도내에서 최고의 효율을 얻기 위해 여러 알고리즘이 존재, 그 중 하나 (FIFO, OPT, LRU, LFU, MFU 등)

### 작동 원리
- 페이지에 저장된 데이터가 언제 사용되었는지를 알 수 있게하는 부분을 구현해서 제일 오랫동안 참조되지 않은 데이터를 제거하는 방법
- 페이지에 데이터를 큐 형식으로 저장하는 방식
- 페이지 내에 데이터가 존재한다면 데이터를 페이지 내에서 제거하고, 맨 위로 다시 올리고, 존재하지 않는다면, 바로 입력하여 맨 아래에 있는 데이터를 삭제하는 과정을 진행

### 과정
- `cache hit`: cache에 이미 있는 값이 새로 들어올 경우, 기존의 값을 삭제하고 맨 뒤에 추가
- `cache miss`: cache에 존재하지 않을 경우, 맨 처음 들어온 값이 삭제되고 맨 뒤에 추가

</details>

## 다익스트라

<details>
    <summary><b>설명</b></summary>

### 다익스트라 알고리즘이란?
- 최단 경로 탐색 알고리즘
- 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려준다. (시작점이 고정된 경우)

### 작동 원리
- 출발 노드 설정
- 출발 노드로부터 시작해서, 방문하지 않은 노드 중 가장 비용이 적은 노드를 선택
- 최소 비용을 갱신하면서, 최소 비용인 노드부터 순차적으로 방문
- 위 과정을 반복
- 모든 노드를 한 번씩만 방문하기 때문에, 시간복잡도 O(ElogV)으로 탐색을 종료할 수 있다.

</details>


<details>
    <summary><b>대표 예제</b></summary>

### 문제 (백준 18352)

```python
"""
    문제:
    어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

    이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

    예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

    입력:
    첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
    둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
    이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

    출력:
    X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

    이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""

import heapq

import sys
input = sys.stdin.readline

n, m, k, x = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    
visited = [False for _ in range(n+1)]

# heap: tuple(해당지점까지의 거리, 해당 지점)
heap = []
heapq.heappush(heap, (0, x)) 
visited[x] = True

answer = []
while heap:
    dist, node = heapq.heappop(heap)

    # 거리가 k를 만족할 경우 다음으로 더 이상 진행할 필요 없음
    if dist == k:
        answer.append(node)
        continue

    for next_node in graph[node]:

        # 최단거리 순으로 pop을 수행하기 때문에, 이미 방문했다면 최단거리가 아니라는 것을 의미
        if visited[next_node]:
            continue
        visited[next_node] = True

        # (거리+1, node) 추가 
        heapq.heappush(heap, (dist+1, next_node))


if not answer:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
```

</details>

## 밸만포드

<details>
    <summary><b>설명</b></summary>

### 밸만포드 알고리즘이란?
- 시작 정점으로부터 다른 정점까지의 최단 경로를 찾기 위한 알고리즘
- **음수 가중치**가 있는 그래프의 시작정점에서 다른 정점까지의 최단거리를 구할 수 있다.
- **음수 사이클** 존재 여부를 알 수 있다.

### 작동 원리
- 출발 노드 설정
- 최단 거리 테이블 초기화
- 다음 과정을 (V-1)번 반복 (V = Node의 개수)
    - 모든 간선 E개를 하나씩 확인
    - 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
- 음수 간선 순환 체크 
    - 위의 과정을 V번 수행했을 때, Table이 갱신될 경우 '음수 간선 순환'이 존재
    - '음수 간선 순환'이 존재할 경우, 최단 거리가 무한대로 업데이트 된다.

### 다익스트라 vs 밸만 포드

#### 다익스트라
- 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
- 음수 간선이 없다면 최적의 해를 찾을 수 있다.
- Time Complexity: O(VlogE)

#### 밸만 포드
- 매번 모든 간선을 전부 확인
    - 다익스트라 알고리즘에서의 최적의 해 역시 항상 포함
- 음수 간선 순환을 탐지할 수 있다.
- Time Complexity: O(VE)

</details>


<details>
    <summary><b>대표 예제</b></summary>

### 문제 (백준 18352)

```python
"""
    문제:
    때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다. 
    (단 도로는 방향이 없으며 웜홀은 방향이 있다.) 
    웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 
    웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

    시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다. 
    한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 
    출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다. 
    여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

    입력:
    첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
    그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 
    각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500), 도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다. 
    그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다. 
    S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다. 
    그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데 S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다. 
    T는 10,000보다 작거나 같은 자연수 또는 0이다.

    두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

    출력:
    TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.

    NOTE: 아래의 예제는, Test Case가 1개라고 가정했을 떄의 코드이다.
"""

import sys
input = sys.stdin.readline

n, m, w = list(map(int, input().split()))

edge = []
for _ in range(m):
    a, b, weight = list(map(int, input().split()))
    edge.append((a, b, weight))
    edge.append((b, a, weight))

for _ in range(w):
    a, b, weight = list(map(int, input().split()))
    edge.append((a, b, -weight))

## (기존 방식 - 시작 지점을 고정하므로, 모든 값을 무한대로 초기화)
# INF = int(1e9)
# dist = [INF for _ in range(n+1)]

## (응용 - 단순 싸이클의 존재 유무만 확인하면 되므로 랜덤값으로 초기화해도 무방)
dist = [0 for _ in range(n+1)]


negative_cycle = False

## (기존 방식 - 시작 지점을 고정)
# start = 1
# dist[start] = 0

## (응용 - 시작 지점을 고정할 필요가 없음)

# 전체 노드에 대하여 반복
for i in range(n):

    # 모든 노드에 대해서 모든 간선을 확인
    for j in range(len(edge)):
        current, next_node, cost = edge[j]
        
        # 현재 간선에서 다음 노드로 이동하는 거리가 더 짧을 경우 갱신
        ## (기존 방식 - 특정 Node에서 출발해서 다른 Node로 가는 최단거리)
        # if dist[current] != INF and dist[next_node] > dist[current] + cost:
        #     dist[next_node] = dist[current] + cost

        #     if i == n-1:
        #         negative_cycle = True

        ## (응용 - 출발 지점이 없고, 단순 싸이클의 존재 유무만 확인)
        if dist[next_node] > dist[current] + cost:
            dist[next_node] = dist[current] + cost

            if i == n-1:
                negative_cycle = True
                break

if negative_cycle:
    print("YES")
else:
    print("NO")
```

</details>

## 최소 스패닝 트리

<details>
    <summary><b>설명</b></summary>

### 스패닝 트리란?
- 그래프 내의 모든 정점을 포함하는 트리
- **최소 연결 부분 그래프** => 즉, 간선의 수가 가장 적은 그래프
- **최소 간선**을 가지는 그래프는 필연적으로 트리 형태가 되고, 이를 **스패닝 트리**라고 한다.

### 스패닝 트리의 특징
- **DFS**, **BFS**를 이용하여 그래프에서 스패닝 트리를 찾을 수 있다.
- 하나의 그래프에는 여러개의 스패닝 트리가 존재할 수 있다.
- 스패닝 트리는 트리의 특수한 형태로서, **모든 정점들이 연결**되어 있고, **사이클을 포함하지 않는다.**

### 최소 스패닝 트리
- 최소 스패닝 트리란, 간선의 가중치가 존재할 때, 가중치를 고려하여 최소 비용을 가지는 스패닝 트리를 의미한다.
- 즉, 스패닝 트리 중, 가중치가 가장 작은 스패닝 트리를 최소 스패닝 트리라고 한다.

### 최소 스패닝 트리의 특징
- N개의 Node가 있을 때, N-1개의 간선만을 사용해야 한다.
- 사이클이 포함되어서는 안된다.
- 간선의 가중치 합이 최소여야 한다.

### 구현 방법

#### Kruskal MST 알고리즘
- 1. 그래프의 간선들을 가중치의 오름차순 정렬
- 2. 간선을 순차적으로 확인하면서, 사이클을 형성하지 않는 간선을 선택한다.
    - 2-1. 사이클 형성 확인 - 분리집합 활용
- 3. 해당 간선을 MST 집합에 추가한다.

#### Prim MST 알고리즘
- 1. 시작 정점만을 MST 집합에 추가
- 2. 현재 선택된 정점들에서 연결된 최소 간선을 선택 (이 때, 상대 노드는 선택되지 않은 노드)
- 3. n-1개의 edge를 가질 때 까지 반복

</details>


<details>
    <summary><b>Kruskal MST 알고리즘 구현 과정</b></summary>

### 크루스칼 MST 알고리즘

```python
n = 6
edges = [(1,2,13), (1,3,5), (2,4,9), (3,4,15), (3,5,3),
         (4,5,1), (4,6,7), (5,6,2)]
edges.sort(key = lambda x: x[2]) # 간선 가중치의 오름차순으로 정렬
edges = deque(edges)

parent = [i for i in range(n+1)] # 0부터 시작 혹은 1부터 시작에 따라서 유동적으로 변경

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
    
mst = []
edge_count = 0
weight_sum = 0
while True:
    if edge_count == n-1: # 최소 스패닝 트리의 최소 edge의 개수는 n-1개
        break

    a, b, weight = edges.popleft()
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b))
        weight_sum += weight
        edge_count += 1
```

</details>

<details>
    <summary><b>Prim MST 알고리즘 구현 과정</b></summary>

### Prim MST 알고리즘

```python
import heapq

n = 6
edges = [(1,2,13), (1,3,5), (2,4,9), (3,4,15), (3,5,3),
         (4,5,1), (4,6,7), (5,6,2)]
graph = [[] for _ in range(n+1)]

# 내 좌표도 함께 넣어주도록 한다.
for edge in edges:
    a, b, weight = edge
    graph[a].append((weight, b, a))
    graph[b].append((weight, a, b))

# 선택된 노드를 확인하기 위해 방문 체크
visited = [False for _ in range(n+1)]

# 시작 노드부터 출발
start_node = 1
candidate = graph[start_node]
heapq.heapify(candidate)
visited[start_node] = True

mst = []
total_weight = 0
while candidate:
    # 가장 가중치가 낮은 간선부터 추출
    weight, you, me = heapq.heappop(candidate)

    if not visited[you]:
        visited[you] = True
        mst.append((me, you))
        total_weight += weight

        # 다음 인접 간선 탐색
        for _next in graph[you]:

            # you에 연결된 노드 중에서 방문하지 않았을 경우에만 candidate에 추가
            if not visited[_next[1]]:
                heapq.heappush(candidate, _next)
```

</details>

## 순열과 조합 구현

<details>
    <summary><b>설명</b></summary>

- 순열과 조합을 활용하면서, 이 함수를 활용하는 도중에 백트래킹이 필요할 때, 직접 구현할 필요성이 있다.
- 모든 순열과, 조합이 필요하다면 `itertools`에서 활용하는 것이 단연 더 좋다.
- 다만, 백트래킹이 필요할 때, 직접 구현해야 하므로 알아두도록 하자.

### 순열
1. 배열과 길이를 입력받는다.
2. 정렬의 경우, 큰 의미는 없지만 출력할 때 정렬된 채로 출력하기 위하여 사용한다.
3. 현재 값이 `chosen`안에 들어있는 지를, `visited`로 확인한다.
4. 배열이 원하는 길이만큼 생성되었다면 종료
5. `visited`, `generate`, `unvisited` 순으로 들어가면서, 배열을 생성한다.

### 조합
1. 배열과 길이를 입력받는다.
2. 정렬의 경우, 큰 의미는 없지만 출력할 때 정렬된 채로 출력하기 위하여 사용한다.
3. `방문 체크를 하지 않고`, `현재 index의 다음 index부터 반복`을 해준다.


</details>


<details>
    <summary><b>순열과 조합</b></summary>

### 순열

```python

def permutation(arr: list, r: int):
    arr = sorted(arr)
    visited = [False for _ in range(len(arr))]

    def generate(chosen, visited):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not visited[i]:
                chosen.append(arr[i])
                visited[i] = True
                generate(chosen, visited)
                visited[i] = False
                chosen.pop()
    
    generate([], used)

```

### 조합

```python

def combination(arr:list, r: int):
    arr = sorted(arr)

    def generate(chosen, num):
        if len(chosen) == r:
            print(chosen)
            return
        
        for i in range(num, len(arr)):
            chosen.append(arr[i])
            generate(chosen, i+1)
            chosen.pop()
    
    generate([], 0)

```

</details>
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
card_list = []
for _ in range(N):
    card_list.append(list(map(int, input().split())))

# 각 행에서의 최소값을 구한다.
# 그 최소값 중 가장 큰 값을 출력한다.
minimum_card_list = []
for card in card_list:
    minimum_card_list.append(min(card))

print(max(minimum_card_list))
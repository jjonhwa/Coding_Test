# 이야기의 진실을 아는 사람이 있을 경우
# 어떤 사람이 어떤 파티에서는 진실, 다른 파티에서는 거짓을 들을 경우

N, M = list(map(int, input().split()))
true_know = list(map(int, input().split()))
if len(true_know) == 0:
    know = []
else:
    know = true_know[1:] # 이야기의 진실을 아는 사람의 번호

party = []
for _ in range(M):
    people = list(map(int, input().split()))
    party.append(people[1:])

# 겹치는 people들을 묶어서 know list 만들기
before_know = []
while True:
    for p in party:
        talk = False
        for people in p:
            if people in know:
                talk = True
                break
  
        if talk:
            know += p
        know = list(set(know))

    if before_know == know:
        break
    else:
        before_know = know.copy()

# 하나씩 돌면서 know_list에 없으면 count
cnt = 0
for p in party:
    talk = False
    for people in p:
        if people in know:
            talk = True
            break
    
    if talk:
        continue
    else:
        cnt += 1

print(cnt)


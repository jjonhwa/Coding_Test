import sys
input = sys.stdin.readline

# 산성 - 양수 / 알칼리성 - 음수
# 섞으면 둘의 합으로 나타낸다.
# 두 용액을 혼합하여 특성값이 0에 가까운 용액을 만든다.
# 같은 류의 용약을 합칠수도 있다. (-1-2 = -3)
N = int(input())
yong = list(map(int, input().split()))

# 절대값과 부호를 가지는 이중list 형태로 구성
abs_yong = []
for i in range(len(yong)):
    if yong[i] > 0:
        abs_yong.append([yong[i], 1])
    else:
        abs_yong.append([abs(yong[i]), -1])

# 절대값을 기준으로 정렬
abs_yong.sort(key = lambda x: x[0])

# 결국 두 값의 합이 0에 가까워야 하므로 서로 다른 부호일 경우 연속되는 두 개의 값만 합친다.
merge = []
for i in range(1, len(abs_yong)):
    first = abs_yong[i-1][0]
    second = abs_yong[i][0]

    first_sign = abs_yong[i-1][1]
    second_sign = abs_yong[i][1]
    if first_sign != second_sign: # 양, 음일 경우에만 연산
        value = first * first_sign + second * second_sign
        merge.append([first * first_sign, second * second_sign, value])


# 같은 류의 용액 => 무조건 맨 앞 2개만
plus_yong = []
minus_yong = []
for y in yong:
    if y > 0:
        plus_yong.append(y)
    else:
        minus_yong.append(y)
plus_yong.sort()
minus_yong.sort()

# 같은 류의 용액이 2개 이상일 경우에만 실행 => 조건이 없을 경우, 모두 알칼리 혹은 산성만 들어올 경우 index error가 발생
if len(plus_yong) >= 2:
    merge.append([plus_yong[0], plus_yong[1], plus_yong[0] + plus_yong[1]])
if len(minus_yong) >= 2:
    merge.append([minus_yong[-1], minus_yong[-2], minus_yong[-1] + minus_yong[-2]])

# 최종 출력
merge.sort(key = lambda x: abs(x[2])) # 절대값 value 기준으로 정렬
final = merge[0][:2] # [-99, 98, -1] => [-99, 98]만 빼냄.
final.sort() # 오름차순 정렬
for f in final:
    print(f, end = ' ')

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)

    for b in B:
        if not A:
            break

        check = False
        while not check and A:
            if b > A[-1]:
                answer += 1
                check = True
                A.pop()
            else:
                A.pop()
    return answer

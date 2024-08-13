# https://school.programmers.co.kr/learn/courses/30/lessons/181916

'''
1 부터 6 까지 숫자가 적힌 주사위가 네 개 있습니다.
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

- 네 주사위에서 나온 숫자가 모두 p 로 같다면 1111 x p 점을 얻습니다.
- 세 주사위에서 나온 숫자가 p 로 같고 나머지 다른 주사위에서 나온 숫자가 q (q!=p)라면 (10 x p + q)**2 점을 얻습니다.
- 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q 라고 한다면 (p + q) x |p - q| 점을 얻습니다.
- 어느 두 주사위에서 나온 숫자가 p 로 같고 나머지 두 주사위에서 나온 숫자가 각각 p 와 다른 q, r 이라면 q x r 점을 얻습니다.
- 네 주사위에서 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d 로 주어질 때,
얻는 점수를 return 하는 solution 함수를 작성해 주세요.
'''
import math
def solution(a, b, c, d):
    num_list = [a, b, c, d]
    num = list(set(num_list))
    if len(num) == 1:
        answer = 1111 * a
    elif len(num) == 4:
        answer = min(num)
    elif len(num) == 3:
        p = []
        qr = []
        for n in num_list:
            if n not in qr:
                qr.append(n)
            elif n not in p:
                    p.append(n)
        p = set(p)
        qr = set(qr)
        qr = list(qr.difference(p))
        answer = qr[0] * qr[1]
    
    # 세 주사위의 값이 같거나 두 주사위씩 값이 같은 경우
    elif len(num) == 2:
        x = [a, b]
        y = [c, d]
        if len(set(x)) == 1 and len(set(y)) == 2:
            if a == c:
                p = a
                q = d
            else:
                p = a
                q = c
            answer = (10 * p + q)**2
        elif len(set(x)) == 2 and len(set(y)) == 1:
            if c == a:
                p = c
                q = b
            else:
                p = c
                q = a
            answer = (10 * p + q)**2
        else:
            p = num[0]
            q = num[1]
            answer = (p + q) * abs(p-q)
    
    return answer



# 예시 값
a, b, c, d = 2, 2, 2, 2
print(solution(a, b, c, d))
a, b, c, d = 4, 1, 4, 4
print(solution(a, b, c, d))
a, b, c, d = 6, 3, 3, 6
print(solution(a, b, c, d))
a, b, c, d = 2, 5, 2, 6
print(solution(a, b, c, d))
a, b, c, d = 6, 4, 2, 5
print(solution(a, b, c, d))

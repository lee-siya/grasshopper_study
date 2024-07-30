# https://school.programmers.co.kr/learn/courses/30/lessons/181930

'''1 부터 6 까지 숫자가 적힌 주사위가 세 개 있습니다.
    세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c 라 했을 때
    얻는 점수는 다음과 같습니다.
    
    - 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
    - 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면
        (a + b + c) x (a**2 + b**2 + c**2) 점을 얻습니다.
    - 세 숫자가 모두 같다면 (a + b + c) x (a**2 + b**2 + c**2) x (a**3 + b**3 + c**3) 점을 얻습니다.
    
    세 정수 a, b, c 가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.'''

def solution(a, b, c):
    if a != b and b != c and c != a:
        result = a + b + c
    elif a == b == c:
        result = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    else:
        result = (a + b + c) * (a**2 + b**2 + c**2)
    answer = result
    return answer


# 조건 순서대로 작성하려다가 길어질거 같고, if 와 elif 를 제외하면 두 숫자가 같은 경우만 남기 때문에 else를 사용함
# 다른 사람 문제 풀이보고 set 함수를 사용하는 것을 배움 저런 방법이



# 예시 값
a = 2
b = 6
c = 1
print(solution(a, b, c))
a = 5
b = 3
c = 3
print(solution(a, b, c))
a = 4
b = 4
c = 4
print(solution(a, b, c))

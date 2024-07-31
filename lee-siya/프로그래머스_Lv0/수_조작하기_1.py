# https://school.programmers.co.kr/learn/courses/30/lessons/181926

'''
정수 n 과 문자열 control 이 주어집니다. control 은 "w", "a", "s", "d" 의 4개의 문자로 이루어져 있으며,
control 의 앞에서 부터 순서대로 문자에 따라 n 의 값을 바꿉니다.

- "w" : n 이 1 커집니다.
- "s" : n 이 1 작아집니다.
- "d" : n 이 10 커집니다.
- "a" : n 이 10 작아집니다.

위 규칙에 따라 n 을 바꿨을 때 가장 마지막에 나오는 n 의 값을  return  하는 solution 함수를 완성해 주세요.
'''

def solution(n,control):
    
    # control 을 리스트화 시키고 순서대로 꺼내와 n 값에 적용해야 하기에 for 문 활용함
    for judge in list(control):
        
        # control 에서 꺼내온 judge 가 "w" 와 같다면 조건 실행 "s", "d", "a" 문제 조건에 따라 if 문 만들기
        if judge == "w":
            n += 1
        elif judge == "s":
            n -= 1
        elif judge == "d":
            n += 10
        elif judge == "a":
            n -= 10

    answer = n
    return answer


# 예시 값
n = 0
control = "wsdawsdassw"
print(solution(n,control))

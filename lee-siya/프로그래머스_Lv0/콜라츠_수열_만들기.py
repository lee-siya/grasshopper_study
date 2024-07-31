# https://school.programmers.co.kr/learn/courses/30/lessons/181919

'''
모든 자연수 x 에 대해서 현재 값이 x 이면 x 가 짝수일 때는 2로 나누고,
x 가 홀수일 때는 3 * x + 1 로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x 가 1 이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.
계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1 에 도달한다는 것이 알려져 있습니다.
임의의 1,000 보다 작거나 같은 양의 정수 n 이 주어질 때 초기값이 n 인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.
'''

def solution(n):
    result = [n]
    ''' 1 <= n <= 1000 에 속하는 n 값이 콜라츠 조건에 따라 1 이 될 때까지 반복하며
    거쳐간 모든 수를 기록해야 하기에 while 반복문 사용 '''
    while n > 1: # n 이 1이 되면 종료
        if n % 2 == 0:
            n //= 2
        elif n % 2 == 1:
            n = 3 * n + 1
        result.append(n)
    return result


# 예시 값
n = 10
print(solution(n))
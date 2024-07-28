'''정수가 담긴 리스트 num_list 가 주어질 때,
    모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을
    return 하도록 solution 함수를 완성해주세요.'''


def solution(num_list):
    
    # 모든 원소들의 곱을 구함
    multiply = 1
    for num in num_list:
        multiply *=num
        
    # 모든 원소들의 합의 제곱을 구함
    square = (sum(num_list))**2
    
    # 조건에 따라 if 문 만들기
    if multiply < square:
        answer = 1
    elif multiply > square:
        answer = 0
    return answer

# 예시 값
num_list = [3,4,5,2,1]
print(solution(num_list))
num_list = [5,7,8,3]
print(solution(num_list))
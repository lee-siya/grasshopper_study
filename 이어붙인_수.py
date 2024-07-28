'''정수가 담긴 리스트 num_list 가 주어집니다.
    num_list 의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을
    return 하도록 solution 함수를 완성해주세요.'''

def solution(num_list):
    # num_list 에서 홀수만 찾아내서 이어붙이기
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 == 1:
            odd += str(num)
    # num_list 에서 짝수만 찾아내서 이어붙이기
        else:
            even += str(num)
    # 숫자열로 변환하고 합 구하기
    answer = int(odd)+int(even)
    return answer




num_list = [3,4,5,2,1]
print(solution(num_list))
num_list = [5,7,8,3]
print(solution(num_list))
# https://school.programmers.co.kr/learn/courses/30/lessons/181921

'''
정수 l 과 r 이 주어졌을 때, l 이상 r 이하의 정수 중에서 숫자 "0" 과 "5" 로만 이루어진 모든 정수를
오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1 이 담긴 배열을 return 합니다.
'''

def solution(l, r):
    result = []
    for num in range(l,r+1): # 문제 조건 l <= num <= r
        
        
        # 숫자의 각 자릿수가 5 또는 0 인지 판단해야 하기에 먼저 자릿수를 분리하고 리스트로 만듦
        digit_list = []
        for digit in str(num):
            digit_list.append(digit)
        digit_list = list(map(int, digit_list))

        # 만들어진 리스트를 0과 5로만 이루어졌는지 파악하고 result 에 추가하기
        # i = index
        i = 0
        for _ in range(len(digit_list)):
            if i == len(digit_list)-1:
                if digit_list[i] == 5 or digit_list[i] == 0:
                    result.append(num)
            elif digit_list[i] != 5 and digit_list[i] != 0:
                break
            elif digit_list[i] == 5 or digit_list[i] == 0:
                i += 1
        
            # 여기서 문제 처음 자릿수가 5일 경우 result 에 추가를 해버림 그럼 어떻게 해야하나 *해결!
    
    answer = result
    if result == []:
        answer = [-1]
    return answer


# 예시 값
l = 5
r = 555
print(solution(l, r))

l = 10
r = 20
print(solution(l, r))
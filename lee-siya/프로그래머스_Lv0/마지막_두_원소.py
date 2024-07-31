# https://school.programmers.co.kr/learn/courses/30/lessons/181927

'''
정수 리스트 num_list 가 주어질 때,
마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여
return 하도록 solution 함수를 완성해주세요.
'''


def solution(num_list):

    # 마지막 원소
    last = num_list[-1]
    
    # 그전 원소
    last2 = num_list[-2]
    
    # 조건에 따라 if 문 만들기
    if last > last2:
        num_list.append(last - last2)
    elif last <= last2:
        num_list.append(last * 2)
        
    answer = num_list
    return answer




# 예시 값
num_list = [2,1,6]

print(solution(num_list))

num_list = [5,2,1,7,5]

print(solution(num_list))

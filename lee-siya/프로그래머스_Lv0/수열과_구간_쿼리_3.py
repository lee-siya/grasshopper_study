# https://school.programmers.co.kr/learn/courses/30/lessons/181924

'''
정수 배열 arr 와 2차원 정수 배열 queries 이 주어집니다.
queries 의 원소는 각각 하나의 query 를 나타내며, [i, j] 꼴입니다.

각 query 마다 순서대로 arr[i] 의 값과 arr[j] 의 값을 서로 바꿉니다.

위 규칙에 따라 queries 를 처리한 이후의 arr 를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(arr, queries):
    for i, j in queries:
        
        # 리스트에 속한 변수 위치를 swap 하는 법을 배움
        arr[i], arr[j] = arr[j], arr[i]
        
    answer = arr
    return answer




# 예시 값
arr = [0,1,2,3,4]
queries = [[0,3],[1,2],[1,4]]
print(solution(arr, queries))

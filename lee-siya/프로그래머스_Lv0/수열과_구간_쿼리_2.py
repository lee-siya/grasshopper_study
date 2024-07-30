# https://school.programmers.co.kr/learn/courses/30/lessons/181923

'''
정수 배열 arr 와 2차원 정수 배열 queries 이 주어집니다.
queries 의 원소는 각각 하나의 query 를 나타내며, [s, e, k] 꼴입니다.

각 query 마다 순서대로 s <= i <= e 인 모든  i 에 대해 k 보다 크면서 가장 작은 arr[i] 를 찾습니다.
각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1 을 저장합니다.
'''

def solution(arr,queries):
    
    result = [] 
    # s,e,k에 query 값을 넣어주고 숫자를 여러번 찾아서 result 를 얻어야 하기에 for 문을 사용함
    for s,e,k in queries:
        num_list = []
        # 문제 조건 s <= i <= e
        for i in range(s,e+1):
            
            # k 보다 큰 arr[i]  리스트 만들고 result 리스트에 최솟값 넣어주기
            if arr[i] > k:
                num_list.append(arr[i])
        
        # 단, 특정 쿼리의 답이 존재하지 않으면 -1 을 저장합니다. if 문으로 만들기
        if num_list == []:
            result.append(-1)
        else:
            result.append(min(num_list))
    answer = result
    return answer




# 예시 값
arr = [0,1,2,4,3]
queries = [[0,4,2],[0,3,2],[0,2,2]]
print(solution(arr, queries))

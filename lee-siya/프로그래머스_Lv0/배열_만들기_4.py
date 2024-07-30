# https://school.programmers.co.kr/learn/courses/30/lessons/181918

'''
정수 배열 arr 가 주어집니다. arr 를 이용해 새로운 배열 stk 를 만들려고 합니다.

변수 i 를 만들어 초기값을 0 으로 설정한 후 i 가 arr 의 길이보다 작으면 다음 작업을 반복합니다.

- 만약 stk 가 빈 배열이라면 arr[i] 를 stk 에 추가하고 i 에 1 을 더합니다.
- stk 에 원소가 있고, stk 의 마지막 원소가 arr[i] 보다 작으면 arr[i] 를 stk 의 뒤에 추가하고 i 에 1 을 더합니다.
- stk 에 원소가 있는데 stk 의 마지막 원소가 arr[i] 보다 크거나 같으면 stk 의 마지막 원소를 stk 에서 제거합니다.

위 작업을 마친 후 만들어진 stk 를 return 하는 solution 함수를 완성해 주세요.
'''


# 문제 조건에 따라서 while 반복문을 활용하여 작성함.
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] >= arr[i]:
            del stk[-1]
    return stk

# 예시 값
arr = [1,4,2,5,3]
print(solution(arr))
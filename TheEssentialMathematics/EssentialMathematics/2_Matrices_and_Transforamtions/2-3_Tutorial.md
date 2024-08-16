## Tutorial / 튜토리얼

### Multiple transformations / 다중 변환

하나의 행렬을 사용하여 다음과 같이 지오메트리를 변환합니다:
먼저 입력 지오메트리의 중심이 원점에 오도록 이동한 다음 z축을 중심으로 45도 회전한 다음 0.2씩 균일하게 배율을 조정하고 다시 원래 위치로 이동합니다.

*성능 노트:*

변환할 점이나 개체의 수가 많은 경우, 한 번에 하나의 행렬로 여러 번 변환하는 것보다 하나의 마스터 변환 행렬을 만든 다음(모든 행렬을 먼저 곱한 다음) 결과 마스터 행렬을 한 번 사용하여 모든 입력을 변환하는 것이 훨씬 더 효율적입니다.

**Input:**

1. 변환할 개체
2. 회전 각도(45도) 및 배율(0.2). <br>
![figure048](img\Figure_(048).png)

**Additional input:**

초기 이동에는 다음이 필요합니다:
+ 입력의 바운딩 박스 중심에서 원점까지의 벡터입니다. <br>
![figure049](img\Figure_(049).png)

**Solution:**

1. 이동, 회전, 크기 조정, 초기 이동의 역방향 등 모든 변환 행렬을 생성합니다.
2. 마지막 행렬에서 첫 번째 행렬을 곱하여 마스터 변환 행렬을 생성합니다.
3. 마스터 변환 행렬을 사용하여 입력을 변환합니다.

![figure050](img\Figure_(050).png)

위의 단계는 스크립팅을 사용하여 해결할 수도 있습니다.

**Using the Grasshopper VB component:** <br>
![figure051](img\Figure_(051).png)

**Using the Grasshopper C# component:** <br>
![figure052](img\Figure_(052).png)

**Using the Grasshopper Python component and the RhinoCommon SDK:** <br>
![figure053](img\Figure_(053).png)
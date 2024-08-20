## Tutorial / 튜토리얼

### Multiple transformations / 다중 변환

하나의 행렬을 사용하여 다음과 같이 지오메트리를 변환합니다:
먼저 입력 지오메트리의 중심이 원점에 오도록 이동한 다음 z축을 중심으로 45도 회전한 다음 0.2씩 균일하게 배율을 조정하고 다시 원래 위치로 이동합니다.

*성능 노트:*

변환할 점이나 개체의 수가 많은 경우, 한 번에 하나의 행렬로 여러 번 변환하는 것보다 하나의 마스터 변환 행렬을 만든 다음(모든 행렬을 먼저 곱한 다음) 결과 마스터 행렬을 한 번 사용하여 모든 입력을 변환하는 것이 훨씬 더 효율적입니다.

**Input:**

1. 변환할 개체
2. 회전 각도(45도) 및 배율(0.2). <br>
![Figure_(048)](https://github.com/user-attachments/assets/2ab62519-3f10-4029-892f-9781ee57fbbd)

**Additional input:**

초기 이동에는 다음이 필요합니다:
+ 입력의 바운딩 박스 중심에서 원점까지의 벡터입니다. <br>
![Figure_(049)](https://github.com/user-attachments/assets/5f3ba557-5ba6-4e9d-a69a-9baf8be6e8dd)

**Solution:**

1. 이동, 회전, 크기 조정, 초기 이동의 역방향 등 모든 변환 행렬을 생성합니다.
2. 마지막 행렬에서 첫 번째 행렬을 곱하여 마스터 변환 행렬을 생성합니다.
3. 마스터 변환 행렬을 사용하여 입력을 변환합니다.

![Figure_(050)](https://github.com/user-attachments/assets/e517e096-441d-4a98-83bc-ef75ac1caff3)

위의 단계는 스크립팅을 사용하여 해결할 수도 있습니다.

**Using the Grasshopper VB component:** <br>
![Figure_(051)](https://github.com/user-attachments/assets/76e174d8-fef9-4407-9286-51534362740b)

**Using the Grasshopper C# component:** <br>
![Figure_(052)](https://github.com/user-attachments/assets/702c17be-6b9a-4e02-884c-9910f5a9ad88)

**Using the Grasshopper Python component and the RhinoCommon SDK:** <br>
![Figure_(053)](https://github.com/user-attachments/assets/548e0090-0dd9-4c91-826f-fab6bc762bac)

## Tutorials

다음 튜토리얼에서는 이 장에서 배운 개념을 사용합니다. Rhinoceros 5와 Grasshopper 0.9를 사용합니다.

### Continuity between curves / 커브 간의 연속성

두 입력 커브 사이의 연속성을 조사합니다. 연속성은 커브가 첫 번째 커브의 끝과 두 번째 커 브 의 시작에서 만난다고 가정합니다.

![Figure_(075)](https://github.com/user-attachments/assets/68b75afd-889d-48e2-a838-ea6900b6643a)

**Input:** <br>
두 개의 입력 커브. <br>
**Parameters:** <br>
두 커브 사이의 연속성을 결정할 수 있도록 다음을 계산합니다:

![Figure_(076)](https://github.com/user-attachments/assets/c032e820-1940-4d15-9dc2-cc4b877a5885)

+ 첫 번째 커브의 끝점(P1)
+ 두 번째 커브의 시작점(P2)
+ 첫 번째 커브의 끝과 두 번째 커브의 시작 부분의 접선(T1 및 T2)입니다.
+ 첫 번째 커브의 끝과 두 번째 커브의 시작 부분의 곡률(C1 및 C2)입니다.

**Solution:**
1. 입력 곡선을 다시 매개변수화합니다. 이렇게 하면 커브의 시작이 t=0에서 평가되고 끝이 t=1에서 평가된다는 것을 알 수 있습니다.
2. 두 커브의 끝점과 시작점을 추출하고 일치하는지 확인합니다. 일치하면 두 커브는 최소 G0 연속입니다. <br>
![Figure_(077)](https://github.com/user-attachments/assets/7debe205-24bc-4c3d-85d6-886a0b98edec)
3. 탄젠트를 계산합니다.
4. 점 곱을 사용하여 탄젠트를 비교합니다. 벡터를 단위화해야 합니다. 커브가 평행하면 최소 G1의 연속성을 갖습니다. <br>
![Figure_(078)](https://github.com/user-attachments/assets/cf1a4cd5-dc7e-4001-af69-405502b45d57)
5. 곡률 벡터를 계산합니다.
6. 곡률 벡터를 비교하여 일치하면 두 곡선은 G2 연속입니다. <br>
![Figure_(079)](https://github.com/user-attachments/assets/0bb082f3-04e0-4965-8981-182627a7bb7d)
7. 세 가지 결과(G1, G2, G3)를 필터링하고 가장 높은 연속성을 선택하는 로직을 만듭니다. <br>
![Figure_(080)](https://github.com/user-attachments/assets/a09486d5-1bb9-44cd-b1f3-dcb30069fdcd)

<br>

### Using the Grasshopper VBScript component: <br>
![Figure_(081)](https://github.com/user-attachments/assets/7d6541f6-4975-4943-babb-50908348e9bd)

<br>

### Using the Grasshopper C# component: <br>
![Figure_(082)](https://github.com/user-attachments/assets/2aae6773-209a-4bde-84ab-9d960b52b80a)

<br>

### Using the Grasshopper Python component: <br>
![Figure_(083)](https://github.com/user-attachments/assets/48ea0261-961b-4f6b-964f-d0c01c1e15df)

<br>
<br>
<br>

### Surfaces with singularity / 특이점이 있는 표면

구와 원뿔에서 특이점을 추출합니다. <br>
**Input:** <br>
구와 원뿔이 하나씩 있습니다.

![Figure_(084)](https://github.com/user-attachments/assets/151c4d41-f168-4e4c-9c95-61ac0d038271)

**Parameters:** <br>
특이점은 유효하지 않거나 길이가 0인 해당 엣지가 있는 2-D 파라미터 공간 trims 을 분석하여 감지할 수 있습니다. 이러한 trims 은 특이점이어야 합니다.

**Solution:**
1. 입력의 모든 trims 을 탐색합니다.
2. 유효하지 않은 가장자리가 있는 trims 가 있는지 확인하고 단일 trim 로 플래그를 지정합니다.
3. 3D 공간에서 포인트 위치를 추출합니다.

<br>

### Using the Grasshopper VB component: <br>
![Figure_(085)](https://github.com/user-attachments/assets/514c4bcf-f412-43ea-afc8-3343afa536d9) <br>
![Figure_(086)](https://github.com/user-attachments/assets/fecfdd9f-ffa6-4b2e-97d1-d280f6ea08d3)

<br>

### Using the Grasshopper C# component: <br>
![Figure_(087)](https://github.com/user-attachments/assets/b6ed2fd3-236e-4f5b-98ca-7a094f154d49) <br>
![Figure_(088)](https://github.com/user-attachments/assets/e3661e67-50e9-4df6-95dd-1a00ef351c65)

<br>

### Using the Grasshopper Python component: <br>
![Figure_(089)](https://github.com/user-attachments/assets/6e42107e-7bbe-4c60-b672-b76313377b21)

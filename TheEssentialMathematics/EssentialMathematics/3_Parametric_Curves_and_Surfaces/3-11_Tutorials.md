## Tutorials

다음 튜토리얼에서는 이 장에서 배운 개념을 사용합니다. Rhinoceros 5와 Grasshopper 0.9를 사용합니다.

### Continuity between curves / 커브 간의 연속성

두 입력 커브 사이의 연속성을 조사합니다. 연속성은 커브가 첫 번째 커브의 끝과 두 번째 커 브 의 시작에서 만난다고 가정합니다.

![figure075](img\Figure_(075).png)

**Input:** <br>
두 개의 입력 커브. <br>
**Parameters:** <br>
두 커브 사이의 연속성을 결정할 수 있도록 다음을 계산합니다:

![figure076](img\Figure_(076).png)

+ 첫 번째 커브의 끝점(P1)
+ 두 번째 커브의 시작점(P2)
+ 첫 번째 커브의 끝과 두 번째 커브의 시작 부분의 접선(T1 및 T2)입니다.
+ 첫 번째 커브의 끝과 두 번째 커브의 시작 부분의 곡률(C1 및 C2)입니다.

**Solution:**
1. 입력 곡선을 다시 매개변수화합니다. 이렇게 하면 커브의 시작이 t=0에서 평가되고 끝이 t=1에서 평가된다는 것을 알 수 있습니다.
2. 두 커브의 끝점과 시작점을 추출하고 일치하는지 확인합니다. 일치하면 두 커브는 최소 G0 연속입니다. <br>
![figure077](img\Figure_(077).png)
3. 탄젠트를 계산합니다.
4. 점 곱을 사용하여 탄젠트를 비교합니다. 벡터를 단위화해야 합니다. 커브가 평행하면 최소 G1의 연속성을 갖습니다. <br>
![figure078](img\Figure_(078).png)
5. 곡률 벡터를 계산합니다.
6. 곡률 벡터를 비교하여 일치하면 두 곡선은 G2 연속입니다. <br>
![figure079](img\Figure_(079).png)
7. 세 가지 결과(G1, G2, G3)를 필터링하고 가장 높은 연속성을 선택하는 로직을 만듭니다. <br>
![figure080](img\Figure_(080).png)

<br>

### Using the Grasshopper VBScript component: <br>
![figure081](img\Figure_(081).png)

<br>

### Using the Grasshopper C# component: <br>
![figure082](img\Figure_(082).png)

<br>

### Using the Grasshopper Python component: <br>
![figure083](img\Figure_(083).png)

<br>
<br>
<br>

### Surfaces with singularity / 특이점이 있는 표면

구와 원뿔에서 특이점을 추출합니다. <br>
**Input:** <br>
구와 원뿔이 하나씩 있습니다.

![figure084](img\Figure_(084).png)

**Parameters:** <br>
특이점은 유효하지 않거나 길이가 0인 해당 엣지가 있는 2-D 파라미터 공간 trims 을 분석하여 감지할 수 있습니다. 이러한 trims 은 특이점이어야 합니다.

**Solution:**
1. 입력의 모든 trims 을 탐색합니다.
2. 유효하지 않은 가장자리가 있는 trims 가 있는지 확인하고 단일 trim 로 플래그를 지정합니다.
3. 3D 공간에서 포인트 위치를 추출합니다.

<br>

### Using the Grasshopper VB component: <br>
![figure085](img\Figure_(085).png) <br>
![figure086](img\Figure_(086).png)

<br>

### Using the Grasshopper C# component: <br>
![figure087](img\Figure_(087).png) <br>
![figure088](img\Figure_(088).png)

<br>

### Using the Grasshopper Python component: <br>
![figure089](img\Figure_(089).png)
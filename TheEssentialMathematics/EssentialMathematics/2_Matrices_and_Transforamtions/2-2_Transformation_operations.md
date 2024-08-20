## Transformation operations / 변환 작업

대부분의 변형은 지오메트리 부분 간의 평행 관계를 유지합니다. 예를 들어, 선형 점은 변환 후에도 선형 상태로 유지됩니다. 또한 한 평면의 점은 변환 후에도 동일 평면을 유지합니다. 이러한 유형의 변환을 아핀 변환이라고 합니다.

<br>

### Translation (move) transformation / 번역(이동) 변환

시작 위치에서 특정 벡터에 따라 점을 이동하는 것은 다음과 같이 계산할 수 있습니다:

P' = P + V

Suppose:

P(x, y, z) is a given point <br>
**v**<a, b, c> is a translation vector

Then:

**P'(x)** = **x + a**
**P'(y)** = **y + b**
P'(z) = z + c

포인트는 행렬 형식으로 표시되며, 마지막 행에 1이 삽입된 [4x1] 행렬(마지막 행에 1이 삽입됨)을 사용합니다. 예를 들어 점 P(x, y, z)는 다음과 같이 표현됩니다. 는 다음과 같습니다: <br>
![figure038](img\Figure_(038).png)

변환에 [3x3] 행렬 대신 [4x4] 행렬(균질 좌표계라고 함)을 사용하면 변환을 포함한 모든 변환을 나타낼 수 있습니다. 변환 행렬의 일반적인 형식은 다음과 같습니다:

![figure039](img\Figure_(039).png)

예를 들어, 점 P(2,3,1)를 벡터 v<2,2,2>로 이동하려면 새 점 위치는: <br>
P’ = P + **v** = (2+2, 3+2, 1+2) = (4, 5, 3)

행렬 형식을 사용하여 변환 행렬에 입력 포인트를 곱하면 다음과 같이 새 포인트 위치를 얻을 수 있습니다:

![figure040](img\Figure_(040).png)

마찬가지로 모든 지오메트리는 구성 점에 변환 행렬을 곱하여 변환됩니다. 예를 들어 8개의 모서리 점으로 정의된 상자가 있고 이를 x 방향으로 4단위, y 방향으로 5단위, z 방향으로 3단위 이동하려면 8개의 상자 모서리 점 각각에 다음 변환 행렬을 곱하여 새 상자를 얻어야 합니다. <br>
![figure19](img\Figure_(19).png) <br>
*Figure (19): Translate all box corner points.* <br>
*그림 (19): 모든 상자 모서리 점을 변환합니다.*

<br>
<br>
<br>

### Rotation transformation / 회전 변환

이 섹션에서는 삼각법을 사용하여 z축과 원점을 중심으로 회전을 계산한 다음 회전에 대
한 일반적인 행렬 형식을 추론하는 방법을 보여 줍니다. <br>
x,y 평면 P(x,y)의 한 점을 각도(b)만큼 회전시킵니다. <br>
그림에서 다음과 같이 말할 수 있습니다:

x = d cos(a) ---(1) <br>
y = d sin(a) ---(2) <br>
x' = d cos(b+a) ---(3) <br>
y' = d sin(b+a) --- (4)

각의 합의 사인과 코사인에 대한 삼각 신원을 사용하여 x'와 y'를 확장합니다:

x' = d cos(a)cos(b) - d sin(a)sin(b) ---(5) <br>
y' = d cos(a)sin(b) + d sin(a)cos(b) ---(6)

식 1과 2를 사용합니다:

x' = x cos(b) - y sin(b) <br>
y' = x sin(b) + y cos(b)

**Z축** 을 중심으로 한 회전 행렬은 다음과 같습니다: <br>
![figure041](img\Figure_(041).png)

각도 **b** 에 의한 **x축** 을 중심으로 한 회전 행렬은 다음과 같습니다: <br>
![figure042](img\Figure_(042).png)

각도 **b** 에 따른 **Y축** 을 중심으로 한 회전 행렬은 다음과 같습니다: <br>
![figure043](img\Figure_(043).png)

예를 들어 상자가 있고 이 상자를 30도 회전하려면 다음이 필요합니다:
1. 30도 회전 행렬을 구성합니다. 일반적인 형태와 30도 각도의 코사인 및 사인 값을 사용하면 회전 행렬은 다음과 같이 됩니다: <br>
![figure044](img\Figure_(044).png)

2. 회전 행렬에 입력 지오메트리를 곱하거나 상자의 경우 각 모서리 점을 곱하여 상자의 새 위치를 찾습니다. <br>
![figure20](img\Figure_(20).png) <br>
*Figure (20): Rotate geometry.* <br>
*그림 (20): 지오메트리 회전.*

<br>
<br>
<br>

### Scale transformation / 규모 변환

지오메트리의 크기를 조정하려면 배율과 축척 중심이 필요합니다. 배율은 x, y, z 방향으로 균일하게 배율을 조정하거나 각 차원에 대해 고유할 수 있습니다. 점의 배율은 다음 공식을 사용할 수 있습니다:

P' = ScaleFactor(S) * P

Or:

P'.x = S<sub>x</sub> * P.x <br>
P'.y = S<sub>y</sub> * P.y <br>
P'.z = S<sub>z</sub> * P.z

스케일 중심이 월드 원점(0,0,0)이라고 가정할 때 스케일 변환을 위한 행렬 형식입니다. <br>
![figure045](img\Figure_(045).png)

예를 들어 월드 원점을 기준으로 상자의 배율을 0.25로 조정하려는 경우 배율 매트릭스는 다음과 같이 표시됩니다:

![figure21](img\Figure_(21).png) <br>
*Figure (21): Scale geometry* <br>
*그림 (21): 스케일 지오메트리*

<br>
<br>
<br>

### Shear transformation / 전단 변형

3D에서의 전단은 세 번째 축을 기준으로 한 쌍의 축을 따라 측정됩니다. 예를 들어, z축을 따라 전단하면 해당 축을 따라 지오메트리가 변경되지 않지만 x와 y를 따라 변경됩니다. 다음은 전단 행렬의 몇 가지 예입니다:

1. Y 좌표는 고정된 상태로 X와 Z로 전단합니다: <br>
![figure046](img\Figure_(046).png)

2. X 좌표는 고정된 상태로 Y와 Z로 전단합니다: <br>
![figure047](img\Figure_(047).png)

3. Z 좌표는 고정된 상태로 X와 Y로 전단합니다: <br>
![figure22](img\Figure_(22).png) <br>
*Figure (22): Shear Matrices.* <br>
*그림 (22): 전단 행렬.*

<br>
<br>
<br>

### Mirror or reflection transformation / 거울 또는 반사 변환

미러 변환은 선 또는 평면에 걸쳐 물체가 반사되도록 만듭니다. 2D 개체는 선을 가로질러 미러링되고, 3D 개체는 평면을 가로질러 미러링됩니다. 거울 변환은 지오메트리 면의 법선 방향을 뒤집습니다.

![figure23](img\Figure_(23).png) <br>
*Figure (23): Mirror matrix across World xy-plane. Face directions are flipped.* <br>
*그림 (23): 월드 xy 평면의 미러 매트릭스. 면 방향이 반전됩니다.*


<br>
<br>
<br>

### Planar Projection transformation / 평면 투영 변환

직관적으로, 주어진 3D 점 P(x,y,z)의 월드 xy-평면 투영점은 z 값을 0으로 설정하면 P<sub>xy</sub> (x,y,0)와 같습니다. 마찬가지로, 점 P의 xz 평면 투영점은 P<sub>xz</sub> (x,0,z)입니다. yz-평면으로 투영할 경우 P<sub>xz</sub> = (0,y,z)가 됩니다. 이를 직교 투영이라고 합니다<sup>1</sup>. 

입력으로 커브를 가지고 평면 투영 변환을 적용하면 해당 평면에 투영된 커브를 얻을 수 있습니다. 다음은 행렬 형식을 사용하여 xy 평면에 투영된 커브의 예시입니다.

참고: NURBS 커브(다음 장에서 설명)는 제어점을 사용하여 커브를 정의합니다.
커브를 투영하는 것은 제어점을 투영하는 것과 같습니다.

![figure24](img\Figure_(24).png) <br>
*Figure (24): Projection matrices.* <br>
*그림 (24): 투영 행렬.*
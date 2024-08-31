## Parametric surfaces

### Surface parameters / Surface 매개 변수

파라메트릭 서페이스는 어떤 2차원 영역에서 두 개의 독립적인 파라미터(일반적으로 u, v 로 표시됨)의 함수입니다. 평면을 예로 들어 보겠습니다. 평면에 점 P가 있고 평면에 두 개의 평행하지 않은 벡터인 **a** 와 **b** 가 있다면, 평면의 파라메트릭 방정식을 다음과 같이 두 파라미터 *u* 와 *v* 의 관점에서 정의할 수 있습니다: <br>
P = P’ + *u* * **a** + *v* * **b**

여기서:<br>
P' 는 평면에서 알려진 점입니다. <br>
**a** 는 평면의 첫 번째 벡터입니다. <br>
**b** 는 평면의 첫 번째 벡터입니다. <br>
u 는 첫 번째 매개변수입니다. <br>
v 는 첫 번째 매개변수입니다. <br>

![Figure_(53)](https://github.com/user-attachments/assets/fcc1e982-9d9e-4a5d-b8dd-3871555c6950) <br>
*Figure (53): The parameter rectangle of a plane.* <br>
*그림 (53): 평면의 매개변수 직사각형.*

또 다른 예로 구를 들 수 있습니다. 원점을 중심으로 반지름 R이 있는 구의 데카르트 방정식( The Cartesian equation of sphere )은 다음과 같습니다. <br>
x² + y² + z² = R²

즉, 각 점마다 세 개의 변수( x, y, z )가 있으므로 두 개의 변수만 필요한 파라메트릭 표현에 사용하기에는 유용하지 않습니다. 그러나 구형 좌표계에서는 세 가지 값을 사용하여 각 점을 찾을 수 있습니다:

r: 점과 원점 사이의 반경 방향 거리 <br>
θ: xy 평면에서 x 축으로부터의 각도 <br>
ø: z축과 점으로부터의 각도

![Figure_(54)](https://github.com/user-attachments/assets/b462794f-0b83-410e-8474-baeab1931fc4) <br>
*Figure (54): Spherical coordinate system.* <br>
*그림 (54): 구형 좌표계.*

구형 좌표에서 데카르트 좌표로의 포인트 변환은 다음과 같이 구할 수 있습니다: <br>
x = ***r*** * sin(ø) * cos(θ) <br>
y = ***r*** * sin(ø) * sin(θ) <br>
z = ***r*** * cos (ø)

여기서: <br>
r은 원점으로부터의 거리 ≥ 0 <br>
θ는 0에서 2π까지 실행 중입니다. <br>
ø는 0에서 π까지 실행 중입니다.

구형 표면에서 r은 상수이므로 두 개의 변수만 남게 되므로 위의 방법을 사용하여 구형 표면의 파라메트릭 표현을 만들 수 있습니다: <br>
u = θ <br>
v = ø

그래서: <br>
x = **r** * sin(v) * cos(u) <br>
y = **r** * sin(v) * sin(u) <br>
z = **r** * cos(v)

여기서 (u, v)는 (2π, π) 영역 내에 있습니다.

![Figure_(55)](https://github.com/user-attachments/assets/3d7f3be1-58b6-4256-acc2-da26ec698678) <br>
*Figure (55): The parameter rectangle of a sphere.* <br>
*그림 (55): 구의 매개변수 직사각형.*

파라메트릭 서페이스는 일반적인 형태를 따릅니다: <br>
x = x( u, v ) <br>
y = y( u, v ) <br>
z = z( u, v )

여기서: <br>
u 와 v 는 표면 도메인(surface domain) 또는 영역(region) 내의 두 매개 변수입니다.

<br>
<br>
<br>

### Surface domain

서피스 도메인은 해당 서피스 에 서 3D 점으로 평가되는 ( u, v ) 파라미터의 범위로 정의됩니다. 각 차원(u 또는 v)의 도메인은 일반적으로 두 개의 실수(u_min ~ u_max)와 (v_min ~ v_max)로 설명됩니다.
서피스 도메인을 변경하는 것을 서피스 *reparameterizing* 라고 합니다.
도메인이 증가한다는 것은 도메인의 최소값이 서페이스의 최소점을 가리킨다는 의미입니다. 도메인은 일반적으로 증가하지만 항상 증가하는 것은 아닙니다.

![Figure_(56)](https://github.com/user-attachments/assets/e7070306-6f64-42ae-960d-01d961846d52) <br>
*Figure (56): NURBS surface in 3-D modeling space (left). The surface parameter rectangle with domain spanning from u0 to u1 in the first direction and v0 to v1 in the second direction
(right).* <br>
*그림 (56): 3D 모델링 공간의 NURBS 서피스(왼쪽). 도메인이 첫 번째 방향은 u0에서 u1까지, 두 번째 방향은 v0에서 v1까지인 서피스 파라미터 직사각형(오른쪽).*

<br>
<br>
<br>

### Surface evaluation

서페이스 도메인 내에 있는 파라미터에서 서페이스를 평가하면 서페이스에 있는 점이 생성됩니다. 도메인의 중간(midu, midv)이 반드시 3D 서페이스의 중간 점으로 평가되지 않을 수도 있다는 점에 유의하세요. 또한 서피스 도메인 외부에 있는 u값과 v값을 평가하면 유용한 결과를 얻지 못합니다.

![Figure_(57)](https://github.com/user-attachments/assets/38d312b4-ee34-45a5-a3bb-0f7e03327c63) <br>
*Figure (57): Surface evaluation.* <br>
*그림 (57): 표면 평가.*

<br>

### Tangent plane of a surface / 서페이스의 접선 평면

특정 지점에서 서페이스에 대한 접하는 평면은 해당 지점에서 서페이스에 닿는 평면입니다. 탄젠트 평면의 z 방향은 해당 지점에서 서페이스의 법선 방향을 나타냅니다.

![Figure_(58)](https://github.com/user-attachments/assets/c0f91e3f-4cfb-4447-98c3-059e5f2d2fe3) <br>
*Figure (58): Tangent and normal vectors to a surface.* <br>
*그림 (58): 서페이스에 대한 탄젠트 및 노멀 벡터.*

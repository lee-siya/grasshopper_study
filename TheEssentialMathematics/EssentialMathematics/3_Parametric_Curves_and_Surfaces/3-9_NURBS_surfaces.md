## NURBS surfaces

NURBS 서페이스는 두 방향으로 이동하는 NURBS 커브의 Grid 라고 생각할 수 있습니다. NURBS 서페이스의 모양은 여러 개의 제어점과 두 방향(u 방향 및 v 방향) 각각에서 해당 서페이스의 차수에 의해 정의됩니다. NURBS 서페이스는 자유형 서페이스를 저장하고 표현하는 데 효율적이며 높은 정확도로 저장하고 표현하는 데 효율적입니다. NURBS 서페이스의 수학적 방정식과 세부 사항은 이 텍스트의 범위를 벗어납니다. 여기서는 디자이너에게 가장 유용한 특성만 가장 유용한 특성에만 집중하겠습니다.

![Figure_(63)](https://github.com/user-attachments/assets/7c829356-2dfb-4261-ba9f-2bab02d56da9) <br>
*Figure (63): NURBS surface with red isocurves in the u-direction and green isocurves in the v-direction.* <br>
*그림 (63): 빨간색 아이소커브가 u 방향에 있고 녹색 아이소커브가 v 방향에 있는 NURBS 표면.*

![Figure_(64)](https://github.com/user-attachments/assets/2abc1fbf-3cb9-4933-9e43-54298899b49d) <br>
*Figure (64): The control structure of a NURBS surface.* <br>
*그림 (64): NURBS 서페이스의 제어 구조.*

![Figure_(65)](https://github.com/user-attachments/assets/2bb232c1-b1a9-4358-8899-32d9ef5ceedc) <br>
*Figure (65): The parameter rectangle of a NURBS surface.* <br>
*그림 (65): NURBS 서페이스의 파라미터 직사각형.*

2-D parameter 직사각형에서 동일한 간격으로 매개변수를 평가하는 것은 대부분의 경우 3D 공간에서 동일한 간격으로 변환되지 않습니다.

![Figure_(66)](https://github.com/user-attachments/assets/065e0b8d-d5cd-4240-9fe6-a56764e320f4) <br>
*Figure (66): Evaluating surfaces.* <br>
*그림 (66): 서페이스 평가하기.*

<br>
<br>
<br>

### Characteristics of NURBS surfaces

NURBS surfaces 특성은 한 가지 추가 파라미터가 있다는 점을 제외하면 NURBS curves 와 매우 유사합니다. NURBS surfaces 에는 다음 정보가 포함됩니다:

+ Dimension, typically 3
+ Degree in u and v directions: (sometimes use order which is degree + 1)
+ Control points (points)
+ Weights of control points (numbers)
+ Knots (numbers)

3D 모델러는 일반적으로 이를 위한 훌륭한 툴 세트를 제공하므로 NURBS 커브와 마찬가지로 NURBS 서페이스를 만드는 방법에 대해 자세히 알 필요는 없습니다. 서페이스(및 커브)는 언제든지 새로운 degree 와 제어점 수로 다시 만들 수 있습니다. 서페이스는 개방형(open), 폐쇄형(closed) 또는 주기적(periodic)일 수 있습니다. 다음은 서페이스의 몇 가지 예입니다:

![Figure_(069)](https://github.com/user-attachments/assets/8868d17d-a7ae-4390-8919-10edd1427fc1) <br>
u 방향과 v 방향 모두에서 degree-1 서피스입니다. 모든 제어점은 surface 에 있습니다.

<br>

![Figure_(070)](https://github.com/user-attachments/assets/c93d18c5-ef40-4db6-87f3-3ccffbeaf7c2) <br>
u 방향의 경우 degree-3, v 방향의 경우 degree-1 개방형 표면입니다. 표면 모서리는 모서리 컨트롤 포인트와 일치합니다.

<br>

![Figure_(071)](https://github.com/user-attachments/assets/bba0fa45-ad04-4763-be5f-22249ac6839f) <br>
u 방향은 degree-3, v 방향은 degree-1 닫힌(비주기적) 표면입니다. 일부 제어점은 표면 이음새와 일치합니다.

<br>

![Figure_(072)](https://github.com/user-attachments/assets/38def693-4893-4528-ab66-f43aca0b6fcb) <br>
닫힌 제어점의 이동. (비주기적) 표면은 꼬임이 발생하고 표면이 매끄럽지 않게 보입니다.

<br>

![Figure_(073)](https://github.com/user-attachments/assets/e0049412-7ae1-4928-8f79-61e754879b3a) <br>
U 방향은 degree-3, V 방향 주기적 표면은 degree-1 입니다. 서피스 제어점이 surface seam 과 일치하지 않습니다.

<br>

![Figure_(074)](https://github.com/user-attachments/assets/6cffff9a-d914-4409-a5f8-09f45ab46fd9) <br>
주기적 서페이스의 제어점을 이동해도 서페이스 평활도에 영향을 미치거나 꼬임이 발생하지 않습니다.

<br>
<br>
<br>

### Singularity in NURBS surfaces / NURBS 서페이스의 특이점

예를 들어 단순 평면의 선형 가장자리가 있고 가장자리의 두 끝 제어점을 가운데에서 겹치도록 끌면(접히도록 하면) 특이점을 얻을 수 있습니다. 서페이스 아이소커브가 특이점에서 수렴하는 것을 볼 수 있습니다.

![Figure_(67)](https://github.com/user-attachments/assets/3f015b68-2666-4afb-a52c-4e275d01c331) <br>
*Figure (67): Collapse two corner points of a rectangular NURBS surface to create a triangular surface with singularity. The parameter rectangle remains rectangular.* <br>
*그림 (67): 직사각형 NURBS 서페이스의 두 모서리 점을 축소하여 특이점이 있는 삼각형 서페이스를 만듭니다. 매개변수 직사각형은 직사각형으로 유지됩니다.*

위의 삼각형 모양은 특이점 없이 만들 수 있습니다. 삼각형 폴리라인으로 서페이스를 다듬을 수 있습니다. 기본 NURBS 구조를 살펴보면 직사각형 모양으로 남아 있음을 알 수 있습니다.

![Figure_(68)](https://github.com/user-attachments/assets/9d1e8dd0-63c2-40b1-a8fe-2b21b5569858) <br>
*Figure (68): Trim a rectangular NURBS surface to create a trimmed triangular surface.* <br>
*그림 (68): 직사각형 NURBS 서페이스를 트림하여 트림된 삼각형 서페이스를 만듭니다.*

특이점 없이 생성하기 어려운 서페이스의 다른 일반적인 예로는 원뿔과 구가 있습니다. 원뿔의 상단과 구의 상단과 하단 가장자리는 한 점으로 접혀 있습니다. 특이점이 있든 없든 매개변수 직사각형은 어느 정도 직사각형 영역을 유지합니다.

<br>
<br>
<br>

### Trimmed NURBS surfaces / 트림된 NURBS 서피스

NURBS 서페이스는 트림하거나 트림하지 않을 수 있습니다. 트림된 서페이스는 기본 NURBS 서페이스와 닫힌 커브를 사용하여 해당 서페이스의 일부를 트림합니다. 각 서페이스에는 외부 테두리(외부 루프)를 정의하는 닫힌 커브가 하나씩 있으며, 다음과 같은 특성을 가질 수 있습니다.

교차하지 않는 닫힌 내부 커브를 사용하여 구멍(내부 루프)을 정의합니다. 기본 NURBS 서페이스와 동일하고 구멍이 없는 외부 루프가 있는 서페이스를 트림되지 않은 서페이스라고 합니다.

![Figure_(69)](https://github.com/user-attachments/assets/93356344-3e1a-4ec8-ae0c-0bdb8fd1aea8) <br>
*Figure (69): Trimmed surface in modeling space (left) and in parameter rectangle (right).* <br>
*그림 (69): 모델링 공간(왼쪽)과 파라미터 직사각형(오른쪽)의 트림된 표면.*

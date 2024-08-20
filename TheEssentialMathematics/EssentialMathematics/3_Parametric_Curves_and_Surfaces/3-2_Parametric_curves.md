## Parametric curves / 파라메트릭 커브

### Curve parameter / 커브 파라미터

커브의 매개변수는 해당 커브의 한 점의 주소를 나타냅니다. 앞서 언급했듯이 파라메트릭 곡선은 일정 시간 동안 두 점 사이를 고정 또는 가변 속도로 이동하는 경로라고 생각할 수 있습니다. 이동하는 데 T 시간이 걸리는 경우 매개변수 t는 곡선의 한 위치(점)로 변환되는 T 내의 시간을 나타냅니다.

두 점 A 와 B 사이에 직선 경로(선분)가 있고 **v** 가 A 에서 B 까지의 벡터(**v** = B - A)라면 파라메트릭 선 방정식을 사용하여 다음과 같이 A 와 B 사이의 모든 점 M을 구할 수 있습니다:

M = A + *t* *(B-A) <br>
Where: <br>
*t* 는 0과 1 사이의 값입니다.

이 경우 *t* 값의 범위( 0~1 )를 커브 영역 또는 구간이라고 합니다. *t* 가 도메인을 벗어난 값( 0보다 작거나 1보다 큰 값 )인 경우 결과점 M 은 선형 커브 AB의 외부에 있습니다.

![Figure_(25)](https://github.com/user-attachments/assets/66daf3b6-9203-401e-ad21-dd632022a164) <br>
*Figure (25): Parametric line in 3-D space and parameter interval.* <br>
*그림 (25): 3D 공간의 매개변수 선 및 매개변수 간격.*

모든 파라메트릭 커브에도 동일한 원리가 적용됩니다. 곡선의 모든 점은 곡선의 한계를 정의하는 값의 구간 또는 도메인 내에서 매개변수 *t* 를 사용하여 계산할 수 있습니다. 도메인의 시작 매개변수는 일반적으로 t0, 도메인의 끝은 t1 이라고 합니다.

![Figure_(26)](https://github.com/user-attachments/assets/0615a9cf-2997-4bc7-8ce8-f11404440f4a) <br>
*Figure (26): Curve in 3-D space and its domain in parameter space.* <br>
*그림 (26): 3D 공간에서의 커브와 파라미터 공간에서의 도메인.*

<br>
<br>
<br>

### Curve domain or interval / 커브 도메인 또는 간격

커브 영역 또는 구간은 해당 커브 내의 한 점으로 평가되는 매개변수의 범위로 정의됩니다. 도메인은 일반적으로 (최소에서 최대) 또는 (최소, 최대) 형식으로 표현되는 도메인 한계를 정의하는 두 개의 실 수 로 설명됩니다. 도메인 한계는 커브의 실제 길이와 관련이 있을 수도 있고 없을 수도 있는 두 값일 수 있습니다. 증가하는 도메인에서 도메인 최소 매개변수는 커브의 시작점으로 평가되고 도메인 최대 매개변수는 커브 의 끝점으로 평가됩니다.

![Figure_(27)](https://github.com/user-attachments/assets/729785fa-d914-4def-a135-bfc24b7df3b5) <br>
*Figure (27): Curve domain or interval is a set of two numbers that is usually ascending. When possible, domain length is set to be close to the 3d curve length, but it can be set to any length without changing the 3d curve.* <br>
*그림 (27): 커브 도메인 또는 간격은 일반적으로 오름차순인 두 개의 숫자 집합입니다. 가능한 경우 도메인 길이는 3D 커브 길이에 가깝게 설정되지만, 3D 커브를 변경하지 않고 원하는 길이로 설정할 수 있습니다.*

커브 도메인을 변경하는 것을 커브의 매개변수를 다시 설정하는 과정이라고 합니다. 예를들어 도메인을 ( 0에서 1 )로 변경하는 것이 매우 일반적입니다.
커브를 다시 파라미터화해도 3D 커브의 모양에는 영향을 미치지 않습니다. 마치 경로의 모양을 바꾸지 않는 걷기 대신 달리기를 통해 경로의 이동 시간을 변경하는 것과 같습니다.

![Figure_(28)](https://github.com/user-attachments/assets/22a9cc2c-6e4e-4bec-9e0b-97268c407072) <br>
*Figure (28): Curve domain can be normalized (set to 0 to 1). Note that if the 3d curve length is much bigger than the domain length (by a factor of 10 or more), the evaluation of a parameter might not yield very accurate location on the 3d curve.* <br>
*그림 (28): 커브 도메인을 정규화할 수 있습니다(0~1로 설정). 3D 커브 길이가 도메인 길이보다 훨씬 큰 경우(10배 이상) 파라미터를 평가해도 3D 커브에서 매우 정확한 위치를 얻지 못할 수 있습니다.*

도메인이 증가한다는 것은 도메인의 최소값이 곡선의 시작을 가리키고 있음을 의미합니다. 도메인은 일반적으로 증가하지만 항상 증가하는 것은 아닙니다.

<br>
<br>
<br>

### Curve evaluation / 곡선 평가

커브 간격은 3D 커브 내의 점으로 평가되는 모든 파라미터 값의 범위라는 것을 배웠습니다. 그러나 예를 들어 도메인의 중간에서 평가한다고 해서 곡선의 중앙에 있는 점이 나온다는 보장은 없습니다.

곡선의 균일한 매개변수화는 일정한 속도로 경로를 이동하는 것으로 생각할 수 있습니다. 두 점 사이의 차수 1 선은 그림 (29)에서와 같이 동일한 간격 또는 매개변수가 선상의 동일한 호 길이 간격으로 변환되는 한 가지 예입니다. 파라메트릭 커브에서 파라미터의 동일한 간격이 3D 커브에서 동일한 간격으로 평가되는 경우는 드뭅니다.

![Figure_(29)](https://github.com/user-attachments/assets/c52c653c-5a41-4516-a5a7-6572c68fa17f) <br>
*Figure (29): A special case of a degree-1 line where equal parameter intervals, evaluate to equal curve lengths.* <br>
*그림 (29): 동일한 매개변수 간격이 동일한 커브 길이로 평가되는 차수 1 선의 특수한 경우입니다.*

경로를 따라 속도가 감소하거나 증가할 가능성이 더 높습니다. 예를 들어, 도로를 이동하는 데 30분이 걸리는 경우 15분째에 정확히 절반을 통과할 가능성은 거의 없습니다. 그림 (30)은 동일한 매개변수 간격이 3D 곡선에서 가변 길이로 평가되는 일반적인 경우를 보여줍니다.

![Figure_(30)](https://github.com/user-attachments/assets/cf85d47d-9c32-4a9a-b9c8-668ee491fa49) <br>
*Figure (30): Equal parameter intervals do not usually translate into equal distances on a parametric curves such as NURBS curves.* <br>
*그림 (30): 동일한 매개변수 간격은 일반적으로 NURBS 커브와 같은 파라메트릭 커브에서 동일한 거리로 변환되지 않습니다.*

3D 커브에서 커브 길이의 정의된 비율에 있는 점을 평가해야 할 수 있습니다. 예를 들어 커브를 동일한 길이로 나누어야 할 수 있습니다. 일반적으로 3D 모델러는 호 길이를 기준으로 커브를 평가하는 도구를 제공합니다.

<br>
<br>
<br>

### Tangent vector to a curve / 커브에 대한 탄젠트 벡터

임의의 매개변수(또는 커브의 한 점)에서 커브에 접하는 벡터는 해당 지점에서 커브에 닿지만 교차하지 않는 벡터입니다. 탄젠트 벡터의 기울기는 같은 지점에서 커브의 기울기와 같습니다. 다음 예는 서로 다른 두 매개변수에서 커브의 접선을 평가하는 예입니다.

![Figure_(31)](https://github.com/user-attachments/assets/91a6d417-5b32-429b-87fa-c934e311feaf) <br>
*Figure (31): Tangents to a curve.* <br>
*그림 (31): 커브에 대한 접선.*

<br>
<br>
<br>

### Cubic polynomial curves / 큐빅 다항식 커브

Hermite<sup>2</sup> 과 Bézier<sup>3</sup> 은 네 개의 파라미터에 의해 결정되는 입방 다항식 곡선의 두 가지 예입니다. Hermite curves 은 두 개의 끝점과 이 지점에서 두 개의 접선 벡터에 의해 결정되는 반면, 베지어 곡선은 네 개의 점으로 정의됩니다. 이 두 곡선은 수학적으로 다르지만 비슷한 특징과 한계를 공유합니다.

![Figure_(32)](https://github.com/user-attachments/assets/a5aac9fe-cb01-44b9-aa60-bbb24dfe1dba) <br>
*Figure (32): Cubic polynomial curves. The Bézier curve (left) is defined by four points. The Hermite curve (right) is defined by two points and two tangents.* <br>
*그림 (32): 3차 다항식 곡선. 베지어 곡선(왼쪽)은 4개의 점으로 정의됩니다. 에르미트 곡선(오른쪽)은 두 점과 두 접선으로 정의됩니다.*

대부분의 경우 커브는 여러 세그먼트로 만들어집니다. 이를 위해서는 piecewise cubic curve 라고 하는 것을 만들어야 합니다. 다음은 7개의 저장점을 사용하여 두 개의 세그먼트 큐빅 커브를 만드는 piecewise Bézier curve 의 그림입니다. 최종 커브가 합쳐지긴 했지만 부드럽거나 연속적으로 보이지 않습니다.

![Figure_(33)](https://github.com/user-attachments/assets/d762fe0f-c53b-467b-9934-0155179d7836) <br>
*Figure (33): Two Bezier spans share one point.* <br>
*그림 (33): 두 개의 베지어 스팬이 하나의 점을 공유합니다.*

Hermite curves 는 베지어 커브와 동일한 수의 파라미터를 사용하지만(하나의 커브를 정의하는 데 4개의 파라미터), 다음 조각과 공유할 수 있는 접선 커브의 추가 정보를 제공하여 총 저장 공간을 줄이면서 더 매끄럽게 보이는 커브를 만들 수 있습니다(아래 그림 참조).

![Figure_(34)](https://github.com/user-attachments/assets/f5138f00-86c9-4269-a24c-85d63a145f4e) <br>
*Figure (34): Two Hermite spans share one point and a tangent.* <br>
*그림 (34): 두 개의 허마이트 스팬은 하나의 점과 접선을 공유합니다.*

The non-uniform rational B-spline<sup>4</sup> (비균일 이성 B-스플라인) (NURBS)은 더욱 매끄럽고 연속적인 커브를 유지하는 강력한 커브 표현입니다. 세그먼트는 더 많은 제어점을 공유하여 더 적은 저장 공간으로 더욱 부드러운 커브를 구현합니다.

![Figure_(35)](https://github.com/user-attachments/assets/27851a45-3ba5-439f-9dfe-2f18bcfbf168) <br>
*Figure (35): Two degree-3 NURBS spans share three control points.* <br>
*그림 (35): 두 개의 3도 NURBS 스팬은 세 개의 제어점을 공유합니다.*

NURBS 커브와 서페이스는 지오메트리를 표현하기 위해 Rhino에서 사용하는 주요 수학적 표현입니다. 이 장의 뒷부분에서 NURBS 커브의 특성과 구성 요소에 대해 자세히 설명합니다.

<br>
<br>
<br>

### Evaluating cubic Bézier curves / 큐빅 베지어 곡선 평가하기

발명자인 폴 드 카스텔조(Paul de Casteljau)의 이름을 딴 드 카스텔조 알고리즘(5 )은 재귀적 방법을 사용하여 베지어 곡선을 평가합니다. 알고리즘 단계는 다음과 같이 요약할 수 있습니다:

**Input:** <br>
커브 도메인 내의 파라미터인 네 점 A, B, C, D는 커브 *t* 를 정의합니다. <br>
**Output:** <br>
커브의 파라미터 *t* 에 있는 점 R 입니다. <br>
**Solution:** <br>
1. AB 라인의 매개변수 *t* 에서 점 M 을 구합니다.
2. BC 라인의 매개변수 *t* 에서 점 N 을 구합니다.
3. CD 라인의 매개변수 *t* 에서 점 O 를 찾습니다.
4. MN 라인의 매개변수 *t* 에서 점 P 를 구합니다.
5. NO 라인의 매개변수 *t* 에서 점 Q 를 찾습니다.
6. PQ 라인의 매개변수 *t* 에서 점 R 을 찾습니다.

![Figure_(057)](https://github.com/user-attachments/assets/bfc628d1-5717-43b1-82e1-cb503885c347)

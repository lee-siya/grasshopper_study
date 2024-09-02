## NURBS curves

NURBS는 커브를 정확하게 수학적으로 표현한 것으로 매우 직관적으로 편집할 수 있습니다. NURBS를 사용하면 자유형 곡선을 쉽게 표현할 수 있으며 제어 구조를 통해 쉽고 예측 가능한 편집이 가능합니다.

![Figure_(36)](https://github.com/user-attachments/assets/11bf1077-a608-40ca-9e21-4310d2eced6f) <br>
*Figure (36): Non-uniform rational B-splines and their control structure.* <br>
*그림 (36): 균일하지 않은 합리적인 B-스플라인과 그 제어 구조.*

NURBS에 대해 자세히 알아보고 싶은 분들을 위해 많은 책과 참고 자료가 있습니다<sup>6</sup>.
하지만 NURBS 모델러를 보다 효과적으로 사용하려면 NURBS에 대한 기본적인 이해가 필요합니다. NURBS 커브를 정의하는 네 가지 주요 속성은 차수( degree ), 제어점( control points ), 매듭점( knots ) 및 평가 규칙(evaluation rules) 입니다.

### Degree

커브 차수는 전체 양수입니다. Rhino에서는 1부터 시작하는 모든 차수의 커브로 작업할 수 있습니다. 1, 2, 3, 5 차수가 가장 유용하지만, 4와 5 이상의 차수는 현실에서 많이 사용되지 않습니다. 다음은 커브와 그 차수의 몇 가지 예입니다:

![Figure_(058)](https://github.com/user-attachments/assets/62e2db49-0fe4-430f-baac-45cae6e5ff51)
+ 선( **Lines** )과 폴리라인( **polylines** )은 degree-1 NURBS 커브입니다.
+ 원과 타원은 degree-2 NURBS 커브의 예입니다.
+ 자유형 커브는 일반적으로 degree-3 또는 5 NURBS 커브로 표현됩니다.

<br>
<br>
<br>

### Control points / 제어 포인트

NURBS 커브의 제어점은 최소 ( degree+1 ) 점의 목록입니다. NURBS 커브의 모양을 변경하는 가장 직관적인 방법은 제어점을 이동하는 것입니다.
NURBS 커브의 각 스팬( span )에 영향을 주는 제어점의 수는 커브의 차수에 따라 정의됩니다. 예를 들어 degree-1 커브의 각 스팬은 두 개의 끝 제어점만 영향을 받습니다. degree-2 커브에서는 세 개의 제어점이 각 스팬에 영향을 줍니다.

![Figure_(059)](https://github.com/user-attachments/assets/17a77cf5-6fd3-4dae-ad5f-698613ac13b4) <br>
degree-1 커브의 제어점은 모든 커브 제어점을 통과합니다. degree-1 NURBS 커브에서는 두 개의 (degree+1) 제어점이 각 스팬을 정의합니다. 5개의 제어점을 사용하면 커브의 스팬은 4개가 됩니다.

![Figure_(060)](https://github.com/user-attachments/assets/3c5c0247-510c-46a4-bfbc-11a424edd2b1) <br>
원과 타원은 degree-2 커브의 예입니다. degree-2 NURBS 커브에서는 3개의 (차수+1) 제어점이 각 스팬을 정의합니다. 5개의 제어점 사용점으로 설정하면 커브는 세 개의 스팬을 갖습니다.

![Figure_(061)](https://github.com/user-attachments/assets/50c6e993-b471-4d50-98f1-35e0427c9d1a) <br>
degree-3 커브의 제어점은 일반적으로 열린 커브의 끝점을 제외하고는 커브에 닿지 않습니다. degree-3 NURBS 커브에서는 4개의 ( degree+1 ) 제어점이 각 스팬을 정의합니다. 5개의 제어점을 사용하는 커브에는 두 개의 스팬이 있습니다.

<br>
<br>
<br>

### Weights of control points / 컨트롤 포인트의 가중치

각 제어점에는 가중치라는 관련 숫자가 있습니다. 몇 가지 예외를 제외하고 가중치는 양수입니다. 모든 제어점의 가중치가 같은 경우, 보통 1이면 non-rational 곡선이라고 합니다. 직관적으로 가중치는 각 제어점이 가진 중력의 양으로 생각할 수 있습니다. 제어점의 상대적 가중치가 높을수록 커브는 해당 제어점을 향해 더 가깝게 당겨집니다.

커브 가중치를 변경하지 않는 것이 가장 좋습니다. 가중치를 변경하면 원하는 결과를 얻을 수 있는 경우는 드물고 교차점과 같은 연산에서 많은 계산 문제가 발생합니다. 합리적인 커브를 사용하는 유일한 좋은 이유는 원이나 타원과 같이 다른 방법으로는
그릴 수 없는 커브를 표현하기 위해서입니다.

![Figure_(37)](https://github.com/user-attachments/assets/07c477c9-c804-48e1-9b73-ac77c2f39881) <br>
*Figure (37): The effect of varying weights of control points on the result curve. <br>
The left curve is non-rational with uniform control point weights. <br>
The circle on the right is a rational curve with corner control points having weights less than 1.* <br>
*그림 (37): 다양한 제어점 가중치가 결과 곡선에 미치는 영향. <br>
왼쪽 곡선은 제어점 가중치가 균일한 비합리적 곡선입니다. <br>
오른쪽의 원은 가중치가 1보다 작은 모서리 제어점이 있는 합리적인 곡선입니다.*

<br>
<br>
<br>

### Knots / 매듭점

각 NURBS 커브에는 매듭점( knot vector 라고도 함 )이라는 연결된 숫자 목록이 있습니다. 매듭점은 이해하고 설정하기가 조금 더 어렵습니다. 3D 모델러를 사용하는 동안 생성하는 각 커브의 매듭점을 수동으로 설정할 필요는 없지만, 매듭점에 대해 알아두면 도움이 될 몇 가지 사항이 있습니다.

### Knots are parameter values / 매듭은 매개변수 값입니다

매듭점은 커브 영역 내에 있는 파라미터 값의 감소하지 않는 목록입니다. Rhino에서는 제어점보다 1차수 더 많은 매듭점이 있습니다. 즉, 매듭점의 수는 제어점의 수에 커브 차수를 더한 수에서 1을 뺀 수와 같습니다:

| knots | = | CVs | + Degree - 1

일반적으로 비주기 곡선의 경우 첫 번째 차수 다항은 도메인 최소값과 같고 마지막 차수 다항은 도메인 최대값과 같습니다. <br>
예를 들어, 제어점이 7개이고 도메인이 0에서 4 사이인 개방형 차수 3 NURBS 커브의 매듭점은 <0, 0, 0, 1, 2, 3, 4, 4, 4>와 같이 보일 수 있습니다.

![Figure_(38)](https://github.com/user-attachments/assets/95e990ae-d7a2-4798-a6b9-f1bc43dafb16) <br>
*Figure (38): There are degree-1 more knots than control points. If the number of control points=7, and curve degree=3, then number of knots is 9. Knots values are parameters that evaluate to points on the 3D curve.* <br>
*그림 (38): 제어점보다 차수 1 더 많은 매듭점이 있습니다. 제어점 수가 7이고 커브 차수가 3이면 매듭점 수는 9입니다. 매듭점 값은 3D 커브의 점으로 평가되는 매개변수입니다.*

매듭점 목록의 크기를 조정해도 3D 커브에는 영향을 미치지 않습니다. 위 예시에서 커브의 도메인( domain ) 을 "0~4"에서 "0~1"로 변경하면 매듭점 목록의 크기가 조정되지만 3D 커브는 변경되지 않습니다.

![Figure_(39)](https://github.com/user-attachments/assets/863f8d99-f736-42b3-a478-e0dabfe2e653) <br>
*Figure (39): Scaling the knot list does not change the 3D curve.* <br>
*그림 (39): 매듭 목록의 크기를 조정해도 3D 커브는 변경되지 않습니다.*

값이 한 번만 나타나는 매듭을 단순 매듭이라고 부릅니다. 내부 매듭은 일반적으로 위의 두 예에서와 같이 단순합니다.

<br>
<br>
<br>

### Knot multiplicity / 매듭점 다중성

매듭점의 다중성은 매듭점 목록에 나열된 매듭점의 횟수입니다. 매듭점의 배수는 커브의 차수보다 클 수 없습니다. 매듭점 배수는 해당 커브 포인트에서 연속성을 제어하는 데 사용됩니다.

### Fully-multiple knots

완전 다중 매듭점은 커브 차수와 같은 다중성을 갖습니다. 완전 다중 매듭점에는 해당 제어점이 있으며 커브는 이 점을 통과합니다.

예를 들어, clamped or open curves 에는 커브 끝에 최대 다중성을 가진 매듭점이 있습니다. 이것이 바로 끝 제어점이 커브 끝점과 일치하는 이유입니다. 내부에 완전 다중 매듭을 사용하면 해당 지점에서 커브가 꼬일 수 있습니다.

예를 들어, 다음 두 커브는 모두 degree-3이며 제어점의 수와 위치가 동일합니다. 하지만 매듭점이 다르고 모양도 다릅니다. 완전 다중성은 연결된 제어점을 통해 커브를 강제로 통과시킵니다.


![Figure_(40)](https://github.com/user-attachments/assets/7721ceae-33ef-4ebe-9c8f-f00fab97eeeb) <br>
*Figure (40) (A): Clamped curves have fully-multiple knots at their start and end that is equal to the curve degree (3 in this case). The rest of the knots are simple. (B): A fully multiple knot in the middle creates a kink and the curve is forced to go through the associated control point.* <br>
*그림 (40) (A): 클램핑된 커브는 시작과 끝에 커브 차수(이 경우 3)와 동일한 완전 다중 매듭점이 있습니다. 나머지 매듭점은 간단합니다. (B): 중간에 완전 다중 매듭점이 있으면 꼬임이 생기고 커브는 관련 제어점을 통과해야 합니다.*

<br>
<br>
<br>

### Uniform knots / 균일한 매듭점

열린 커브의 매듭점 목록은 다음 조건을 충족합니다: <br>
매듭점은 완전 다중 매듭점으로 시작하여 단순 매듭점으로 이어지며, 완전 다중 매듭점으로 끝납니다. 값이 증가하고 간격이 균등합니다. 이는 개방형(클램핑된 ) 커브의 전형적인 모습입니다. 주기적으로 닫힌 커브( Periodic closed curve )는 나중에 살펴볼 것처럼 다르게 작동합니다.

![Figure_(41)](https://github.com/user-attachments/assets/425a9756-e5b6-47c4-98b4-9110ba7472a5) <br>
*Figure (41) Uniform knot list means that spacing between knots is constant, with the exception of clamped curves where they can full multiplicity knot at start and end, and still be considered uniform. The left curve is periodic (closed without kink), and the right is clamped (open).* <br>
*그림 (41) 균일한 매듭점 목록은 시작과 끝에서 전체 다중 매듭점이 될 수 있는 클램프 커브를 제외하고 매듭점 사이의 간격이 일정하다는 의미이며, 여전히 균일하다고 간주됩니다. 왼쪽 커브는 주기적(꼬임 없이 닫힘)이고 오른쪽 커브는 클램핑된(열려 있음) 커브입니다.*

<br>
<br>
<br>

### Non uniform knots / 균일하지 않은 매듭

NURBS 커브는 매듭점 사이의 간격이 균일하지 않을 수 있습니다. 이렇게 하면 커브를 따라 곡률을 제어하여 보다 부드러운 커브를 만들 수 있습니다. 다음 예는 왼쪽의 비균일 매듭점 목록과 오른쪽의 균일 매듭점 목록을 사용하여 점을 보간하는 예제입니다. 일반적으로 NURBS 커브의 매듭점 간 격 이 제어점 사이의 간격에 비례하면 커브가 더 부드러워집니다.

![Figure_(42)](https://github.com/user-attachments/assets/02415c35-42c8-46dd-8b0a-a407d0e1d046) <br>
*Figure (42) Non-uniform knot list can help produce smoother curves. The curve on the left interpolate through points with non-uniform knots, and produces smoother curvature. The curve on the right interpolate through the same points but forces a uniform spacing of knots, resulting curve is not as smooth.* <br>
*그림 (42) 균일하지 않은 매듭점 목록은 더 부드러운 커브를 생성하는 데 도움이 됩니다. 왼쪽의 커브는 매듭점이 균일하지 않은 점을 보간하여 더 부드러운 곡률을 생성합니다. 오른쪽의 커브는 동일한 점을 보간하지만 매듭점 간격을 균일하게 하여 커브가 부드럽지 않습니다.*

균일하지 않으면서도 합리적인 커브의 예로 NURBS 원을 들 수 있습니다. 다음은 9개의 제어점과 10개의 노트가 있는 degree-2 커브입니다. 영역은 0-4이고 간격은 0과 1 사이를 번갈아 가며 나타납니다.

knots = <0,0,1,1,2,2,3,3,4,4> --- (full multiplicity in the interior knots) <br>
spacing between knots = [0,1,0,1,0,1,0,1,0] --- (non-uniform)

![Figure_(43)](https://github.com/user-attachments/assets/28cd05a4-56fc-4419-b34c-32aa416459c3) <br>
*Figure (43) A NURBS approximation of a circle is rational and non-uniform NURBS.* <br>
*그림 (43) 원의 NURBS 근사치는 합리적이고 균일하지 않은 NURBS입니다.*

<br>
<br>
<br>

### Evaluation rule / 평가 규칙

평가 규칙은 커브 영역 내에서 숫자를 취하고 포인트를 할당하는 수학 공식을 사용합니다. 이 공식은 차수, 제어점 및 매듭점을 고려합니다.

이 공식을 사용하면 특수 커브 함수는 커브 파라미터를 사용하여 해당 커브에서 해당 점을 생성할 수 있습니다. 매개변수는 커브 도메인 내에 있는 숫자입니다. 도메인은 일반적으로 증가하며 두 개의 숫자로 구성됩니다. 최소 도메인 파라미터(일반적으로 t0이라고 함)는 커브의 시작점에 대해 평가되고 최대 파라미터(t1)는 커브의 끝점에 대해 평가됩니다.

![Figure_(44)](https://github.com/user-attachments/assets/c7766ed6-bc03-4abe-afbf-89dac6234f4b) <br>
*Figure (44): Evaluate parameters (a, b, c, …) to points on 3D curve (A, B, C, …). Minimum and maximum parameters (t0 and t1) evaluate to the start and end points of the 3D curve.* <br>
*그림 (44): 매개변수(a, b, c, ...)를 3D 곡선(A, B, C, ...)의 점으로 평가합니다. 최소 및 최대 매개변수(t0 및 t1)는 3D 커브의 시작점과 끝점으로 평가합니다.*

<br>
<br>
<br>

### Characteristics of NURBS curves / NURBS 커브의 특성

NURBS 커브를 만들려면 다음 정보를 제공해야 합니다:
+ Dimension, 일반적으로 3
+ Degree, (때로는 degree+1과 같은 순서를 사용하기도 함)
+ Control points (list of points)
+ Weight of the control point (list of numbers)
+ Knots (list of numbers)

커브를 만들 때는 최소한 제어점의 차수와 위치를 정의해야 합니다. NURBS 커브를 구성하는 데 필요한 나머지 정보는 자동으로 생성할 수 있습니다. 시작점과 일치하는 끝점을 선택하면 일반적으로 주기적으로 부드러운 닫힌 커브가 생성됩니다. 다음 표는 열린 커브와 닫힌 커브의 예를 보여줍니다:

![Figure_(062)](https://github.com/user-attachments/assets/284e3200-99f0-4d4d-95e5-b251d19f2c47)

+ Degree-1 open curve <br>
커브는 모든 제어점을 통과합니다.
+ Degree-3 open curve <br>
두 커브 끝은 모두 끝 제어점과 일치합니다.
+ Degree-3 closed periodic curve <br>
커브 심은 제어점을 통과하지 않습니다.

![Figure_(063)](https://github.com/user-attachments/assets/bee4e0c4-a136-4706-9e97-011bddfa401d)

+ periodic curve 의 제어점을 이동해도 커브 부드러움에는 영향을 주지 않습니다.
+ 커브가 일부 제어점을 강제로 통과할 때 꼬임이 생깁니다.
+ non-periodic curve 의 제어점 이동은 커브의 매끄러운 연속성을 보장하지는 않지만 결과를 더 잘 제어할 수 있습니다.

<br>
<br>
<br>

### Clamped vs. periodic NURBS curves / 클램프형과 주기적 NURBS 커브 비교

닫힌 클램프 커브의 끝점은 끝 제어점과 일치합니다. periodic curve 는 부드러운 닫힌 커브입니다. 이 둘의 차이점을 이해하는 가장 좋은 방법은 제어점과 매듭점을 비교하는 것입니다.

다음은 개방형, 클램핑된 non-rational NURBS 커브의 예시입니다. 이 커브에는 4개의 제어점이 있고, 시작 매듭점과 끝 매듭점에 최대 다중성을 가진 균일한 매듭점이 있으며 모든 제어점의 가중치는 1입니다.

![Figure_(45)](https://github.com/user-attachments/assets/36089daf-9a09-4b82-a4d9-b3e8d065d5f5) <br>
*Figure (45): Analyze degree-3 open non-rational NURBS curve.* <br>
*그림 (45): degree-3 의 개방형 비차수 NURBS 커브 분석하기*

<br>

다음 원형 커브는 degree-3 의 닫힌 주기적 NURBS 커브의 예입니다. 모든 가중치가 동일하기 때문에 비합리적이기도 합니다. periodic curve 는 겹치는 제어점이 거의 없이 더 많은 제어점이 필요합니다. 또한 매듭점도 간단합니다.

![Figure_(46)](https://github.com/user-attachments/assets/2d75a270-5175-46e0-b57b-738bdab814bb) <br>
*Figure (46): Analyze degree-3 closed (periodic) NURBS curve.* <br>
*그림 (46): 차수 3 닫힘(주기적) NURBS 커브 분석하기*

<br>

주기 커브는 4개의 입력점을 7개의 제어점( degree+4 )으로 바꾼 반면, 클램프 커브는 4개의 제어점만 사용했음을 알 수 있습니다. 주기 커브의 매듭점은 단순 매듭점만 사용하는 반면, 클램프 커브의 시작 및 끝 매듭점은 커브가 시작 및 끝 제어점을 통과하도록 완전 다중성을 갖습니다.

이전 예제의 차수를 3이 아닌 2로 설정하면 매듭점이 작아지고 주기 곡선의 제어점 수가 변경됩니다.

![Figure_(47)](https://github.com/user-attachments/assets/c8eff84e-3837-4716-ad52-200bf4719c3c) <br>
*Figure (47): Analyze degree-2 open NURBS curve.* <br>
*그림 (47): 차수 2 개방형 NURBS 커브 분석하기.*

![Figure_(48)](https://github.com/user-attachments/assets/7d323136-ecd9-4986-8b8f-f73d2d9d8148) <br>
*Figure (48): Analyze degree-2 closed (periodic) NURBS curve.* <br>
*그림 (48): degree-2 닫힘(주기적) NURBS 커브 분석.*

<br>
<br>
<br>

### Weights / 가중치

균일한 NURBS 커브에서 제어점의 가중치는 1로 설정되지만, rational NURBS 커브에서는 이 숫자가 달라질 수 있습니다. 다음 예는 제어점의 가중치를 변경했을 때의 효과를 보여줍니다.

![Figure_(49)](https://github.com/user-attachments/assets/8575c71b-210b-46dc-8d94-48cda422e169) <br>
*Figure (49): Analyze weights in open NURBS curve.* <br>
*그림 (49): 열린 NURBS 커브에서 가중치 분석하기.*

![Figure_(50)](https://github.com/user-attachments/assets/d00672a6-bcc8-4fa5-bb86-d87dab103a95) <br>
*Figure (50): Analyze weights in closed NURBS curve.* <br>
*그림 (50): 닫힌 NURBS 커브의 가중치 분석.*

<br>
<br>
<br>

### Evaluating NURBS curves / NURBS 커브 평가

발명자인 칼 드 부어(Carl de Boor)의 이름을 딴 de Boor’s algorithm<sup>7</sup>은 Bézier curves에 대한 de Casteljau algorithm을 일반화한 것입니다. 수치적으로 안정적이며 3D 애플리케이션에서 NURBS 커브의 점을 평가하는 데 널리 사용됩니다. 다음은 드 부어 알고리즘을 사용하여 degree-3 NURBS 커브의 점을 평가하는 예제입니다.<sup>8</sup>

![Figure_(064)](https://github.com/user-attachments/assets/3cde4160-f55e-400b-84e3-317b52e7c102) <br>
**Input:** <br>
7개의 제어점 P<sub>0</sub> ~ P<sub>6</sub> 매듭: <br>
u0 = 0.0 <br>
u1 = 0.0 <br>
u2 = 0.0 <br>
u3= 0.25 <br>
u4 = 0.5 <br>
u5 = 0.75 <br>
u6 = 1.0 <br>
u7 = 1.0 <br>
u8 = 1.0 <br>

**Output:** <br>
u=0.4에 있는 커브의 점


**Solution:** <br>
![Figure_(065)](https://github.com/user-attachments/assets/1544c9db-6628-42d1-850d-ec494d6b6e27) ![Figure_(066)](https://github.com/user-attachments/assets/f137c5c4-dffc-498e-ab0e-88f2ce1781ea) ![Figure_(067)](https://github.com/user-attachments/assets/9ed2ba52-7680-49ae-a5ae-17a2f28bb1f8)

1. 첫 번째 반복에 대한 계수를 계산합니다: <br>
Ac = (u – u<sub>1</sub> ) / ( u<sub>1+3</sub> – u<sub>1</sub> ) = 0.8 <br>
Bc = (u – u<sub>2</sub> ) / ( u<sub>2+3</sub> – u<sub>2</sub> ) = 0.53 <br>
Cc = (u – u<sub>3</sub> ) / ( u<sub>3+3</sub> – u<sub>3</sub> ) = 0.2

2. 계수 데이터를 사용하여 포인트를 계산합니다: <br>
**A** = 0.2 **P<sub>1</sub>** + 0.8 **P<sub>2</sub> <br>**
**B** = 0.47 **P<sub>2</sub>** + 0.53 **P<sub>3</sub>** <br>
**C** = 0.8 **P<sub>3</sub>** + 0.2 **P<sub>4</sub>**

3. 두 번째 반복을 위한 계수를 계산합니다: <br>
Dc = (u – u<sub>2</sub> ) / (u<sub>2+3-1</sub> – u<sub>2</sub> ) = 0.8 <br>
Ec = (u – u<sub>3</sub> ) / (u<sub>3+3-1</sub> – u<sub>3</sub> ) = 0.3

4. 계수(coefficient) 데이터를 사용하여 포인트를 계산합니다: <br>
**D** = 0.2 **A** + 0.8 **B** <br>
**E** = 0.7 **B** + 0.3 **C**

5. 마지막 계수를 계산합니다: <br>
Fc = (u – u<sub>3</sub> )/ (u<sub>3+3-2</sub> – u<sub>3</sub> ) = 0.6 <br>
Find the point on curve at u=0.4 <br>
parameter: <br>
F= 0.4 **D** + 0.6 **E**


<sup>6</sup> [Michigan Tech, Department of Computer Science, De Boor's algorithm](https://pages.mtu.edu/%7Eshene/COURSES/cs3621/NOTES/spline/de-Boor.html)
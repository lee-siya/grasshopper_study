## Vector operations / 벡터 연산

### Vector scalar operation / 벡터 스칼라 연산

벡터 스칼라 연산에는 벡터에 숫자를 곱하는 작업이 포함됩니다. 예를 들어 <br>
**a** = <4, 3, 0> <br>
2\***a** = <2\*4, 2\*3, 2\*0> <br>
2\***a** = <8, 6, 0>

![figure7](img\Figure_(7).png) <br>
*Figure (7): Vector scalar operation* <br>
*그림 (7): 벡터 스칼라 연산*

일반적으로 벡터 **a** = <A1, A2, A3>와 실수 *t* <br> t\***a** = < t\*a1, t\*a2, t\*a3 >가 주어집니다.

<br>
<br>
<br>


### Vector addition / 벡터 추가

벡터 덧셈은 두 개의 벡터를 가져와서 세 번째 벡터를 생성합니다. 벡터의 구성 요소를 추가하는 방식으로 벡터를 더합니다. <br>
벡터는 구성 요소를 추가하여 추가합니다. <br>
예를 들어 두 개의 벡터가 있다고 가정해 보겠습니다:

**a**<1, 2, 0> <br>
**b**<4, 1, 3> <br>
**a**+**b** = <1+4, 2+1, 0+3> <br>
**a**+**b** = <5, 3, 3>

![figure8](img\Figure_(8).png) <br>
*Figure (8): Vector addition.* <br>
*그림 (8): 벡터 더하기.*

일반적으로 두 벡터 a와 b의 벡터 덧셈은 다음과 같이 계산됩니다:

**a** = <a1, a2, a3> <br>
**b** = <b1, b2, b3> <br>
**a** + **b** = <a1+b1, a2+b2, a3+b3>

벡터 덧셈은 두 개 이상의 벡터의 평균 방향을 찾는 데 유용합니다. 이 경우 일반적으로 길이가 같은 벡터를 사용합니다. 다음은 벡터 덧셈 결과에서 길이가 같은 벡터와 길이가 다른 벡터를 사용할 때의 차이를 보여주는 예시입니다:

![figure9](img\Figure_(9).png) <br>
*Figure (9): Adding various length vectors (left). Adding same length vectors (right) to get the average direction.* <br>
*그림 (9): 다양한 길이 벡터 추가하기(왼쪽). 동일한 길이의 벡터를 추가하여 평균 방향을 구하기(오른쪽).*

입력 벡터의 길이가 같지 않을 가능성이 높습니다. 평균 방향을 구하려면 입력 벡터의 단위 벡터를 사용해야 합니다. 앞서 언급했듯이 단위 벡터는 길이가 1과 같은 벡터입니다.

<br>
<br>
<br>

### Vector subtraction / 벡터 빼기

벡터 뺄셈은 두 개의 벡터를 취해 세 번째 벡터를 생성합니다. 두 벡터에서 해당 구성 요소를 빼는 방식으로 뺍니다. 예를 들어  벡터 a와 b가 두 개 있고 a에서 b를 뺀다면 다음과 같습니다:

**a** <1, 2, 0> <br>
**b** <4, 1, 4> <br>
**a** - **b** = <1-4, 2-1, 0-4> <br>
**a** - **b** = <-3, 1, -4> <br>

a에서 b를 빼면 다른 결과가 나옵니다:

**b** - **a** = <4-1, 1-2, 4-0> <br>
**b** - **a** = <3, -1, 4> <br>

벡터 **b** - **a**는 벡터 **a** - **b**와 길이가 같지만 반대 방향이라는 점에 유의하세요.

![figure10](img\Figure_(10).png) <br>
*Figure (10): Vector subtraction.* <br>
*그림 (10): 벡터 빼기.*

일반적으로 a와 b라는 두 개의 벡터가 있는 경우 a - b는 다음과 같이 계산되는 벡터입니다:

**a** = <a1, a2, a3> <br>
**b** = <b1, b2, b3> <br>
**a** - **b** = <a1 - b1, a2 - b2, a3 - b3>

벡터 뺄셈은 일반적으로 점 사이의 벡터를 찾는 데 사용됩니다. 따라서 위치 벡터 **b**의 끝점
에서 위치 벡터 **a**의 끝점까지 가는 벡터를 찾아야 하는 경우 그림 (11)과 같이 벡터 빼기(**a-b**)
를 사용합니다.

![figure11](img\Figure_(11).png) <br>
*Figure (11): Use vector subtraction to find a vector between two points.* <br>
*그림 (11): 벡터 뺄셈을 사용하여 두 점 사이의 벡터를 찾습니다.**

<br>
<br>
<br>

### Vector properties / 벡터 속성

벡터에는 8가지 속성이 있습니다. a, b, c가 벡터이고 s와 t가 숫자라면 다음과 같습니다:

**a + b = b + a** <br>
**a** + 0 = **a** <br>
*s* * ( **a** + **b** ) = *s* * **a** + *s* * **b** <br>
*s* * *t* * ( **a** ) = *s* * ( *t* * **a** ) <br>
**a** + ( **b** + **c** ) = ( **a** + **b** ) + **c** <br>
**a** + (- **a** ) = 0 <br>
( *s* + *t* ) * **a** = *s* * **a** + *t* * **a** <br>
1 * **a** = **a**

<br>
<br>
<br>

### Vector dot product / 벡터 닷 제품

도트 곱은 두 개의 벡터를 사용하여 숫자를 생성합니다. <br> 예를들어 두 개의 벡터 **a** 와 **b**가 있다고 가 정 해 보겠습니다:

**a** = <1, 2, 3>
**b** = <5, 6, 7>

그런 다음 도트 곱은 다음과 같이 구성 요소를 곱한 합계입니다:

**a** · **b** = 1 * 5 + 2 * 6 + 3 * 7 <br>
**a** · **b** = 38

일반적으로 두 개의 벡터 **a** 와 **b**가 주어집니다:

**a** = <a1, a2, a3> <br>
**b** = <b1, b2, b3> <br>
**a** · **b** = a1 * b1 + a2 * b2 + a3 * b3

두 벡터 사이의 도트 곱은 두 벡터가 같은 일반적인 방향을 향할 때 항상 양수를 얻습니다. <br>
두 벡터 사이의 점 곱이 음수이면 두 벡터가 일반적인 방향이 반대라는 뜻입니다.

![figure12](img\Figure_(12).png) <br>
*Figure (12): When the two vectors go in the same direction (left), the result is a positive dot product. <br>
When the two vectors go in the opposite direction (right), the result is a negative dot product.*
*그림 (12): 두 벡터가 같은 방향(왼쪽)으로 이동하면 결과는 양의 점 곱이 됩니다. 두 벡터가 반대 방향(오른쪽)으로 이동하면 결과는 음의 점 곱이 됩니다.*

두 단위 벡터의 도트 곱을 계산할 때 결과는 항상 1과 +1 사이입니다. 예를 들어

**a** = <1, 0, 0> <br>
**b** = <0.6, 0.8, 0> <br>
**a** · **b** = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6

또한 벡터와 벡터 자체의 도트 곱은 해당 벡터의 길이를 2의 제곱으로 나눈 값과 같습니다. 예를 들어

**a** = <0, 3, 4> <br>
**a** · **a** = 0 * 0 + 3 * 3 + 4 * 4 <br>
**a** · **a** = 25

벡터 a의 제곱 길이를 계산합니다:

| **a** | = √(4^2 + 3^2 + 0^2 ) <br>
| **a** | = 5 <br>
| **a** | 2 = 25

<br>
<br>
<br>

### Vector dot product, lengths, and angles / 벡터 도트 제품, 길이 및 각도

두 벡터의 도트 곱과 벡터 사이의 각도 사이에는 관계가 있습니다. <br>
0이 아닌 두 단위 벡터의 점 곱은 두 벡터 사이의 각도의 코사인과 같습니다.

일반적으로

**a** · **b** = | **a** | * | **b** | * cos( ө ), or <br>
**a** · **b** / (| **a** | * | **b** |) = cos( ө )

여기서:

ө는 벡터 사이에 포함된 각도입니다.

벡터 **a** 와 **b**가 단위 벡터라면 다음과 같이 간단히 말할 수 있습니다:

**a** · **b** = cos( ө )

그리고 90도 각도의 코사인은 0과 같으므로 다음과 같이 말할 수 있습니다: <br>
벡터 a와 b는 a - b = 0인 경우에만 직교합니다.

예를 들어, 두 직교 벡터인 월드 x축과 y축의 도트 곱을 계산하면 결과는 0이 됩니다.

**x** = <1, 0, 0> <br>
**y** = <0, 1, 0> <br>
**x** · **y** = (1 * 0) + (0 * 1) + (0 * 0) <br>
**x** · **y** = 0

도트 곱과 한 벡터의 다른 벡터로의 투영 길이 사이에도 관계가 있습니다. 예를 들어

**a** = <5, 2, 0> <br>
**b** = <9, 0, 0> <br>
unit( **b** ) = <1, 0, 0> <br>
**a** · unit( **b** ) = (5 * 1) + (2 * 0) + (0 * 0) <br>
**a** · unit( **b** ) = 2(**a** 를 **b** 에 투영한 길이와 같음)

![figure13](img\Figure_(13).png) <br>
*Figure (13): The dot product equals the projection length of one vector onto a non-zero unit vector.* <br>
*그림 (13): 도트 곱은 0이 아닌 단위 벡터에 대한 한 벡터의 투영 길이와 같습니다.*

일반적으로 벡터 **a** 와 0이 아닌 벡터 **b** 가 주어지면 도트 곱을 사용하여 벡터 **a** 의 벡터
**b** 에 대한 투영 길이 *pL*을 계산할 수 있습니다.

pL = | **a** | * cos( ө ) <br>
pL = **a** · unit( **b** )

<br>
<br>
<br>

### Dot product properties / 도트 제품 속성

**a**, **b**, **c**가 벡터이고 *s*는 숫자입니다:

**a** · **a** = | **a** | 2 <br>
**a** · ( **b** + **c** ) = **a** · **b** + **a** · **c** <br>
0 · **a** = 0 <br>
**a** · **b** = **b** · **a** <br>
( *s* * **a** ) · **b** = *s* * ( **a** · **b** ) = **a** · ( *s* * **b** )

<br>
<br>
<br>

### Vector cross product / 벡터 크로스 제품

교차 곱은 두 벡터를 취하여 두 벡터에 직교하는 세 번째 벡터를 생성합니다.

![figure14](img\Figure_(14).png) <br>
*Figure (14): Calculating the cross product of two vectors.* <br>
*그림 (14): 두 벡터의 교차 곱 계산하기.*

예를 들어, 두 개의 벡터가 월드 xy 평면에 놓여 있는 경우, 그 교차 곱은 양수 또는 음수 월드 z축 방향으로 가는 xy 평면에 수직인 벡터입니다. 예를 들어

**a** = <3, 1, 0>
**b** = <1, 2, 0>
**a** × **b** = < (1 * 0 – 0 * 2), ( 0 * 1 - 3 * 0), (3 * 2 - 1 * 1) >
**a** × **b** = <0, 0, 5>

벡터 *a x b* 는 *a* 와 *b* 모두에 직교합니다.

두 벡터의 교차 곱을 직접 계산할 필요는 없겠지만 어떻게 계산하는지 궁금하다면 계속 읽어보시고, 그렇지 않다면 이 섹션을 건너뛰셔도 됩니다. 교차 곱 **a** × **b**는 *결정자를* 사용하여 정의됩니다. 다음은 표준 기저 벡터를 사용하여 행렬식을 계산하는 방법에 대한 간단한 그림입니다:

**i**= <1, 0, 0> <br>
**j** = <0,1, 0> <br>
**k** = <0, 0, 1>

![figure0](img\Figure_(0).png) <br>

위의 다이어그램을 사용하여 두 벡터 **a**<a1, a2, a3>와 **b**<b1, b2, b3>의 교차 곱은 다음과 같이 계산할 수 있습니다:

**a** × **b** = **i** (a2 * b3) + **j** (a3 * b1) + **k** (a1 * b2) - **k** (a2 * b1) - **i** (a3 * b2) - **j** (a1 * b3) <br>
**a** × **b** = **i** (a2 * b3 - a3 * b2) + **j** (a3 * b1 - a1 * b3) + **k** (a1 * b2 - a2 * b1) <br>
**a** × **b** = < a2 * b3 – a3 * b2 , a3 * b1 - a1 * b3, a1 * b2 - a2 * b1 >

<br>
<br>
<br>

### Cross product and angle between vectors / 벡터 사이의 교차 곱과 각도

두 벡터 사이의 각도와 교차 곱 벡터의 길이 사이에는 관계가 있습니다. 각도가 작을수록(사인이 작을수록) 교차 곱 벡터의 길이가 짧아집니다. 벡터 교차 곱에서는 피연산자의 순서가 중요합니다. <br>
예를 들어:

**a** = <1, 0, 0> <br>
**b** = <0, 1, 0> <br>
**a** × **b** = <0, 0, 1> <br>
**b** × **a** = <0, 0, -1>

![figure15](img\Figure_(15).png) <br>
*Figure (15): The relationship between the sine of the angle between two vectors and the length of their cross product vector.*
*그림 (15): 두 벡터 사이의 각도의 사인과 교차 곱 벡터의 길이 사이의 관계.*

Rhino의 오른손잡이 시스템에서는 오른손잡이 규칙(**a** = 검지, **b** = 중지, **a** × **b** = 엄지)에 따라 **a** × **b** 의 방향이 정해집니다.

![figure01](img\Figure_(01).png)

일반적으로 3D 벡터 **a** 와 **b** 쌍의 경우:

| **a** × **b** | = | **a** | | **b** | sin( ө )

여기서: <br>
ө는 **a** 와 **b** 의 위치 벡터 사이에 포함된 각도입니다.

**a** 와 **b** 가 단위 벡터인 경우, 이들의 교차 곱의 길이는 두 벡터 사이의 각도의 사인과 같다고 간단히 말할 수 있습니다. 다시 말해:

| **a** × **b** | = sin( ө )

두 벡터 사이의 교차 곱은 두 벡터가 평행한지를 판단하는 데 도움이 됩니다. 결과는 항상 0 벡터가 되기 때문입니다.<br>
벡터 *a* 와 *b* 는 *a* x *b* = 0인 경우에만 평행합니다.

<br>
<br>
<br>

### Cross product properties / 교차 제품 속성

**a**, **b**, **c** 가 벡터이고 s가 숫자인 경우:
**a** × **b** = - **b** × **a** <br>
( s * **a** ) × **b** = s * ( **a** × **b** ) = **a** × ( s * **b** ) <br>
**a** × ( **b** + **c** ) = **a** × **b** + **a** × **c** <br>
( **a** + **b** ) × **c** = **a** × **c** + **b** × **c** <br>
**a** · ( **b** × **c** ) = ( **a** × **b** ) · **c** <br>
**a** × ( **b** × **c** ) = ( **a** · **c** ) * **b** – ( **a** · **b** ) * **c**
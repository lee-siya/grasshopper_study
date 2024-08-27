# Vector Mathematics / 벡터 수학


벡터는 방향과 길이를 갖는 속도나 힘과 같은 양을 나타냅니다. 3차원 좌표계의 벡터는 3개의 실수로 구성된 순서 집합으로 표현됩니다. 숫자와 모양은 다음과 같습니다.
**v** = <a1, a2, a3>

<br>
<br>
<br>

## Vector representation / 벡터 표현

이 문서에서는 굵은 글씨로 벡터를 표기합니다. 벡터 성분은 각 괄호 안에 함께 들어 있습니다. 대문자로 점을 표기합니다. 점 좌표는 항상 괄호로 둘러싸여 있습니다.

좌표계와 그 시스템의 임의의 앵커 포인트 집합을 사용하여, 우리는 선분 표현을 사용하여 이 벡터들을 나타내거나 시각화할 수 있습니다. 화살촉은 벡터의 방향을 보여줍니다.

예를 들어, 주어진 3차원 좌표계의 x축과 평행한 방향과 5단위의 길이를 갖는 벡터가 있다면, 다음과 같이 벡터를 쓸 수 있습니다.
**v** = <5, 0, 0>

그 벡터를 표현하기 위해서는 좌표계에 앵커 포인트가 필요합니다. 예를 들어, 다음 그림의 화살표들은 모두 다른 위치에 앵커 포인트가 있음에도 불구하고 같은 벡터를 동등하게 표현한 것입니다.

![Figure_(1)](https://github.com/user-attachments/assets/97493cc6-cc38-4abd-a0cc-3c5b1e5cfb76) <br>
*Figure (1): Vector representation in the 3-D coordinate system.* <br>
*그림 (1): 3차원 좌표계에서의 벡터 표현.*

3차원 벡터 ***v*** = <a1, a2, a3> 가 주어지면, 모든 벡터 성분 a1, a2, a3 는 실수입니다. 또한 점 A(x,y,z)에서 점 B(x+a1, y+a2, z+a3)까지의 모든 선분은 벡터 ***v***의 동등한 표현입니다.

그렇다면 주어진 벡터를 나타내는 선분의 끝점은 어떻게 정의합니까?

다음과 같이 앵커 포인트(A)를 정의합니다:
A = (1, 2, 3)
그리고 벡터:
**v** = <5, 6, 7>
벡터의 팁 포인트(B)는 앵커 포인트와 벡터 **v**에서 해당 성분을 더하여 계산됩니다:
B = A + **v**
B = (1+5, 2+6, 3+7)
B = (6, 8, 10)

![Figure_(2)](https://github.com/user-attachments/assets/2db131d8-cd6b-45f3-965f-17f60a396ccc) <br>
*Figure (2): The relationship between a vector, the vector anchor point, and the point coinciding with the vector tip location.* <br>
*그림 (2): 벡터, 벡터 앵커 포인트, 벡터 팁 위치와 일치하는 포인트 사이의 관계.*

<br>
<br>
<br>

### Position Vector / 위치 벡터

하나의 특수 벡터 표현은 원점(0,0,0)을 벡터 앵커 포인트로 사용합니다. 위치 벡터 **v** = <a1, a2, a3>는 원점과 B, 두 점 사이의 선분으로 표현되며, 따라서 다음과 같습니다:
원점 = (0,0,0)
B = (a1, a2, a3)

![Figure_(3)](https://github.com/user-attachments/assets/a2098212-4300-4df8-8238-2fdbb7f452be) <br>
*Figure (3): Position vector. The tip point coordinates equal the corresponding vector components.* <br>
*그림 (3): 위치 벡터. 끝점 좌표는 해당 벡터의 구성요소와 같습니다.*

주어진 벡터 **v** = < a1,a2,a3 >에 대한 위치 벡터는 원점(0, 0, 0)에서 점 (a1, a2, a3)까지의 특수 선분 표현입니다.

<br>
<br>
<br>

### Vector vs. point / 벡터 vs. 포인트

벡터와 포인트를 혼동하지 마세요. 벡터와 포인트는 매우 다른 개념입니다. 앞서 언급했듯이 벡터는 방향과 길이가 있는 양을 나타내는 반면, 점은 위치를 나타냅니다. 예를 들어 북쪽 방향은 벡터이고 북극은 위치(점)입니다.

다음과 같이 동일한 구성 요소를 가진 벡터와 점이 있는 경우:

    v = <3, 1, 0>
    P = (3, 1, 0)

다음과 같이 벡터와 점을 그릴 수 있습니다:

![Figure_(4)](https://github.com/user-attachments/assets/6a2c8a6a-25a5-4bce-982d-23d8c1feac13) <br>
*Figure (4): A vector defines a direction and length. A point defines a location.* <br>
*그림 (4): 벡터는 방향과 길이를 정의합니다. 점은 위치를 정의합니다.*

<br>
<br>
<br>

### Vector length / 벡터 길이

앞서 언급했듯이 벡터에는 길이가 있습니다. 예를 들어 주어진 벡터 a의 길이를 표기할 때는 |**a**|를 사용합니다: <br>
**a** = <4, 3, 0> <br>
|**a**| = √( 4² + 3² + 0² ) <br>
|**a**| = 5

일반적으로 벡터 a<a1,a2,a3>의 **길이**는 다음과 같이 계산됩니다: <br>
|**a**| = √(a1² + a2² + a3²)

![Figure_(5)](https://github.com/user-attachments/assets/1c5a4d5f-df9f-47e5-8d02-08851ed33724) <br>
*Figure (5): Vector length.* <br>
*그림 (5): 벡터 길이.*

<br>
<br>
<br>

### Unit vector / 단위 벡터

단위 벡터는 길이가 한 단위와 같은 벡터입니다. 단위 벡터는 일반적으로 벡터의 방향을 비교하는 데 사용됩니다. 단위 벡터는 길이가 1단위인 벡터입니다. 단위 벡터를 계산하려면 주어진 벡터의 길이를 구한 다음 벡터 성분을 길이로 나눠야 합
니다. 예를 들어:

**a** = < 4, 3, 0 > <br>
|**a**| = √( 4² + 3² + 0² ) <br>
|**a**| = 5 단위 길이 <br>
**b** = **a**의 단위 벡터인 경우: <br>
**b** = < 4/5, 3/5, 0/5 > <br>
**b** = < 0.8, 0.6, 0 > <br>
|**b**| = √( 0.8² + 0.6² + 0² ) <br>
|**b**| = √( 0.64 + 0.36 + 0 ) <br>
|**b**| = √( 1 ) = 1 단위 길이 <br>
일반적으로: <br>
**a** = <1, a2, a3> <br>
**a**의 단위 벡터 = < a1/|**a**|, a2/|**a**|, a3/|**a**| >입니다.

![Figure_(6)](https://github.com/user-attachments/assets/eae991c7-6737-4dcb-acaf-d4d3b04ed07d) <br>
*Figure (6): Unit vector equals one-unit length of the vector.* <br>
*그림 (6): 단위 벡터는 벡터의 한 단위 길이와 같습니다.*


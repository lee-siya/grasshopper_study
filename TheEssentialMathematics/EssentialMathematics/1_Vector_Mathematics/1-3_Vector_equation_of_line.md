## Vector equation of line / 선의 벡터 방정식

선의 벡터 방정식은 3D 모델링 애플리케이션과 컴퓨터 그래픽에 사용됩니다.

![Figure_(16)](https://github.com/user-attachments/assets/7249fb54-3fd3-4ca9-a958-ac8a68a151ef) <br>
*Figure (16): Vector equation of a line.* <br>
*그림 (16): 선의 벡터 방정식.*

예를 들어 선의 방향과 그 선의 한 점을 알고 있다면 다음과 같이 벡터를 사용하여 선의 임의의 다른 점을 찾을 수 있습니다:

L = 라인 <br>
**v** = < a, b, c > 선 방향 단위 벡터 <br>
Q = ( x0, y0, z0 ) 선 위치 점 <br>
P = ( x, y, z ) 선상의 임의의 점

우리는 알고 있습니다:

**a** = *t* * **v** --- (2) <br>
**p** = **q** + **a** --- (1)

1과 2에서: <br>
**p** = **q** + *t* * **v** --- (3)

그러나 (3)은 다음과 같이 쓸 수 있습니다:

< x, y, z > = < x0, y0, z0 > + < *t** a, *t* * b, *t* * c > <br>
< x, y, z > = < x0 + *t* * a, y0 + *t* * b, z0 + *t* * c >

따라서:

x = x0 + *t* * a <br>
y = y0 + *t* * b <br>
z = z0 + *t* * c

Which is the same as: <br>
P = Q + *t* * **v**

선상의 점 Q와 방향 v 가 주어지면 해당 선상의 모든 점 P는 선의 벡터 방정식 P = Q + t * v 를 사용하여 계산할 수 있습니다(여기서 t는 숫자입니다).

또 다른 일반적인 예는 두 점 사이의 중간점을 찾는 것입니다. 다음은 선의 벡터 방정식을 사용하여 중간점을 찾는 방법을 보여 줍니다:

**q** 는 점 Q의 위치 벡터 <br>
**p** 는 점 P의 위치 벡터 <br>
**a** 는 Q에서 P로 이동하는 벡터입니다.

벡터 빼기에서 우리는 알고 있습니다: <br>
**a** = **p** - **q**

선 방정식을 통해 알 수 있습니다: <br>
M = Q + *t* * **a**

And since we need to find midpoint, then: <br>
*t* = 0.5

따라서 다음과 같이 말할 수 있습니다: <br>
M = Q + 0.5 * **a**

![Figure_(17)](https://github.com/user-attachments/assets/d57f0f5b-7ccf-4e2d-8ecf-c89e82503aa9) <br>
*Figure (17): Find the midpoint between two input points.* <br>
*그림 (17): 두 입력점 사이의 중간점 찾기.*

일반적으로 일반 방정식을 사용하여 *t* 값을 0과 1 사이에서 변경하면 Q와 P 사이의 모든 지점을 찾을 수 있습니다: <br>
M = Q + *t* * (P - Q)

두 점 Q와 P가 주어지면 두 점 사이의 임의의 점 M은 M = Q + t * (P - Q) 방정식을 사용하여 계산되며, 여기서 t는 0과 1 사이의 숫자입니다.
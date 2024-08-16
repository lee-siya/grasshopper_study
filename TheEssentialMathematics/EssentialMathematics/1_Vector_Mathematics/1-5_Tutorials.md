## Tutorials / 튜토리얼

이 장에서 살펴본 모든 개념은 모델링할 때 발생하는 일반적인 기하학 문제를 해결하는 데 직접 적용됩니다. 다음은 이 장에서 배운 개념을 Rhinoceros와 Grasshopper(GH)를 사용하여 사용하는 단계별 자습서입니다.

<br>

### Face direction / 얼굴 방향

점과 서페이스가 주어졌을 때, 그 점이 서페이스의 앞면을 향하고 있는지 뒷면을 향하고 있는지 어떻게 확인할 수 있을까요?

**Input:** <br>
1. 표면
2. 포인트

![figure02](img\Figure_(02).png)

**Parameters 매개변수:**

면 방향은 표면 법선 방향으로 정의됩니다. 다음 정보가 필요합니다:

+ 입력 지점에 가장 가까운 표면 위치의 표면 법선 방향입니다.
+ 입력 지점에서 가장 가까운 지점까지의 벡터 방향입니다.

위의 두 방향을 비교하여 같은 방향이면 포인트가 앞쪽을 향하고, 그렇지 않으면 뒤쪽을 향합니다.

**Solution:**
1. Pull 컴포넌트를 사용하여 입력 지점을 기준으로 서페이스에서 가장 가까운 점 위치를 찾습니다. 이렇게 하면 가장 가까운 점의 자외선 위치를 알 수 있으며, 이 를 사용하여 서페이스를 평가하고 법선 방향을 찾을 수 있습니다.

![figure03](img\Figure_(03).png)

2. 이제 가장 가까운 점을 사용하여 입력 지점을 향하는 벡터를 그릴 수 있습니다. 그릴수도 있습니다:

![figure04](img\Figure_(04).png)

3. 도트 곱을 사용하여 두 벡터를 비교할 수 있습니다. 결과가 양수이면 점이 서페이스 앞에 있습니다. 결과가 음수이면 점이 서페이스 뒤에 있습니다.

![figure05](img\Figure_(05).png)

위의 단계는 다른 스크립팅 언어를 사용하여 해결할 수도 있습니다.

**Using Grasshopper VB component:** <br>
![figure06](img\Figure_(06).png) <br>
![figure07](img\Figure_(07).png)

**Using the Grasshopper C# component:** <br>
![figure08](img\Figure_(08).png)

**Using the Grasshopper Python component and the RhinoCommon SDK:** <br>
![figure09](img\Figure_(09).png)

**Using the Grasshopper Python component and the RhinoScriptSyntax Library:** <br>
![figure010](img\Figure_(010).png)

<br>
<br>
<br>

### Exploded box

다음 튜토리얼은 폴리서페이스를 분해하는 방법을 보여줍니다. 최종적으로 분해된 상자의 모습은 이렇습니다:

![figure011](img\Figure_(011).png)

**Input:** <br>
Identify the input, which is a box. We will use the **Box** parameter in GH:

![figure012](img\Figure_(012).png)

Parameters 매개변수:

이 튜토리얼을 풀기 위해 알아야 할 모든 매개변수를 생각해 보세요.

+ The center of explosion.
+ The box faces we are exploding.
+ The direction in which each face is moving.

![figure013](img\Figure_(013).png)

매개변수를 파악한 후에는 논리적 단계를 조합하여 해답에 도달할 수 있는 솔루션으로 통합하는 것이 중요합니다.

**Solution:**

1. GH의 **Box Properties** 구성 요소를 사용하여 상자의 중심을 찾습니다: <br>
![figure014](img\Figure_(014).png)

2. **Deconstruct Brep** 컴포넌트로 박스 면을 추출합니다: <br>
![figure015](img\Figure_(015).png)

3. 면을 움직이는 방향은 까다로운 부분입니다. 먼저 각 면의 중심을 찾은 다음 상자 중심에서 각 면의 중심을 향한 방향을 다음과 같이 정의해야 합니다: <br>
![figure016](img\Figure_(016).png)

4. 모든 파라미터를 스크립팅했으면 **Move** 컴포넌트를 사용하여 면을 적절한 방향으로 이동할 수 있습니다. 벡터를 원하는 진폭으로 설정하기만 하면 됩니다. <br>
![figure017](img\Figure_(017).png)

위의 단계는 VB 스크립트, C# 또는 Python을 사용하여 해결할 수도 있습니다. 다음은 이러한 스크립팅 언어를 사용한 솔루션입니다.

**Using the Grasshopper VB component:** <br>
![figure018](img\Figure_(018).png) <br>
![figure019](img\Figure_(019).png)

**Using the Grasshopper C# component:** <br>
![figure020](img\Figure_(020).png)

**Using the Grasshopper Python component:** <br>
![figure021](img\Figure_(021).png)

<br>
<br>
<br>

### Tangent spheres / 접하는 구체

이 튜토리얼에서는 두 입력점 사이에 두 개의 접하는 구를 만드는 방법을 보여드립니다. <br>
결과는 다음과 같습니다:

![figure022](img\Figure_(022).png)

**Input:** <br>
3D 좌표계에서 두 점(A와 B)입니다. <br>
![figure023](img\Figure_(023).png)

**Parameters / 매개변수:**

다음은 문제를 해결하기 위해 필요한 매개변수의 다이어그램입니다:
+ 두 구체 사이의 접점 D, 점 A와 점 B 사이의 일부 매개변수(0-1)에서의 접점입니다.
+ 첫 번째 구의 중심 또는 A와 D 사이의 중간점 C1입니다.
+ 두 번째 구의 중심 또는 D와 B 사이의 중간점 C2입니다.
+ 첫 번째 구의 반지름(r1) 또는 A와 C1 사이의 거리입니다.
+ 두 번째 구의 반지름(r2) 또는 D와 C2 사이의 거리입니다.

![figure024](img\Figure_(024).png)

**Solution:**
1. **Expression** 컴포넌트를 사용하여 어떤 매개변수 **t**에서 **A** 와 **B** 사이의 점 **D** 를 정의합니다. 여기서 사용할 표현식은 선의 벡터 방정식을 기반으로 합니다: **D** = **A** + t\*(**B**-**A**). <br>
B-A: 벡터 빼기 연산을 사용하여 B에서 A로 이동하는 벡터입니다. <br>
t*(B-A): 여기서 t는 0과 1 사이의 값으로 벡터의 위치를 구합니다. <br>
A+t*(B-A): A와 B 사이의 벡터에서 점을 구합니다. <br>
![figure025](img\Figure_(025).png)

2. **Expression** 컴포넌트를 사용하여 중간 지점 **C1** 과 **C2** 도 정의할 수 있습니다. <br>
![figure026](img\Figure_(026).png)

3. 첫 번째 구체 반경(**r1**)과 두 번째 구체 반경(**r2**)은 **Distance** 구성 요소를 사용하여 계산할 수 있습니다. <br>
![figure027](img\Figure_(027).png)

4. 마지막 단계는 기본 평면과 반지름으로 구를 만드는 것입니다. 원점이 **C1** 과 **C2** 에 연결되고 **r1** 과 **r2** 에서 반지름이 있는지 확인해야 합니다.  <br>
![figure028](img\Figure_(028).png)

**Using the Grasshopper VB component:** <br>
![figure029](img\Figure_(029).png)

**Using the Grasshopper C# component:** <br>
![figure030](img\Figure_(030).png) <br>
![figure031](img\Figure_(031).png)

**Using the Grasshopper Python component:** <br>
![figure032](img\Figure_(032).png)
## Tutorials / 튜토리얼

이 장에서 살펴본 모든 개념은 모델링할 때 발생하는 일반적인 기하학 문제를 해결하는 데 직접 적용됩니다. 다음은 이 장에서 배운 개념을 Rhinoceros와 Grasshopper(GH)를 사용하여 사용하는 단계별 자습서입니다.

<br>

### Face direction / 면 방향

점과 서페이스가 주어졌을 때, 그 점이 서페이스의 앞면을 향하고 있는지 뒷면을 향하고 있는지 어떻게 확인할 수 있을까요?

**Input:** <br>
1. 표면
2. 포인트

![Figure_(02)](https://github.com/user-attachments/assets/053903ee-7d91-4044-8a31-682e700bdeff)

**Parameters 매개변수:**

면 방향은 표면 법선 방향으로 정의됩니다. 다음 정보가 필요합니다:

+ 입력 지점에 가장 가까운 표면 위치의 표면 법선 방향입니다.
+ 입력 지점에서 가장 가까운 지점까지의 벡터 방향입니다.

위의 두 방향을 비교하여 같은 방향이면 포인트가 앞쪽을 향하고, 그렇지 않으면 뒤쪽을 향합니다.

**Solution:**
1. **Pull** 컴포넌트를 사용하여 입력 지점을 기준으로 서페이스에서 가장 가까운 점 위치를 찾습니다. 이렇게 하면 가장 가까운 점의 uv 위치를 알 수 있으며, 이를 사용하여 서페이스를 평가하고 법선 방향을 찾을 수 있습니다. <br>
![Figure_(03)](https://github.com/user-attachments/assets/421a40bb-cf30-47a8-bbce-710f917de537)

2. 이제 가장 가까운 점을 사용하여 입력 지점을 향하는 벡터를 그릴 수 있습니다: <br>
![Figure_(04)](https://github.com/user-attachments/assets/f408257e-4e4a-4907-854e-7a2c812c3c13)

3. 도트 곱을 사용하여 두 벡터를 비교할 수 있습니다. 결과가 양수이면 점이 서페이스 앞에 있습니다. 결과가 음수이면 점이 서페이스 뒤에 있습니다.

![Figure_(05)](https://github.com/user-attachments/assets/803272e8-6340-419e-95f8-5bc47072bdbc)

위의 단계는 다른 스크립팅 언어를 사용하여 해결할 수도 있습니다.

**Using Grasshopper VB component:** <br>
![Figure_(06)](https://github.com/user-attachments/assets/fa0f214f-9430-4273-a925-8bd411ccfa3a) <br>
![Figure_(07)](https://github.com/user-attachments/assets/075574fa-eb23-4f1a-90df-58d33a095438)

**Using the Grasshopper C# component:** <br>
![Figure_(08)](https://github.com/user-attachments/assets/a93e0c19-6d58-4737-8fca-8190c4d4fa50)

**Using the Grasshopper Python component and the RhinoCommon SDK:** <br>
![Figure_(09)](https://github.com/user-attachments/assets/0121abec-e51f-4bff-8d79-b89a01feb1b1)

**Using the Grasshopper Python component and the RhinoScriptSyntax Library:** <br>
![Figure_(010)](https://github.com/user-attachments/assets/47e67f94-da68-41b5-a689-a2288bc6f802)

<br>
<br>
<br>

### Exploded box

다음 튜토리얼은 폴리서페이스를 분해하는 방법을 보여줍니다. 최종적으로 분해된 상자의 모습은 이렇습니다:

![Figure_(011)](https://github.com/user-attachments/assets/d039cd34-6f48-4d0f-9034-2c130eebf2b8)

**Input:** <br>
Identify the input, which is a box. We will use the **Box** parameter in GH:

![Figure_(012)](https://github.com/user-attachments/assets/d7473c89-5d9e-4080-8889-999109e3216a)

Parameters 매개변수:

이 튜토리얼을 풀기 위해 알아야 할 모든 매개변수를 생각해 보세요.

+ The center of explosion.
+ The box faces we are exploding.
+ The direction in which each face is moving.

![Figure_(013)](https://github.com/user-attachments/assets/f04fad63-0bfa-4055-a33e-1923872ef750)

매개변수를 파악한 후에는 논리적 단계를 조합하여 해답에 도달할 수 있는 솔루션으로 통합하는 것이 중요합니다.

**Solution:**

1. GH의 **Box Properties** 구성 요소를 사용하여 상자의 중심을 찾습니다: <br>
![Figure_(014)](https://github.com/user-attachments/assets/acfd5797-4ef4-4827-90c0-62b60dd9c476)

2. **Deconstruct Brep** 컴포넌트로 박스 면을 추출합니다: <br>
![Figure_(015)](https://github.com/user-attachments/assets/17407a54-8fc0-48f8-8117-5c1618ab2712)

3. 면을 움직이는 방향은 까다로운 부분입니다. 먼저 각 면의 중심을 찾은 다음 상자 중심에서 각 면의 중심을 향한 방향을 다음과 같이 정의해야 합니다: <br>
![Figure_(016)](https://github.com/user-attachments/assets/f33f6311-9da1-4cf8-a807-148906262ee4)


4. 모든 파라미터를 스크립팅했으면 **Move** 컴포넌트를 사용하여 면을 적절한 방향으로 이동할 수 있습니다. 벡터를 원하는 진폭으로 설정하기만 하면 됩니다. <br>
![Figure_(017)](https://github.com/user-attachments/assets/d382a7fa-4ab5-499b-ab88-f28814981a76)

위의 단계는 VB 스크립트, C# 또는 Python을 사용하여 해결할 수도 있습니다. 다음은 이러한 스크립팅 언어를 사용한 솔루션입니다.

**Using the Grasshopper VB component:** <br>
![Figure_(018)](https://github.com/user-attachments/assets/02863615-8147-441d-91e1-13eef019c340) <br>
![Figure_(019)](https://github.com/user-attachments/assets/8eba0900-7c30-407f-956e-87a2a772af59)

**Using the Grasshopper C# component:** <br>
![Figure_(020)](https://github.com/user-attachments/assets/d08f99ab-ec89-4703-aa7b-26c5e1d1ec7f)

**Using the Grasshopper Python component:** <br>
![Figure_(021)](https://github.com/user-attachments/assets/6d18ee50-c250-4233-b552-2f8e1ca15dd6)

<br>
<br>
<br>

### Tangent spheres / 접하는 구체

이 튜토리얼에서는 두 입력점 사이에 두 개의 접하는 구를 만드는 방법을 보여드립니다. <br>
결과는 다음과 같습니다:

![Figure_(022)](https://github.com/user-attachments/assets/576c9a10-4439-4325-8dad-423d269b1452)

**Input:** <br>
3D 좌표계에서 두 점 ( A 와 B ) 입니다. <br>
![Figure_(023)](https://github.com/user-attachments/assets/fbb11317-0938-4f9b-9987-435b6cc7c173)

**Parameters / 매개변수:**

다음은 문제를 해결하기 위해 필요한 매개변수의 다이어그램입니다:
+ 두 구체 사이의 접점 D, 점 A와 점 B 사이의 일부 매개변수(0-1)에서의 접점입니다.
+ 첫 번째 구의 중심 또는 A와 D 사이의 중간점 C1입니다.
+ 두 번째 구의 중심 또는 D와 B 사이의 중간점 C2입니다.
+ 첫 번째 구의 반지름(r1) 또는 A와 C1 사이의 거리입니다.
+ 두 번째 구의 반지름(r2) 또는 D와 C2 사이의 거리입니다.

![Figure_(024)](https://github.com/user-attachments/assets/07b00860-5329-4b8e-acab-ce27e0fdcba0)

**Solution:**
1. **Expression** 컴포넌트를 사용하여 어떤 매개변수 *t* 에서 **A** 와 **B** 사이의 점 **D** 를 정의합니다. 여기서 사용할 표현식은 선의 벡터 방정식을 기반으로 합니다: <br>
 **D** = **A** + *t* \* ( **B** - **A** ). <br>
B - A : 벡터 빼기 연산을 사용하여 B 에서 A 로 이동하는 벡터입니다. <br>
*t* * ( B - A ) : 여기서 t는 0과 1 사이의 값으로 벡터의 위치를 구합니다. <br>
A + *t* * ( B - A ) : A와 B 사이의 벡터에서 점을 구합니다. <br>
![Figure_(025)](https://github.com/user-attachments/assets/532fc4a0-adca-416a-a2e8-d793d83ccac8)

2. **Expression** 컴포넌트를 사용하여 중간 지점 **C1** 과 **C2** 도 정의할 수 있습니다. <br>
![Figure_(026)](https://github.com/user-attachments/assets/568969a6-ed95-434a-ad18-b1b8fc2067c5)

3. 첫 번째 구체 반경(**r1**)과 두 번째 구체 반경(**r2**)은 **Distance** 구성 요소를 사용하여 계산할 수 있습니다. <br>
![Figure_(027)](https://github.com/user-attachments/assets/40d6678e-1b8f-49a2-b1fc-e5c2f9691867)

4. 마지막 단계는 기본 평면과 반지름으로 구를 만드는 것입니다. 원점이 **C1** 과 **C2** 에 연결되고 **r1** 과 **r2** 에서 반지름이 있는지 확인해야 합니다.  <br>
![Figure_(028)](https://github.com/user-attachments/assets/32a69269-1e1a-4eda-ac6e-f4fffa2814ec)

**Using the Grasshopper VB component:** <br>
![Figure_(029)](https://github.com/user-attachments/assets/01becf3b-6039-4be6-a423-99156696a7e4)

**Using the Grasshopper C# component:** <br>
![Figure_(030)](https://github.com/user-attachments/assets/b5c88327-4c58-469a-8f9d-fa4ab4b852a8) <br>
![Figure_(031)](https://github.com/user-attachments/assets/11423649-88fa-400d-b1bc-633d5f14527f)

**Using the Grasshopper Python component:** <br>
![Figure_(032)](https://github.com/user-attachments/assets/4924b06b-281d-4909-b508-15062dbcbb31)

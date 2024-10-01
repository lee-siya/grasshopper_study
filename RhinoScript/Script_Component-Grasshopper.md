# Script Component: Grasshopper

by Ehsan Iran-Nejad (Last updated: Thursday, August 15, 2024)

## Create Script Component

Grasshopper에서 통합 스크립트 편집기에 액세스하려면 수학(Maths) 탭과 스크립트(Script) 패널로 이동하여 캔버스에 스크립트 구성 요소를 끌어다 놓습니다:

![Figure_31](https://github.com/user-attachments/assets/313284dc-a589-4d26-8d42-8336a50ba187)

이 컴포넌트는 지원되는 모든 언어에서 작동하도록 설계되었습니다. 완전히 새롭고 내부적으로 기존 GHPython 및 C# 컴포넌트와는 다르지만, 기존 컴포넌트와 동일한 동작을 복제하고 가능한 한 친숙하게 유지하려고 노력합니다.

<br>

## First Script

캔버스에 스크립트 컴포넌트의 인스턴스를 배치하면 스크립트가 누락되었다는 경고가 표시됩니다. 먼저 컴포넌트를 초기화하기 위해 스크립트를 작성할 프로그래밍 언어를 선택해야 합니다:

Note : 컴포넌트를 두 번 클릭하면 가장 최근에 사용한 언어를 사용하여 새 스크립트를 빠르게 시작할 수 있습니다.

![Figure_32](https://github.com/user-attachments/assets/30fa128c-d5c1-4583-8516-26f43f0c50f2)

컴포넌트 하단의 첫 번째 버튼에는 이 컴포넌트의 기본 언어 또는 마지막으로 사용된 언어가 표시됩니다. 컴포넌트 자체를 두 번 클릭하면 자동으로 이 언어를 사용하여 컴포넌트를 초기화하고 새 스크립트를 시작합니다:

![Figure_33](https://github.com/user-attachments/assets/ba4d47f6-7837-4103-81dc-b3f69f291461)

지원되는 다른 언어는 [ ● ● ● ] 메뉴에서 선택할 수 있습니다:

![Figure_34](https://github.com/user-attachments/assets/f64c2a21-4edd-4902-90fa-83f9d5477f3d)

새 스크립트를 시작하려면 Python 3을 선택합니다:

![Figure_35](https://github.com/user-attachments/assets/23e4a35a-cce1-43bb-b7fe-9a3adf5ce6d8)

기본 스크립트는 다음과 같습니다:

    """Grasshopper Script"""
    a = "Hello Python 3 in Grasshopper!"
    print(a)

<br>

## Script Inputs and Outputs

스크립트 컴포넌트는 줌 가능한 사용자 인터페이스(*Zoomable User Interface* 줄여서 *ZUI*)를 지원합니다. 즉, 삽입 [ ⊕ ] 및 제거 [ ⊖ ] 컨트롤이 양쪽에 표시될 때까지 확대하여 컴포넌트의 입력 및 출력을 수정할 수 있습니다:

![Figure_36](https://github.com/user-attachments/assets/a0aa1d92-8993-4d5d-8a33-7b77e910d71d)

양쪽의 모든 매개변수가 제거되면 컴포넌트는 해당 쪽에 들쭉날쭉한 가장자리를 그립니다. 모든 스크립트에 입력이 필요하거나 다른 출력에 값을 생성하는 것은 아니므로 이는 완전히 괜찮습니다:

![Figure_37](https://github.com/user-attachments/assets/29586fd5-a8d0-4c7e-90e1-b238f601833a)

이 예제에서는 x 및 y 입력과 a를 출력으로 유지하겠습니다:

![Figure_38](https://github.com/user-attachments/assets/bcc9f65b-746c-45dc-b4f9-aabf1e075e4c)

<br>

## Edit Script

스크립트 내용을 제거하고 대신 새 줄을 입력해 보겠습니다. 편집기가 이름을 자동으로 완성해 줍니다:

    import Rhino
    a = Rhino.RhinoApp.Version
<br>

![Figure_39](https://github.com/user-attachments/assets/e27667a6-3f04-41d5-8735-aa9d4e0d8cea)

편집기를 닫고 예를 클릭하여 스크립트를 컴포넌트에 적용합니다:

![Figure_40](https://github.com/user-attachments/assets/b87cdef4-68e7-484f-8bc0-a2cd0b0dfaa6)

<br>

## Run Scripts

패널을 출력 a에 연결하고 Grasshopper 캔버스를 실행합니다. 스크립트가 현재 Rhino 버전을 출력합니다:

![Figure_41](https://github.com/user-attachments/assets/a581bf25-f911-4ff7-9973-c63608d998d4)

total이라는 다른 출력을 추가하고 스크립트에 몇 줄을 더 추가하여 주어진 입력의 합계를 계산해 보겠습니다:

    import Rhino
    a = Rhino.RhinoApp.Version

    total = x + y

편집기는 이러한 입력에 아직 값이 할당되지 않았기 때문에 x 및 y의 유형을 알지 못하므로 실행 오류를 표시합니다:

![Figure_42](https://github.com/user-attachments/assets/b38f7545-174a-4238-8f8a-2d469bec43fd)

각 입력을 마우스 오른쪽 버튼으로 클릭하고 유형 힌트 하위 메뉴에서 부동 소수점 옵션을 선택합니다. 이렇게 하면 입력이 선택한 유형에 대한 기본값으로 초기화됩니다:

![Figure_43](https://github.com/user-attachments/assets/3de9e299-15e5-4b10-88ed-8bb813f2dce4)

스크립트를 적용하고 Range 컴포넌트를 입력에 연결한 다음 총 출력 매개변수의 합계 목록을 확인합니다:

![Figure_44](https://github.com/user-attachments/assets/df956e8a-e82d-40ee-b6ea-0281bf6d9fec)

<br>

## Debugging Scripts

스크립트 에디터는 지원되는 모든 언어의 스크립트를 디버그할 수 있습니다. 디버그 중에 스크립트를 한 줄씩 실행하거나 중단점이라는 특정 줄에서 실행을 일시 중지하고 전역 및 로컬 변수의 값을 검사할 수 있습니다.

마우스 커서를 5번째 줄의 줄 번호 열 왼쪽으로 이동하고 클릭합니다. 그러면 빨간색 점이 추가되고 해당 줄이 중단점으로 표시됩니다:

![Figure_45](https://github.com/user-attachments/assets/1505f7eb-d6a4-424e-b1d0-9cde7910a9fb)

하단의 중단점 트레이에는 모든 활성 중단점이 표시되며, 모든 중단점 또는 개별 중단점을 지우거나 전환할 수 있는 버튼이 제공됩니다:

![Figure_46](https://github.com/user-attachments/assets/22da2efa-1482-46e5-acd0-07b84dda8f56)

중단점을 추가하면 에디터에서 몇 가지 UI가 변경되고 디버깅을 위한 몇 가지 유틸리티가 추가로 제공됩니다:
+ 실행 버튼이 디버그
+ Variables, Watch, and Call Stack 트레이가 하단 트레이 막대에 추가됩니다.

이제 대시보드에서 녹색 디버그 버튼을 클릭합니다. 편집기가 스크립트를 실행하고
+ 5줄의 중단점에서 중지
+ 중단점 선을 주황색으로 강조 표시하고 선의 왼쪽에 화살표를 표시합니다.
+ 상태 표시줄을 주황색으로 강조 표시하여 스크립트를 디버깅 중임을 표시합니다.
+ 대시보드에서 디버그 제어 버튼을 활성화합니다.
+ 하단의 변수 트레이를 열어 전역 및 로컬 변수를 표시합니다.

![Figure_47](https://github.com/user-attachments/assets/0eba4797-24ab-4ddb-9efa-6a3cb8dd692b)

대시보드의 디버그 제어 버튼을 사용하여 스크립트 실행을 제어할 수 있습니다:

![Figure_48](https://github.com/user-attachments/assets/2d9ead20-6441-492d-924e-b55a5110a966)

왼쪽부터 차례대로 설명합니다:
+ **Continue**: 다른 중단점에서 멈출 때까지 스크립트를 계속 실행합니다.
+ **Step Over**: 현재 줄을 실행하고 다음 줄로 이동합니다.
+ **Step In**: 현재 줄에 함수 호출이 포함되어 있으면 함수 코드를 정의하는 줄로 이동합니다.
+ **Step Out**:  이전에 함수 코드에 들어간 경우 함수에서 호출 코드로 제어가 반환될 때까지 함수 코드를 계속 실행하고 거기서 멈춥니다.
+ **Stop**: 스크립트 디버깅을 중지하고 나머지 실행을 계속하지 않습니다.

계속을 클릭하면 실행이 다음 줄로 이동합니다:

이제 변수 패널에 x 및 y에 대한 새 값이 표시됩니다. 패널 헤더의 오른쪽 상단에 스크립트 실행(11개 중 2개)이 표시되어 Grasshopper가 x 및 y 입력 쌍으로 이 컴포넌트를 두 번째로 실행한다는 것을 알 수 있습니다:

![Figure_49](https://github.com/user-attachments/assets/d9443626-c9c8-4a3c-9bad-506fb19a439e)

계속을 계속 클릭하면 스크립트가 계속 실행되고 변수가 수정됩니다. 각 중지 시 변수 트레이에 전역 및 로컬 변수의 현재 값이 표시됩니다.

이제 중지 버튼을 클릭하여 디버깅을 중지합니다. 스크립트 컴포넌트에 디버그 중지 메시지와 함께 오류 표시가 표시됩니다:

![Figure_50](https://github.com/user-attachments/assets/7ce35c79-f3d0-4b65-a44f-3e320b0d0913)

디버그가 중지되면 에디터 UI가 다시 정상으로 바뀌고 변수 트레이에 변수의 마지막 상태가 표시됩니다. 트레이에는 다른 디버깅 세션이 시작될 때까지 이러한 데이터가 보관됩니다.

언제든지 중단점 패널의 토글 버튼을 사용하여 중단점을 활성화 또는 비활성화할 수 있습니다. 비활성화된 중단점은 에디터에서 회색 점으로 표시됩니다:

![Figure_51](https://github.com/user-attachments/assets/8c38eba3-c57f-4b70-881d-cafafd45aa18)

<br>

## Using Packages

### Python Packages

스크립트 소스 내에서 스크립트에 필요한 패키지를 지정할 수 있습니다. 이렇게 하면 모든 요구 사항을 포함하는 독립된 스크립트가 생성됩니다.

+ 파이썬 3는 pip를 사용하여 PyPI.org의 패키지를 설치합니다.
    + pip는 더 이상 파이썬 2를 지원하지 않으므로 IronPython에서 사용되는 패키지로 제한됩니다.
+ C#은 NuGet을 사용하여 NuGet.org의 패키지를 설치합니다.

각 언어의 기본 스크립트에는 상단에 스크립트에서 요구 사항을 지정하는 방법을 설명하는 참고 섹션이 있습니다. Python 3 기본 스크립트를 살펴보면 이 구문을 사용하여 필요한 패키지를 지정할 수 있습니다:

    # r: numpy
or

    # requirements: numpy

새 Python 3 스크립트를 만들고 패키지로 numpy를 추가하여 스크립트에 사용해 보겠습니다:

    # requirements: numpy
    
    import numpy
    
    print(f"using numpy: {numpy.version.full_version}\n")
    
    a = numpy.random.rand(10)

실행을 클릭하면 스크립트 에디터가 스크립트를 실행하기 전에 필요한 패키지를 설치하려고 시도합니다. 이 과정은 다소 시간이 걸릴 수 있으며 편집기가 비활성화될 수 있습니다. 패키지가 설치되면 편집기는 스크립트를 계속 실행합니다:

![Figure_52](https://github.com/user-attachments/assets/970ad52f-fd70-423d-a46e-ef38a69eeaeb)

<br>

### Python Libraries (Modules)

파이썬 스크립트에 로컬 패키지를 추가하는 또 다른 방법은 sys.path에 해당 패키지의 경로를 추가하는 것입니다. 스크립트에서 # env: 지정자를 사용하여 스크립트를 실행하기 전에 sys.path에 경로를 자동으로 추가하면 이 단계를 간소화할 수 있습니다:

    # env: C:/Path/To/Where/My/Library/Is/Located/
    
    import mylibrary
    
    mylibrary.do_something()

<br>

## Editor Features

스크립트 에디터에는 다른 주목할 만한 기능도 있습니다. 여기에서는 자주 사용되는 몇 가지 기능을 소개합니다:

### Search

검색 탭을 클릭하여 검색 패널을 엽니다. 키워드를 검색하면 패널에 일치하는 모든 항목이 표시됩니다. 일치하는 항목을 클릭하면 해당 항목으로 이동할 수 있습니다:

![Figure_54](https://github.com/user-attachments/assets/17c72ef1-e1c7-4515-bad6-f2dfc358651f)

### Help

도움말 탭을 클릭하면 도움말 패널이 열립니다. 이 패널에서는 Rhino와 Grasshopper API 및 제공된 Python 모듈에 대한 간단한 도움말을 확인할 수 있습니다:

![Figure_55](https://github.com/user-attachments/assets/1bf2df7f-2d47-46a9-877b-47877a131588)

검색 필드를 사용하여 클래스 또는 메서드 이름을 검색합니다. 하단의 정보 패널에는 메서드 및 해당 매개변수에 대한 몇 가지 정보가 제공됩니다:

![Figure_56](https://github.com/user-attachments/assets/af6225d8-1845-4e7e-8eed-cee7b4e6f5ef)

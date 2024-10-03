# ScriptEditor Command / 스크립트 편집기 명령
by Ehsan Iran-Nejad (Last updated: Thursday, August 15, 2024)

<br>

## Opening Script Editor / 스크립트 편집기 열기

Rhino에서 통합 스크립트 편집기에 액세스하려면, 명령 프롬프트에 ScriptEditor를 입력하고 Enter 키를 선택하여 명령을 실행합니다:

![Figure_1](https://github.com/user-attachments/assets/b5efbfb3-eee7-4d0a-9b08-32374e76ee3b)

Rhino에서 스크립팅 기능을 처음 사용하는 경우, 편집기가 즉시 언어 초기화를 시작합니다. Python 3 (CPython) 환경을 설정하는 것이 가장 중요하며, 일반적으로 가장 오랜 시간이 걸리는 작업입니다. 편집기에 각 초기화 작업을 보여주는 진행률 표시줄이 표시됩니다. 이 시점에서는 모든 편집기 기능이 비활성화되므로 초기화 프로세스가 완료될 때까지 기다려야 합니다.

![Figure_2](https://github.com/user-attachments/assets/27261897-779e-4b95-b690-28771b477cd2)

초기화가 완료되면 편집기는 이전에 열려 있던 모든 스크립트(있는 경우)를 로드하고 버튼과 메뉴를 활성화합니다:

![Figure_3](https://github.com/user-attachments/assets/79354d8d-81c4-4f3d-befa-62345fcb758d)

<br>

## First Script

첫 번째 스크립트를 만들어 보겠습니다. 이 예제에서는 IronPython을 사용하겠습니다. 대시보드(편집기 창 상단에 있는 버튼 줄)에서 새로 만들기 버튼을 클릭하고 "Iron Python"을 선택하여 첫 번째 스크립트를 만듭니다:

![Figure_4](https://github.com/user-attachments/assets/8c3ecd59-1a98-41e0-8fa5-abdaef2682bf)

기본 스크립트에는 메모: 여러 줄 댓글(또는 문서 문자열) 아래에 많은 양의 정보가 포함되어 있습니다. 이 가이드의 뒷부분에서 이러한 고급 주제에 대해 설명할 예정이므로 지금은 건너뛰겠습니다. 이러한 주석을 제거해 보겠습니다.

![Figure_5](https://github.com/user-attachments/assets/6c8cc888-1366-493b-bc44-efd026ca639f)

대시보드에서 저장 버튼을 클릭하여 스크립트를 저장합니다:

![Figure_6](https://github.com/user-attachments/assets/15d14e70-e336-45e9-8304-2c935514810e)

<br>

## Edit Script
스크립트 하단에 새 줄을 입력해 보겠습니다. 편집기가 이름을 자동 완성해 줍니다:

![Figure_7](https://github.com/user-attachments/assets/9f7e3814-16f3-4f83-9d9f-abdbe617e3e9)


이 예제에서 스크립트 이름(FirstScript.py)을 표시하는 스크립트 탭에는 이제 스크립트가 수정되었지만 저장되지 않았음을 나타내는 어두운 원이 이름 옆에 표시됩니다.

![Figure_8](https://github.com/user-attachments/assets/d05a35e0-4e75-4a77-a2e5-96744ed770b0)

<br>

## Running Scripts

대시보드에서 녹색 실행 버튼을 클릭하거나 F5 키를 눌러 스크립트를 실행합니다. 스크립트에서 결과를 생성하는 유일한 줄은 인쇄 문(print statement)입니다. 그러면 터미널에서 사용 중인 Rhino 버전이 인쇄됩니다. 화면 하단의 터미널 탭을 클릭하여 터미널 트레이를 열고 인쇄된 결과를 확인합니다.

![Figure_9](https://github.com/user-attachments/assets/4431360d-a8f3-42be-8d9f-8c78f2145712)

터미널 트레이의 오른쪽 상단에는 터미널의 내용을 복사하고 지우는 일련의 버튼이 있습니다. 편집기의 대부분의 패널과 트레이는 동일한 디자인을 따르며, 가장 많이 사용하는 작업을 위한 버튼이 오른쪽 상단에 있습니다.

![Figure_10](https://github.com/user-attachments/assets/bf13f6e1-3458-4cc9-8e6b-f1174a2ea5f7)

<br>

## Debugging Scripts

스크립트 에디터는 지원되는 모든 언어의 스크립트를 디버그할 수 있습니다. 디버그 중에 스크립트를 한 줄씩 실행하거나 중단점(Breakpoints)이라는 특정 줄에서 실행을 일시 중지하고 전역 및 로컬 변수의 값을 검사할 수 있습니다.

스크립트에 이 라인을 추가해 보겠습니다:

    total = 0
    for i in range(5):
    total += i

마우스 커서를 12번째 줄의 줄 번호 열 왼쪽으로 이동하고 클릭합니다. 그러면 빨간색 점이 추가되고 해당 줄이 중단점으로 표시됩니다. 14번째 줄에 대해서도 같은 작업을 수행합니다:

![Figure_12](https://github.com/user-attachments/assets/ba995561-309b-406d-9082-79d576b98885)

하단의 중단점 트레이에는 모든 활성 중단점이 표시되며, 모든 중단점 또는 개별 중단점을 지우거나 전환할 수 있는 버튼이 제공됩니다:

![Figure_13](https://github.com/user-attachments/assets/542184eb-acce-444e-a1fc-3accc119c331)

중단점을 추가하면 에디터에서 몇 가지 UI가 변경되고 디버깅을 위한 몇 가지 유틸리티가 추가로 제공됩니다:
+ 실행 버튼이 디버그
+ 변수(Variables), 감시(Watch) 및 콜(Call) 스택 트레이가 하단 트레이 막대에 추가됩니다.

이제 대시보드에서 녹색 디버그 버튼을 클릭합니다. 편집기가 스크립트를 실행합니다:
+ 12줄의 첫 번째 중단점에서 중지
+ 중단점 선을 주황색으로 강조 표시하고 선의 왼쪽에 화살표를 표시합니다.
+ 상태 표시줄을 주황색으로 강조 표시하여 스크립트를 디버깅 중임을 표시합니다.
+ 대시보드에서 디버그 제어 버튼을 활성화합니다.
+ 하단의 변수 트레이를 열어 전역 및 로컬 변수를 표시합니다.

![Figure_14](https://github.com/user-attachments/assets/ba0c9864-3e64-4c22-ab97-7dbec1a65fb6)

대시보드의 디버그 제어 버튼을 사용하여 스크립트 실행을 제어할 수 있습니다:

![Figure_15](https://github.com/user-attachments/assets/ee4b1447-1012-4b67-897f-c4ac9cb5fd4e)

왼쪽부터 차례대로 설명합니다: <br>
+ **Continue**: 다른 중단점에서 멈출 때까지 스크립트를 계속 실행합니다.
+ **Step Over**:  현재 줄을 실행하고 다음 줄로 이동합니다.
+ **Step In**: 현재 줄에 함수 호출이 포함되어 있으면 함수 코드를 정의하는 줄로 이동합니다.
+ **Step Out**: 이전에 함수 코드에 들어간 경우 함수에서 호출 코드로 제어가 반환될 때까지 함수 코드를 계속 실행하고 거기서 멈춥니다.
+ **Stop**: 스크립트 디버깅을 중지하고 나머지 실행을 계속하지 않습니다.

다음 단계로 넘어가기를 클릭하면 실행이 다음 줄로 이동하는 것을 볼 수 있습니다:

![Figure_16](https://github.com/user-attachments/assets/a30a664d-a930-4b39-8c90-700f21a38ae7)

**Step Over** 를 한 번 더 클릭하면 스크립트가 14줄에서 중지됩니다. 이 시점에서 변수 트레이에 i 및 총 변수에 대한 현재 값(및 해당 데이터 타입)이 표시됩니다:

![Figure_17](https://github.com/user-attachments/assets/7e351ba3-61ae-4ffb-8deb-56031b1b1d1c)

**Step Over** 를 계속 클릭하면 스크립트가 계속 실행되고 변수가 수정됩니다. 각 단계에서 변수 트레이는 변수 이름 왼쪽에 빨간색 점으로 수정된 값을 강조 표시합니다:

![Figure_18](https://github.com/user-attachments/assets/b9ae8928-bc53-400c-9bfc-12ffb2fdbb2a)

스크립트가 종료되면 편집기 UI가 다시 정상으로 바뀌고 변수 트레이에 변수의 마지막 상태가 표시됩니다. 스크립트가 닫히거나 다른 디버깅 세션이 시작될 때까지 트레이에 이러한 데이터가 보관됩니다:

![Figure_19](https://github.com/user-attachments/assets/00164856-3d31-47d0-9c4b-2b4c0a5675ed)

언제든지 중단점 패널의 토글 버튼을 사용하여 중단점을 활성화 또는 비활성화할 수 있습니다. 비활성화된 중단점은 편집기에서 회색 점으로 표시됩니다:

![Figure_20](https://github.com/user-attachments/assets/9edf930c-2b7e-4d4f-b5a2-efd88292b522)

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

    for i in numpy.random.rand(10):
        print(i)

<br>

![Figure_21](https://github.com/user-attachments/assets/4f51c4db-46c9-47bb-9e30-a0f046288ae6)

실행을 클릭하면 스크립트 에디터가 스크립트를 실행하기 전에 필요한 패키지를 설치하려고 시도합니다. 이 과정은 다소 시간이 걸릴 수 있으며 편집기가 비활성화될 수 있습니다. 패키지가 설치되면 편집기는 스크립트를 계속 실행합니다:

![Figure_22](https://github.com/user-attachments/assets/385bad2b-21e1-4f87-9c40-6b57afe7164d)

<br>

### Python Libraries (Modules)

파이썬 스크립트에 로컬 패키지를 추가하는 또 다른 방법은 sys.path에 해당 패키지의 경로를 추가하는 것입니다. 스크립트에서 # env: 지정자를 사용하여 스크립트를 실행하기 전에 sys.path에 경로를 자동으로 추가하면 이 단계를 간소화할 수 있습니다:

    # env: C:/Path/To/Where/My/Library/Is/Located/

    import mylibrary

    mylibrary.do_something()

<br>

### Nuget Packages

C# 스크립트에도 동일한 규칙이 적용됩니다. 다른 구문을 사용하여 사용하려는 패키지에 대해 NuGet.org 페이지에 제공된 형식과 일치하는 패키지를 지정합니다:

![Figure_23](https://github.com/user-attachments/assets/040dfb23-006f-4af0-a538-a43b28eccf50)

다음은 웹사이트의 일부 데이터를 가져오기 위해 RestSharp NuGet 패키지를 사용하는 스크립트 예시입니다. 스크립트의 첫 번째 줄은 RestSharp 패키지 버전 110.2.0을 지정합니다.

    #r "nuget: RestSharp, 110.2.0"
 
    using System;
    using System.Collections.Generic;
    using Rhino;
 
    using RestSharp;
    using RestSharp.Authenticators;
 
    var client = new RestClient("https://httpbin.org");
    var request = new RestRequest("get");
    var response = client.Get(request);
 
    Console.WriteLine(response.Content);
<br>

![Figure_24](https://github.com/user-attachments/assets/cc0c6adb-477d-4944-adb0-da72c1fd6ec9)

<br>

## Editor Features

스크립트 에디터에는 다른 주목할 만한 기능도 있습니다. 여기에서는 자주 사용되는 몇 가지 기능을 소개합니다:

### Explorer

편집기 창 왼쪽에 있는 탐색기 패널을 사용하여 로컬 스크립트를 찾아보고 편집합니다. 탐색기 탭을 클릭하여 패널을 열고 패널 오른쪽 상단에 있는 폴더 아이콘을 클릭하여 폴더로 이동합니다:

![Figure_25](https://github.com/user-attachments/assets/40fcdc81-226d-4570-bc87-c8104486fa4f)

폴더가 설정되면 탐색기에 해당 폴더와 모든 하위 폴더의 스크립트가 표시되고 스크립트를 관리할 수 있는 새 버튼 세트가 활성화됩니다:

![Figure_26](https://github.com/user-attachments/assets/d424fea4-02d6-4fa8-8c78-6ce46bbaffbb)

<br>

### Search

검색 탭을 클릭하여 검색 패널을 엽니다. 키워드를 검색하면 패널에 열려 있는 모든 스크립트에 대한 모든 일치 항목이 표시됩니다. 일치하는 항목을 클릭하면 해당 스크립트 및 줄로 이동할 수 있습니다:

![Figure_27](https://github.com/user-attachments/assets/ca88abb9-f781-4e13-a200-c5ef63838e3f)

<br>

### Help

도움말 탭을 클릭하면 도움말 패널이 열립니다. 이 패널에서는 Rhino와 Grasshopper API에 대한 간단한 도움말을 얻을 수 있으며, Python 모듈을 제공합니다:

![Figure_28](https://github.com/user-attachments/assets/3db3908c-0ec8-43fa-b481-12f464969068)

검색 필드를 사용하여 클래스 또는 메서드 이름을 검색합니다. 하단의 정보 패널에는 메서드 및 해당 매개변수에 대한 몇 가지 정보가 제공됩니다:

![Figure_29](https://github.com/user-attachments/assets/442ff863-2476-4e92-9490-7c2e25e3de7a)

선택한 멤버에게 온라인 문서가 있는 경우 편집기에 내용을 보여주는 미리 보기 탭이 열립니다:

![Figure_30](https://github.com/user-attachments/assets/5ea1e718-88f3-485e-a94c-cf474fb28351)

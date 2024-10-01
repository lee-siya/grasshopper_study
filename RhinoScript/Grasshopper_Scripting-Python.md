# Grasshopper Scripting: Python

by Ehsan Iran-Nejad (Last updated: Thursday, August 15, 2024)

Note <br>
이 가이드는 Grasshopper Python 3 또는 2 스크립트 컴포넌트의 모든 중요한 측면과 기능에 대한 자세한 참조를 위한 것입니다. 스크립트 컴포넌트에 대한 간략한 소개를 원하시면 여기를 확인하시기 바랍니다:

[Grasshopper Script Component](https://developer.rhino3d.com/guides/scripting/scripting-component/) or Script_Component-Grasshopper.md

Note <br>
이 안내서는 Rhino 또는 Grasshopper API에 대해서는 설명하지 않습니다. Rhino와 Grasshopper에서 복잡한 지오메트리를 만드는 방법을 알고 싶으시다면, 여기를 확인하시기 바랍니다:

[Python in Rhino & Grasshopper](https://developer.rhino3d.com/guides/rhinopython/)

## Python Component

스크립트 컴포넌트를 생성하여 Grasshopper에서 Python 스크립팅에 대해 알아봅시다. 수학 탭과 스크립트 패널로 이동하여 Python 3 스크립트 컴포넌트를 캔버스에 끌어다 놓습니다. 사용할 수 있는 IronPython 2 Script 컴포넌트도 있습니다. 차이점은 위를 참조하세요:

    Figure_57

모든 언어를 실행할 수 있는 일반 스크립트 컴포넌트를 사용할 수도 있으며 [ ● ● ● ] 메뉴에서 파이썬 3을 선택할 수도 있습니다:

    Figure_58

<br>

### Opening Script Editor

이제 컴포넌트를 두 번 클릭하여 스크립트 편집기를 열 수 있습니다. 컴포넌트가 이 컴포넌트와 연결된 편집기를 가리키는 원뿔을 그린다는 점에 유의하세요.

    Figure_59

스크립트 편집기의 상태 표시줄에 Python 언어 버전이 표시됩니다:

    Figure_60

<br>

### Component Options

언제든지 스크립트 구성 요소를 마우스 오른쪽 버튼으로 클릭하여 구성 요소의 동작 방식을 변경할 수 있는 몇 가지 옵션에 액세스할 수 있습니다. **Preview**, **Enable**, and **Bake**와 같은 다른 Grasshopper 구성 요소와 공통된 몇 가지 옵션을 알고 계실 것입니다. 아래에서 이 스크립트 컴포넌트와 관련된 모든 옵션에 대해 자세히 설명하겠습니다:

    Figure_61

#### Advanced Options

Shift 키를 누른 상태에서 컴포넌트를 마우스 오른쪽 버튼으로 클릭하여 컨텍스트 메뉴에 액세스할 수 있는 경우 확장된(고급) flavour입니다. 이 메뉴에는 특별한 경우에 필요한 일련의 고급 옵션이 있으며, 이 가이드의 뒷부분에서 설명합니다.

#### Script Name

Grasshopper의 스크립트는 파일로 저장되지 않습니다. 대부분 스크립트 컴포넌트 안에 포함되어 있습니다. 스크립트 이름을 지정하려면 기본적으로 구성 요소 자체의 이름을 변경합니다. 스크립트 탭과 중단점 패널에는 스크립트 이름이 반영됩니다:

    Figure_62

<br>

## Inputs, Outputs

스크립트 컴포넌트에서 가장 중요한 개념은 입력/출력입니다. 스크립트 컴포넌트는 줌 가능한 사용자 인터페이스(줄여서 ZUI)를 지원합니다. 즉, 삽입 [ ⊕ ] 및 제거 [ ⊖ ] 컨트롤이 양쪽에 표시될 때까지 확대하여 컴포넌트의 입력 및 출력을 수정할 수 있습니다:

    Figure_63

기본적으로 스크립트 컴포넌트에는 x 와 y 입력이 있고 출력으로 out 과 a가 있습니다. 양쪽의 모든 매개변수가 제거되면 컴포넌트는 해당 쪽에 들쭉날쭉한 가장자리를 그립니다. 모든 스크립트에 입력이 필요하거나 값을 출력으로 생성하는 것은 아니므로 이는 완전히 괜찮습니다:

    Figure_64

매개변수를 추가할 때마다 새 임시 이름이 할당됩니다. 매개변수 자체를 마우스 오른쪽 버튼으로 클릭하여 이름을 편집할 수 있습니다. 다른 사람들이 컴포넌트에 전달할 입력의 종류나 이러한 입력의 용도를 이해할 수 있도록 매개변수에 의미 있는 이름을 지정하는 것이 좋습니다.

<br>

### Reserved Name

모든 프로그래밍 언어에는 해당 언어 구조에 사용되는 예약어(또는 키워드) 집합이 있습니다. 예를 들어 Python에서는 dir, filter 또는 str이라는 단어가 모두 예약어입니다. Python 스크립트 컴포넌트는 입력 또는 출력 매개변수에 이러한 키워드를 사용할 때 경고를 표시하지만 사용을 막지는 않습니다. Python 언어 자체는 dir 또는 filter와 같은 기본 제공 함수에 값을 할당하는 것을 막지 않으며 이 컴포넌트는 이 동작을 따릅니다:

    Figure_65

이러한 키워드에 대한 자세한 내용은 파이썬 3 키워드 및 파이썬 3 내장 함수에서 확인하세요.

<br>

### Standard Output (out)

out 출력 매개변수는 특별합니다. 스크립트가 콘솔에 출력하는 모든 내용을 캡처합니다(print()). 캡처된 출력은 이 매개변수에 하나의 문자열 또는 여러 문자열(각 줄에 하나씩)로 전달됩니다. 기본 동작은 콘솔에 인쇄되는 각 줄이 out 매개변수에 하나의 항목이 되는 것입니다:

    Figure_66

출력 줄 접목 방지 옵션을 사용하여 단일 줄과 다중 줄 동작을 제어할 수 있습니다. 이 옵션을 선택하면 모든 콘솔 출력이 하나의 단일 항목으로 out 파라미터에 전달됩니다.

    Figure_67

#### Toggling Output

스크립트가 출력에 아무것도 인쇄하지 않는 경우 컴포넌트 컨텍스트 메뉴의 표준 출력/오류 매개변수 옵션을 사용하여 출력 및 토글할 수 있습니다. 이 옵션을 선택하면 출력 매개변수가 첫 번째 출력 매개변수로 추가됩니다. 그렇지 않으면 제거됩니다:

    Figure_68

out 매개변수를 제거하면 스크립트 컴포넌트가 출력 캡처, 처리(줄로 분할), 결과 설정 등을 시도하지 않기 때문에 스크립트 컴포넌트의 성능이 약간 향상될 수 있습니다. 이러한 성능 향상은 단일 컴포넌트에서는 의미가 없을 수 있지만, 데이터를 처리하기 위해 각각 수천 번 실행되는 여러 스크립트 컴포넌트가 있는 대규모 Grasshopper 정의에서는 눈에 띄게 향상될 수 있습니다. 일반적으로 사용하지 않을 때는 out 매개변수를 해제하는 것이 좋습니다.

<br>

### Type Safety

파이썬은 타입 안전 언어가 아닙니다. 즉, x라는 변수에 어떤 유형이든 값을 할당할 수 있습니다. 이는 변수 x가 int로 정의된 경우 Sphere 유형의 값을 할당할 수 없는 C#과 같은 타입이 지정된 언어와는 매우 다릅니다.

이 스크립트가 포함된 파이썬 스크립트 컴포넌트가 있다고 가정해 보겠습니다:

    a = x + y

x와 y 입력이 연결되지 않아서 어떤 값도 전달하지 않는 경우(값은 None), 파이썬은 None을 다른 None에 추가하는 방법을 모르기 때문에 이 컴포넌트가 실행될 때 에러를 던집니다:

    Figure_69

유형 안전성이란 실제로 언어가 컴파일 중에(스크립트를 실행하기 전에) 변수 유형을 감지하고 연산이나 함수 호출이 특정 변수 유형을 지원하지 않는 경우 오류를 발생시키는 것을 의미합니다. 하지만 앞서 언급했듯이 파이썬은 타입 안전하지 않기 때문에 컴파일 중에 a = x + y에서 + 연산을 지원하는 값을 제공할 것이라고 가정합니다. 따라서 스크립트를 실행하는 동안 위에 표시된 오류가 발생합니다.

이 예제에서는 정수와 같이 덧셈을 지원하는 값을 제공하면 컴포넌트가 오류 없이 실행됩니다:

    Figure_70

<br>

### Type Hints

스크립트의 입력값을 변환해야 하는 경우가 많습니다. Grasshopper에서 잘 알려진 매개변수 변환은 우리 모두가 잘 알고 사랑하는 기능입니다. 예를 들어 Line 매개변수를 숫자 매개변수로 전달하면 자동으로 줄의 길이를 숫자 매개변수의 값으로 가져올 수 있습니다:

    Figure_71

이러한 자동 변환을 스크립트 컴포넌트 입력 파라미터에 쉽게 적용할 수 있습니다. 이 예제에서는 두 개의 Line 값이 Python 스크립트 a = x + y에 전달됩니다. x와 y 입력 모두 부동 소수점 값을 보유할 수 있는 float 유형 힌트(Grasshopper의 숫자)가 할당되었습니다:

    Figure_72

따라서 스크립트를 실행하기 전에 두 입력 줄은 유형 힌트에 의해 플로트 값으로 변환되고 출력 a는 줄 길이의 합으로 설정됩니다:

    Figure_73

선택할 수 있는 유형 힌트는 다양합니다. 입력 및 출력 매개변수 모두에서 사용할 수 있습니다.

고급을 확인하세요: 이러한 유형 힌트 및 사용 사례에 대한 자세한 내용은 고급: 유형 힌트에서 확인하세요.

### Parameter Access

컴포넌트 입력 매개변수에는 컨텍스트 메뉴에 또 다른 유용한 옵션이 있습니다. 이 기능은 매개변수 액세스라고 하며 Grasshopper SDK(GH_ParamAccess)의 일부입니다:

    Figure_74

스크립트 컴포넌트 입력에서도 이 옵션을 수정할 수 있습니다:

    Figure_75

다음은 세 가지 액세스 유형에 대해 x 매개변수에서 스크립트 컴포넌트에 전달되는 데이터 유형의 예입니다. Item 액세스의 경우 x는 숫자 값을 나타내는 개별 이중으로 전달되고, List 액세스의 경우 x는 한 분기에 모든 숫자 값을 포함하는 List<객체>로 설정되며, Tree 액세스의 경우 x는 입력의 모든 분기와 항목에 대한 액세스를 제공하는 DataTree<객체>로 설정된다는 점에 주목하세요:

    Figure_76

항목 및 목록 액세스에는 기본 제공 파이썬 유형인 float 및 목록이 표시되지만, 트리 액세스에는 Grasshopper.DataTree[Object] 유형이 표시됩니다(데이터트리 참조). 이는 마샬링에서 논의되는 중요한 주제입니다.

일반 데이터트리 구조가 올바른 유형을 사용하도록 하려면 입력 매개변수 x에 float 유형 힌트를 적용하면 됩니다. 일반 데이터트리 구조는 요소 유형으로 Double을 표시합니다. 이것은 큰 부동 소수점 값을 넣을 수 있는 Grasshopper의 숫자 매개변수 유형으로, 파이썬의 float와 다소 유사합니다:

    Figure_77

### Extracting Parameters

Grasshopper를 사용하면 컴포넌트에서 입력 파라미터를 추출할 수 있습니다. 컴포넌트의 매개변수는 컴포넌트의 입력 또는 출력 또는 부동 매개변수(매개변수 유형)로 존재할 수 있는 독립적인 엔티티입니다.

매개변수의 오른쪽 클릭 메뉴에서 추출을 선택하여 스크립트 입력을 추출할 수 있습니다:

    Figure_78

매개변수에 유형 힌트가 설정되어 있는 경우, 추출된 부동형 매개변수는 해당 데이터 유형이 됩니다:

    Figure_79

<br>

## Script-Mode

Grasshopper에서 Python 스크립트를 작성하는 방법에는 두 가지가 있습니다. 첫 번째이자 가장 쉬운 방법은 가장 간단한 형태로 Python 스크립트를 작성하는 것으로, **Script-Mode** 라고 합니다. 예를 들어, 두 개의 x 및 y 입력의 합계를 a 출력에 전달하려면 이 스크립트로 스크립트 컴포넌트를 만들면 됩니다:

    a = x + y

다음은 또 다른 간단한 예입니다:

    Figure_80

스크립트가 시작되기 전에 x 입력 매개변수가 마술처럼 정의되고 설정되는 것을 볼 수 있습니다. 파이썬 3 스크립트 컴포넌트이므로 F-Strings나 Walrus 연산자 같은 새로운 구문 기능을 사용할 수 있습니다.

다른 예제는 PyPI 패키지를 확인하세요.

Note <br>
Grasshopper 컴포넌트처럼 동작하는 Python 스크립트 컴포넌트를 만들려면 SDK-Mode를 참조하세요.

SDK-Mode와 Script-Mode는 모두 Python 스크립트 컴포넌트에서 스크립트를 작성하는 유효한 방법입니다. 사용 사례에 가장 적합하고 편한 것을 선택하세요.

### Accessing Inputs

위에서 언급했듯이 입력 매개변수는 스크립트가 시작되기 전에 마술처럼 정의되고 설정됩니다. 스크립트 어디에서나 입력 값을 참조할 수 있습니다.

위의 예에서 출력 x는 스크립트 범위에서 이미 정의 및 설정되어 있으므로 스크립트에서 해당 값을 사용할 수 있습니다:

    a = f'Hello {x}'

스크립트에서 함수를 정의할 수도 있습니다. 이러한 함수는 정의된 매개변수에 액세스할 수 있습니다:

    def Solve() -> float:
        return x + y
    
    a = Solve()

더 복잡한 경우에는 전역 변수에 액세스할 때 같은 이름의 다른 변수와 명명 충돌이 발생하지 않도록 전역으로 참조해야 합니다:

    s = Solver()
    a = s.Compute()
    
    class Solver:
        def __init__(self):
            pass
    
        def Compute() -> float
            global x
            global y
            return x + y

### Settings Outputs

위에서 언급했듯이 스크립트 모드에서 출력 변수는 컴포넌트에 의해 스크립트 범위에서 마술처럼 정의됩니다. 스크립트에서 원하는 값을 출력에 할당하면 컴포넌트 출력에 설정됩니다.

<br>

## SDK-Mode

일반적인 그래스호퍼 컴포넌트는 다음과 같습니다:

+ 컴포넌트가 입력을 풀기 전에 코드 실행하기 ([BeforeSolveInstance](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_BeforeSolveInstance.htm))
+ 입력을 풀고 결과를 출력으로 전달하기 ([SolveInstance](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_SolveInstance.htm))
+ 컴포넌트가 입력값 해결을 완료한 후 코드 실행하기 ([AfterSolveInstance](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_AfterSolveInstance.htm))
+ Rhino 뷰포트에서 지오메트리 와이어를 그리는 코드 실행하기 ([DrawViewportWires](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm))
+ Rhino 뷰포트에서 지오메트리 메쉬를 그리는 코드 실행하기 ([DrawViewportMeshes](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_DrawViewportMeshes.htm))

위에 링크된 메서드는 사용자 정의 컴포넌트 생성을 위한 Grasshopper SDK의 일부입니다. Grasshopper 플러그인을 만드는 모든 개발자는 이러한 메서드를 알고 있으며 이를 사용하여 컴포넌트 동작을 사용자 정의할 수 있습니다.

Python 스크립트 컴포넌트에서도 비슷한 방식으로 스크립트를 구현할 수 있습니다. 그렇기 때문에 Grasshopper SDK에서 사용할 수 있는 유사한 기능을 제공하므로 이를 SDK 모드라고 부릅니다.

기본적으로 Python 스크립트 컴포넌트를 만들 때 템플릿 스크립트는 스크립트 모드에 있으며, 이는 Rhino 8 이전 Python 컴포넌트의 작동 방식이며, Rhino 8 이후에도 동일하게 유지되었습니다. 이 모드는 스크립트 전후에 코드를 실행하거나 Rhino 뷰포트에서 사용자 정의 그래픽을 만드는 기능은 지원하지 않지만, 이러한 기능이 필요하지 않은 스크립트에 적합합니다. 스크립트 모드를 참조하십시오.

기본 스크립트의 모습은 다음과 같습니다 (실제 스크립트는 동일하지 않을 수 있습니다):

    """Grasshopper Script"""
    a = "Hello Python 3 in Grasshopper!"
    print(a)

기본 스크립트를 SDK 모드로 변환하려면 편집기 대시보드에서 GH_ScriptInstance로 변환 버튼을 클릭합니다:

    Figure_81

기존 코드는 GH_ScriptInstance 클래스의 구현 안에 배치됩니다. RunScript 메서드가 이미 추가되어 있고 시그니처에 컴포넌트 입력이 있는 것을 확인할 수 있습니다:

    Figure_82

GH_ScriptInstance는 Grasshopper 컴포넌트와 유사하게 아래 메서드를 구현하는 베이스 클래스입니다:
+ BeforeRunScript: 컴포넌트가 입력을 풀기 전에 코드를 실행합니다.
+ RunScript: 입력값을 풀고 결과를 출력으로 전달하기
+ AfterRunScript: 컴포넌트가 입력값 해결을 마친 후 코드를 실행합니다.
+ DrawViewportWires: Rhino 뷰포트에 지오메트리 와이어를 그리는 코드를 실행합니다.
+ DrawViewportMeshes: Rhino 뷰포트에서 지오메트리 메쉬를 그리는 코드를 실행합니다.

이 클래스는 우리가 구현해야 하는 RunScript를 제외한 이러한 메서드에 대한 기본 구현을 제공합니다. 위의 예제에서는 GH_ScriptInstance에서 서브클래스를 생성하고 RunScript에 대한 empty implementation 을 제공합니다.

<br>

### RunScript Signature

RunScript 메서드 서명에는 모든 컴포넌트 입력과 출력이 이름과 데이터 유형(유형 힌트에 따라)에 따라 포함됩니다. 출력 값은 반환 문을 사용하여 반환해야 합니다:

    Figure_83

컴포넌트의 로직을 RunScript 블록 안에 작성하고 입력값을 받아 계산한 후 출력을 반환할 수 있습니다. 다른 Grasshopper 컴포넌트와 마찬가지로, 입력 데이터의 페어링에 따라 RunScript 메서드가 여러 번 호출될 수 있습니다.

#### Python 3 Type Hints

x와 y 입력에 유형이 어떻게 힌트되는지 주목하세요. 이것은 유형 힌트(Type Hinting)라고 하는 Python 3의 기능이며 Grasshopper의 유형 힌트와 혼동해서는 안 됩니다. Python 3 유형 힌트는 Python 코드의 정적 분석(예: 자동 완성, 진단 등)에만 사용되며 스크립트 실행에는 아무런 영향을 미치지 않습니다. 위의 예에서, 입력 y는 Rhino.Geometry.Plane 유형으로 힌트되어 자동완성에서 y의 유형을 결정하고 더 나은 자동완성을 제공하는 데 도움이 됩니다:

    Figure_84

#### RunScript Returns

간단한 반환 문을 사용하여 모든 컴포넌트 출력을 반환할 수 있습니다. 이 예제에서는 런스크립트에서 a 및 b 값을 계산하여 반환합니다:

    class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
        def RunScript(self, x: int, y: Rhino.Geometry.Plane):
            a = self.compute_a(x)
            b = self.compute_b(x)
            return a, b

값을 튜플로 명시적으로 반환하는 것도 허용됩니다:

            return (a, b)

<br>

### Changing RunScript Signature

스크립트 컴포넌트는 컴포넌트의 매개변수가 변경될 때 RunScript 서명을 업데이트할 수 있을 만큼 똑똑합니다. 또한 RunScript 서명을 수동으로 편집할 때 컴포넌트의 매개변수를 업데이트할 수도 있습니다:

<iframe title="vimeo-player" src="https://player.vimeo.com/video/943289663?h=f21bbb6cd8" width="640" height="360" frameborder="0"    allowfullscreen></iframe>

[VideoLink](https://developer.rhino3d.com/guides/scripting/scripting-gh-python/)

입력 유형은 매개변수에 적절한 유형 힌트를 적용하는 데 사용됩니다. 입력의 컬렉션 유형(목록 또는 데이터트리)은 연결된 입력 매개변수에 올바른 액세스 종류를 적용하는 데에도 사용됩니다.

또한 유형 힌트로 list를 사용하더라도 자동으로 System.Collections.Generic.List[object]로 변환된다는 점에 유의하세요. 이에 대해서는 마샬링에 자세히 설명되어 있습니다.

<br>

### Before, After Solve Overrides

다음을 통해 스크립트 인스턴스 구현에 BeforeRunScript 및 AfterRunScript 메서드를 쉽게 추가할 수 있습니다:
+ 에디터 대시보드에서 솔브인스턴스 오버라이드 추가(**Add SolveInstance Overrides**) 버튼을 클릭합니다.
+ 에디터의 그래스호퍼 메뉴에서 솔브인스턴스 오버라이드 추가(**Add SolveInstance Overrides**) 메뉴를 클릭합니다.
+ 직접 입력하기

    Figure_85

이 두 메서드는 클래스 구현에 추가됩니다:

    Figure_86

Note <br>
이 두 메서드를 사용하는 좋은 예는 BeforeRunScript 중에 클래스 인스턴스에 인스턴스 변수를 설정하고 AfterRunScript 중에 실행 후 정리하는 것입니다. 컴포넌트는 이러한 메서드 내에서 출력 매개변수를 변경할 수 없습니다.

이러한 각 메서드는 이 컴포넌트가 완전히 실행될 때마다 한 번만 실행됩니다. 이러한 메서드에 몇 개의 인쇄문을 넣고 실행 순서를 확인할 수 있습니다:

    Figure_87

이 예시에는 스크립트 컴포넌트에 입력을 제공하기 위해 두 개의 범위 컴포넌트가 포함되어 있습니다. 각 범위 컴포넌트는 3개의 항목을 출력하며, 스크립트 컴포넌트의 관련 입력 매개변수에는 실수 유형 힌트가 할당되어 있습니다. 즉, 실행 스크립트 메서드가 3쌍의 x와 y에 대해 3번 실행됩니다.

입력값을 푸는 첫 번째 반복인 Solve #0과 동일한 출력 항목에 Before Solve라는 텍스트가 인쇄되어 있는 것을 볼 수 있습니다. 이는 스크립트 컴포넌트가 출력 매개변수에 값을 설정할 수 있기 전에 BeforeRunScript가 실행되므로 콘솔에 출력되는 모든 출력은 바로 뒤에 실행되는 RunScript의 첫 번째 반복에 의해 캡처되기 때문입니다.

RunScript의 다른 모든 반복은 첫 번째 반복 이후에도 계속됩니다.

AfterRunScript는 실행 스크립트의 모든 반복이 실행을 완료한 후에 실행됩니다. After Solve 텍스트가 캡처되어 바로 전에 실행된 RunScript의 마지막 반복에 속하는 out 매개 변수의 마지막 메시지에 추가되는 것을 확인할 수 있습니다.

<br>

### Preview Overrides

Note <br>
미리보기 오버라이드는 Rhino 뷰포트와 상호 작용할 때 계속 호출됩니다. 이러한 오버라이드의 작동 방식에 대한 자세한 내용은 그리기 호출을 참고하세요.

다음과 같이 스크립트_인스턴스 구현에 DrawViewportWires 및 DrawViewportMeshes 메서드를 쉽게 추가할 수 있습니다:
+ 편집기 대시보드에서 미리보기 재정의 추가(**Add Preview Overrides**) 버튼을 클릭합니다.
+ 편집기의 **Grasshopper** 메뉴에서 미리보기 오버라이드 추가(**Add Preview Overrides**) 메뉴를 클릭합니다.
+ 직접 입력하기

    Figure_88

이 두 메서드는 클래스 구현에 추가됩니다:

    Figure_89

DrawViewportWires가 먼저 호출되며 여기에서 점과 곡선을 그릴 수 있습니다. DrawViewportMeshes는 나중에 호출되며 여기에서 메쉬와 같은 투명한 도형을 그릴 수 있습니다.

ClippingBox 속성 구현도 추가되었습니다. 기본값은 BoundingBox.Empty이지만 컴포넌트에서 그리는 사용자 정의 지오메트리의 경계를 지정하는 더 큰 바운딩 박스로 변경해야 합니다.

다음은 Rhino 뷰포트의 왼쪽 상단에 2D로 채워진 직사각형을 그리는 컴포넌트의 예입니다:

    Figure_90

이러한 미리보기 오버라이드 메서드에는 IGH_PreviewArgs 유형의 인수가 전달됩니다. 위의 예에서 볼 수 있듯이, Rhino DisplayPipeline 인스턴스이며 유용한 그리기 메서드가 많이 있는 args.Display 프로퍼티에 액세스할 수 있습니다.

args: Grasshopper.Kernel.IGH_PreviewArgs 유형 힌트(type hint)를 추가하면, args 변수에서 더 나은 자동 완성 결과를 얻을 수 있습니다:

    Figure_91

System.Drawing vs Eto.Drawing <br>
Rhino 8 이상에서는 주로 Eto라는 UI 프레임워크를 사용합니다. 그러나 Grasshopper 1은 이 프레임워크가 채택되기 이전 버전으로, 그래픽 인터페이스에 System.Drawing 프레임워크를 사용합니다. 둘 다 비슷한 데이터 구조(예: 직사각형)를 가지고 있지만, Grasshopper 미리보기 오버라이드로 작업할 때 System.Drawing 데이터 유형을 사용한다는 점을 알아두는 것이 중요합니다.

<br>

### Draw Calls

미리보기 오버라이드(**Preview Overrides**)는 Grasshopper 솔루션 외부에서 실행되고 솔브 메서드와 함께 작동하도록 설계되었다는 점에서 솔브 오버라이드(BeforeRunScript, RunScript, AfterRunScript)와 근본적으로 다르다는 점을 아는 것이 매우 중요합니다.

컴포넌트와 상호 작용하면 Grasshopper는 정의에 대한 새 솔루션을 트리거합니다. 솔루션이 완료되면, 캔버스에서 컴포넌트에 의해 생성된 모든 지오메트리에 대한 미리보기를 그릴 준비가 된 것입니다.

Rhino 뷰포트와 상호 작용할 때마다 Grasshopper는 Rhino로부터 뷰포트에 미리보기를 그리라는 요청을 받습니다. 이러한 그리기 요청은 Rhino 뷰포트와 상호 작용하고 Grasshopper 정의가 열려 있을 때 언제든지 발생합니다.

바로 이 지점에서 미리보기 오버라이드가 작동합니다. 미리보기 오버라이드의 주요 목적은 솔브 오버라이드로 수행한 계산 결과를 기반으로 Rhino 뷰포트에서 사용자 정의 그리기를 수행하는 것입니다. 풀기 메서드와 달리, 미리보기 오버라이드는 Rhino 뷰포트와 상호 작용할 때 계속 호출됩니다.

<br>

## Marshalling

### Mashalling Guids

The ubiquitous rhinoscriptsyntax modules(보통 rs로 가져오기)은 고유 식별자(Guid)로 Rhino 문서 요소를 참조합니다. Python 스크립트 컴포넌트에는 rhinoscriptsyntax 함수를 보다 쉽게 다룰 수 있는 몇 가지 기능이 있습니다:

+ 출력 매개변수는 기본적으로 고유 식별자를 관련 Rhino 문서 요소로 자동 변환합니다. 이 기능은 컴포넌트 컨텍스트 메뉴 항목 출력 안내선 마샬링 방지에서 토글할 수 있습니다:

    Figure_92

Type Hint가 **ghdoc Object**인 입력 매개변수는 입력 Rhino 문서 요소를 고유 식별자로 자동 마샬링하여 rhinoscriptsyntax 함수에 전달할 수 있도록 합니다. 위의 예에서 출력 Sphere를 ghdoc Object의 유형 힌트를 가진 구의 입력이 있는 또 다른 스크립트 컴포넌트에 전달하면, 구에 포함된 실제 값이 고유 식별자가 됩니다. 이 식별자를 rs.RebuildSurface에 전달하여 구체를 다시 빌드할 수 있습니다:

    Figure_93

Note <br>
입력 요소를 고유 식별자로 마샬링할 때 해당 요소는 프록시 헤드리스 문서(proxy headless document)에 저장됩니다. 그런 다음 이 문서는 스크립트 실행 기간 동안 scriptcontext.doc에 할당됩니다(Grasshopper 컨텍스트를 나타내기 위해 scriptcontext.id == 2 설정과 함께). 모든 rhinoscriptsyntax 함수는 이 프록시 문서를 사용하여 작업을 수행하므로 모든 것이 원활하게 실행됩니다.

<br>

### Marshalling Data Types (CPython)

현재 Rhino의 Python 3 구현은 CPython을 사용하며, 그 데이터 유형은 닷넷 유형(dotnet data types)과 매우 다릅니다. 예를 들어, 닷넷 List<int>에는 목록의 길이를 보고하는 Count 속성이 있습니다. 그러나 Python 3의 목록 유형에는 이러한 속성이 없으며, 일반적으로 이터러블(iterable)의 길이를 측정하기 위해 내장 함수 len()을 사용합니다.

#### Input

스크립트 모드에서 파이썬 3 스크립트로 작업할 때 닷넷 데이터 유형은 자동으로 파이썬 3 데이터 유형으로 마샬링됩니다. 따라서 List<int> 입력은 정수만 포함된 파이썬 목록으로 변환됩니다. 이 동작은 컴포넌트 고급 옵션의 입력 마샬링 방지(**Avoid Marshalling Inputs**) 항목을 사용하여 전환할 수 있습니다. 아래 예시에서 입력 매개변수 x는 Access of List를 가집니다. 위쪽 컴포넌트는 기본적으로 닷넷 입력 List<>를 파이썬 목록으로 변환하고 있으며, 아래쪽 컴포넌트는 마샬링 입력 회피가 선택되어 있어 변환을 건너뛰고 있습니다.

    Figure_94

SDK 모드에서 작업할 때 Access가 List인 입력 매개변수는 런스크립트 구문에서 dotnet List<>로 정의되며, 기본적으로 입력 마샬링 방지 옵션이 선택되어 있습니다. 아래 예제에서 입력 매개변수 x는 Access of Item과 Type Hint가 정수입니다. 런스크립트 서명에서 매개변수 x가 x로 힌트된 것을 확인할 수 있습니다: System.Collections.Generic.List<int>:

    class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
        def RunScript(self, x: System.Collections.Generic.List<int>):
            ...

<br>

### Outputs

출력 매개 변수는 동일한 논리를 따릅니다. 기본적으로 Python 3 목록의 출력은 다른 grasshopper components 가 데이터를 사용할 수 있도록 dotnet list\<object>로 변환됩니다. 이 동작은 구성 요소 고급 컨텍스트 메뉴에서 **Avoid Marshalling Outputs** 항목을 사용하여 토글할 수 있습니다.

Note <br>
여러 Python 3 컴포넌트가 함께 작동하는 경우, 데이터가 중간에 다른 컴포넌트의 개입 없이 한 Python 3 컴포넌트에서 다른 Python 3 컴포넌트로 직접 흐르기 때문에 입력 및 출력 마샬링을 피할 수 있는 옵션이 있습니다. 이 경우 파이썬 목록을 닷넷 List<>로 변환했다가 다시 파이썬 목록으로 변환할 필요가 없습니다. Upstream 컴포넌트에서 마샬링 출력을 피하기만 하면 변환 없이 정확히 동일한 데이터가 downstream 으로 전달됩니다. 이제 single python list instance 를 전달하므로 컴포넌트 사이의 Grasshopper 와이어는 한 줄입니다:

    Figure_95

<br>

## Debugging Scripts

스크립트 에디터에서 Python 스크립트를 디버그할 수 있습니다. 디버그 중에 스크립트를 한 줄씩 실행하거나 중단점이라는 특정 줄에서 실행을 일시 중지하고 전역 및 로컬 변수의 값을 검사할 수 있습니다. 

마우스 커서를 스크립트 줄의 왼쪽으로 이동하고 클릭하여 중단점을 추가합니다:

    Figure_96

하단의 중단점 트레이에는 모든 중단점이 표시되며, 활성화/비활성화 또는 지우기 버튼이 제공됩니다:s

    Figure_97

토글 버튼을 사용하여 중단점을 활성화 또는 비활성화합니다. 비활성화된 중단점은 편집기에서 회색 점으로 표시됩니다:

    Figure_98

중단점을 추가하면 에디터에서 몇 가지 UI가 변경되고 디버깅을 위한 몇 가지 유틸리티가 추가로 제공됩니다:
+ 실행 버튼이 디버그
+ **Variables**, **Watch**, and **Call Stack** 트레이가 하단 트레이 막대에 추가됩니다.

이제 편집기 대시보드에서 녹색 디버그 버튼을 클릭합니다. 편집기가 스크립트를 실행하고:
+ 중단점에서 중지
+ 중단점 선을 주황색으로 강조 표시하고 선의 왼쪽에 화살표를 표시합니다.
+ 상태 표시줄을 주황색으로 강조 표시하여 스크립트를 디버깅 중임을 표시합니다.
+ 에디터 대시보드에서 디버그 제어 버튼을 활성화합니다.
+ 하단의 **Variables** 트레이를 열어 전역 및 로컬 변수를 표시합니다.

    Figure_99

에디터 대시보드의 디버그 제어 버튼을 사용하여 스크립트 실행을 제어할 수 있습니다:

    Figure_100

왼쪽부터 차례대로 설명합니다:
+ **Continue**: 다른 중단점에서 멈출 때까지 스크립트를 계속 실행합니다.
+ **Step Over**: 현재 줄을 실행하고 다음 줄로 이동합니다.
+ **Step In**: 현재 줄에 함수 호출이 포함되어 있으면 함수 코드를 정의하는 줄로 이동합니다.
+ **Step Out**: 이전에 함수 코드에 들어간 경우 함수에서 호출 코드로 제어가 반환될 때까지 함수 코드를 계속 실행하고 거기서 멈춥니다.
+ **Stop**: 스크립트 디버깅을 중지하고 나머지 실행을 계속하지 않습니다.

**Continue** 를 클릭하면 실행이 다음 줄로 이동합니다:

이제 변수 패널에 x 및 y에 대한 새 값이 표시됩니다. 패널 헤더의 오른쪽 상단에 스크립트 실행(11개 중 2개)이 표시되어 Grasshopper가 x 및 y 입력 쌍으로 이 컴포넌트를 두 번째로 실행한다는 것을 알 수 있습니다:

    Figure_101

**Continue** 를 클릭하면 스크립트가 계속 실행되고 변수가 수정됩니다. 각 중지 시 변수 트레이에 전역 및 로컬 변수의 현재 값이 표시됩니다.

디버그 중 언제든지 중지 버튼을 누르면 디버깅이 중지됩니다. 스크립트 컴포넌트에 디버그 중지 메시지와 함께 오류 표시가 표시됩니다:

    Figure_102

디버그가 중지되면 에디터 UI가 다시 정상으로 바뀌고 변수 트레이에 변수의 마지막 상태가 표시됩니다. 트레이에는 다른 디버깅 세션이 시작될 때까지 이러한 데이터가 보관됩니다.

### Variables Tray

변수 트레이는 스크립트에 있는 모든 전역 및 로컬 변수의 현재 값을 검사할 수 있는 훌륭한 도구입니다. 변수 데이터는 3개의 열이 있는 표에 표시됩니다: 이름, 값, 유형입니다. 각 변수에 대해 현재 값과 해당 변수가 보유하고 있는 데이터 유형을 확인할 수 있습니다. 빨간색 마커는 디버그 중에 변경된 변수를 강조 표시합니다:

    Figure_103

필드와 속성이 있는 더 복잡한 데이터 유형의 경우 변수를 확장하여 해당 멤버의 현재 값을 확인할 수 있습니다:

    Figure_104

값이 다른 값의 모음인 경우 변수를 확장하여 각 항목을 개별적으로 볼 수 있습니다. 이름 열에는 [0]과 같은 항목 인덱스가 표시됩니다:

    Figure_105

### Watch Tray

Watch tray 는 Variables tray 와 매우 유사합니다. 주요 차이점은 Watch tray에는 특별히 감시하도록 추가한 변수만 표시된다는 점입니다. 트레이 도구 모음에서 표현식 추가(**Add Expression**) 버튼을 사용하여 새 변수를 감시 대상에 추가합니다. 추가된 표현식 항목에서 Enter 키를 눌러 변수 이름을 편집하고 입력합니다:

    Figure_106

디버그 중에 변수 값을 추출할 수 있으면 Watch tray 에 녹색 확인 표시가 나타납니다. 변수가 범위에 없는 경우 노란색 경고 아이콘이 표시됩니다:

    Figure_107

### Call Stack Tray

Call Stack Tray에는 Call Stack 프레임이 표시됩니다. 이는 스크립트에서 함수 호출로 느슨하게 해석할 수 있습니다. 맨 위에 있는 항목은 스크립트가 실행 중인 마지막 함수이며, 목록에는 현재 함수를 호출한 다른 함수가 계속 표시됩니다.

아래 예제에서는 RunScript를 실행하여 스크립트 실행을 시작했습니다. 그런 다음 스크립트에서 Sum 메서드를 호출했고, 지금 디버그 중에 일시 중지된 곳이 바로 이 지점입니다. 호출 스택 트레이에는 이 함수가 목록의 맨 위에 표시되고 바로 뒤에 RunScript가 표시됩니다. 변수 및 감시 트레이에도 현재 호출 프레임에 있는 변수의 값이 표시됩니다:

    Figure_108

다른 스택 프레임을 클릭하고 변수 또는 감시 트레이로 전환하여 해당 범위의 값을 검사할 수 있습니다:

    Figure_109

Call Stack Tray 에는 스크립트의 여러 스레드에 대한 스택 프레임이 독립적으로 표시됩니다.

<br>

## PyPl Packages

Python 3 스크립트는 PyPI 패키지 서버에 게시된 타사 패키지의 이점을 활용할 수 있습니다. 패키지 설치 버튼을 사용하여 이러한 패키지를 설치하여 스크립트에서 사용할 수 있습니다:

    Figure_110

패키지 설치 대화 상자에는 패키지 이름과 버전 요구 사항을 지정하는 방법에 대한 몇 가지 예가 나와 있습니다.

스크립트에 **Add Package Reference to Script**(default)을 선택하면 스크립트 텍스트에 패키지 참조가 추가됩니다. 이렇게 하면 이 스크립트를 다른 사람에게 보내는데 필요한 패키지가 설치되어 있지 않은 경우에도 스크립트가 필요한 패키지를 항상 알 수 있습니다.

    # requirements: numpy
    
    import numpy as np
    
    # numpy array with random values
    a = list(np.random.rand(7))

### Module Search Paths

스크립트 편집기에는 Python 3 및 2 검색 경로에 대한 전역 구성이 있습니다. 편집기 설정을 참조하세요: Python 경로에서 자세한 정보를 확인하세요.

아래와 같이 #env 지시문을 사용하여 스크립트에 검색 경로를 구체적으로 추가할 수도 있습니다:

    #! python 3
    # env: C:\Path\To\MyPythonModules\
    
    import my_module

### Virtual Environments

<br>

## Nuget Packages

Python 스크립트는 NuGet 패키지 서버에 게시된 타사 패키지의 이점을 활용할 수 있습니다. 패키지 설치 대화 상자를 사용하여 패키지 소스 옵션을 NuGet으로 변경할 수 있습니다:

    Figure_111

패키지 설치 대화 상자에는 패키지 이름과 버전 요구 사항을 지정하는 방법에 대한 몇 가지 예가 나와 있습니다.

스크립트에 패키지 참조 추가 옵션(기본값)을 선택하면 스크립트 텍스트에 패키지 참조가 추가됩니다. 이렇게 하면 이 스크립트를 다른 사람에게 보내는데 필요한 패키지가 설치되어 있지 않은 경우에도 스크립트가 필요한 패키지를 항상 알 수 있습니다.

아래 예제 스크립트에서 #r "nuget: RestSharp, 110.2.0" 줄을 아래 예제 스크립트에서 확인하세요. 형식은 NuGet 웹사이트의 스크립트 패키지 참조를 따릅니다:

    Figure_112

<br>

## Assembly References

Python 스크립트는 닷넷 어셈블리 파일을 직접 참조할 수도 있습니다. 패키지 설치 대화 상자를 사용하여 패키지 소스 옵션을 DLL 참조로 변경할 수 있습니다:

    Figure_113

어셈블리가 Rhino에 이미 로드되어 있는 경우, 어셈블리 이름을 입력하기만 하면 참조할 수 있습니다. 어셈블리 이름에 확장자가 포함되어 있는지 확인합니다(예: .dll) 아래 예제와 같은 패키지 참조는 선택적으로 스크립트에 추가됩니다:

    #r "System.Text.Json.dll"
    
    from System.Text.Json import JsonElement

패키지 설치 대화 상자 예제에서 볼 수 있듯이 어셈블리의 상대 경로 또는 절대 경로를 제공할 수도 있습니다:

    #r "/path/to/my/assemblies/MySharedAssembly.dll"
    
    from MySharedAssembly import MyData

<br>

## Customizing Editor

Python 스크립트 컴포넌트에서 사용되는 스크립트 에디터는 Rhino의 기본 스크립트 에디터의 내장된 변형으로, ScriptEditor 명령에서 실행됩니다. 컴포넌트 스크립트 편집기에는 Grasshopper 메뉴와 몇 가지 다른 Grasshopper 전용 버튼이 있습니다.

편집기 대시보드의 SDK 모드 관련 버튼에 대해서는 이미 설명했습니다. 다음은 Grasshopper에서 유용한 다른 편집기 옵션에 대한 설명입니다:

### Close On Save

기본적으로 Python 스크립트 컴포넌트에 스크립트를 저장할 때 편집기는 열려 있는 상태로 유지됩니다. 스크립트를 저장하고 새로 업데이트된 스크립트로 Grasshopper 정의에서 솔루션을 트리거합니다.

이 동작은 **Grasshopper -> Toggle Close Editor On Save** 를 사용하여 변경할 수 있습니다. 활성화된 경우 파일 -> 저장 또는 Ctrl + S를 선택하면 스크립트가 저장되고 편집기가 닫힙니다(이는 GHPython 컴포넌트의 레거시 스크립트 편집기의 기본 동작입니다).

### Layout Options

Python 스크립트 컴포넌트에서 사용되는 스크립트 편집기에는 편집기의 레이아웃을 변경하고 더 간결하게 만들기 위한 일련의 토글 메뉴가 있습니다. 이러한 옵션은 에디터의 창 메뉴에서 액세스할 수 있으며, 스크립트 영역에 더 많은 화면 공간을 할애하고 Grasshopper 에디터를 Rhino의 메인 에디터와 시각적으로 구분하는 데 사용할 수 있습니다.

편집기의 **Tools -> Options** 메뉴에서도 액세스할 수 있습니다. 물음표 아이콘 위에 마우스를 올리면 각 옵션에 대한 자세한 정보를 볼 수 있습니다:

    Figure_114

#### Toggle Dashboard

편집기 대시보드를 완전히 숨기고 스크립트를 위한 더 많은 공간을 확보할 수 있습니다:

    Figure_115

#### Toggle Compact Dashboard

대시보드가 표시되면 더 컴팩트하게 만들어 공간을 절약할 수 있습니다:

    Figure_116

#### Toggle Compact Script Tabs

디버그가 기본 스크립트 이외의 소스 파일로 이동하지 않는 한 기본적으로 Grasshopper 편집기에는 스크립트 탭이 표시되지 않습니다. 탭을 항상 표시하려면 이 옵션을 토글하세요:

    Figure_117

#### Toggle Compact Browser

기본적으로 브라우저 탭은 Grasshopper의 편집기 왼쪽에 표시되지 않습니다. 탭 선택기 버튼은 공간을 절약하기 위해 상태 표시줄에 표시됩니다. 왼쪽에 브라우저 탭을 표시하려면 이 옵션을 토글하세요:

    Figure_118

#### Toggle Compact Console

기본적으로 콘솔 탭은 Grasshopper의 편집기 하단 가장자리에 표시됩니다. 상태 표시줄에 탭 선택기 버튼을 표시하여 공간을 절약하려면 이 옵션을 토글하세요:

    Figure_119

<br>

## Publishing Scripts

Grasshopper 플러그인에 스크립트 컴포넌트를 게시하려는 경우 몇 가지 고려해야 할 사항이 있습니다.

스크립트 컴포넌트를 마우스 오른쪽 버튼으로 클릭하고 툴팁에 적절한 값을 설정합니다. 이 설명은 스크립트를 게시할 때 사용되며 게시된 컴포넌트에 표시됩니다.

    Figure_120

모든 입력 및 출력 매개변수를 마우스 오른쪽 버튼으로 클릭하고 각 매개변수에 대해 이름(사람이 읽을 수 있는)과 도구 설명을 설정합니다. 사람이 읽을 수 있는 이름은 Grasshopper에서 **Display -> Draw Full Names** 를 활성화하면 표시됩니다. 사람이 읽을 수 있는 이름과 설명을 설정하면 컴포넌트에 필요한 입력과 제공하는 출력을 이해하는 데 도움이 되며, 일반적으로 게시된 컴포넌트로 작업하기가 더 쉬워집니다.

    Figure_121

스크립트 구성 요소를 Grasshopper 플러그인에 게시하는 방법은 Rhino와 Grasshopper 플러그인 만들기에서 확인하세요.

<br>

## Template Scripts

편집기의 템플릿 패널에서 몇 가지 템플릿 스크립트를 사용할 수 있습니다. 이러한 템플릿 중 하나를 두 번 클릭하여 스크립트의 내용을 해당 템플릿으로 바꿀 수 있습니다. 이 방법은 조금 더 복잡한 스크립트를 시작하기에 좋은 방법입니다:

    Figure_122

### User Objects As Templates

템플릿 스크립트를 만드는 또 다른 좋은 방법은 원하는 입력, 출력 및 템플릿 스크립트로 하나의 스크립트 컴포넌트를 설정한 다음 이를 Grasshopper 사용자 객체로 저장하는 것입니다. 구성 요소에 추가 메타데이터를 설정하고 아이콘을 사용자 지정할 수 있습니다. 이 사용자 객체의 인스턴스를 배치할 때마다 템플릿 스크립트와 매개변수가 포함된 새 스크립트 컴포넌트 인스턴스를 효과적으로 생성하는 것입니다.

### Resetting Icon

재정의되었거나 부정확하거나 해상도가 낮은 아이콘이 있는 스크립트 컴포넌트가 있는 경우 고급 상황에 맞는 메뉴의 아이콘 재설정 메뉴 버튼(Shift + 오른쪽 클릭)을 사용하여 스크립트 언어의 기본값으로 아이콘을 다시 재설정할 수 있습니다.

<br>

## Shared Scripts

파이썬 스크립트 컴포넌트는 컴포넌트 내부에 포함된 파이썬 스크립트와 함께 가장 일반적으로 사용됩니다. 그러나 여러 스크립트 컴포넌트 간에 단일 스크립트를 공유할 수도 있습니다.

### Input Script

그래스호퍼 패널에서 Python 스크립트(공유 스크립트에는 아직 SDK 모드가 지원되지 않음)를 만들어 여러 스크립트 컴포넌트에 입력으로 전달할 수 있습니다. 스크립트 컴포넌트에는 고급 컨텍스트 메뉴에서 활성화할 수 있는 특수 스크립트 입력 매개변수가 있습니다. 이 입력을 토글하려면 컴포넌트를 Shift + 마우스 오른쪽 버튼으로 클릭하고 스크립트 입력 매개변수("**script**")를 선택합니다:

    Figure_123

### Language Specifier Directive

스크립트가 #! 파이썬 3으로 시작하는 것을 주목하세요. 이를 언어 지정자 지시어라고 합니다. 그 목적은 스크립트 코드 자체에 주석과 알려진 패턴으로 예상되는 언어를 포함시키는 것입니다. 이러한 방식으로 저장된 스크립트에는 파일 확장자가 없으므로 스크립트 컴포넌트가 스크립트를 실행하는 데 사용할 언어를 결정하려면 언어 지정자가 필요합니다. 또는 스크립트 매개변수를 마우스 오른쪽 버튼으로 클릭하고 메뉴에서 언어를 선택할 수도 있지만 모든 입력 스크립트가 선택한 언어여야 합니다. 파이썬 2를 언어로 지정하려면 #! 파이썬 2를 사용합니다.

또한 컴포넌트 아이콘이 일반 스크립트 아이콘으로 변경된다는 점에 유의하세요. 그 이유는 스크립트 입력이 있는 스크립트 컴포넌트는 지원되는 모든 언어를 실행할 수 있기 때문입니다. 두 번째 스크립트의 언어 지정자는 // #! csharp입니다:

    Figure_124

### Output Script

Grasshopper 패널에서 스크립트를 편집하는 것은 그리 편리하지 않습니다. 스크립트 구성 요소에는 고급 상황에 맞는 메뉴에서 활성화할 수 있는 특수 스크립트 출력 매개변수가 있습니다. 이 출력을 토글하려면 컴포넌트를 Shift + 마우스 오른쪽 버튼으로 클릭하고 스크립트 출력 매개변수("**script**")를 선택합니다:

    Figure_125

이러한 방식으로 첫 번째 컴포넌트를 사용하여 스크립트를 생성하고 사용하고, 다른 컴포넌트에 동일한 스크립트를 전달하여 모두 동일한 스크립트를 실행할 수 있습니다. 그리고 위와 같이 다른 언어의 스크립트도 스크립트 입력에 전달할 수 있습니다:

    Figure_126

<br>

## Output Previews

출력 매개변수에는 개별 미리보기 컨트롤이 있습니다. 이 옵션은 기본적으로 켜져 있으며 Grasshopper는 출력 매개변수의 지오메트리 값에 대한 미리보기를 렌더링합니다:

    Figure_127

컴포넌트 컨텍스트 메뉴의 미리보기 메뉴를 사용하여 출력 매개변수에 대해 이 옵션을 끄고 미리 보기를 숨길 수 있습니다. 구가 미리 보기 상태인 동안에는 상자 미리 보기가 표시되지 않습니다:

    Figure_128

<br>

## Exporting Script

컴포넌트 컨텍스트 메뉴에서 스크립트 내보내기 메뉴 항목을 사용하여 Python 스크립트 컴포넌트에 포함된 스크립트를 저장할 수 있습니다. 저장 대화 상자가 열리면 스크립트를 저장할 파일 이름과 위치를 선택하고 저장을 누릅니다.

## Script Cache

Python 스크립트 컴포넌트는 스크립트를 컴파일하고 캐시하므로 스크립트가 변경되지 않은 경우 더 빠르게 실행할 수 있습니다. 일반적으로 캐시는 스크립트나 매개변수를 변경하면 자동으로 만료됩니다.

그러나 컴포넌트가 새 빌드를 사용하도록 하기 위해 캐시를 수동으로 만료해야 하는 경우도 있습니다. 컴파일 캐시를 만료하려면 컴포넌트 컨텍스트 메뉴에서 캐시 폐기를 선택합니다.
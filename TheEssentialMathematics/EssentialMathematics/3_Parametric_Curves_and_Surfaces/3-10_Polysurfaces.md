## Polysurfaces

폴리서페이스는 두 개 이상의 (트림된) NURBS 서페이스가 서로 결합된 것으로 구성됩니다. 각 서페이스에는 일치할 필요가 없는 고유한 구조, 파라미터화 및 아이소커브 방향이 있습니다. 폴리서페이스는 경계 표현(BRep)을 사용하여 표현됩니다. BRep 구조는 서페이스, 가장자리, 정점을 트리밍 데이터와 서로 다른 부분 간의 연결로 설명합니다. 트림된 서피스도 BRep 데이터 구조를 사용하여 표현됩니다.

![figure70](img\Figure_(70).png) <br>
*Figure (70): Polysurfaces are made out of joined surfaces with common edges aligning perfectly within tolerance.* <br>
*그림 (70): 폴리서페이스는 공차 내에서 완벽하게 정렬된 공통 가장자리를 가진 결합된 서페이스로 만들어집니다.*

BRep은 각 면을 기본 표면( underlying surface ), 주변 3D 가장자리( surrounding 3-D edges ), 정점( vertices ), 파라미터 공간 2D 트림 ( parameter space 2-D trims ) 및 인접한 면 간의 관계( relationship between neighboring faces )로 설명하는 데이터 구조입니다. BRep 개체는 닫혀 있을 때 솔리드라고도 합니다(watertight).

<br>

폴리서페이스의 예는 트림되지 않은 6개의 서페이스를 서로 결합하여 만든 간단한 상자입니다.

![figure71](img\Figure_(71).png) <br>
*Figure (71): Box made out of six untrimmed surfaces joined in one polysurface.* <br>
*그림 (71): 트림되지 않은 6개의 서페이스가 하나의 폴리서페이스에 결합된 상자.*

<br>

다음 예제의 상단 상자와 같이 다듬어진 표면을 사용하여 동일한 상자를 만들 수 있습니다.

![figure72](img\Figure_(72).png) <br>
*Figure (72): Box faces can be trimmed.* <br>
*그림 (72): 상자 면을 다듬을 수 있습니다.*

<br>

다음 예제에서 원통의 윗면과 아랫면은 평면 표면에서 잘라낸 것입니다.

![figure73](img\Figure_(73).png) <br>
*Figure (73) shows the control points of the underlying surfaces.* <br>
*그림 (73)은 기본 서페이스의 제어점을 보여줍니다.*

NURBS 커브와 트림되지 않은 서페이스를 편집하는 것은 직관적이며 제어점을 이동하여 interactively 하게 수행할 수 있다는 것을 확인했습니다. 하지만 트림된 서페이스와 폴리서페이스 편집은 어려울 수 있습니다. 가장 큰 문제는 서로 다른 면의 결합된 가장 자리를 원하는 허용 오차 범위 내에서 유지하는 것입니다. 공통 가장자리를 공유하는 인접 면은 트림할 수 있지만 일반적으로 일치하는 NURBS 구조를 갖지 않으므로 공통 가장자리를 변형하는 방식으로 개체를 수정하면 간격이 발생할 수 있습니다.

![figure74](img\Figure_(74).png) <br>
*Figure (74): Two triangular faces joined in one polysurface but do not have matching joined edge. Moving one corner create a hole.* <br>
*그림 (74): 하나의 폴리서페이스에 두 개의 삼각형 면이 결합되었지만 일치하는 결합 가장자리가 없습니다. 한쪽 모서리를 이동하면 구멍이 생깁니다.*

<br>

또 다른 문제는 일반적으로 특히 트림된 지오메트리를 수정할 때 결과물에 대한 제어력이 떨어진다는 점입니다.

<br>

![figure75](img\Figure_(75).png) <br>
*Figure (75): Once a trimmed surface is created, there is limited control to edit the result.* <br>
*그림 (75): 트림된 서페이스가 생성되면 결과를 편집할 수 있는 제어 기능이 제한됩니다.*

![figure76](img\Figure_(76).png) <br>
*Figure (76): Use cage edit technique in Rhino to edit polysurfaces.* <br>
*그림 (76): Rhino에서 케이지 편집 기법을 사용하여 폴리서페이스 편집하기.*

트림된 서페이스는 트림되지 않은 기본 서페이스와 3D 서페이스 내의 3D 가장자리로 평가되는 2D 트림 커브를 결합하여 파라미터 공간에서 설명합니다.

Trimmed surfaces are described in parameter space using the untrimmed underlying surface combined with the 2-D trim curves that evaluate to the 3-D edges within the 3-D surface.
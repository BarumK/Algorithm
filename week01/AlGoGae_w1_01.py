"""
- 알고리즘이란?
문제에 대한 해결책을 찾기 위한 일련의 연산 절차
문제(problems): 해답(solution)을 찾기 위해 물어보는 질문
    우리는 컴퓨터를 사용해서 문제에 대한 해결책을 찾는다고 가정해야 함.
    -> 컴퓨터가 데이터를 처리해서 문제애 대한 해결책을 찾도록 프로그램을 작성해야 한다는 의미.
    예: N개의 항목으로 구성된 리스트 L에서 x라는 수가 있는가?
    매개변수(parameter): 문제에서 어떤 특정 값이 주어지지 않은 변수(variable), e.g., L, n, x
    입력(input): 매개변수에 특정 값을 지정한 것, e.g., L = [10, 7, 11, 5, 3, 8], n = 6, x = 5
    출력(output): 입력에 대한 해답, e.g., “예”
알고리즘(algorithm): 문제에 어떠한 입력이 주어지더라도 해당 입력을 유한한 시간 내에 출력으로 전환시켜줄 수 있는 일련의 연산 절차
    같은 전략을 택하면 계산 절차(알고리즘)가 매우 유사해진다.
    본 강의에서는 이 전략에 초점을 둠.
    예: 선형검색(linear search)

- 알고리즘의 표기(기술)
한글 또는 영어 등의 자연어(natural language)
    1. Start from the leftmost element of a list L of size n and one by one compare x with each element of L.
    2. If x matches with an element, return “yes”.
    3. If x does not match with any of elements, return “no”.
    -> 프로그램(program)으로 전환하기 용이하지 않으며, 모호한 경우가 많음

C, C++, C#, JAVA 등의 프로그래밍 언어(programming language)
    AlGoGae_w1_02.c 파일 참조
    연산 절차와 표기가 주가 되어야 하는데, 이렇게 할 경우 언어의 문법같은 것들이 주가 되어버려 연산 절차에 대한 신경이 적어지게 됨.
    ->프로그램이므로 직접 실행 가능(executable)하지만 가독성(readability)이 떨어짐

의사코드(pseudocode): 프로그래밍 언어와 유사하게 연산 과정을 표현할 수 있는 언어
    Algorithm 1 Linear Search
    Parameter(Input) a list L, the number n of items in L, a number of x
    Output "yes" if x is in L and "No" if it is not.
    Procedure
    1: for each item i in L do
    2:  if i == x then
    3:      return "yes"
    4:  end if
    5: end for
    6: return "no"
    End of Procedure
    가독성이 뛰어나며 프로그래밍 언어로 옮기기 편리함. 작성의 규칙이 따로 존재하지 않으며 사람마다 다 다름.
    자연어에 가깝게 하는 사람도 있으며, 프로그래밍 언어에 가깝게 하는 사람도 존재한다.
    개인의 규칙을 만드는 것을 추천함.
    -> 컴퓨터에서 직접 실행이 불가능하지만 가독성이 좋음

Python(본 강의에서는 Python으로 알고리즘을 표기)
    AlGoGae_w1_03.py 파일 참조
    -> 프로그램이므로 컴퓨터에서 직접 실행 가능하며 가독성이 좋음

- 알고리즘 학습의 목표
우리는 컴퓨터 상에서 프로그램을 실행함으로써 문제를 해결(문제의 입력을 유한한 시간 내에 출력으로 변환)한다고 가정
프로그램의 작성 과정
          설계            분석          예
    문제 ------> 알고리즘 ------> 만족? -----> 프로그램
                   ^             |
                   |             | 아니오
                   ---------------
                        재설계
    설계: 특정 전략에 따라 설계를 하면 편함.
    분석: 성능이 좋은지 등을 따져본다.
본 과목의 목표
    (1) 알고리즘을 설계하는 대표적인 전략을 학습하고
    (2) 각 전략을 여러 기존 문제에 적용시키는 학습을 통해서, 새로운 문제가 주어졌을 때 그 문제를 해결하기 위해
        가장 적합한 알고리즘 설계 전략을 선택하여 알고리즘을 설계할 수 있도록 함
            (‘적합한’이란 설계한 알고리즘이 "정확성"과 "효율성"을 보장할 수 있어야 한다는 의미)
            (정확성 >>> 효율성이다. 정확성이 더욱 중요하다. 빨라봤자 오답이면 말짱 도루묵.)
    알고리즘의 효율성은 (시간·공간) 계산 복잡도(computational complexity)로 분석(analysis)하는 것이 일반적임. 이 강의는 사간 복잡도에 초점.
    따라서 알고리즘의 계산 복잡도를 구하는 방법을 학습함으로써 새로운 문제를 해결하기 위해 설계한 알고리즘의 효율성을 분석할 수 있도록 함
"""
# 1주차
## 기본 미션 : p.63 3~5번 실행결과 쓰고 인증샷
#### p.63 : 문제 3
![문제3 결과](./63페이지%20문제3.png)

#### p.63 : 문제 4
![문제4 결과](./63페이지%20문제4.png)

#### p.63 : 문제 5
![문제5 결과](./63페이지%20문제5.png)


## 선택 미션 : 모르는 용어(3~5개) 찾아 혼공 용어 노트에 정리하고 인증샷
1. 이진 코드
   1. 이진 코드 = 바이너리 코드
      * 컴퓨터가 인식할 수 있는 0과 1로 구성된 이진수로 이루어진 코드
   2. 바이트 코드
      * CPU가 이해할 수 있는 언어가 바이너리 코드, 바이트 코드는 VM이 이해 할 수 있는 언어입니다.
      * 어떠한 플랫폼에 종속된 것이 아닌 가상 머신이 실행할 수 있는 기계어 코드입니다.
      * 중간 코드로 컴파일한 것을 말합니다.
      * JAVA의 가상 머신을 JVM이라고 하며, JVM을 위한 바이트 코드를 "자바 바이트 코드"라고 합니다.
2. 이스케이프 문자
   * 어떤 부호 또는 언어로부터 이탈하는 것을 뜻합니다.
   * 파이썬에서는 특수 문자로 문자열에서 사용되며, 일반적인 문자가 아닌 특수 문자들로 문자열에서 일반적인 출력이 아닌 특수한 기능을 합니다.
   * 예시

        |표현|한국어이름|
        |---|---|
        | \b | 백스페이스 |
        | \t | 탭 |
        | \n | 라인피드, 줄바꿈 |
        | \\ | 역슬레시 출력 |    
        | \' | 작은 따옴표 출력 |
        | \" | 큰 따옴표 출력 |
    
3. 파이썬 인터프리터
   * 인터프리터?
     * 프로그래밍 소스 코드를 곧바로 실행해주는 프로그램.
     * 한 번에 코드 한 줄씩 읽어 실행.
     * 파이썬 코드를 실행할 수 있는 도구는 파이썬 인터프리터.
   * 컴파일러
     * 컴파일러는 고급 언어로 작성된 프로그램 전체를 목적 프로그램으로 번역한 후, 링킹 작업을 통해 컴퓨터에서 실행 가능한 실행 프로그램을 생성합니다.
     * 번역 실행 과정을 거쳐야 하기 때문에 번역 과정이 번거롭고 번역 시간이 오래 걸리지만, 한번 번역한 후에는 번역하지 않으므로 실행 속도가 빠릅니다.
     * 대표적인 컴파일러를 사용하는 언어에는 C언어 Java 등이 있습니다.
4. 파이썬 인터렉티브 셸
   * 컴퓨터와 상호 작용하는 공간이라는 의미로 "인터렉티브 셸"이라고 부릅니다.
   * 인터렉티브 셸?
     * 코드 한 줄 넣고 바로 결과 확인할 수 있습니다.
   * interactive?
     * 사람들로부터 입력을 받는 것을 말합니다.
     * 사용자와 컴퓨터가 출력한 내용에 따라 사용자가 적절한 입력을 하는 식으로, 입력과 출력이 공존하는 프로그램을 뜻 합니다.
5. 리터럴
   * 자료를 리터럴(literal)이라고 합니다. 
   * 리터럴은 데이터(값) 그 자체를 뜻합니다. 변수에 넣는 변하지 않는 데이터를 의미하는 것입니다.
     * 예시
        ``` c
        a = 1
        ```
     * a는 상수이고, 1은 리터럴이다.

#### 참조 자료
* [UsefulToKnow - 바이너리와 바이트 코드란?(+ 기계어란?)](https://usefultoknow.tistory.com/entry/%EB%B0%94%EC%9D%B4%EB%84%88%EB%A6%AC%EC%99%80-%EB%B0%94%EC%9D%B4%ED%8A%B8-%EC%BD%94%EB%93%9C%EB%9E%80-%EA%B8%B0%EA%B3%84%EC%96%B4%EB%9E%80)
* [제타위키 - 이스케이프 문자](https://zetawiki.com/wiki/%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84_%EB%AC%B8%EC%9E%90)
* [코딩팩토리 - [Language]컴파일러와 인터프리터란 무엇인가?](https://coding-factory.tistory.com/303)
* [텀즈 - 인터랙티브](http://www.terms.co.kr/interactive.htm)
* [혼공 - 파이썬을 실습하는 두 가지 방법 - 인터렉티브 셸 VS 텍스트 에디터](https://hongong.hanbit.co.kr/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A4%EC%8A%B5-%EB%B0%A9%EB%B2%95-%EC%9D%B8%ED%84%B0%EB%A0%89%ED%8B%B0%EB%B8%8C%EC%85%B8-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%97%90%EB%94%94%ED%84%B0/)
* [velog - JY.log - 리터럴(Literal)이란?](https://velog.io/@pjeeyoung/%EB%A6%AC%ED%84%B0%EB%9F%B4)

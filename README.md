# Mulcam B Algo Study

### :pencil: Rule

- 스터디 시간: 매일 아침 8시 30분
- 일주일 중 6일 알고리즘 / SQL 문제풀고 올리기 (문제난이도 및 소요 시간이 따라 1 ~ 3문제)
- 알고리즘 문제사이트 : [SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6) -> swea, [백준](https://www.acmicpc.net/workbook/top) -> bj 
- SQL 문제사이트 : [프로그래머스](https://programmers.co.kr/learn/challenges) -> prog, [HackerRank](https://www.hackerrank.com/domains/sql)-> hack

#### 1. 최초 클론 방법 (VSCode 활용 가정)

1. VSCode 탐색기에서 내가 사용할 폴더(빈 폴더여야 한다)에 오른쪽 버튼 통합터미널 열기를 누른다 -> 사용할 폴더 경로로 터미널이 열린다.
<img src="https://user-images.githubusercontent.com/67591105/157668642-71972ab7-273b-4b76-90ca-431a6e62c6b6.png" width="600" height="400"/>

2. 명령창에 아래와 같이 입력하고 클론한다. 
```
git clone https://github.com/BBstudyFighting/algorithm.git .
```

3. 아래 규칙에 따라 파일을 생성하고 push 한다

### Push 규칙

#### 1. 파일생성 규칙

1. 매주 새 폴더를 만듭니다. (ex. 01주차, 02주차 ... 10주차...)
2. 본인 이름의 폴더와 문제사이트 폴더를 또 만듭니다. (ex. jisu/swea, jisu/sql.. )
-> 문제를 풀고 n주차/이름/문제사이트 폴더 안에 문제명.py 이런 식으로 올려주시면 됩니다.  

e.g)  - 알고리즘 파일은 n주차/jisu/swea/4834_색칠하기.py   
      - SQL 파일은 n주차/jisu/prog/select.sql 과 같이 추가  


#### 2. 파일 push 방법

-> pull부터 합니다.
-> pull했는데 해당 주차의 디렉터리가 안보이면 따로 만들어 주세요.  
```
git pull origin main
```

-> 파일을 추가, 커밋, 푸시한다
```
$ git add .
```
```
$ git commit -m "홍길동_문제이름(algo 혹은 sql)"
```
```
$ git push origin main
```

> push할 때 conflict 생길 경우 pull 한번 해주고 다시 하면 됩니다.

#### 일단 이렇게 정리해 봤습니다,, 보완할 부분 있으면 자유롭게 수정해주세요! :smile:

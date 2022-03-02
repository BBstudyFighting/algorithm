# Mulcam B Algo Study

### :pencil: Rule  
- 스터디 시간: 매일 아침 8시 30분  
- 일주일 동안 알고리즘 6문제 / SQL 18 문제 풀기    
- [Algo - SWEA](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)
- [SQL - Progrmmers](https://programmers.co.kr/learn/challenges) 

### :apple: How to Contribute   
1. 매주 새 디렉터리를 만듭니다. (ex. 01주차, 02주차 ... 10주차...)
2. 디렉터리에 본인 이름으로 디렉터리를 또 만듭니다. (ex. jisu, yoonju, eunwon)
3. 이름 디렉터리에 각자 푼 문제를 추가합니다.

#### 1. 파일 생성/업로드 규칙   
알고리즘 파일은 n주차/jisu/swea_1000.py 와 같이 푼 문제를 표시해서 추가합니다.  
SQL 파일은 n주차/jisu/prog_select.md 로 업로드  
(swea, bj, prog 등은 문제사이트,  1000, select는 문제번호 or 문제주제)

#### 2. Push 규칙  
-> pull부터 합니다.  
```
$ git pull <remote 이름> master
```
-> pull했는데 해당 주차의 디렉터리가 안보이면 따로 만들어 주세요.  
-> n주차/algo/swea_list1,2_홍길동.py
-> n주차/sql/prog_select_홍길동.sql 형식에 맞게 저장 후 commit&push 해주세요.
```
$ git add .
$ git commit -m "swea_list1,2_홍길동"
$ git push <remote 이름> master
```

> push할 때 conflict 생길 경우 pull 한번 해주고 다시 하면 됩니다.


### :banana: How to Code Review   
#### 1. Commit History로 리뷰하는 방법 
다른 사람이 커밋한 데다가 댓글 다는 방식 =>
[예시](https://github.com/ohgyun/using-github-for-code-reviews/commit/8a85b15805237214aea83a1131f0548b3b69a2d8)    

#### 2. Pull Request로 리뷰하는 방법   
- [fork해서 Pull Request 보내는 법](https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/)  
- [fork된 레포지토리 최신상태 유지하는 법](https://jybaek.tistory.com/775)   
-------

1) 새로운 branch를 하나 만듭니다.  
2) 새로 만든 branch에 코드를 push합니다.  
3) push 완료 후 GitHub branch 페이지에 들어오면 Pull Request(PR)할건지 버튼이 생깁니다. 클릭!
4) 코드 리뷰 받고 <b>스터디 시간 전에 merge</b>하면 됩니다. (merge 후 branch는 삭제해도 됩니다.)
리뷰는 오픈된 PR에 하면 됩니당.   
   
#### 일단 이렇게 정리해 봤습니다,, 보완할 부분 있으면 자유롭게 수정해주세요! :smile:

# 출처 : https://techblog-history-younghunjo1.tistory.com/175
-- Write a query to find the node type ofBinary Treeordered by the value of the node. Output one of the following for each node(각 노드가 어떤 노드를 가리키는지 문자열로 명시하고 출력 결과를 노드의 값 기준으로 오름차순하여 정렬해라. 이 때 루트노드라면 Root를, 가장 마지막의 노드들이라면 Leaf를, Root 노드를 제외한 나머지 부모노드들은 Inner를 출력해라.)

-- 특정 조건에 맞는 값에 따라 문자열을 출력해주어야 하므로 CASE WHEN 또는 IF 문을 사용할 수 있을 것 이다.
-- 우선 문제 원본에서 예시 I/O으로 주어진 데이터들로 이진트리 구조를 만들어 그려보자.
-- N은 자식노드 P는 부모노드를 가리키므로 이 두개가 동일하도록 하면서 INNER JOIN을 시켜보자.

SELECT N,
       CASE WHEN N IN (SELECT DISTINCT b2.N
                       FROM BST b1
                        INNER JOIN BST b2 ON b1.P = b2.N
                       WHERE b2.P IS NULL) THEN 'Root'
            WHEN N IN (SELECT DISTINCT b2.N
                       FROM BST b1
                        INNER JOIN BST b2 ON b1.P = b2.N
                       WHERE b2.P IS NOT NULL) THEN 'Inner'
            ELSE 'Leaf'
            END
FROM BST
ORDER BY N
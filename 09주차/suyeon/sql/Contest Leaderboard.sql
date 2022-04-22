'''
You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  0 from your result.

한 명 hacker의 total score란, 그 hacker가 푼 모든 문제들에 대한 score의 최댓값의 합을 의미한다. 이 때 hacker_id, name, total_score를 출력하는데 1차적인 정렬 기준은 total_score를 내림차순으로, 2차적인 정렬 기준은 hacker_id 오름차순으로 정렬해라. 단, 결과값에서 total score가 0인 데이터들은 제외시켜라.
'''
SELECT H.hacker_id, H.name, sub2.total_score
FROM (SELECT sub.hacker_id, SUM(max_score) AS total_score
      FROM (SELECT hacker_id, challenge_id, MAX(score) AS max_score
            FROM Submissions 
            GROUP BY hacker_id, challenge_id) sub
      GROUP BY sub.hacker_id
      HAVING total_score != 0) sub2
 INNER JOIN Hackers H ON sub2.hacker_id = H.hacker_id
ORDER BY sub2.total_score DESC, H.hacker_id
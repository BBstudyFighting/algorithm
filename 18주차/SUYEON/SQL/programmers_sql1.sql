#  조건에 맞는 도서 리스트 출력하기
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE;

SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE 
FROM BOOK
WHERE CATEGORY = '인문' AND PUBLISHED_DATE LIKE '%2021%';

SELECT book_id, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book
where category = '인문' and date_format(PUBLISHED_DATE, '%Y') = '2021'
order by PUBLISHED_DATE asc
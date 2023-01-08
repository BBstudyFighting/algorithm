# 카테고리 별 도서 판매량 집계하기
select a.category, sum(b.sales) as total_sales
from book a
join book_sales b on a.book_id = b.book_id
where date_format(b.sales_date, '%Y-%m') = '2022-01'
group by a.category
order by 1;

SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
LEFT JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE MONTH(S.SALES_DATE) = 1
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC
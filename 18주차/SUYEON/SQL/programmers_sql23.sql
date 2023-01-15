# 저자 별 카테고리 별 매출액 집계하기
SELECT B.AUTHOR_ID,B.AUTHOR_NAME,A.CATEGORY,SUM(C.SALES * A.PRICE) AS TOTAL_SALES 
FROM BOOK A, AUTHOR B, BOOK_SALES C 
WHERE A.BOOK_ID = C.BOOK_ID AND A.AUTHOR_ID = B.AUTHOR_ID AND C.SALES_DATE LIKE '2022-01%' 
GROUP BY B.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY 
ORDER BY B.AUTHOR_ID ASC, A.CATEGORY DESC

SELECT book.author_id, author.author_name, book.category, SUM(book.price * sales.sales)
FROM book_sales AS sales
LEFT JOIN book ON sales.book_id = book.book_id
LEFT JOIN author ON book.author_id = author.author_id
WHERE sales.sales_date LIKE '2022-01%'
GROUP BY book.author_id, book.category
ORDER BY book.author_id, book.category DESC
# 재구매가 일어난 상품과 회원 리스트 구하기
SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(online_sale_id) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

select
    user_id, product_id
    # , count(*)
from online_sale
group by user_id, product_id
having count(*) >= 2
order by 1 asc, 2 desc

SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID,PRODUCT_ID
HAVING COUNT(*)>=2
ORDER BY USER_ID,PRODUCT_ID DESC;
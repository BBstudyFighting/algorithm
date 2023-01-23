# 그룹별 조건에 맞는 식당 목록 출력하기
SELECT PRO.MEMBER_NAME, REV.REVIEW_TEXT, DATE_FORMAT(REV.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE 
FROM MEMBER_PROFILE PRO
JOIN REST_REVIEW REV ON REV.MEMBER_ID = PRO.MEMBER_ID
WHERE PRO.MEMBER_NAME = (SELECT PROF.MEMBER_NAME 
                         FROM MEMBER_PROFILE PROF
                         JOIN REST_REVIEW REST ON REST.MEMBER_ID = PROF.MEMBER_ID
                         GROUP BY MEMBER_NAME
                         ORDER BY COUNT(MEMBER_NAME) DESC
                         LIMIT 1)
ORDER BY REV.REVIEW_DATE, REV.REVIEW_TEXT
--------------------------------------------------------------------------------
select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from rest_review
inner join (
    select member_id as join1_member_id, count(*) as count
    from rest_review
    group by member_id
    order by count desc
    limit 1
) join1 on rest_review.member_id = join1.join1_member_id
inner join (
    select member_id as join2_member_id, member_name
    from member_profile
) join2 on rest_review.member_id = join2.join2_member_id
order by review_date asc, review_text asc
--------------------------------------------------------------------------------
-- group by 회원 count 찾기
-- max값 찾기
-- max 회원 찾기
-- 회원의 이름, 리뷰, 날짜 찾기
 -------- max 회원의 이름, 리뷰, 날짜 찾기

select x.MEMBER_NAME, y.REVIEW_TEXT, date_format(y.REVIEW_DATE, "%Y-%m-%d") review_date
from member_profile x inner join rest_review y
on x.member_id = y.member_id
where (y.member_id) in 
    -- ------------------ max 회원 찾기
    (select member_id
    from rest_review
    group by member_id
    having count(member_id) =
        -- -------------------- max 찾기
        (select max(cnt)
        from (
        select count(member_id) cnt
        from rest_review
        group by member_id) a
        )
        -- --------------------
    )
    -- ------------------
order by review_date
-- --------
;
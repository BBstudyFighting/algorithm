-- Type of Triangle
-- 각 변 A B C 길이에 따라 삼각형의 종류 판별

SELECT 
CASE -- 조건에 따라 값을 정하는 CASE 함수 
    WHEN A = B AND B = C THEN "Equilateral"
    WHEN A + B <= C THEN "Not A Triangle"
    WHEN A != B AND B != C AND A != C THEN "Scalene"
    ELSE "Isosceles"
END AS A
FROM TRIANGLES;
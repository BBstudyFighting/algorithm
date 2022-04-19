"""
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
Output one of the following statements for each record in the table:
세개 변의 길이들을 이용해서 TRIANGLES테이블의 각 레코드에서 타입을 알아내는 쿼리를 써라.
Equilateral: It's a triangle with  3sides of equal length. / 세 변의 길이가 모두 같은 삼각형 - Equilateral
Isosceles: It's a triangle with  2sides of equal length. / 두 변의 길이가 같은 삼각형 - Isosceles
Scalene: It's a triangle with  3sides of differing lengths. / 세 변의 길이가 모두 다른 삼각형 - Scalene
Not A Triangle: The given values of A, B, and C don't form a triangle. / 주어진 3개변의 길이로 삼각형이 형성되지 않는 경우 - Not A Triangle
"""
SELECT 
    CASE # CASE - WHEN - THEN - ELSE - END 로 구성
    WHEN A = B AND B = C AND A= C THEN 'Equilateral' # 정삼각형
    WHEN A+B <= C OR A+C <= B OR B+C <= A THEN 'Not A Triangle' #삼각형이 아님
    WHEN A = B OR B = C OR A = C THEN 'Isosceles' #이등변 삼각형
    ELSE 'Scalene' # 3변의 길이가 다른 삼각형
END 
FROM TRIANGLES 

SELECT 
CASE
    WHEN A = B AND B = C THEN "Equilateral"
    WHEN A + B <= C THEN "Not A Triangle"
    WHEN A != B AND B != C AND A != C THEN "Scalene"
    ELSE "Isosceles"
END 
FROM TRIANGLES
"""
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  3sides of equal length.
Isosceles: It's a triangle with  2sides of equal length.
Scalene: It's a triangle with  3sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
"""
SELECT CASE WHEN A = B AND B = C AND A = C THEN 'Equilateral'
            WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
            WHEN A = B OR B = C OR A = C THEN 'Isosceles'
            WHEN A != B AND B != C AND A != C THEN 'Scalene'
       END AS type
FROM TRIANGLES
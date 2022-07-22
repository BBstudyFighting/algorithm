-- SET은 어떤 변수에 특정 값을 할당할때 쓰는 명령어
-- SET 사용시 대입 연산자를 '='를 사용하고 그 외에는 := 를 사용
SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR,  # := 기호는 대입해주다는 뜻
    (SELECT COUNT(HOUR(DATETIME)) 
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR < 23;

###############################################

SET @HOUR := -1; # 변수선언
SELECT (@HOUR := @HOUR +1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR < 23
-- group by 를 사용해서 몇마리 이니까 count를 사용해서
-- select 범주별로 세어주고 싶은 필드명, count(*) from 테이블명
-- group by 범주별로 세어주고 싶은 필드명;


SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) 
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE
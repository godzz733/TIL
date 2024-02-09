SELECT C.CAR_ID FROM CAR_RENTAL_COMPANY_CAR AS C 
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE LIKE '%세단%'
AND H.START_DATE LIKE '____-10%'
GROUP BY C.CAR_ID
ORDER BY C.CAR_ID DESC;


-- Distinct
SELECT DISTINCT(A.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR AS A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = '세단'
    AND MONTH(START_DATE) = 10
ORDER BY CAR_ID DESC

-- subquery

SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = '세단'
AND CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) = 10
)
ORDER BY CAR_ID DESC

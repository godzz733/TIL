SELECT COUNT(I.FISH_TYPE) AS FISH_COUNT,N.FISH_NAME
FROM FISH_INFO AS I
INNER JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY N.FISH_NAME, N.FISH_TYPE
ORDER BY FISH_COUNT DESC;
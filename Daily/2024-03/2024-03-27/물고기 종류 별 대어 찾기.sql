SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I
INNER JOIN FISH_NAME_INFO N
ON I.FISH_TYPE = N.FISH_TYPE
WHERE (N.FISH_NAME,I.LENGTH) IN (
            SELECT N.FISH_NAME, MAX(I.LENGTH)
                FROM FISH_INFO I
                INNER JOIN FISH_NAME_INFO N
                ON I.FISH_TYPE = N.FISH_TYPE
                GROUP BY N.FISH_NAME
)
ORDER BY I.ID;
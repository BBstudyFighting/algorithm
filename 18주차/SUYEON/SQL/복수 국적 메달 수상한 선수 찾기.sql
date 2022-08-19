SELECT distinct at.name
FROM records re
     LEFT JOIN athletes at ON re.athlete_id = at.id
     LEFT JOIN teams te ON re.team_id = te.id
     LEFT JOIN games ga ON re.game_id = ga.id
WHERE re.medal IS NOT null AND ga.year >= 2000
GROUP BY at.id
HAVING COUNT(distinct te.team) > 1
ORDER BY at.name
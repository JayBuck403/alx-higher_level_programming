--Displays maximum temperature of each state by State name
SELECT `state`, MAX(value) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

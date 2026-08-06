SELECT a.name, 
cast((((b.math * 2)+(b.specific * 3)+(b.project_plan*5))/10)AS NUMERIC(15,2)) as avg
FROM score as b JOIN candidate as a ON (a.id = b.candidate_id) ORDER BY avg DESC;
SELECT CAST('Approved: ' AS VARCHAR) || name, grade FROM students
WHERE grade >= 7 ORDER BY grade DESC;
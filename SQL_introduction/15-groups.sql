-- computes the score average of all records in the table second_table
SELECT score, COUNT(*) as `name`
FROM second_table
GROUP BY score
ORDER BY score DESC;

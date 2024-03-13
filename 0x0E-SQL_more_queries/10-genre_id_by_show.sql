-- lists all cities contained in the database hbtn_0d_usa.
SELECT a.id 
FROM cities a 
INNER JOIN states b 
ON a.state_id = b.id
ORDER BY a.id ASC;

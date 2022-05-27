/* 
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your T-SQL query statement below
 */
Delete  Person 
where 
id not in 
(SELECT 
      MIN(P.id) 
    FROM 
      Person P 
    GROUP BY 
      P.email );
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      # select salary from (select *,Row_number() OVER( order by salary desc ) as rank_n from (select distinct salary from Employee)e)t where  rank_n=N limit 1
       select salary from (select *,DENSE_RANK() OVER( order by salary desc ) as rank_n from  Employee)t where  rank_n=N limit 1
  );
END
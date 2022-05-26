# Write your MySQL query statement below
select Department.name as Department,a.name as Employee,a.salary as Salary from (
select *,RANK() over (partition by departmentId  order by salary DESC) as ranks from Employee )  a
join Department  on a.departmentId=Department.id and a.ranks =1

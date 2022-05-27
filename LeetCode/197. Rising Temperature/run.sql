# Write your MySQL query statement below
select id from (
    select t1.temperature, t1.id, t2.temperature as temperature2 from Weather t1 join Weather t2 on t1.recordDate=DATE_ADD(t2.recordDate, INTERVAL 1 DAY)
)
a  where temperature > temperature2

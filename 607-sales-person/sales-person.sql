# Write your MySQL query statement below
select name from SalesPerson 
where sales_id not in (
    select distinct t1.sales_id
    from Orders as t1
    join Company as t2 on 
    t1.com_id=t2.com_id 
    where t2.name="RED"
)
;
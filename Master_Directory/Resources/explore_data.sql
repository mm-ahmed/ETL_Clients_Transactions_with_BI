-- TEST 1:
-- select count(1) as rec_cnt from clients
-- union
-- select count(1) as rec_cnt from payments;

-- TEST 2:
-- select avg(payment_amt) from clients where entity_type like '%sole%'
-- select * from payments limit 10;

-- TEST 3:
-- select client_id, count(1) from payments group by client_id;
-- select client_id, count(1) from clients group by client_id having count(client_id) > 1;

--TEST 4:
-- select  *
-- from    clients
-- where   entity_type is null
--     or entity_year_established is null
-- limit 10;

-- select  *
-- from    payments
-- where   contract_id is null
--     or  transaction_date is null
--     or  payment_amt is null
--     or  payment_code is null
-- limit 10;

-- select client_id, count(transaction_id), sum(payment_amt) from payments where client_id = 1132 group by client_id;

-- select distinct a.client_id from clients a join payments b on a.client_id = b.client_id limit 1500; -- where  a.client_id = 3;

-- select avg(payment_amt) from clients a join payments b on a.client_id = b.client_id where entity_type like '%sole trader%' and entity_year_established = 2017;

-- select count(distinct client_id) from payments limit 1500;

-- select min(payment_amt) from payments;
-- select max(payment_amt) from payments;

-- select count(1) from clients where entity_type = ''

-- with cte as (
-- SELECT payment_amt, cast(strftime("%m", DATE(transaction_date, 'unixepoch')) as int) as month from payments
-- )
-- select month, sum(payment_amt) / 100.0 from cte
-- where month in (6,7)
-- group by month

-- select sum(payment_amt)/100.0 from payments where client_id = 11;
-- select count(transaction_id) from payments where client_id = 11;
-- select * from clients where client_id = 11;
-- select * from payments where client_id = 11;

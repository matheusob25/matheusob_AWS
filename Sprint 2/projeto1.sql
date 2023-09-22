-- projeto 1 SQL
-- 1º query
with leads as
	(
	select 
	   date_trunc('month',visit_page_date)::date as visit_page_month,
	   count(*) as visit_page_count

	from sales.funnel 
	group by visit_page_month
	order by visit_page_month
	),
	payments as
	(
	select 
		  date_trunc('month', fu.paid_date)::date as paid_month,
		  count(fu.paid_date) as paid_count,
		  sum(pr.price * (1 + fu.discount)) as receita
	from sales.funnel as fu 
	left join sales.products as pr
	on fu.product_id = pr.product_id
	where fu.paid_date is not null
	group by paid_month
	order by paid_month 
	)


select
	  l.visit_page_month as "mês",
	  l.visit_page_count as leads,
	  pa.paid_count as "vendas",
	  (pa.receita/1000) as "receita (k,R$)",
	  (pa.paid_count::float / l.visit_page_count::float) as "conversão(%)",
	  (pa.receita / pa.paid_count/1000  ) as "ticket médio"

from leads as l
left join payments as pa
on l.visit_page_month = pa.paid_month


--2º query

select
	  'Brazil' as país,
	  c.state as estado,
	  count(f.paid_date) as vendas

from sales.funnel as f
left join sales.customers as c
on f.customer_id = c.customer_id
where paid_date between '2021-08-01' and '2021-08-31'
group by país,estado
order by vendas desc
limit 5

-- 3º query


select 
	 p.brand as marca,
	 count(f.paid_date) as vendas

from sales.funnel as f
left join sales.products as p
on f.product_id = p.product_id
where paid_date between '2021-08-01' and '2021-08-31' 
group by marca 
order by vendas desc
limit 5


-- Query 4

select
	sto.store_name as loja,
	count(fun.paid_date) as "vendas (#)"

from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
where paid_date between '2021-08-01' and '2021-08-31'
group by loja
order by "vendas (#)" desc
limit 5


-- Query 5

select
	extract('dow' from visit_page_date) as dia_semana,
	case 
		when extract('dow' from visit_page_date)=0 then 'domingo'
		when extract('dow' from visit_page_date)=1 then 'segunda'
		when extract('dow' from visit_page_date)=2 then 'terça'
		when extract('dow' from visit_page_date)=3 then 'quarta'
		when extract('dow' from visit_page_date)=4 then 'quinta'
		when extract('dow' from visit_page_date)=5 then 'sexta'
		when extract('dow' from visit_page_date)=6 then 'sábado'
		else null end as "dia da semana",
	count(*) as "visitas (#)"

from sales.funnel
where visit_page_date between '2021-08-01' and '2021-08-31'
group by dia_semana
order by dia_semana








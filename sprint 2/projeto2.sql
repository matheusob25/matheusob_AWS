-- projeto 2 
-- 1º query

select case when i.gender = 'male' then 'homens'
			when i.gender = 'female' then 'mulheres'
		end as genero,
		count(*) as leads
from sales.customers as c left join 
temp_tables.ibge_genders as i
on lower(c.first_name) = lower(i.first_name)
group by genero
order by leads

-- 2º query

select 
	  case when  professional_status = 'freelancer' then 'freelancer'
		   when professional_status =	 'retired' then 'aposentado'
		   when professional_status =	 'clt' then 'clt'
           when professional_status = 'self_employed' then 'autônomo'
		   when professional_status =	'other' then 'outro'
		   when professional_status =	'businessman' then 'empresário(a)'
		   when professional_status =	'civil_servant' then 'funcionário(a) público(a)'
		   when professional_status =	'student' then 'estudante'
		   end as "status profissional",
		   (count (*):: float) / (select count(*) from sales.customers) as "leads em porcentagem"
		   
from sales.customers
group by professional_status
order by "leads em porcentagem"


-- 3º query

select case when date_diff('y', birth_date, current_date) < 20 then '0-19'
			when date_diff('y', birth_date, current_date) < 40 then '20-39'
			when date_diff('y', birth_date, current_date) < 60 then '40-59'
			when date_diff('y', birth_date, current_date) < 80 then '60-79'
			else '80+'
			end as faixa_etaria,
		count(*)::float / (select count(*) from sales.customers) as leads
		
from sales.customers 
group by faixa_etaria
order by faixa_etaria

-- 4º query


select case 
			when income < 5000 then '0-5000'
			when income < 10000 then '5000-10000'
			when income < 15000 then '10000-15000'
			when income < 20000 then '15000-20000'
			else '20000+' end as faixa_salarial,
		count(*)::float / (select count(*) from sales.customers) as leads,
		case
			when income < 5000 then 1
			when income < 10000 then 2
			when income < 15000 then 3
			when income < 20000 then 4
			else 5 end as ordem	
		
from sales.customers 
group by faixa_salarial,ordem
order by ordem

-- 5º query


with classificacao_veiculos as 
(

	select
		f.visit_page_date,
		p.model_year,
		extract('year' from visit_page_date) - p.model_year::int as idade_veiculo,
		case 
			when (extract('year' from visit_page_date) - p.model_year::int) <= 2 then 'novo'
			else 'seminovo'
			end as classificacao_veiculo
	from sales.funnel as f
	left join sales.products as p
	on f.product_id = p.product_id

)
select 
	classificacao_veiculo,
	count(*) as  "veículos visitados"
from classificacao_veiculos
group by "classificacao_veiculo"


-- 6º query

with faixa_idade_veiculo as 
(

	select
		f.visit_page_date,
		p.model_year,
		extract('year' from visit_page_date) - p.model_year::int as idade_veiculo,
		case 
			when (extract('year' from visit_page_date) - p.model_year::int) <= 2 then 'até 2 anos'
			when (extract('year' from visit_page_date) - p.model_year::int) <= 4 then '2 a 4 anos'
			when (extract('year' from visit_page_date) - p.model_year::int) <= 6 then '4 a 6 anos'
			when (extract('year' from visit_page_date) - p.model_year::int) <= 8 then '6 a 8 anos'
			when (extract('year' from visit_page_date) - p.model_year::int) <= 10 then '8 a 10 anos'
			else 'mais de 10 anos '
			end as "idade do veiculo",
		case 
			when (extract('year' from visit_page_date) - p.model_year::int) <= 2 then 1
			when (extract('year' from visit_page_date) - p.model_year::int) <= 4 then 2
			when (extract('year' from visit_page_date) - p.model_year::int) <= 6 then 3
			when (extract('year' from visit_page_date) - p.model_year::int) <= 8 then 4
			when (extract('year' from visit_page_date) - p.model_year::int) <= 10 then 5
			else 6 
			end as ordem
	from sales.funnel as f
	left join sales.products as p
	on f.product_id = p.product_id

)
select 
	"idade do veiculo",
	count(*)::float / (select count(*) from sales.funnel) as porcentagem,
	ordem
from faixa_idade_veiculo
group by "idade do veiculo", ordem
order by ordem


-- 7º query

select
	p.brand,
	p.model,
	count(*) as "visitas (#)"

from sales.funnel as f
left join sales.products as p
on f.product_id = p.product_id
group by p.brand, p.model
order by p.brand, p.model, "visitas (#)"


  

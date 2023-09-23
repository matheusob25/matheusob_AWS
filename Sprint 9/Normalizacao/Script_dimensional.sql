select * from tb_locacao tl 
-- criando dimensões
create view dim_cliente as 
select DISTINCT  tl.idCliente, tl.nomeCliente, tl.cidadeCliente, tl.estadoCliente, tl.paisCliente 
from tb_locacao tl 

select * from dim_cliente 

create view dim_carro as 
select tl.idCarro, tl.kmCarro, tl.classiCarro, tl.marcaCarro,  tl.modeloCarro, tl.modeloCarro, tl.anoCarro, tl.idcombustivel, tl.tipoCombustivel  
from tb_locacao tl 

select * from dim_carro 

create view dim_vendedor as
select tl.idVendedor, tl.nomeVendedor, tl.sexoVendedor, tl.estadoVendedor
from tb_locacao tl 

create view dim_data as 
select tl.idLocacao as  idData ,tl.dataLocacao, tl.horaLocacao, tl.dataEntrega, tl.horaEntrega 
from tb_locacao tl 


select * from dim_data

-- criando fato 
create view fato_locacao as 
select tl.idLocacao, tl.qtdDiaria, tl.vlrDiaria, tl.idCliente, tl.idCarro, tl.idVendedor, tl.idLocacao as idData 
from tb_locacao tl

select * from fato_locacao 





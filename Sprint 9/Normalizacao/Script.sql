-- criação e inserção tabela cliente
create table tb_cliente(
	idCliente integer primary key not null,
	nomeCliente text,
	cidadeCliente text,
	estadoCliente text,
	paisCliente text
)

insert into tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
select DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente 
from tb_locacao 

select * from tb_cliente

-- criação e inserção tabela vendedor
create table tb_vendedor(
	idVendedor integer primary key NOT NULL,
	nomeVendedor text,
	sexoVendedor text,
	estadoVendedor text
)

insert into tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
select DISTINCT  idVendedor, nomeVendedor, sexoVendedor, estadoVendedor  
from tb_locacao 

select * from tb_vendedor tv  

-- criação e inserção da tabela combustivel

create table tb_combustivel(
	idCombustivel integer primary key NOT NULL,
	tipoCombustivel
)

insert into tb_combustivel (idCombustivel, tipoCombustivel)
select DISTINCT idcombustivel, tipoCombustivel 
from tb_locacao  


select * from tb_combustivel 
				
-- criação e inserção tabela carro

create table tb_carro(
	idCarro integer primary key NOT NULL,
	classiCarro text,
	marcaCarro text, 
	modeloCarro text, 
	anoCarro integer,
	idCombustivel integer,
	foreign key (idCombustivel) references tb_combustivel(idCombustivel)
)

insert into tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select distinct idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel 
from tb_locacao

select * from tb_carro tc 

-- tabela quilometragem que referencia o id do carro como foreign key
create table tb_quilometragem(
	idKms integer primary key autoincrement,
	kmCarro integer,
	idCarro integer,
	foreign key (idCarro) references tb_carro(idCarro)
)

insert into tb_quilometragem(kmCarro, idCarro)
select kmCarro, idCarro
from tb_locacao 

select * from tb_quilometragem

-- tabela principal locacao

create table tbb_locacao(
	idLocacao integer primary key not null,
	dataLocacao datetime,
	horaLocacao time,
	qtdDiaria integer,
	vlrDiaria DECIMAL,
	dataEntrega date,
	horaEntrega time,
	idCliente integer,
	idCarro integer,
	idVendedor integer,
	foreign key (idCliente) references tb_cliente(idCliente),
	foreign key (idCarro) references tb_carro(idCarro),
	foreign key (idVendedor) references tb_vendedor(idVendedor)
)

insert into tbb_locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idVendedor)
select	idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega,idCliente, idCarro, idVendedor
from tb_locacao 


select tl.*, tb_cliente.nomeCliente  
from tbb_locacao tl 
left join tb_cliente 
on tl.idCliente == tb_cliente.idCliente 

select loc.idLocacao, loc.dataLocacao, loc.horaLocacao, loc.dataEntrega, loc.horaEntrega, car.idCarro, car.modeloCarro, combus.tipoCombustivel 
from tbb_locacao as loc 
left join tb_carro as car
on loc.idCarro = car.idCarro
left join tb_combustivel as combus
on car.idCombustivel = combus.idCombustivel 




-- resolvi deixar a table locacao original no arquivo para fins de teste se funcionou as normalizações




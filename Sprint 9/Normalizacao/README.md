# Modelo relacional e dimensional
</hr>

## Normalização modelo relacional
    Primeiramente para entender oque eu tinha que fazer nas 3 formas eu coloquei elas em uma planilha para ir comparando:
 
 <img src = "normalizacao.png" alt= "planilha da normalização" width = '500px'  height = '400px'>

    Na planilha em questão eu não apliquei os conceitos na ordem correta, pois eu não tinha visto nenhum campo multivalorado como telefone, ou composto como endereço. Portanto desde o começo eu já fiz a segunda forma que era separar tabelas para que dependessem de uma chave primária apenas e que essa chave tenha correlação com suas colunas como 'nomecliente' e 'cidadecliente' fazem parte de 'idCliente'. Finalmente na terceira forma eu me certifiquei que colunas não chaves não dependessem de colunas que também não fossem chaves primárias, então para resolver isso eu sabia que campos como 'cliente', 'carro' e 'vendedor' deveriam ter relação com 'locação', mas como cada um desses campos tem muitos atributos específicos, eu criei uma tabela para cada um e deixei o id deles como chave estrangeira na tabela principal.

### Modelo físico
</hr>
    
    Aqui basicamente peguei as tabelas finais na 3FN e criei todas com campos vazios e depois eu inseria os dados com a consulta na tabela principal:

 <img src = "tabela1.png" alt= "script modelo fisico" width = '500px'  height = '400px'>
<img src = "tabela2.png" alt= "continuação script" width = '500px'  height = '400px'>

    esses foram apenas alguns prints, mas o script está todo na pasta onde se encontra esse readme.md.
### Modelo Lógico
    Essa é uma explicação das relações no modelo lógico:
- Vendedor/Locação
    - Um vendedor pode vender muitas locações: 1 para N
    - Uma locação só pode ser vendida por um vendedor por vez: 1 para 1
- Carro/Locação
    - Um carro só pode ter uma locação por vez: 1 para 1
    - Um processo de locação só pode ter um carro: 1 para 1
- Carro/Quilometragem
    - Um carro pode ter muitas quilometragens em períodos diferentes: 1 para N
    - Uma quilometragem só pode estar em um carro: 1 para 1
- Carro/Combustível
    - Um carro só pode ter um tipo de combustível: 1 para 1
    - Um tipo de combustível pode estar em diferentes carros: 1 para N
- Cliente/Locação
    - Um cliente pode fazer várias locações: 1 para N
    - Uma locação só pode ser feita por um cliente por vez: 1 para 1
 <img src = "desenho_logico.png" alt= "diagrama" width = '500px'  height = '400px'>
 <img src = "logico.png" alt= "diagrama" width = '500px'  height = '400px'>

## Modelagem dimensional
 
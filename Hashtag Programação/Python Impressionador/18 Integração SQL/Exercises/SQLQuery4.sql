-- Quantos produtos a gente vende na empresa?
-- COUNT(*)
SELECT COUNT(ProductName) from DimProduct

-- Preço do produto mais caro que a gente vendde na loja 
SELECT MAX(UnitPrice) From DimProduct

-- Qual a média de preço dos produtos?
-- round, Casas decimais - Arredondamento
SELECT ROUND(AVG(UnitPrice), 2) From DimProduct 

-- Quantas marcas diferentes temos na empresa?
-- distinct - como se fosse o unique() no pandas
--SELECT DISTINCT(BrandName) From DimProduct
-- Mas eu quero contar, não ver quais são
SELECT COUNT(DISTINCT(BrandName)) From DimProduct

-- Segunda forma de mostrar informações unicas - Group By

SELECT BrandName From DimProduct group by BrandName

-- Contar os produtos vendidos de cada marca
SELECT BrandName, COUNT(ProductName) as 'ProductsAmount' From DimProduct group by BrandName

-- Preço mais caro que cada marca cobra
SELECT BrandName, MAX(UnitPrice) as 'MaxPrice' From DimProduct group by BrandName

-- Exiba todas as marcas e todas as classes
SELECT BrandName, ClassName From DimProduct group by BrandName, ClassName

-- Quantos produtos cada marca de cada classe vende
SELECT BrandName, ClassName, COUNT(ProductName) as 'ProductsAmount' From DimProduct group by BrandName, ClassName

-- O preço médio de cada marca/classe
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct group by BrandName, ClassName

-- Filtre só a classe econômica
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' group by BrandName, ClassName

-- Média de preços da classe econômica
SELECT ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' Group By ClassName

-- Média de preço da contoso e classe economica
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' and BrandName = 'Contoso' group by BrandName, ClassName


-- Order By e Top

-- Exiba a tabela de produtos com as colunas (Nome Produto, Marca, Preço)
SELECT ProductName, BrandName, UnitPrice From DimProduct

-- Ordene do mais caro para o mais barato
SELECT ProductName, BrandName, UnitPrice From DimProduct Order By UnitPrice desc

-- Exiba apenas os 10 produtos mais baratos
SELECT TOP 10 ProductName, BrandName, UnitPrice From DimProduct Order By UnitPrice asc
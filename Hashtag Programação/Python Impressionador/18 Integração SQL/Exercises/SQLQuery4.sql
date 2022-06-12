-- Quantos produtos a gente vende na empresa?
-- COUNT(*)
SELECT COUNT(ProductName) from DimProduct

-- Pre�o do produto mais caro que a gente vendde na loja 
SELECT MAX(UnitPrice) From DimProduct

-- Qual a m�dia de pre�o dos produtos?
-- round, Casas decimais - Arredondamento
SELECT ROUND(AVG(UnitPrice), 2) From DimProduct 

-- Quantas marcas diferentes temos na empresa?
-- distinct - como se fosse o unique() no pandas
--SELECT DISTINCT(BrandName) From DimProduct
-- Mas eu quero contar, n�o ver quais s�o
SELECT COUNT(DISTINCT(BrandName)) From DimProduct

-- Segunda forma de mostrar informa��es unicas - Group By

SELECT BrandName From DimProduct group by BrandName

-- Contar os produtos vendidos de cada marca
SELECT BrandName, COUNT(ProductName) as 'ProductsAmount' From DimProduct group by BrandName

-- Pre�o mais caro que cada marca cobra
SELECT BrandName, MAX(UnitPrice) as 'MaxPrice' From DimProduct group by BrandName

-- Exiba todas as marcas e todas as classes
SELECT BrandName, ClassName From DimProduct group by BrandName, ClassName

-- Quantos produtos cada marca de cada classe vende
SELECT BrandName, ClassName, COUNT(ProductName) as 'ProductsAmount' From DimProduct group by BrandName, ClassName

-- O pre�o m�dio de cada marca/classe
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct group by BrandName, ClassName

-- Filtre s� a classe econ�mica
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' group by BrandName, ClassName

-- M�dia de pre�os da classe econ�mica
SELECT ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' Group By ClassName

-- M�dia de pre�o da contoso e classe economica
SELECT BrandName, ClassName, ROUND(AVG(UnitPrice), 2) as 'AveragePrice' From DimProduct where ClassName = 'Economy' and BrandName = 'Contoso' group by BrandName, ClassName


-- Order By e Top

-- Exiba a tabela de produtos com as colunas (Nome Produto, Marca, Pre�o)
SELECT ProductName, BrandName, UnitPrice From DimProduct

-- Ordene do mais caro para o mais barato
SELECT ProductName, BrandName, UnitPrice From DimProduct Order By UnitPrice desc

-- Exiba apenas os 10 produtos mais baratos
SELECT TOP 10 ProductName, BrandName, UnitPrice From DimProduct Order By UnitPrice asc
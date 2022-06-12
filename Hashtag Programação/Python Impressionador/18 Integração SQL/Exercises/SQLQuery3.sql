SELECT * FROM DimStore
-- puxando a tabela

SELECT StoreName, StoreDescription, Status, AddressLine1 From DimStore

-- Renomear a coluna
SELECT StoreName, StoreDescription, Status, AddressLine1 as 'Endereco' From DimStore
-- Só colocar um as e depois o nome entre aspas
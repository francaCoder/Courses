-- Selecione as top 5 lojas ativas (que continuam vendendo) e que tem a maior quantidade de funcionários
-- Apenas as colunas - nome da loja, status e qtde funcionários

SELECT * From DimStore

SELECT TOP 5 StoreName, Status, EmployeeCount From DimStore where Status = 'On' Order By EmployeeCount desc
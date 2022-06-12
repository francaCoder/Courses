SELECT
Cotacoes.ExchangeRateKey,
Cotacoes.CurrencyKey,
CONVERT(varchar(10), Cotacoes.DateKey, 103) as 'DateKey',
-- 10 caracteres : 01/01/2000      3 = dd/mm/yy ou 103 dd/mm/yyyy
Cotacoes.AverageRate,
-- Moedas.CurrencyName, 
CONCAT(CONVERT(varchar(10), Cotacoes.DateKey, 103), Cotacoes.CurrencyKey) as 'DateCurrencyKey'
From FactExchangeRate Cotacoes
-- LEFT JOIN DimCurrency Moedas on Cotacoes.CurrencyKey
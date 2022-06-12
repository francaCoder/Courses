SELECT
SalesKey,
CONVERT(varchar(10), DateKey, 103) as 'DateKey',
StoreKey,
ProductKey,
CurrencyKey,
SalesQuantity,
ReturnQuantity,
ReturnAmount,
DiscountAmount,
CONCAT(CONVERT(varchar(10), DateKey, 103), CurrencyKey) as 'DateCurrencyKey'
From FactSales
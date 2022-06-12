SELECT EmployeeKey, CONCAT(FirstName, ' ', LastName) as 'FullName', Title, REPLACE(REPLACE(Gender, 'M', 'Masculino'), 'F', 'Feminino') as 'Gender', DepartmentName From DimEmployee

-- 3
where Gender = 'M'

-- 4
--where Gender = 'M' and Title = 'Sales Region Manager'

-- 5
--where Gender = 'M' and (Title = 'Sales Region Manager' or Title = 'Sales State Manager') 

-- 6 
--where Gender = 'M' and (Title = 'Sales Region Manager' or Title = 'Sales State Manager') and DepartmentName = 'Production'

--7
--where Gender = 'M' and (Title = 'Sales Region Manager' or Title = 'Sales State Manager') and (DepartmentName = 'Production' or DepartmentName = 'Marketing')
SELECT SupplierName FROM Suppliers WHERE Country = "USA" OR Country = 'UK';
SELECT SupplierName FROM Suppliers  WHERE Country = 'USA' and City = 'Boston' or City = 'New Orleans';
SELECT SupplierName FROM Suppliers  WHERE NOT Country = 'Japan' or NOT Country = 'Kanada';
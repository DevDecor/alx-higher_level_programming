-- creates a database if it does not already exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'MyTestDataBase')
BEGIN
  CREATE DATABASE MyTestDataBase;
END;

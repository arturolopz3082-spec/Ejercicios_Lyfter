PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS InvoicePerProduct;
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS ShoppingCart;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS ShoppingCartProducts;

CREATE TABLE IF NOT EXISTS Products (
    Code INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL CHECK (Price >= 0),
    EntryDate TEXT NOT NULL,
    Brand TEXT,
    StockAvailable INTEGER NOT NULL CHECK (StockAvailable >= 0)
);

CREATE TABLE IF NOT EXISTS Invoices (
    InvoiceNumber INTEGER PRIMARY KEY AUTOINCREMENT,
    PurchaseDate TEXT NOT NULL,
    BuyerEmail TEXT NOT NULL,
    TotalAmount REAL NOT NULL CHECK (TotalAmount >= 0)
);

CREATE TABLE IF NOT EXISTS InvoicePerProduct (
    InvoiceNumber INTEGER NOT NULL,
    ProductCode INTEGER NOT NULL,
    Quantity INTEGER NOT NULL CHECK (Quantity > 0),
    TotalAmount REAL NOT NULL CHECK (TotalAmount >= 0),

    PRIMARY KEY (InvoiceNumber, ProductCode),
    FOREIGN KEY (InvoiceNumber) REFERENCES Invoices(InvoiceNumber),
    FOREIGN KEY (ProductCode) REFERENCES Products(Code)
);

CREATE TABLE IF NOT EXISTS ShoppingCart (
    ShoppingCartID INTEGER PRIMARY KEY AUTOINCREMENT,
    BuyerEmail TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ShoppingCartProducts (
	ShoppingCartID INTEGER NOT NULL,
	ProductCode INTEGER NOT NULL,
	Quantity INTEGER NOT NULL CHECK (Quantity > 0),

	PRIMARY KEY (ShoppingCartID, ProductCode),
	FOREIGN KEY (ShoppingCartID) REFERENCES ShoppingCart(ShoppingCartID),
	FOREIGN KEY (ProductCode) REFERENCES Products(Code)
);

ALTER TABLE Invoices ADD COLUMN BuyerPhone TEXT;
ALTER TABLE Invoices ADD COLUMN CashierEmployeeCode TEXT;

SELECT * From Products;

Select * from Products Where Price = 50000;

SELECT
    ipp.InvoiceNumber,
    ipp.ProductCode,
    p.Name,
    ipp.Quantity,
    ipp.TotalAmount
FROM InvoicePerProduct AS ipp
INNER JOIN Products AS p
    ON ipp.ProductCode = p.Code
WHERE ipp.ProductCode = 1;

SELECT
    ipp.ProductCode,
    p.Name,
    SUM(ipp.Quantity) AS TotalQuantityPurchased,
    SUM(ipp.TotalAmount) AS TotalPurchasedAmount
FROM InvoicePerProduct AS ipp
INNER JOIN Products AS p
    ON ipp.ProductCode = p.Code
GROUP BY ipp.ProductCode, p.Name;

SELECT * FROM Invoices WHERE BuyerEmail = 'comprador01@email.com';

SELECT * FROM Invoices ORDER BY TotalAmount DESC;

SELECT * FROM Invoices WHERE InvoiceNumber = 1;
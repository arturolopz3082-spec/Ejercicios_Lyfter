PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Rents;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Authors;


CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE Books (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    AuthorID INTEGER,

    FOREIGN KEY (AuthorID)
        REFERENCES Authors(ID)
);

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookID INTEGER NOT NULL,
    CustomerID INTEGER NOT NULL,
    State TEXT NOT NULL
        CHECK (State IN ('Returned', 'On time', 'Overdue')),

    FOREIGN KEY (BookID)
        REFERENCES Books(ID),

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(ID)
);


INSERT INTO Authors (ID, Name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');


INSERT INTO Books (ID, Name, AuthorID) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);


INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');


INSERT INTO Rents (BookID, CustomerID, State) VALUES
(1, 2, 'Returned'),
(2, 2, 'Returned'),
(1, 1, 'On time'),
(3, 1, 'On time'),
(2, 2, 'Overdue');

---Obtenga todos los libros y sus autores (en caso de tenerlos)
select * from books join authors on books.AuthorId = Authors.ID;

--Obtenga todos los libros que no tiene autor
SELECT * FROM books WHERE AuthorID IS NULL;

--Obtenga todos los autores que no tienen libro
SELECT * FROM authors LEFT JOIN books ON Authors.ID = books.AuthorID WHERE books.AuthorID IS NULL;

--Obtenga todos los libros que han sido rentados en algún momento
SELECT * FROM books JOIN rents ON books.id = rents.BookID;

--Obtenga todos los libros que nunca han sido rentados
SELECT * FROM Books as b LEFT JOIN Rents as r ON b.id = r.BookID WHERE r.BookID IS NULL;

--Obtenga todos los clientes que nunca han rentado un libro
SELECT * FROM Customers AS c LEFT JOIN Rents as r ON c.id = r.CustomerID WHERE r.CustomerID IS NULL;

--Obtenga todos los libros que han sido rentados y están en estado overdue
SELECT * FROM Books AS B JOIN Rents as R ON B.id = R.CustomerID WHERE State = 'Overdue';
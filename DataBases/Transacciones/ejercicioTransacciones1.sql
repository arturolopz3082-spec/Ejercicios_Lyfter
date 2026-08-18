-- =========================================================
-- Ejercicio 1: Creación de la base de datos
-- Entidades: Products, Users, Bills (+ tabla cruz Bill_Items)
-- =========================================================

-- Limpieza previa (útil para poder ejecutar el script varias veces)
DROP TABLE IF EXISTS bill_items;
DROP TABLE IF EXISTS bills;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- ---------------------------------------------------------
-- Tabla: Users
-- ---------------------------------------------------------
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(150) NOT NULL,
    email       VARCHAR(150) NOT NULL UNIQUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------
-- Tabla: Products
-- ---------------------------------------------------------
CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(150) NOT NULL,
    description TEXT,
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock       INTEGER NOT NULL CHECK (stock >= 0),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------
-- Tabla: Bills (facturas)
-- ---------------------------------------------------------
CREATE TABLE bills (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(id),
    total       NUMERIC(10,2) NOT NULL DEFAULT 0,
    status      VARCHAR(20) NOT NULL DEFAULT 'Activa'
                CHECK (status IN ('Activa', 'Retornada', 'Cancelada')),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------
-- Tabla cruz: Bill_Items (detalle de productos por factura)
-- ---------------------------------------------------------
CREATE TABLE bill_items (
    id          SERIAL PRIMARY KEY,
    bill_id     INTEGER NOT NULL REFERENCES bills(id),
    product_id  INTEGER NOT NULL REFERENCES products(id),
    quantity    INTEGER NOT NULL CHECK (quantity > 0),
    unit_price  NUMERIC(10,2) NOT NULL,
    UNIQUE (bill_id, product_id)
);

-- ---------------------------------------------------------
-- Datos de ejemplo (opcional, para poder probar los ejercicios 2 y 3)
-- ---------------------------------------------------------
INSERT INTO users (name, email) VALUES
    ('Ana Pérez',   'ana.perez@example.com'),
    ('Luis Gómez',  'luis.gomez@example.com');

INSERT INTO products (name, description, price, stock) VALUES
    ('Teclado mecánico', 'Teclado mecánico switch rojo', 45.99, 20),
    ('Mouse inalámbrico', 'Mouse óptico inalámbrico',      15.50, 50),
    ('Monitor 24"',        'Monitor Full HD 24 pulgadas',  120.00, 10);
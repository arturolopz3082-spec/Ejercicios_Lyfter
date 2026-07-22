-- =========================================================
-- Ejercicio 2: Transacción de Compra
-- Bloque anónimo (DO $$...$$) en PL/pgSQL
--
-- Ajuste las variables v_user_id, v_product_ids y v_quantities
-- según el usuario y los productos que se desean comprar.
-- =========================================================

DO $$
DECLARE
    v_user_id      INTEGER := 1;                  -- id del usuario que compra
    v_product_ids  INTEGER[] := ARRAY[1, 2];       -- ids de productos comprados
    v_quantities   INTEGER[] := ARRAY[3, 1];       -- cantidades respectivas (misma posición)
    v_bill_id      INTEGER;
    v_stock        INTEGER;
    v_price        NUMERIC(10,2);
    v_total        NUMERIC(10,2) := 0;
    i              INTEGER;
BEGIN
    -- Validación básica: que ambos arreglos tengan la misma longitud
    IF array_length(v_product_ids, 1) <> array_length(v_quantities, 1) THEN
        RAISE EXCEPTION 'La cantidad de productos y cantidades no coincide';
    END IF;

    -- 1. Confirmar que el usuario que realiza la compra existe
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario con id % no existe', v_user_id;
    END IF;

    -- 2. Comprobar existencias suficientes de cada producto
    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        SELECT stock, price
          INTO v_stock, v_price
          FROM products
         WHERE id = v_product_ids[i]
         FOR UPDATE;                       -- bloquea la fila mientras dura la transacción

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto con id % no existe', v_product_ids[i];
        END IF;

        IF v_stock < v_quantities[i] THEN
            RAISE EXCEPTION
                'Stock insuficiente para el producto %. Disponible: %, solicitado: %',
                v_product_ids[i], v_stock, v_quantities[i];
        END IF;

        v_total := v_total + (v_price * v_quantities[i]);
    END LOOP;

    -- 3. Insertar la factura con el usuario relacionado
    INSERT INTO bills (user_id, total, status)
    VALUES (v_user_id, v_total, 'Activa')
    RETURNING id INTO v_bill_id;

    -- 4. Insertar el detalle de la factura y reducir el stock
    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        SELECT price INTO v_price
          FROM products
         WHERE id = v_product_ids[i];

        INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
        VALUES (v_bill_id, v_product_ids[i], v_quantities[i], v_price);

        UPDATE products
           SET stock = stock - v_quantities[i]
         WHERE id = v_product_ids[i];
    END LOOP;

    RAISE NOTICE 'Compra registrada exitosamente. Factura id: %, total: %', v_bill_id, v_total;
END $$;
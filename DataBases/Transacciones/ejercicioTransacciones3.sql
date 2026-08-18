-- =========================================================
-- Ejercicio 3: Transacción de Retorno de Productos
-- Bloque anónimo (DO $$...$$) en PL/pgSQL
--
-- Ajuste la variable v_bill_id según la factura que se desea
-- retornar.
-- =========================================================

DO $$
DECLARE
    v_bill_id  INTEGER := 1;   -- id de la factura a devolver
    v_status   VARCHAR(20);
    r          RECORD;
BEGIN
    -- 1. Verificar que la factura existe
    SELECT status
      INTO v_status
      FROM bills
     WHERE id = v_bill_id
     FOR UPDATE;               -- bloquea la fila mientras dura la transacción

    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura con id % no existe', v_bill_id;
    END IF;

    -- Evitar retornar dos veces la misma factura
    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada previamente', v_bill_id;
    END IF;

    -- 2. Aumentar el stock de los productos según la cantidad comprada
    FOR r IN
        SELECT product_id, quantity
          FROM bill_items
         WHERE bill_id = v_bill_id
    LOOP
        UPDATE products
           SET stock = stock + r.quantity
         WHERE id = r.product_id;
    END LOOP;

    -- 3. Modificar la factura original: marcarla como "Retornada"
    UPDATE bills
       SET status = 'Retornada'
     WHERE id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como Retornada y stock restaurado', v_bill_id;
END $$;

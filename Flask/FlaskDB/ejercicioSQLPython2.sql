-- ============================================================
-- Tarea: Scripts de operación sobre la DB lyfter_car_rental
-- ============================================================


-- ------------------------------------------------------------
-- 1. Agregar un usuario nuevo
-- ------------------------------------------------------------
INSERT INTO lyfter_car_rental.usuarios
    (first_name, last_name, email, username, password, birthdate, state_account)
VALUES
    ('Arturo', 'Lopez', 'arturo.lopez@example.com', 'alopez', 'hashed_password_123', '1995-04-12', 'activo');


-- ------------------------------------------------------------
-- 2. Agregar un automovil nuevo
-- ------------------------------------------------------------
INSERT INTO lyfter_car_rental.automoviles
    (make, model, fabrication_year, state)
VALUES
    ('Toyota', 'Corolla', 2023, 'disponible');


-- ------------------------------------------------------------
-- 3. Cambiar el estado de un usuario
--    (reemplaza el ID y el nuevo estado según lo necesites)
-- ------------------------------------------------------------
UPDATE lyfter_car_rental.usuarios
SET state_account = 'suspendido'
WHERE id = 1;


-- ------------------------------------------------------------
-- 4. Cambiar el estado de un automovil
--    (reemplaza el ID y el nuevo estado según lo necesites)
-- ------------------------------------------------------------
UPDATE lyfter_car_rental.automoviles
SET state = 'mantenimiento'
WHERE id = 1;


-- ------------------------------------------------------------
-- 5. Generar un alquiler nuevo con los datos de un usuario y un automovil
--    - Se valida que el automovil exista y esté 'disponible' antes de alquilarlo.
--    - Se inserta el alquiler (rental_date se autogenera con DEFAULT).
--    - Se marca el automovil como 'alquilado'.
--    Reemplaza los valores 1 (usuario) y 5 (automovil) según corresponda.
-- ------------------------------------------------------------
DO $$
DECLARE
    v_user_id   INTEGER := 1;
    v_car_id    INTEGER := 5;
    v_state     VARCHAR(20);
BEGIN
    SELECT state INTO v_state
    FROM lyfter_car_rental.automoviles
    WHERE id = v_car_id;

    IF v_state IS NULL THEN
        RAISE EXCEPTION 'El automovil con id % no existe.', v_car_id;
    ELSIF v_state <> 'disponible' THEN
        RAISE EXCEPTION 'El automovil con id % no esta disponible (estado actual: %).', v_car_id, v_state;
    END IF;

    INSERT INTO lyfter_car_rental.alquiler (user_id, car_id, rental_state)
    VALUES (v_user_id, v_car_id, 'activo');

    UPDATE lyfter_car_rental.automoviles
    SET state = 'alquilado'
    WHERE id = v_car_id;
END $$;


-- ------------------------------------------------------------
-- 6. Confirmar la devolución del auto al completar el alquiler
--    - Coloca el automovil como 'disponible'.
--    - Marca el alquiler activo de ese automovil como 'finalizado'.
--    Reemplaza el valor 5 (automovil) según corresponda.
-- ------------------------------------------------------------
DO $$
DECLARE
    v_car_id INTEGER := 5;
BEGIN
    UPDATE lyfter_car_rental.alquiler
    SET rental_state = 'finalizado'
    WHERE car_id = v_car_id
      AND rental_state = 'activo';

    UPDATE lyfter_car_rental.automoviles
    SET state = 'disponible'
    WHERE id = v_car_id;
END $$;


-- ------------------------------------------------------------
-- 7. Deshabilitar un automovil del alquiler
--    - Marca el automovil como 'fuera_de_servicio' (ya no se puede alquilar).
--    - Si tenía un alquiler activo, lo cancela.
--    Reemplaza el valor 5 (automovil) según corresponda.
-- ------------------------------------------------------------
DO $$
DECLARE
    v_car_id INTEGER := 5;
BEGIN
    UPDATE lyfter_car_rental.alquiler
    SET rental_state = 'cancelado'
    WHERE car_id = v_car_id
      AND rental_state = 'activo';

    UPDATE lyfter_car_rental.automoviles
    SET state = 'fuera_de_servicio'
    WHERE id = v_car_id;
END $$;


-- ------------------------------------------------------------
-- 8a. Obtener todos los automoviles alquilados
-- ------------------------------------------------------------
SELECT id, make, model, fabrication_year, state
FROM lyfter_car_rental.automoviles
WHERE state = 'alquilado';


-- ------------------------------------------------------------
-- 8b. Obtener todos los automoviles disponibles
-- ------------------------------------------------------------
SELECT id, make, model, fabrication_year, state
FROM lyfter_car_rental.automoviles
WHERE state = 'disponible';
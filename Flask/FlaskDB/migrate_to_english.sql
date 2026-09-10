-- Run this once against your existing lyfter_car_rental schema.

ALTER TABLE lyfter_car_rental.usuarios RENAME TO users;
ALTER TABLE lyfter_car_rental.automoviles RENAME TO cars;
ALTER TABLE lyfter_car_rental.alquiler RENAME TO rentals;

-- The constraint names are the default names PostgreSQL creates from your original DDL.
ALTER TABLE lyfter_car_rental.users DROP CONSTRAINT IF EXISTS usuarios_state_account_check;
ALTER TABLE lyfter_car_rental.cars DROP CONSTRAINT IF EXISTS automoviles_state_check;
ALTER TABLE lyfter_car_rental.rentals DROP CONSTRAINT IF EXISTS alquiler_rental_state_check;

UPDATE lyfter_car_rental.users
SET state_account = CASE state_account
    WHEN 'activo' THEN 'active'
    WHEN 'inactivo' THEN 'inactive'
    WHEN 'suspendido' THEN 'suspended'
    ELSE state_account
END;

UPDATE lyfter_car_rental.cars
SET state = CASE state
    WHEN 'disponible' THEN 'available'
    WHEN 'alquilado' THEN 'rented'
    WHEN 'mantenimiento' THEN 'maintenance'
    WHEN 'fuera_de_servicio' THEN 'out_of_service'
    ELSE state
END;

UPDATE lyfter_car_rental.rentals
SET rental_state = CASE rental_state
    WHEN 'activo' THEN 'active'
    WHEN 'finalizado' THEN 'completed'
    WHEN 'cancelado' THEN 'cancelled'
    ELSE rental_state
END;

ALTER TABLE lyfter_car_rental.users
    ALTER COLUMN state_account SET DEFAULT 'active',
    ADD CONSTRAINT users_state_account_check
        CHECK (state_account IN ('active', 'inactive', 'suspended'));

ALTER TABLE lyfter_car_rental.cars
    ADD CONSTRAINT cars_state_check
        CHECK (state IN ('available', 'rented', 'maintenance', 'out_of_service'));

ALTER TABLE lyfter_car_rental.rentals
    ALTER COLUMN rental_state SET DEFAULT 'active',
    ADD CONSTRAINT rentals_state_check
        CHECK (rental_state IN ('active', 'completed', 'cancelled'));

ALTER TABLE lyfter_car_rental.users
    ADD COLUMN IF NOT EXISTS is_delinquent BOOLEAN NOT NULL DEFAULT FALSE;

-- Because your seed inserted explicit SERIAL ids, synchronize the sequences once.
SELECT setval(
    pg_get_serial_sequence('lyfter_car_rental.users', 'id'),
    COALESCE((SELECT MAX(id) FROM lyfter_car_rental.users), 1),
    true
);

SELECT setval(
    pg_get_serial_sequence('lyfter_car_rental.cars', 'id'),
    COALESCE((SELECT MAX(id) FROM lyfter_car_rental.cars), 1),
    true
);

SELECT setval(
    pg_get_serial_sequence('lyfter_car_rental.rentals', 'id'),
    COALESCE((SELECT MAX(id) FROM lyfter_car_rental.rentals), 1),
    true
);
/*
Updates warehouse and transporter master tables.
*/

BEGIN;

-- Warehouses

ALTER TABLE master.warehouses
    DROP CONSTRAINT chk_warehouses_type;

ALTER TABLE master.warehouses
    ADD CONSTRAINT chk_warehouses_type
    CHECK (
        warehouse_type IN (
            'central',
            'regional',
            'depot',
            'cross_dock'
        )
    );

-- Locations

ALTER TABLE master.locations
    DROP CONSTRAINT locations_location_code_key;

ALTER TABLE master.locations
    ADD CONSTRAINT uq_locations_warehouse_code
    UNIQUE (warehouse_id, location_code);

-- Transporters

ALTER TABLE master.transporters
    DROP COLUMN performance_rating;

COMMIT;
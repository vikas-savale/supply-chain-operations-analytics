/*
Creates the master.warehouses table.
Stores warehouse master data.
*/

CREATE TABLE master.warehouses
(
    warehouse_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    warehouse_code VARCHAR(30) NOT NULL UNIQUE,
    warehouse_name VARCHAR(150) NOT NULL,
    warehouse_type VARCHAR(30) NOT NULL,

    address_line1 VARCHAR(150) NOT NULL,
    address_line2 VARCHAR(150),
    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(80) NOT NULL DEFAULT 'India',

    total_capacity_ltr NUMERIC(14,2) NOT NULL DEFAULT 0,
    usable_capacity_ltr NUMERIC(14,2) NOT NULL DEFAULT 0,
    storage_mode VARCHAR(20) NOT NULL DEFAULT 'mixed',

    warehouse_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_warehouses_status
        CHECK (warehouse_status IN ('active', 'inactive')),

    CONSTRAINT chk_warehouses_type
        CHECK (
            warehouse_type IN (
                'central',
                'regional',
                'depot',
                'cross_dock'
            )
        ),

    CONSTRAINT chk_warehouses_storage_mode
        CHECK (storage_mode IN ('ambient', 'covered', 'mixed', 'controlled')),

    CONSTRAINT chk_warehouses_capacity
        CHECK (
            total_capacity_ltr >= 0
            AND usable_capacity_ltr >= 0
            AND usable_capacity_ltr <= total_capacity_ltr
        )
);
/*
Creates the master.locations table.
Stores warehouse location data.
*/

CREATE TABLE master.locations
(
    location_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    warehouse_id BIGINT NOT NULL,
    location_code VARCHAR(40) NOT NULL,
    location_name VARCHAR(150) NOT NULL,

    zone_code VARCHAR(20) NOT NULL,
    aisle_no VARCHAR(20),
    rack_no VARCHAR(20),
    bin_no VARCHAR(20),

    location_type VARCHAR(20) NOT NULL DEFAULT 'storage',
    storage_mode VARCHAR(20) NOT NULL DEFAULT 'mixed',
    max_capacity_ltr NUMERIC(14,2) NOT NULL DEFAULT 0,
    location_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_locations_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_locations_warehouse_code
        UNIQUE (warehouse_id, location_code),

    CONSTRAINT chk_locations_type
        CHECK (
            location_type IN (
                'receiving',
                'storage',
                'picking',
                'dispatch',
                'quarantine',
                'returns',
                'damage',
                'staging'
            )
        ),

    CONSTRAINT chk_locations_storage_mode
        CHECK (storage_mode IN ('ambient', 'covered', 'mixed', 'controlled')),

    CONSTRAINT chk_locations_status
        CHECK (location_status IN ('active', 'inactive')),

    CONSTRAINT chk_locations_capacity
        CHECK (max_capacity_ltr >= 0)
);
/*
Creates the master.vehicles table.
Stores vehicle master data.
*/

CREATE TABLE master.vehicles
(
    vehicle_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    transporter_id BIGINT NOT NULL,
    vehicle_number VARCHAR(20) NOT NULL UNIQUE,
    vehicle_type VARCHAR(30) NOT NULL,
    body_type VARCHAR(30) NOT NULL DEFAULT 'closed',

    capacity_tons NUMERIC(10,2) NOT NULL DEFAULT 0,
    capacity_ltr NUMERIC(14,2) NOT NULL DEFAULT 0,

    registration_state VARCHAR(80) NOT NULL,
    ownership_type VARCHAR(20) NOT NULL DEFAULT 'attached',
    vehicle_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_vehicles_transporter
        FOREIGN KEY (transporter_id)
        REFERENCES master.transporters (transporter_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_vehicles_status
        CHECK (vehicle_status IN ('active', 'inactive')),

    CONSTRAINT chk_vehicles_ownership
        CHECK (ownership_type IN ('owned', 'attached', 'hired')),

    CONSTRAINT chk_vehicles_capacity
        CHECK (
            capacity_tons >= 0
            AND capacity_ltr >= 0
        )
);
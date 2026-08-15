/*
Creates the master.customer_locations table.
Stores customer delivery locations.
*/

CREATE TABLE master.customer_locations
(
    customer_location_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    customer_id BIGINT NOT NULL,

    location_code VARCHAR(30) NOT NULL,
    location_name VARCHAR(150) NOT NULL,

    contact_person VARCHAR(100),
    phone VARCHAR(20),

    address_line1 VARCHAR(150) NOT NULL,
    address_line2 VARCHAR(150),
    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,

    country VARCHAR(80) NOT NULL DEFAULT 'India',

    is_default BOOLEAN NOT NULL DEFAULT FALSE,
    location_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_customer_locations_customer
        FOREIGN KEY (customer_id)
        REFERENCES master.customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_customer_locations_code
        UNIQUE (customer_id, location_code),

    CONSTRAINT chk_customer_locations_status
        CHECK (location_status IN ('active', 'inactive'))
);

CREATE UNIQUE INDEX uq_customer_locations_one_active_default
    ON master.customer_locations (customer_id)
    WHERE is_default = TRUE
      AND location_status = 'active';
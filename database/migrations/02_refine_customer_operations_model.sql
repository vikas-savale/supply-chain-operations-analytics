/*
Refines the customer and operational master model.

This migration:
- connects customers to reusable payment terms
- moves customer delivery destinations into a separate master table
- adds an operational employee master
*/

BEGIN;

-- ============================================================
-- 1. Customers: connect reusable payment terms
-- ============================================================

ALTER TABLE master.customers
    ADD COLUMN payment_term_id BIGINT;

ALTER TABLE master.customers
    ADD CONSTRAINT fk_customers_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id);

ALTER TABLE master.customers
    ALTER COLUMN payment_term_id SET NOT NULL;

ALTER TABLE master.customers
    DROP COLUMN payment_terms_days;


-- ============================================================
-- 2. Customers: remove single ship-to address
-- ============================================================

ALTER TABLE master.customers
    DROP COLUMN ship_to_address_line1,
    DROP COLUMN ship_to_address_line2,
    DROP COLUMN ship_to_city,
    DROP COLUMN ship_to_state,
    DROP COLUMN ship_to_postal_code;


-- ============================================================
-- 3. Customer Locations
-- ============================================================

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


-- ============================================================
-- 4. One active default ship-to per customer
-- ============================================================

CREATE UNIQUE INDEX uq_customer_locations_one_active_default
    ON master.customer_locations (customer_id)
    WHERE is_default = TRUE
      AND location_status = 'active';


-- ============================================================
-- 5. Operational Employee Master
-- ============================================================

CREATE TABLE master.employees
(
    employee_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    employee_code VARCHAR(30) NOT NULL UNIQUE,
    employee_name VARCHAR(150) NOT NULL,

    department VARCHAR(80) NOT NULL,
    role VARCHAR(80) NOT NULL,

    warehouse_id BIGINT,

    employee_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_employees_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_employees_status
        CHECK (employee_status IN ('active', 'inactive'))
);

COMMIT;
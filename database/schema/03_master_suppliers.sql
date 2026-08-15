/*
Creates the master.suppliers table.
Stores supplier master data.
*/

CREATE TABLE master.suppliers
(
    supplier_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    supplier_code VARCHAR(30) NOT NULL UNIQUE,
    supplier_name VARCHAR(150) NOT NULL,
    supplier_type VARCHAR(30) NOT NULL,

    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(150),

    gstin VARCHAR(20),
    state_code VARCHAR(5),

    address_line1 VARCHAR(150) NOT NULL,
    address_line2 VARCHAR(150),
    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,

    country VARCHAR(80) NOT NULL DEFAULT 'India',

    lead_time_days SMALLINT NOT NULL DEFAULT 0,
    payment_term_id BIGINT NOT NULL,

    supplier_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_suppliers_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id),

    CONSTRAINT chk_suppliers_status
        CHECK (supplier_status IN ('active', 'inactive')),

    CONSTRAINT chk_suppliers_lead_time
        CHECK (lead_time_days >= 0)
);
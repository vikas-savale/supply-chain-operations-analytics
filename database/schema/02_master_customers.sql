/*
Creates the master.customers table.
Stores customer master data.
*/

CREATE TABLE master.customers
(
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    customer_code VARCHAR(30) NOT NULL UNIQUE,
    customer_name VARCHAR(150) NOT NULL,
    customer_type VARCHAR(30) NOT NULL,

    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(150),

    gstin VARCHAR(20),
    state_code VARCHAR(5),

    billing_address_line1 VARCHAR(150) NOT NULL,
    billing_address_line2 VARCHAR(150),
    billing_city VARCHAR(80) NOT NULL,
    billing_state VARCHAR(80) NOT NULL,
    billing_postal_code VARCHAR(20) NOT NULL,

    country VARCHAR(80) NOT NULL DEFAULT 'India',

    payment_term_id BIGINT NOT NULL,
    credit_limit NUMERIC(14,2) NOT NULL DEFAULT 0,

    customer_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_customers_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id),

    CONSTRAINT chk_customers_status
        CHECK (customer_status IN ('active', 'inactive')),

    CONSTRAINT chk_customers_credit_limit
        CHECK (credit_limit >= 0)
);
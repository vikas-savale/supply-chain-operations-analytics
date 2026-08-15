/*
Creates the master.transporters table.
Stores transporter master data.
*/

CREATE TABLE master.transporters
(
    transporter_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    transporter_code VARCHAR(30) NOT NULL UNIQUE,
    transporter_name VARCHAR(150) NOT NULL,
    transporter_type VARCHAR(30) NOT NULL,

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

    service_mode VARCHAR(20) NOT NULL DEFAULT 'both',
    contract_start_date DATE,
    contract_end_date DATE,

    transporter_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_transporters_status
        CHECK (transporter_status IN ('active', 'inactive')),

    CONSTRAINT chk_transporters_service_mode
        CHECK (service_mode IN ('inbound', 'outbound', 'both')),

    CONSTRAINT chk_transporters_contract_dates
        CHECK (
            contract_start_date IS NULL
            OR contract_end_date IS NULL
            OR contract_end_date >= contract_start_date
        )
);
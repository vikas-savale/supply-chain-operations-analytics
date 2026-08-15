/*
Creates the master.brands table.
Stores brand master data.
*/

CREATE TABLE master.brands
(
    brand_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    brand_code VARCHAR(30) NOT NULL UNIQUE,
    brand_name VARCHAR(150) NOT NULL UNIQUE,
    brand_owner_company VARCHAR(150),

    brand_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_brands_status
        CHECK (brand_status IN ('active', 'inactive'))
);
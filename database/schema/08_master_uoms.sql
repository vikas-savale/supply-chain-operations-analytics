/*
Creates the master.uoms table.
Stores units of measurement.
*/

CREATE TABLE master.uoms
(
    uom_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    uom_code VARCHAR(20) NOT NULL UNIQUE,
    uom_name VARCHAR(100) NOT NULL UNIQUE,
    uom_category VARCHAR(30) NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_uoms_category
        CHECK (
            uom_category IN (
                'volume',
                'weight',
                'quantity',
                'length',
                'area'
            )
        )
);
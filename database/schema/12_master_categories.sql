/*
Creates the master.categories table.
Stores product category data.
*/

CREATE TABLE master.categories
(
    category_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    category_code VARCHAR(30) NOT NULL UNIQUE,
    category_name VARCHAR(150) NOT NULL,

    category_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_categories_status
        CHECK (category_status IN ('active', 'inactive'))
);
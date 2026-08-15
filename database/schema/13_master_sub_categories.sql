/*
Creates the master.sub_categories table.
Stores product sub-category data.
*/

CREATE TABLE master.sub_categories
(
    sub_category_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    category_id BIGINT NOT NULL,
    sub_category_code VARCHAR(30) NOT NULL UNIQUE,
    sub_category_name VARCHAR(100) NOT NULL,

    description VARCHAR(250),

    sub_category_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_sub_categories_category
        FOREIGN KEY (category_id)
        REFERENCES master.categories(category_id),

    CONSTRAINT uq_sub_categories_category_name
        UNIQUE (category_id, sub_category_name),

    CONSTRAINT chk_sub_categories_status
        CHECK (sub_category_status IN ('active', 'inactive'))
);
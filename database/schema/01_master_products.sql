/*
Creates the master.products table.
Stores product master data.
*/

CREATE TABLE master.products
(
    product_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    sku VARCHAR(30) NOT NULL UNIQUE,
    product_name VARCHAR(150) NOT NULL,

    brand_id BIGINT NOT NULL,
    sub_category_id BIGINT NOT NULL,
    base_uom_id BIGINT NOT NULL,

    pack_type VARCHAR(30) NOT NULL,
    pack_size VARCHAR(30) NOT NULL,
    base_quantity_per_pac NUMERIC(14,3) NOT NULL,

    viscosity_grade VARCHAR(20),

    product_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_products_brand
        FOREIGN KEY (brand_id)
        REFERENCES master.brands (brand_id),

    CONSTRAINT fk_products_sub_category
        FOREIGN KEY (sub_category_id)
        REFERENCES master.sub_categories (sub_category_id),

    CONSTRAINT fk_products_base_uom
        FOREIGN KEY (base_uom_id)
        REFERENCES master.uoms (uom_id),

    CONSTRAINT chk_products_base_quantity_per_pac
        CHECK (base_quantity_per_pac > 0),

    CONSTRAINT chk_products_status
        CHECK (product_status IN ('active', 'inactive', 'discontinued'))
);
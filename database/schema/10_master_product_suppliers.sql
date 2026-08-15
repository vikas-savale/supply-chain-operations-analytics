/*
Creates the master.product_suppliers table.
Stores product and supplier relationships.
*/

CREATE TABLE master.product_suppliers
(
    product_supplier_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    product_id BIGINT NOT NULL,
    supplier_id BIGINT NOT NULL,

    supplier_product_code VARCHAR(50),
    supplier_product_name VARCHAR(150),

    purchase_uom_id BIGINT NOT NULL,

    unit_purchase_price NUMERIC(14,2) NOT NULL DEFAULT 0,
    minimum_order_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,

    lead_time_days SMALLINT NOT NULL DEFAULT 0,

    is_primary_source BOOLEAN NOT NULL DEFAULT FALSE,
    relationship_status VARCHAR(20) NOT NULL DEFAULT 'active',

    effective_from DATE NOT NULL DEFAULT CURRENT_DATE,
    effective_to DATE,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_product_suppliers_product
        FOREIGN KEY (product_id)
        REFERENCES master.products(product_id),

    CONSTRAINT fk_product_suppliers_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES master.suppliers(supplier_id),

    CONSTRAINT fk_product_suppliers_purchase_uom
        FOREIGN KEY (purchase_uom_id)
        REFERENCES master.uoms(uom_id),

    CONSTRAINT uq_product_suppliers_relationship
        UNIQUE (product_id, supplier_id),

    CONSTRAINT chk_product_suppliers_price
        CHECK (unit_purchase_price >= 0),

    CONSTRAINT chk_product_suppliers_moq
        CHECK (minimum_order_quantity >= 0),

    CONSTRAINT chk_product_suppliers_lead_time
        CHECK (lead_time_days >= 0),

    CONSTRAINT chk_product_suppliers_status
        CHECK (relationship_status IN ('active', 'inactive')),

    CONSTRAINT chk_product_suppliers_dates
        CHECK (effective_to IS NULL OR effective_to >= effective_from)
);

CREATE UNIQUE INDEX uq_product_suppliers_one_active_primary
    ON master.product_suppliers (product_id)
    WHERE is_primary_source = TRUE
      AND relationship_status = 'active';
/*
Creates the inventory.stock_audits table.
Stores physical stock audit results.
*/

CREATE TABLE inventory.stock_audits
(
    stock_audit_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    audit_date DATE NOT NULL,

    product_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    sloc_code VARCHAR(10) NOT NULL,
    location_id BIGINT NOT NULL,

    batch_code VARCHAR(50) NOT NULL,

    system_base_quantity NUMERIC(14,3) NOT NULL,
    physical_good_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,
    physical_damaged_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,
    physical_leakage_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,

    variance_base_quantity NUMERIC(14,3) NOT NULL,

    adjustment_reason VARCHAR(30),

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_inventory_stock_audits_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_stock_audits_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_stock_audits_location
        FOREIGN KEY (location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_inventory_stock_audits_system_base_quantity
        CHECK (system_base_quantity >= 0),

    CONSTRAINT chk_inventory_stock_audits_good_base_quantity
        CHECK (physical_good_base_quantity >= 0),

    CONSTRAINT chk_inventory_stock_audits_damaged_base_quantity
        CHECK (physical_damaged_base_quantity >= 0),

    CONSTRAINT chk_inventory_stock_audits_leakage_base_quantity
        CHECK (physical_leakage_base_quantity >= 0),

    CONSTRAINT chk_inventory_stock_audits_variance
        CHECK (
            variance_base_quantity =
            physical_good_base_quantity
            + physical_damaged_base_quantity
            + physical_leakage_base_quantity
            - system_base_quantity
        ),

    CONSTRAINT chk_inventory_stock_audits_adjustment_reason
        CHECK (
            adjustment_reason IS NULL
            OR adjustment_reason IN (
                'damage',
                'theft',
                'counting_error',
                'other'
            )
        )
);
/*
Refines the inventory measurement and stock-location model.

This migration:
- adds SAP storage-location codes to inventory stock
- stores PAC quantity explicitly
- stores normalized base quantity explicitly
- adds PAC and base quantity to inventory movements
- separates physical leakage from physical damage in stock audits
*/

BEGIN;

-- ============================================================
-- 1. Inventory Stock
-- ============================================================

ALTER TABLE inventory.stock
    ADD COLUMN sloc_code VARCHAR(10) NOT NULL,
    ADD COLUMN pac_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0;

ALTER TABLE inventory.stock
    DROP CONSTRAINT uq_inventory_stock_position;

ALTER TABLE inventory.stock
    ADD CONSTRAINT uq_inventory_stock_position
        UNIQUE (
            product_id,
            warehouse_id,
            sloc_code,
            location_id,
            batch_code,
            stock_status
        );

ALTER TABLE inventory.stock
    ADD CONSTRAINT chk_inventory_stock_pac_quantity
        CHECK (pac_quantity >= 0);

ALTER TABLE inventory.stock
    ADD CONSTRAINT chk_inventory_stock_base_quantity
        CHECK (base_quantity >= 0);

ALTER TABLE inventory.stock
    DROP COLUMN quantity;


-- ============================================================
-- 2. Inventory Movements
-- ============================================================

ALTER TABLE inventory.movements
    ADD COLUMN sloc_code VARCHAR(10) NOT NULL,
    ADD COLUMN pac_quantity NUMERIC(14,3) NOT NULL,
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE inventory.movements
    ADD CONSTRAINT chk_inventory_movements_pac_quantity
        CHECK (pac_quantity > 0);

ALTER TABLE inventory.movements
    ADD CONSTRAINT chk_inventory_movements_base_quantity
        CHECK (base_quantity > 0);

ALTER TABLE inventory.movements
    DROP COLUMN quantity;


-- ============================================================
-- 3. Stock Audits
-- ============================================================

ALTER TABLE inventory.stock_audits
    RENAME COLUMN system_quantity
        TO system_base_quantity;

ALTER TABLE inventory.stock_audits
    RENAME COLUMN physical_good_quantity
        TO physical_good_base_quantity;

ALTER TABLE inventory.stock_audits
    RENAME COLUMN physical_damaged_quantity
        TO physical_damaged_base_quantity;

ALTER TABLE inventory.stock_audits
    ADD COLUMN physical_leakage_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0;

ALTER TABLE inventory.stock_audits
    DROP CONSTRAINT chk_inventory_stock_audits_system_quantity;

ALTER TABLE inventory.stock_audits
    DROP CONSTRAINT chk_inventory_stock_audits_good_quantity;

ALTER TABLE inventory.stock_audits
    DROP CONSTRAINT chk_inventory_stock_audits_damaged_quantity;

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT chk_inventory_stock_audits_system_base_quantity
        CHECK (system_base_quantity >= 0);

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT chk_inventory_stock_audits_good_base_quantity
        CHECK (physical_good_base_quantity >= 0);

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT chk_inventory_stock_audits_damaged_base_quantity
        CHECK (physical_damaged_base_quantity >= 0);

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT chk_inventory_stock_audits_leakage_base_quantity
        CHECK (physical_leakage_base_quantity >= 0);

ALTER TABLE inventory.stock_audits
    DROP CONSTRAINT chk_inventory_stock_audits_variance;

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT chk_inventory_stock_audits_variance
        CHECK (
            variance_quantity =
            physical_good_base_quantity
            + physical_damaged_base_quantity
            + physical_leakage_base_quantity
            - system_base_quantity
        );

COMMIT;
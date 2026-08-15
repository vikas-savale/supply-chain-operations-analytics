/*
Refines the product and supplier reference model.

This migration:
- connects products to brand, sub-category and UOM master data
- simplifies the category hierarchy
- connects suppliers to payment terms
- defines primary source logic for product suppliers
*/

BEGIN;

-- ============================================================
-- 1. Products: add master-data relationships
-- ============================================================

ALTER TABLE master.products
    ADD COLUMN brand_id BIGINT,
    ADD COLUMN sub_category_id BIGINT,
    ADD COLUMN base_uom_id BIGINT;

ALTER TABLE master.products
    ADD CONSTRAINT fk_products_brand
        FOREIGN KEY (brand_id)
        REFERENCES master.brands (brand_id),

    ADD CONSTRAINT fk_products_sub_category
        FOREIGN KEY (sub_category_id)
        REFERENCES master.sub_categories (sub_category_id),

    ADD CONSTRAINT fk_products_base_uom
        FOREIGN KEY (base_uom_id)
        REFERENCES master.uoms (uom_id);

ALTER TABLE master.products
    ALTER COLUMN brand_id SET NOT NULL,
    ALTER COLUMN sub_category_id SET NOT NULL,
    ALTER COLUMN base_uom_id SET NOT NULL;

ALTER TABLE master.products
    DROP COLUMN brand,
    DROP COLUMN category,
    DROP COLUMN sub_category,
    DROP COLUMN unit_of_measure;


-- ============================================================
-- 2. Categories: keep a single hierarchy model
-- ============================================================

ALTER TABLE master.categories
    DROP COLUMN parent_category_id,
    DROP COLUMN category_level;


-- ============================================================
-- 3. Suppliers: use reusable payment terms
-- ============================================================

ALTER TABLE master.suppliers
    ADD COLUMN payment_term_id BIGINT;

ALTER TABLE master.suppliers
    ADD CONSTRAINT fk_suppliers_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id);

ALTER TABLE master.suppliers
    ALTER COLUMN payment_term_id SET NOT NULL;

ALTER TABLE master.suppliers
    DROP COLUMN payment_terms_days;


-- ============================================================
-- 4. Product suppliers: clarify primary source
-- ============================================================

ALTER TABLE master.product_suppliers
    RENAME COLUMN is_preferred_supplier TO is_primary_source;


-- ============================================================
-- 5. One active primary source per product
-- ============================================================

CREATE UNIQUE INDEX uq_product_suppliers_one_active_primary
    ON master.product_suppliers (product_id)
    WHERE is_primary_source = TRUE
      AND relationship_status = 'active';

COMMIT;
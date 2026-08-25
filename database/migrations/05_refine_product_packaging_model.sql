/*
Adds structured packaging attributes to the product master.

This migration:
- stores the packaging type separately from the display pack size
- stores the base quantity represented by one PAC
*/

BEGIN;

ALTER TABLE master.products
    ADD COLUMN pack_type VARCHAR(30) NOT NULL,
    ADD COLUMN base_quantity_per_pac NUMERIC(14,3) NOT NULL;

ALTER TABLE master.products
    ADD CONSTRAINT chk_products_base_quantity_per_pac
        CHECK (base_quantity_per_pac > 0);

COMMIT;
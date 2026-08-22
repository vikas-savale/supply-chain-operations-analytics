/*
Adds batch tracking to goods receipt items.
*/

BEGIN;

ALTER TABLE procurement.goods_receipt_items
    ADD COLUMN batch_code VARCHAR(50) NOT NULL;

COMMIT;
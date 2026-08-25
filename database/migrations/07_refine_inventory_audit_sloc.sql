/*
Adds SAP storage-location tracking to stock audit records.

This migration:
- stores the SAP storage-location code for each stock audit
- renames the audit variance field to clarify that it uses the base quantity measure
*/

BEGIN;

ALTER TABLE inventory.stock_audits
    ADD COLUMN sloc_code VARCHAR(10) NOT NULL;

ALTER TABLE inventory.stock_audits
    RENAME COLUMN variance_quantity TO variance_base_quantity;

COMMIT;
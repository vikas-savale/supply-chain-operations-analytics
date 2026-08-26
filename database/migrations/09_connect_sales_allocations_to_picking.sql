/*
Connects sales order allocations to warehouse picking items.

This migration:
- links picking items to sales order allocations
- keeps the existing stock reference on picking items
- allows an allocation to be fulfilled through multiple picking items
*/

BEGIN;

ALTER TABLE warehouse.picking_items
    ADD COLUMN sales_order_allocation_id BIGINT NOT NULL;

ALTER TABLE warehouse.picking_items
    ADD CONSTRAINT fk_picking_items_sales_order_allocation
        FOREIGN KEY (sales_order_allocation_id)
        REFERENCES sales.sales_order_allocations (sales_order_allocation_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT;

COMMIT;
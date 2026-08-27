/*
Adds the sales order allocation reference to warehouse picking items.

This keeps the final schema consistent with the sales allocation to picking flow.
*/

ALTER TABLE warehouse.picking_items
    ADD COLUMN sales_order_allocation_id BIGINT NOT NULL;

ALTER TABLE warehouse.picking_items
    ADD CONSTRAINT fk_picking_items_sales_order_allocation
        FOREIGN KEY (sales_order_allocation_id)
        REFERENCES sales.sales_order_allocations (sales_order_allocation_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT;

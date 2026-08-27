/*
Adds consistency checks between related transaction records.

This keeps the final schema consistent with the transaction relationships.
*/

-- ============================================================
-- 1. Customer and Ship-To Location
-- ============================================================

ALTER TABLE master.customer_locations
    ADD CONSTRAINT uq_customer_locations_id_customer
        UNIQUE (customer_location_id, customer_id);

ALTER TABLE sales.sales_orders
    ADD CONSTRAINT fk_sales_orders_customer_location_match
        FOREIGN KEY (customer_location_id, customer_id)
        REFERENCES master.customer_locations (
            customer_location_id,
            customer_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 2. Inventory Stock and Physical Location
-- ============================================================

ALTER TABLE master.locations
    ADD CONSTRAINT uq_locations_id_warehouse
        UNIQUE (location_id, warehouse_id);

ALTER TABLE inventory.stock
    ADD CONSTRAINT fk_inventory_stock_location_match
        FOREIGN KEY (location_id, warehouse_id)
        REFERENCES master.locations (
            location_id,
            warehouse_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 3. Inventory Movements and Physical Location
-- ============================================================

ALTER TABLE inventory.movements
    ADD CONSTRAINT fk_inventory_movements_location_match
        FOREIGN KEY (location_id, warehouse_id)
        REFERENCES master.locations (
            location_id,
            warehouse_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 4. Stock Audits and Physical Location
-- ============================================================

ALTER TABLE inventory.stock_audits
    ADD CONSTRAINT fk_inventory_stock_audits_location_match
        FOREIGN KEY (location_id, warehouse_id)
        REFERENCES master.locations (
            location_id,
            warehouse_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 5. Picking Item and Allocation Stock
-- ============================================================

ALTER TABLE sales.sales_order_allocations
    ADD CONSTRAINT uq_sales_order_allocations_id_stock
        UNIQUE (sales_order_allocation_id, stock_id);

ALTER TABLE warehouse.picking_items
    ADD CONSTRAINT fk_picking_items_allocation_stock_match
        FOREIGN KEY (
            sales_order_allocation_id,
            stock_id
        )
        REFERENCES sales.sales_order_allocations (
            sales_order_allocation_id,
            stock_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 6. Picking Item and Stock Location
-- ============================================================

ALTER TABLE inventory.stock
    ADD CONSTRAINT uq_inventory_stock_id_location
        UNIQUE (stock_id, location_id);

ALTER TABLE warehouse.picking_items
    ADD CONSTRAINT fk_picking_items_stock_location_match
        FOREIGN KEY (stock_id, source_location_id)
        REFERENCES inventory.stock (
            stock_id,
            location_id
        )
        ON UPDATE CASCADE
        ON DELETE RESTRICT;


-- ============================================================
-- 7. Allocation Product and Stock Product
-- ============================================================

CREATE OR REPLACE FUNCTION sales.check_allocation_product_match()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM sales.sales_order_items soi
        JOIN inventory.stock s
            ON s.stock_id = NEW.stock_id
        WHERE soi.sales_order_item_id = NEW.sales_order_item_id
          AND soi.product_id = s.product_id
    ) THEN
        RAISE EXCEPTION
            'Sales order item product does not match allocated stock product';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_sales_order_allocations_product_match
BEFORE INSERT OR UPDATE OF sales_order_item_id, stock_id
ON sales.sales_order_allocations
FOR EACH ROW
EXECUTE FUNCTION sales.check_allocation_product_match();


-- ============================================================
-- 8. Shipment Item and Dispatch Match
-- ============================================================

CREATE OR REPLACE FUNCTION logistics.check_shipment_item_dispatch_match()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM logistics.shipments sh
        JOIN warehouse.dispatch_items di
            ON di.dispatch_item_id = NEW.dispatch_item_id
        WHERE sh.shipment_id = NEW.shipment_id
          AND sh.dispatch_id = di.dispatch_id
    ) THEN
        RAISE EXCEPTION
            'Shipment item does not belong to the shipment dispatch';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_shipment_items_dispatch_match
BEFORE INSERT OR UPDATE OF shipment_id, dispatch_item_id
ON logistics.shipment_items
FOR EACH ROW
EXECUTE FUNCTION logistics.check_shipment_item_dispatch_match();


-- ============================================================
-- 9. Delivery Item and Shipment Match
-- ============================================================

CREATE OR REPLACE FUNCTION logistics.check_delivery_item_shipment_match()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM logistics.deliveries d
        JOIN logistics.shipment_items si
            ON si.shipment_item_id = NEW.shipment_item_id
        WHERE d.delivery_id = NEW.delivery_id
          AND d.shipment_id = si.shipment_id
    ) THEN
        RAISE EXCEPTION
            'Delivery item does not belong to the delivery shipment';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_delivery_items_shipment_match
BEFORE INSERT OR UPDATE OF delivery_id, shipment_item_id
ON logistics.delivery_items
FOR EACH ROW
EXECUTE FUNCTION logistics.check_delivery_item_shipment_match();
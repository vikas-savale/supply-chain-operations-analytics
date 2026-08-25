/*
Refines transaction line quantities across procurement, warehouse and logistics.

This migration:
- stores PAC quantity explicitly
- stores normalized base quantity explicitly
- removes ambiguous generic quantity fields
- keeps received, accepted and rejected quantities separate
*/

BEGIN;

-- ============================================================
-- 1. Purchase Order Items
-- ============================================================

ALTER TABLE procurement.purchase_order_items
    RENAME COLUMN ordered_quantity
        TO ordered_pac_quantity;

ALTER TABLE procurement.purchase_order_items
    ADD COLUMN ordered_base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE procurement.purchase_order_items
    ADD CONSTRAINT chk_purchase_order_items_ordered_base_quantity
        CHECK (ordered_base_quantity > 0);


-- ============================================================
-- 2. Goods Receipt Items
-- ============================================================

ALTER TABLE procurement.goods_receipt_items
    RENAME COLUMN received_quantity
        TO received_pac_quantity;

ALTER TABLE procurement.goods_receipt_items
    RENAME COLUMN accepted_quantity
        TO accepted_pac_quantity;

ALTER TABLE procurement.goods_receipt_items
    RENAME COLUMN rejected_quantity
        TO rejected_pac_quantity;

ALTER TABLE procurement.goods_receipt_items
    ADD COLUMN received_base_quantity NUMERIC(14,3) NOT NULL,
    ADD COLUMN accepted_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,
    ADD COLUMN rejected_base_quantity NUMERIC(14,3) NOT NULL DEFAULT 0;

ALTER TABLE procurement.goods_receipt_items
    ADD CONSTRAINT chk_goods_receipt_items_received_base_quantity
        CHECK (received_base_quantity > 0);

ALTER TABLE procurement.goods_receipt_items
    ADD CONSTRAINT chk_goods_receipt_items_accepted_base_quantity
        CHECK (accepted_base_quantity >= 0);

ALTER TABLE procurement.goods_receipt_items
    ADD CONSTRAINT chk_goods_receipt_items_rejected_base_quantity
        CHECK (rejected_base_quantity >= 0);

ALTER TABLE procurement.goods_receipt_items
    ADD CONSTRAINT chk_goods_receipt_items_base_quantity_split
        CHECK (
            accepted_base_quantity
            + rejected_base_quantity
            = received_base_quantity
        );


-- ============================================================
-- 3. Putaway Items
-- ============================================================

ALTER TABLE warehouse.putaway_items
    RENAME COLUMN quantity
        TO pac_quantity;

ALTER TABLE warehouse.putaway_items
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE warehouse.putaway_items
    ADD CONSTRAINT chk_putaway_items_base_quantity
        CHECK (base_quantity > 0);


-- ============================================================
-- 4. Picking Items
-- ============================================================

ALTER TABLE warehouse.picking_items
    RENAME COLUMN quantity
        TO pac_quantity;

ALTER TABLE warehouse.picking_items
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE warehouse.picking_items
    ADD CONSTRAINT chk_picking_items_base_quantity
        CHECK (base_quantity > 0);


-- ============================================================
-- 5. Dispatch Items
-- ============================================================

ALTER TABLE warehouse.dispatch_items
    RENAME COLUMN quantity
        TO pac_quantity;

ALTER TABLE warehouse.dispatch_items
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE warehouse.dispatch_items
    ADD CONSTRAINT chk_dispatch_items_base_quantity
        CHECK (base_quantity > 0);


-- ============================================================
-- 6. Shipment Items
-- ============================================================

ALTER TABLE logistics.shipment_items
    RENAME COLUMN quantity
        TO pac_quantity;

ALTER TABLE logistics.shipment_items
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE logistics.shipment_items
    ADD CONSTRAINT chk_shipment_items_base_quantity
        CHECK (base_quantity > 0);


-- ============================================================
-- 7. Delivery Items
-- ============================================================

ALTER TABLE logistics.delivery_items
    RENAME COLUMN quantity
        TO pac_quantity;

ALTER TABLE logistics.delivery_items
    ADD COLUMN base_quantity NUMERIC(14,3) NOT NULL;

ALTER TABLE logistics.delivery_items
    ADD CONSTRAINT chk_delivery_items_base_quantity
        CHECK (base_quantity > 0);

COMMIT;
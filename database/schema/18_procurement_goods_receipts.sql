/*
Creates the procurement.goods_receipts table.
Stores goods receipt header data.
*/

CREATE TABLE procurement.goods_receipts
(
    goods_receipt_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    grn_number VARCHAR(30) NOT NULL UNIQUE,

    purchase_order_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    vehicle_id BIGINT,

    receipt_date DATE NOT NULL,

    receipt_status VARCHAR(20) NOT NULL DEFAULT 'pending',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_goods_receipts_purchase_order
        FOREIGN KEY (purchase_order_id)
        REFERENCES procurement.purchase_orders (purchase_order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_goods_receipts_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_goods_receipts_vehicle
        FOREIGN KEY (vehicle_id)
        REFERENCES master.vehicles (vehicle_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_goods_receipts_status
        CHECK (
            receipt_status IN (
                'pending',
                'received',
                'cancelled'
            )
        )
);
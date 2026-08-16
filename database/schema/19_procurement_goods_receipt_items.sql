/*
Creates the procurement.goods_receipt_items table.
Stores product lines received against a goods receipt.
*/

CREATE TABLE procurement.goods_receipt_items
(
    goods_receipt_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    goods_receipt_id BIGINT NOT NULL,
    purchase_order_item_id BIGINT NOT NULL,

    line_number SMALLINT NOT NULL,

    product_id BIGINT NOT NULL,
    receipt_uom_id BIGINT NOT NULL,

    received_quantity NUMERIC(14,3) NOT NULL,
    accepted_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,
    rejected_quantity NUMERIC(14,3) NOT NULL DEFAULT 0,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_goods_receipt_items_goods_receipt
        FOREIGN KEY (goods_receipt_id)
        REFERENCES procurement.goods_receipts (goods_receipt_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_goods_receipt_items_purchase_order_item
        FOREIGN KEY (purchase_order_item_id)
        REFERENCES procurement.purchase_order_items (purchase_order_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_goods_receipt_items_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_goods_receipt_items_uom
        FOREIGN KEY (receipt_uom_id)
        REFERENCES master.uoms (uom_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_goods_receipt_items_line
        UNIQUE (goods_receipt_id, line_number),

    CONSTRAINT chk_goods_receipt_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_goods_receipt_items_received_quantity
        CHECK (received_quantity > 0),

    CONSTRAINT chk_goods_receipt_items_accepted_quantity
        CHECK (accepted_quantity >= 0),

    CONSTRAINT chk_goods_receipt_items_rejected_quantity
        CHECK (rejected_quantity >= 0),

    CONSTRAINT chk_goods_receipt_items_quantity_split
        CHECK (accepted_quantity + rejected_quantity = received_quantity)
);
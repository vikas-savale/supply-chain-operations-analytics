/*
Creates the procurement.purchase_order_items table.
Stores product lines within a purchase order.
*/

CREATE TABLE procurement.purchase_order_items
(
    purchase_order_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    purchase_order_id BIGINT NOT NULL,
    line_number SMALLINT NOT NULL,

    product_id BIGINT NOT NULL,
    purchase_uom_id BIGINT NOT NULL,

    ordered_quantity NUMERIC(14,3) NOT NULL,
    unit_cost NUMERIC(14,2) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_purchase_order_items_purchase_order
        FOREIGN KEY (purchase_order_id)
        REFERENCES procurement.purchase_orders (purchase_order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_purchase_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_purchase_order_items_uom
        FOREIGN KEY (purchase_uom_id)
        REFERENCES master.uoms (uom_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_purchase_order_items_line
        UNIQUE (purchase_order_id, line_number),

    CONSTRAINT chk_purchase_order_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_purchase_order_items_quantity
        CHECK (ordered_quantity > 0),

    CONSTRAINT chk_purchase_order_items_unit_cost
        CHECK (unit_cost >= 0)
);
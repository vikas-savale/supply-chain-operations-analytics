/*
Creates the logistics.delivery_items table.
Stores quantities delivered against shipment items.
*/

CREATE TABLE logistics.delivery_items
(
    delivery_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    delivery_id BIGINT NOT NULL,
    shipment_item_id BIGINT NOT NULL,

    line_number SMALLINT NOT NULL,

    pac_quantity NUMERIC(14,3) NOT NULL,
    base_quantity NUMERIC(14,3) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_delivery_items_delivery
        FOREIGN KEY (delivery_id)
        REFERENCES logistics.deliveries (delivery_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_delivery_items_shipment_item
        FOREIGN KEY (shipment_item_id)
        REFERENCES logistics.shipment_items (shipment_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_delivery_items_line
        UNIQUE (delivery_id, line_number),

    CONSTRAINT chk_delivery_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_delivery_items_pac_quantity
        CHECK (pac_quantity > 0),

    CONSTRAINT chk_delivery_items_base_quantity
        CHECK (base_quantity > 0)
);
/*
Creates the logistics.shipment_items table.
Stores quantities shipped against warehouse dispatch items.
*/

CREATE TABLE logistics.shipment_items
(
    shipment_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    shipment_id BIGINT NOT NULL,
    dispatch_item_id BIGINT NOT NULL,

    line_number SMALLINT NOT NULL,

    quantity NUMERIC(14,3) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_shipment_items_shipment
        FOREIGN KEY (shipment_id)
        REFERENCES logistics.shipments (shipment_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_shipment_items_dispatch_item
        FOREIGN KEY (dispatch_item_id)
        REFERENCES warehouse.dispatch_items (dispatch_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_shipment_items_line
        UNIQUE (shipment_id, line_number),

    CONSTRAINT chk_shipment_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_shipment_items_quantity
        CHECK (quantity > 0)
);
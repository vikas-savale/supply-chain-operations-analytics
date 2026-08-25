/*
Creates the warehouse.putaway_items table.
Stores product quantities moved during putaway.
*/

CREATE TABLE warehouse.putaway_items
(
    putaway_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    putaway_id BIGINT NOT NULL,
    goods_receipt_item_id BIGINT NOT NULL,

    line_number SMALLINT NOT NULL,

    source_location_id BIGINT NOT NULL,
    destination_location_id BIGINT NOT NULL,

    pac_quantity NUMERIC(14,3) NOT NULL,
    base_quantity NUMERIC(14,3) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_putaway_items_putaway
        FOREIGN KEY (putaway_id)
        REFERENCES warehouse.putaways (putaway_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_putaway_items_goods_receipt_item
        FOREIGN KEY (goods_receipt_item_id)
        REFERENCES procurement.goods_receipt_items (goods_receipt_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_putaway_items_source_location
        FOREIGN KEY (source_location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_putaway_items_destination_location
        FOREIGN KEY (destination_location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_putaway_items_line
        UNIQUE (putaway_id, line_number),

    CONSTRAINT chk_putaway_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_putaway_items_pac_quantity
        CHECK (pac_quantity > 0),

    CONSTRAINT chk_putaway_items_base_quantity
        CHECK (base_quantity > 0),

    CONSTRAINT chk_putaway_items_locations
        CHECK (source_location_id <> destination_location_id)
);
/*
Creates the warehouse.picking_items table.
Stores stock quantities picked from warehouse locations.
*/

CREATE TABLE warehouse.picking_items
(
    picking_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    picking_id BIGINT NOT NULL,
    line_number SMALLINT NOT NULL,

    stock_id BIGINT NOT NULL,
    source_location_id BIGINT NOT NULL,

    quantity NUMERIC(14,3) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_picking_items_picking
        FOREIGN KEY (picking_id)
        REFERENCES warehouse.pickings (picking_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_picking_items_stock
        FOREIGN KEY (stock_id)
        REFERENCES inventory.stock (stock_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_picking_items_source_location
        FOREIGN KEY (source_location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_picking_items_line
        UNIQUE (picking_id, line_number),

    CONSTRAINT chk_picking_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_picking_items_quantity
        CHECK (quantity > 0)
);
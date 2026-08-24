/*
Creates the warehouse.dispatch_items table.
Stores quantities loaded and dispatched against picking items.
*/

CREATE TABLE warehouse.dispatch_items
(
    dispatch_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    dispatch_id BIGINT NOT NULL,
    picking_item_id BIGINT NOT NULL,

    line_number SMALLINT NOT NULL,

    quantity NUMERIC(14,3) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_dispatch_items_dispatch
        FOREIGN KEY (dispatch_id)
        REFERENCES warehouse.dispatches (dispatch_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_dispatch_items_picking_item
        FOREIGN KEY (picking_item_id)
        REFERENCES warehouse.picking_items (picking_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_dispatch_items_line
        UNIQUE (dispatch_id, line_number),

    CONSTRAINT chk_dispatch_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_dispatch_items_quantity
        CHECK (quantity > 0)
);
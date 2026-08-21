/*
Creates the inventory.movements table.
Stores inventory movement history.
*/

CREATE TABLE inventory.movements
(
    movement_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    movement_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    product_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,

    batch_code VARCHAR(50) NOT NULL,

    movement_type VARCHAR(20) NOT NULL,

    quantity NUMERIC(14,3) NOT NULL,

    stock_status VARCHAR(20) NOT NULL,

    reference_type VARCHAR(30),
    reference_id BIGINT,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_inventory_movements_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_movements_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_movements_location
        FOREIGN KEY (location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_inventory_movements_type
        CHECK (
            movement_type IN (
                'inbound',
                'outbound',
                'transfer_in',
                'transfer_out',
                'damage',
                'adjustment',
                'cycle_count'
            )
        ),

    CONSTRAINT chk_inventory_movements_quantity
        CHECK (quantity > 0),

    CONSTRAINT chk_inventory_movements_status
        CHECK (
            stock_status IN (
                'available',
                'reserved',
                'damaged',
                'quality_hold',
                'blocked'
            )
        )
);
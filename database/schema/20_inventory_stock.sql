/*
Creates the inventory.stock table.
Stores current stock by product, warehouse, location, batch and status.
*/

CREATE TABLE inventory.stock
(
    stock_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    product_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,

    batch_code VARCHAR(50) NOT NULL,

    stock_status VARCHAR(20) NOT NULL DEFAULT 'available',

    quantity NUMERIC(14,3) NOT NULL DEFAULT 0,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_inventory_stock_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_stock_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_inventory_stock_location
        FOREIGN KEY (location_id)
        REFERENCES master.locations (location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_inventory_stock_position
        UNIQUE (
            product_id,
            warehouse_id,
            location_id,
            batch_code,
            stock_status
        ),

    CONSTRAINT chk_inventory_stock_status
        CHECK (
            stock_status IN (
                'available',
                'reserved',
                'damaged',
                'quality_hold',
                'blocked'
            )
        ),

    CONSTRAINT chk_inventory_stock_quantity
        CHECK (quantity >= 0)
);
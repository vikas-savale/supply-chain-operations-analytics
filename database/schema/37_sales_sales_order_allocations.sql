/*
Creates the sales.sales_order_allocations table.
Stores stock allocated to sales order items.
*/

CREATE TABLE sales.sales_order_allocations
(
    sales_order_allocation_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    sales_order_item_id BIGINT NOT NULL,
    stock_id BIGINT NOT NULL,

    allocation_date DATE NOT NULL DEFAULT CURRENT_DATE,

    allocated_pac_quantity NUMERIC(14,3) NOT NULL,
    allocated_base_quantity NUMERIC(14,3) NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'allocated',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_sales_order_allocations_sales_order_item
        FOREIGN KEY (sales_order_item_id)
        REFERENCES sales.sales_order_items (sales_order_item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sales_order_allocations_stock
        FOREIGN KEY (stock_id)
        REFERENCES inventory.stock (stock_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_sales_order_allocations_pac_quantity
        CHECK (allocated_pac_quantity > 0),

    CONSTRAINT chk_sales_order_allocations_base_quantity
        CHECK (allocated_base_quantity > 0),

    CONSTRAINT chk_sales_order_allocations_status
        CHECK (
            status IN (
                'allocated',
                'released',
                'fulfilled',
                'cancelled'
            )
        )
);
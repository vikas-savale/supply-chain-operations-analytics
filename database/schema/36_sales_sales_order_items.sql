/*
Creates the sales.sales_order_items table.
Stores product lines within a sales order.
*/

CREATE TABLE sales.sales_order_items
(
    sales_order_item_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    sales_order_id BIGINT NOT NULL,
    line_number SMALLINT NOT NULL,

    product_id BIGINT NOT NULL,

    ordered_pac_quantity NUMERIC(14,3) NOT NULL,
    ordered_base_quantity NUMERIC(14,3) NOT NULL,

    unit_price NUMERIC(14,2) NOT NULL,
    final_rate NUMERIC(14,2) NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_sales_order_items_sales_order
        FOREIGN KEY (sales_order_id)
        REFERENCES sales.sales_orders (sales_order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sales_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES master.products (product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_sales_order_items_line
        UNIQUE (sales_order_id, line_number),

    CONSTRAINT chk_sales_order_items_line_number
        CHECK (line_number > 0),

    CONSTRAINT chk_sales_order_items_pac_quantity
        CHECK (ordered_pac_quantity > 0),

    CONSTRAINT chk_sales_order_items_base_quantity
        CHECK (ordered_base_quantity > 0),

    CONSTRAINT chk_sales_order_items_unit_price
        CHECK (unit_price >= 0),

    CONSTRAINT chk_sales_order_items_final_rate
        CHECK (final_rate >= 0)
);
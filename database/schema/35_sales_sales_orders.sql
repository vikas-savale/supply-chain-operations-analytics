/*
Creates the sales.sales_orders table.
Stores customer sales order header data.
*/

CREATE TABLE sales.sales_orders
(
    sales_order_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    sales_order_number VARCHAR(30) NOT NULL UNIQUE,

    customer_id BIGINT NOT NULL,
    customer_location_id BIGINT NOT NULL,

    order_date DATE NOT NULL,

    customer_po_number VARCHAR(50),
    customer_po_date DATE,

    payment_term_id BIGINT NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'confirmed',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_sales_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES master.customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sales_orders_customer_location
        FOREIGN KEY (customer_location_id)
        REFERENCES master.customer_locations (customer_location_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sales_orders_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_sales_orders_status
        CHECK (
            status IN (
                'confirmed',
                'partially_fulfilled',
                'completed',
                'cancelled'
            )
        )
);
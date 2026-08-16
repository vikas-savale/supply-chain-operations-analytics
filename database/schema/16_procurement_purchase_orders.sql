/*
Creates the procurement.purchase_orders table.
Stores purchase order header data.
*/

CREATE TABLE procurement.purchase_orders
(
    purchase_order_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    po_number VARCHAR(30) NOT NULL UNIQUE,

    supplier_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    payment_term_id BIGINT NOT NULL,

    po_date DATE NOT NULL,
    expected_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'draft',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_purchase_orders_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES master.suppliers (supplier_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_purchase_orders_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_purchase_orders_payment_term
        FOREIGN KEY (payment_term_id)
        REFERENCES master.payment_terms (payment_term_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_purchase_orders_status
        CHECK (
            status IN (
                'draft',
                'approved',
                'sent',
                'partially_received',
                'received',
                'cancelled'
            )
        ),

    CONSTRAINT chk_purchase_orders_dates
        CHECK (expected_date >= po_date)
);
/*
Creates the logistics.deliveries table.
Stores customer delivery header data.
*/

CREATE TABLE logistics.deliveries
(
    delivery_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    delivery_number VARCHAR(30) NOT NULL UNIQUE,

    shipment_id BIGINT NOT NULL,

    delivery_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'planned',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_deliveries_shipment
        FOREIGN KEY (shipment_id)
        REFERENCES logistics.shipments (shipment_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_deliveries_status
        CHECK (
            status IN (
                'planned',
                'delivered',
                'delayed',
                'cancelled'
            )
        )
);
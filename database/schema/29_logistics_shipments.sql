/*
Creates the logistics.shipments table.
Stores shipment and transport header data.
*/

CREATE TABLE logistics.shipments
(
    shipment_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    shipment_number VARCHAR(30) NOT NULL UNIQUE,

    dispatch_id BIGINT NOT NULL,
    transporter_id BIGINT NOT NULL,
    vehicle_id BIGINT NOT NULL,

    shipment_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'planned',

    expected_delivery_date DATE,
    actual_delivery_date DATE,

    tracking_reference VARCHAR(50),

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_shipments_dispatch
        FOREIGN KEY (dispatch_id)
        REFERENCES warehouse.dispatches (dispatch_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_shipments_transporter
        FOREIGN KEY (transporter_id)
        REFERENCES master.transporters (transporter_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_shipments_vehicle
        FOREIGN KEY (vehicle_id)
        REFERENCES master.vehicles (vehicle_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_shipments_status
        CHECK (
            status IN (
                'planned',
                'in_transit',
                'delivered',
                'delayed',
                'cancelled'
            )
        ),

    CONSTRAINT chk_shipments_dates
        CHECK (
            expected_delivery_date IS NULL
            OR expected_delivery_date >= shipment_date
        ),

    CONSTRAINT chk_shipments_actual_delivery_date
        CHECK (
            actual_delivery_date IS NULL
            OR actual_delivery_date >= shipment_date
        )
);
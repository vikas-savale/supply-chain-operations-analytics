/*
Creates the logistics.shipment_events table.
Stores the operational event timeline for shipments.
*/

CREATE TABLE logistics.shipment_events
(
    shipment_event_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    shipment_id BIGINT NOT NULL,

    event_type VARCHAR(30) NOT NULL,
    event_time TIMESTAMP NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_shipment_events_shipment
        FOREIGN KEY (shipment_id)
        REFERENCES logistics.shipments (shipment_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_shipment_events_type
        CHECK (
            event_type IN (
                'vehicle_arrived',
                'loading_started',
                'loading_completed',
                'departed',
                'delivery_completed'
            )
        )
);

CREATE INDEX idx_shipment_events_timeline
    ON logistics.shipment_events (shipment_id, event_time);
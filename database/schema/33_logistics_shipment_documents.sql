/*
Creates the logistics.shipment_documents table.
Stores document references associated with shipments.
*/

CREATE TABLE logistics.shipment_documents
(
    shipment_document_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    shipment_id BIGINT NOT NULL,

    document_type VARCHAR(30) NOT NULL,
    document_number VARCHAR(50) NOT NULL,
    document_date DATE NOT NULL,

    document_status VARCHAR(20) NOT NULL DEFAULT 'issued',

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_shipment_documents_shipment
        FOREIGN KEY (shipment_id)
        REFERENCES logistics.shipments (shipment_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_shipment_documents_type
        CHECK (
            document_type IN (
                'invoice',
                'e_way_bill',
                'lorry_receipt',
                'pod'
            )
        ),

    CONSTRAINT chk_shipment_documents_status
        CHECK (
            document_status IN (
                'draft',
                'issued',
                'cancelled'
            )
        ),

    CONSTRAINT uq_shipment_documents_reference
        UNIQUE (
            shipment_id,
            document_type,
            document_number
        )
);
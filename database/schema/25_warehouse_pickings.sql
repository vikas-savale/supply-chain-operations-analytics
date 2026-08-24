/*
Creates the warehouse.pickings table.
Stores warehouse picking header data.
*/

CREATE TABLE warehouse.pickings
(
    picking_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    picking_number VARCHAR(30) NOT NULL UNIQUE,

    warehouse_id BIGINT NOT NULL,
    picking_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'pending',

    employee_id BIGINT NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_pickings_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_pickings_employee
        FOREIGN KEY (employee_id)
        REFERENCES master.employees (employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_pickings_status
        CHECK (
            status IN (
                'pending',
                'partial',
                'completed',
                'cancelled'
            )
        )
);
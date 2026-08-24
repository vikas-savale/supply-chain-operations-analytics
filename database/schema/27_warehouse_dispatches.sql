/*
Creates the warehouse.dispatches table.
Stores warehouse dispatch and loading header data.
*/

CREATE TABLE warehouse.dispatches
(
    dispatch_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    dispatch_number VARCHAR(30) NOT NULL UNIQUE,

    warehouse_id BIGINT NOT NULL,
    dispatch_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'pending',

    vehicle_id BIGINT NOT NULL,
    employee_id BIGINT NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_dispatches_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_dispatches_vehicle
        FOREIGN KEY (vehicle_id)
        REFERENCES master.vehicles (vehicle_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_dispatches_employee
        FOREIGN KEY (employee_id)
        REFERENCES master.employees (employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_dispatches_status
        CHECK (
            status IN (
                'pending',
                'loading',
                'loaded',
                'dispatched',
                'cancelled'
            )
        )
);
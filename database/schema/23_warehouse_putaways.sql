/*
Creates the warehouse.putaways table.
Stores warehouse putaway header data.
*/

CREATE TABLE warehouse.putaways
(
    putaway_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    putaway_number VARCHAR(30) NOT NULL UNIQUE,

    warehouse_id BIGINT NOT NULL,
    putaway_date DATE NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'pending',

    employee_id BIGINT NOT NULL,

    notes TEXT,

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_putaways_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_putaways_employee
        FOREIGN KEY (employee_id)
        REFERENCES master.employees (employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_putaways_status
        CHECK (
            status IN (
                'pending',
                'partial',
                'completed',
                'cancelled'
            )
        )
);
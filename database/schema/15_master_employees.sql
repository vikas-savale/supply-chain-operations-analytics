/*
Creates the master.employees table.
Stores employees used in warehouse operations.
*/

CREATE TABLE master.employees
(
    employee_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    employee_code VARCHAR(30) NOT NULL UNIQUE,
    employee_name VARCHAR(150) NOT NULL,

    department VARCHAR(80) NOT NULL,
    role VARCHAR(80) NOT NULL,

    warehouse_id BIGINT,

    employee_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT fk_employees_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES master.warehouses (warehouse_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_employees_status
        CHECK (employee_status IN ('active', 'inactive'))
);
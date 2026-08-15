/*
Creates the master.payment_terms table.
Stores customer and supplier payment terms.
*/

CREATE TABLE master.payment_terms
(
    payment_term_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    payment_term_code VARCHAR(30) NOT NULL UNIQUE,
    payment_term_name VARCHAR(100) NOT NULL,
    payment_term_days SMALLINT NOT NULL,

    payment_term_description VARCHAR(255),

    payment_term_status VARCHAR(20) NOT NULL DEFAULT 'active',

    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'system',
    updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'system',

    CONSTRAINT chk_payment_terms_days
        CHECK (payment_term_days >= 0),

    CONSTRAINT chk_payment_terms_status
        CHECK (payment_term_status IN ('active', 'inactive'))
);
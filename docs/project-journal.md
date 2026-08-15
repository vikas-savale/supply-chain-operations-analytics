# Project Journal

## Project Goal

Build a practical end-to-end Supply Chain and Operations Analytics project that demonstrates business understanding, data modeling, SQL analysis and reporting.

---

## Milestone 1 — Project Foundation ✅

Completed

- Project repository created
- Project folder structure created
- README.md added
- `.gitignore` added

---

## Milestone 2 — Database Foundation ✅

Completed

- PostgreSQL installed
- pgAdmin configured
- Database created (`supply_chain_operations_analytics`)
- `01_create_database.sql`
- `02_create_schemas.sql`
- Business schemas created

Schemas:

- `master`
- `inventory`
- `procurement`
- `warehouse`
- `logistics`
- `sales`
- `analytics`

---

## Milestone 3 — Architecture Planning ✅

Completed

- Database architecture document created
- Initial data model prepared
- Master and transaction data identified
- Database build order defined

---

## Milestone 4 — Data Modeling ✅

### Completed

#### Master Tables

- `master.products` table designed and created in PostgreSQL
- `master.customers` table designed and created in PostgreSQL
- `master.suppliers` table designed and created in PostgreSQL
- `master.transporters` table designed and created in PostgreSQL
- `master.warehouses` table designed and created in PostgreSQL
- `master.locations` table designed and created in PostgreSQL
- `master.vehicles` table designed and created in PostgreSQL
- `master.uoms` table designed and created in PostgreSQL
- `master.payment_terms` table designed and created in PostgreSQL
- `master.product_suppliers` table designed and created in PostgreSQL
- `master.brands` table designed and created in PostgreSQL
- `master.categories` table designed and created in PostgreSQL
- `master.sub_categories` table designed and created in PostgreSQL
- `master.customer_locations` table designed and created in PostgreSQL
- `master.employees` table designed and created in PostgreSQL

#### Master Data Audit and Refinement

- Master tables reviewed for business purpose and relationships
- Product reference fields normalized
- Category hierarchy simplified to `categories → sub_categories → products`
- Product master connected to brands, sub-categories and UOMs
- Supplier master connected to reusable payment terms
- Customer master connected to reusable payment terms
- Multiple customer ship-to locations supported
- One active default ship-to location per customer supported
- Multiple approved supplier relationships supported for products
- One active primary supplier/source per product enforced
- Transporter performance kept out of master data for later analytical calculation
- Warehouse and warehouse-location relationships refined
- Operational employee master added

#### Database Migration and Verification

- `database/migrations/01_refine_product_reference_model.sql` created and executed
- `database/migrations/02_refine_customer_operations_model.sql` created and executed
- `database/migrations/03_refine_warehouse_logistics_model.sql` created and executed
- Product foreign keys verified
- Supplier payment-term foreign key verified
- Customer payment-term foreign key verified
- Customer-location foreign key verified
- Employee-warehouse foreign key verified
- Product-supplier relationships verified
- Primary-source index verified
- Customer-location default index verified
- Final master table count verified: 15
- Master tables verified before adding data

### Current Focus

Procurement transaction design

### Next

- Define the purchase order structure
- Define the purchase order item structure
- Define the goods receipt flow

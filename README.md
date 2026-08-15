# Supply Chain & Operations Analytics

A practical end-to-end supply chain and operations analytics project based on realistic business processes.

## Project Goal

The objective is to design, build and analyze a supply chain system covering master data, procurement, inventory, warehouse operations, logistics and sales.

## Technology Stack

- PostgreSQL
- SQL
- Power BI
- Python (synthetic data generation)
- Git & GitHub

## Current Status

### Completed

- Project and database foundation
- Database schemas
- Master data model
- 15 master/reference tables
- Master data normalization and relationship refinement
- PostgreSQL migrations and validation

### Current Focus

Procurement transaction design.

## Database Setup

The database files are organized into setup, schema and migration folders.

### Setup

Run:

1. `database/setup/01_create_database.sql`
2. `database/setup/02_create_schemas.sql`

### Master Tables

The schema files are numbered for reference. They should be created in the following order because some tables depend on others:

1. `11_master_brands.sql`
2. `12_master_categories.sql`
3. `09_master_payment_terms.sql`
4. `04_master_transporters.sql`
5. `08_master_uoms.sql`
6. `05_master_warehouses.sql`
7. `13_master_sub_categories.sql`
8. `03_master_suppliers.sql`
9. `06_master_locations.sql`
10. `07_master_vehicles.sql`
11. `15_master_employees.sql`
12. `01_master_products.sql`
13. `10_master_product_suppliers.sql`
14. `02_master_customers.sql`
15. `14_master_customer_locations.sql`

### Migrations

The migration files contain changes made after the initial table definitions.

Run them in order:

1. `database/migrations/01_refine_product_reference_model.sql`
2. `database/migrations/02_refine_customer_operations_model.sql`
3. `database/migrations/03_refine_warehouse_logistics_model.sql`

## Project Structure

```text
database/
├── migrations/
├── schema/
├── seed/
└── setup/

docs/
datasets/
images/
powerbi/
tools/
```

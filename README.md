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
- Material-level product and packaging model
- PostgreSQL migrations and validation
- Procurement transaction model
- 4 procurement transaction tables
- Purchase order and goods receipt flow
- Procurement PAC and base quantity model
- Inventory transaction model
- 3 inventory tables
- Inventory PAC and base quantity model
- Inventory SLOC tracking
- Inventory physical damage and leakage tracking
- Warehouse putaway model
- Warehouse picking model
- Warehouse dispatch model
- 6 warehouse transaction tables
- Warehouse PAC and base quantity model
- Sales order allocation connection to warehouse picking
- Logistics shipment model
- Logistics delivery model
- Shipment document tracking
- Logistics shipment event tracking
- 6 logistics transaction tables
- Logistics PAC and base quantity model
- Sales order model
- Sales order allocation model
- 3 sales transaction tables
- Customer and ship-to order structure
- Sales order and stock allocation flow

### Current Focus

Warehouse picking and sales order fulfillment model.

## Database Setup

The database files are organized into setup, schema and migration folders.

### Setup

Run:

1. `database/setup/01_create_database.sql`
2. Connect to `supply_chain_operations_analytics`
3. Run `database/setup/02_create_schemas.sql`

### Master Tables

The schema files contain the current master table definitions.

They should be created in the following order because some tables depend on others:

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

### Procurement Tables

After the master tables are created, the procurement tables can be created in this order:

16. `16_procurement_purchase_orders.sql`
17. `17_procurement_purchase_order_items.sql`
18. `18_procurement_goods_receipts.sql`
19. `19_procurement_goods_receipt_items.sql`

### Inventory Tables

After the procurement tables, the inventory tables can be created in this order:

20. `20_inventory_stock.sql`
21. `21_inventory_movements.sql`
22. `22_inventory_stock_audits.sql`

### Warehouse Tables

After the inventory tables, the warehouse tables can be created in this order:

23. `23_warehouse_putaways.sql`
24. `24_warehouse_putaway_items.sql`
25. `25_warehouse_pickings.sql`
26. `26_warehouse_picking_items.sql`
27. `27_warehouse_dispatches.sql`
28. `28_warehouse_dispatch_items.sql`

### Logistics Tables

After the warehouse tables, the logistics tables can be created in this order:

29. `29_logistics_shipments.sql`
30. `30_logistics_shipment_items.sql`
31. `31_logistics_deliveries.sql`
32. `32_logistics_delivery_items.sql`
33. `33_logistics_shipment_documents.sql`
34. `34_logistics_shipment_events.sql`

### Sales Tables

After the required inventory and sales order tables are available, the sales tables can be created in this order:

35. `35_sales_sales_orders.sql`
36. `36_sales_sales_order_items.sql`
37. `37_sales_sales_order_allocations.sql`

### Migrations

The migration files show changes made during the database design process.

They are kept as part of the project history and should not be run after the current schema files have been created.

The migration files are:

1. `database/migrations/01_refine_product_reference_model.sql`
2. `database/migrations/02_refine_customer_operations_model.sql`
3. `database/migrations/03_refine_warehouse_logistics_model.sql`
4. `database/migrations/04_add_batch_to_goods_receipt_items.sql`
5. `database/migrations/05_refine_product_packaging_model.sql`
6. `database/migrations/06_refine_inventory_measurement_model.sql`
7. `database/migrations/07_refine_inventory_audit_sloc.sql`
8. `database/migrations/08_refine_transaction_quantity_model.sql`
9. `database/migrations/09_connect_sales_allocations_to_picking.sql`

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

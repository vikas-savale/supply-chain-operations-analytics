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
- Purchase order transaction flow
- Goods receipt transaction flow
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
- Transaction consistency checks across related records
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
- Synthetic master-data generation framework
- Complete synthetic master datasets
- Supplier master dataset
- Product master dataset
- Product-supplier relationship dataset
- Customer master dataset
- Customer location dataset
- Transporter master dataset
- Vehicle master dataset
- Employee master dataset
- 3,600 product-supplier relationships
- Master-data validation checks
- Warehouse and location capacity consistency checks
- Product packaging and quantity consistency checks
- Customer and customer-location relationship checks
- Transporter and vehicle relationship checks
- Employee and warehouse relationship checks
- Product-supplier relationship validation checks
- Primary supplier/source rules
- Complete master-network relationship validation
- Purchase order transaction generation
- Purchase order item transaction generation
- Goods receipt transaction generation
- Goods receipt item transaction generation
- 1,500 purchase orders
- 6,534 purchase order items
- 1,563 goods receipts
- 6,655 goods receipt items
- Purchase order status distribution validation
- Purchase order line-count distribution validation
- Purchase order PAC/base quantity validation
- Purchase order supplier/product relationship validation
- Purchase order MOQ validation
- Goods receipt reference validation
- Goods receipt warehouse consistency validation
- Goods receipt product and UOM validation
- Goods receipt batch tracking validation
- Goods receipt PAC/base quantity validation
- Goods receipt cumulative receipt validation
- Procurement receiving reconciliation validation
- Purchase order PostgreSQL load
- Goods receipt PostgreSQL load
- Procurement database relational validation
- Procurement end-to-end verification
- Procurement post-load verification
- Procurement identity sequence alignment

### Current Master Data

- 6 UOMs
- 8 payment terms
- 10 brands
- 8 categories
- 42 sub-categories
- 24 suppliers
- 1,500 products
- 3,600 product-supplier relationships
- 180 customers
- 360 customer locations
- 9 warehouses
- 500 warehouse locations
- 18 transporters
- 135 vehicles
- 110 employees

### Current Procurement Data

- 1,500 purchase orders
- 6,534 purchase order items
- 1,563 goods receipts
- 6,655 goods receipt items
- PO date range: 2026-01-01 to 2026-06-30
- Expected dates generated using supplier lead-time logic
- Purchase order status distribution validated
- Purchase order line-count distribution validated
- Goods receipt references validated
- Goods receipt warehouse, product and UOM consistency validated
- Goods receipt batch tracking validated
- Procurement PAC/base quantities validated
- Cumulative receipt quantities validated
- Purchase order and goods receipt reconciliation completed with zero true errors
- PostgreSQL procurement load completed and verified

## Current Focus

Continue transaction-data generation from accepted goods receipts into the inventory and downstream operational flows.

Next:

- Inventory stock generation
- Inventory movement generation
- Stock audit generation
- Procurement-to-inventory reconciliation
- Warehouse transaction generation
- Logistics transaction generation
- Sales transaction generation
- Cross-module transaction validation
- PostgreSQL transaction verification
- Preparation of the completed dataset for SQL analysis and Power BI reporting

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

After the required preceding tables are available, the sales tables can be created in this order:

35. `35_sales_sales_orders.sql`
36. `36_sales_sales_order_items.sql`
37. `37_sales_sales_order_allocations.sql`

### Final Schema Links

After the sales allocation table is created:

38. `38_sales_allocations_to_picking.sql`
39. `39_transaction_integrity.sql`

Schema file 38 adds the sales order allocation reference to warehouse picking items.

Schema file 39 adds consistency rules between related transaction records.

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
10. `database/migrations/10_refine_transaction_integrity.sql`

Migration 09 connects sales order allocations to warehouse picking.

Migration 10 adds consistency rules between related transaction records.

## Project Structure

```text
database/
├── migrations/
├── schema/
├── seed/
└── setup/

datasets/
docs/
images/
powerbi/
tools/
```

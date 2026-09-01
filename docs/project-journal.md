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
- Product material variants represented at SKU level
- Product packaging attributes refined to include pack type, pack size and base quantity per PAC
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
- `database/migrations/04_add_batch_to_goods_receipt_items.sql` created and executed
- `database/migrations/05_refine_product_packaging_model.sql` created and executed
- `database/migrations/06_refine_inventory_measurement_model.sql` created and executed
- `database/migrations/07_refine_inventory_audit_sloc.sql` created and executed
- `database/migrations/08_refine_transaction_quantity_model.sql` created and executed
- `database/migrations/09_connect_sales_allocations_to_picking.sql` created and executed
- `database/migrations/10_refine_transaction_integrity.sql` created and executed
- Product foreign keys verified
- Supplier payment-term foreign key verified
- Customer payment-term foreign key verified
- Customer-location foreign key verified
- Employee-warehouse foreign key verified
- Product-supplier relationships verified
- Primary-source index verified
- Customer-location default index verified
- Product packaging fields verified
- Product PAC quantity check verified
- Transaction quantity fields verified
- Generic `quantity` fields removed from affected transaction lines
- Final master table count verified: 15
- Master tables verified before adding data

#### Procurement Transactions

- `procurement.purchase_orders` table designed and created
- `procurement.purchase_order_items` table designed and created
- `procurement.goods_receipts` table designed and created
- `procurement.goods_receipt_items` table designed and created
- Batch tracking added to `procurement.goods_receipt_items`
- Purchase order foreign keys verified
- Purchase order item foreign keys verified
- Goods receipt foreign keys verified
- Goods receipt item foreign keys verified
- Purchase order status rules verified
- Goods receipt quantity rules verified
- PAC and base quantities verified across procurement transaction lines
- Current procurement table count verified: 4
- Procurement tables verified before adding data

#### Inventory Transactions

- `inventory.stock` table designed and created
- `inventory.movements` table designed and created
- `inventory.stock_audits` table designed and created
- Inventory foreign keys verified
- Inventory stock status rules verified
- Inventory movement rules verified
- Stock audit quantity rules verified
- Stock position unique rule verified
- PAC and base quantity fields verified
- SLOC tracking verified
- Physical leakage tracking verified
- Stock audit variance rule verified
- Warehouse and physical location consistency verified
- Current inventory table count verified: 3
- Inventory tables verified before adding data

#### Warehouse Transactions

- `warehouse.putaways` table designed and created
- `warehouse.putaway_items` table designed and created
- Putaway foreign keys verified
- Putaway status rules verified
- Putaway quantity check verified
- Putaway line uniqueness verified
- Source and destination location check verified
- `warehouse.pickings` table designed and created
- `warehouse.picking_items` table designed and created
- Picking foreign keys verified
- Picking status rules verified
- Picking quantity check verified
- Picking line uniqueness verified
- `warehouse.dispatches` table designed and created
- `warehouse.dispatch_items` table designed and created
- Dispatch foreign keys verified
- Dispatch status rules verified
- Dispatch quantity check verified
- Dispatch line uniqueness verified
- PAC and base quantities verified across warehouse transaction lines
- Sales order allocation reference added to `warehouse.picking_items`
- Picking allocation foreign key verified
- Picking stock and allocation consistency verified
- Picking stock and source location consistency verified
- Current warehouse transaction table count verified: 6
- Warehouse tables verified before adding data

#### Logistics Transactions

- `logistics.shipments` table designed and created
- `logistics.shipment_items` table designed and created
- Shipment foreign keys verified
- Shipment status rules verified
- Shipment date rules verified
- Shipment item quantity check verified
- Shipment item line uniqueness verified
- `logistics.deliveries` table designed and created
- `logistics.delivery_items` table designed and created
- Delivery foreign keys verified
- Delivery item quantity check verified
- Delivery item line uniqueness verified
- `logistics.shipment_documents` table designed and created
- Shipment document foreign key verified
- Shipment document type rules verified
- Shipment document status rules verified
- Shipment document reference uniqueness verified
- `logistics.shipment_events` table designed and created
- Shipment event foreign key verified
- Shipment event type rules verified
- Shipment event timeline index verified
- Shipment and dispatch consistency verified
- Delivery and shipment consistency verified
- PAC and base quantities verified across logistics transaction lines
- Current logistics table count verified: 6
- Logistics tables verified before adding data

#### Sales Transactions

- `sales.sales_orders` table designed and created
- `sales.sales_order_items` table designed and created
- Sales order foreign keys verified
- Sales order status rules verified
- Sales order number uniqueness verified
- Sales order item foreign keys verified
- Sales order item line uniqueness verified
- Sales order PAC and base quantity fields verified
- `sales.sales_order_allocations` table designed and created
- Sales order allocation foreign keys verified
- Sales order allocation quantity checks verified
- Sales order allocation status rules verified
- Sales order item and stock product consistency verified
- Sales order and customer ship-to consistency verified
- Sales table count verified: 3
- Sales tables verified before adding data

---

## Milestone 5 — Synthetic Master Data Generation ✅

### Completed

- Python virtual environment configured for the project
- Synthetic master-data generation framework created
- UOM master dataset generated
- Payment term master dataset generated
- Brand master dataset generated
- Category master dataset generated
- Sub-category master dataset generated
- Warehouse master dataset generated
- Warehouse location master dataset generated
- Master-data validation checks added
- Category and sub-category relationships validated
- Warehouse and location relationships validated
- Warehouse location capacity consistency validated
- Initial master datasets generated as CSV files

### Current Master Dataset Counts

- UOMs: 6
- Payment Terms: 8
- Brands: 10
- Categories: 8
- Sub-categories: 42
- Warehouses: 9
- Warehouse Locations: 500

### Current Dataset Files

- `datasets/master_uoms.csv`
- `datasets/master_payment_terms.csv`
- `datasets/master_brands.csv`
- `datasets/master_categories.csv`
- `datasets/master_sub_categories.csv`
- `datasets/master_warehouses.csv`
- `datasets/master_locations.csv`

### Generator

- `tools/generate_master_data.py`

The generator validates the generated master data before writing the CSV files.

### Next

- Generate supplier master data
- Generate product-supplier relationships
- Generate product master data
- Generate customer master data
- Generate customer location data
- Generate employee master data
- Generate transporter master data
- Generate vehicle master data
- Validate the complete master-data network
- Prepare master datasets for database loading

---

## Current Focus

Synthetic master data generation.

---

## Next

- Complete remaining master datasets
- Validate master-data relationships
- Prepare master datasets for database loading
- Define transaction data generation rules
- Generate linked procurement, inventory, warehouse, logistics and sales data
- Validate transaction quantities and business relationships
- Prepare data for SQL analysis

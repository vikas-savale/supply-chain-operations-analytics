# Project Journal

## Project Goal

Build a practical end-to-end Supply Chain and Operations Analytics project that demonstrates business understanding, data modeling, SQL analysis and reporting.

---

## Milestone 1 — Project Foundation ✅

### Completed

- Project repository created
- Project folder structure created
- `README.md` added
- `.gitignore` added

---

## Milestone 2 — Database Foundation ✅

### Completed

- PostgreSQL installed
- pgAdmin configured
- Database created (`supply_chain_operations_analytics`)
- `01_create_database.sql`
- `02_create_schemas.sql`
- Business schemas created

### Schemas

- `master`
- `inventory`
- `procurement`
- `warehouse`
- `logistics`
- `sales`
- `analytics`

---

## Milestone 3 — Architecture Planning ✅

### Completed

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
- Supplier master dataset generated
- Warehouse master dataset generated
- Warehouse location master dataset generated
- Product master dataset generated
- Product-supplier relationship dataset generated
- Master-data validation checks added
- Supplier payment-term references validated
- Category and sub-category relationships validated
- Warehouse and location relationships validated
- Warehouse location capacity consistency validated
- Product reference and packaging validations added
- Product-supplier relationship validations added
- Master datasets generated as CSV files

### Current Master Dataset Counts

- UOMs: 6
- Payment Terms: 8
- Brands: 10
- Categories: 8
- Sub-categories: 42
- Suppliers: 24
- Products: 1,500
- Product-Supplier Relationships: 3,600
- Warehouses: 9
- Warehouse Locations: 500

### Current Dataset Files

- `datasets/master_uoms.csv`
- `datasets/master_payment_terms.csv`
- `datasets/master_brands.csv`
- `datasets/master_categories.csv`
- `datasets/master_sub_categories.csv`
- `datasets/master_suppliers.csv`
- `datasets/master_warehouses.csv`
- `datasets/master_locations.csv`
- `datasets/master_products.csv`
- `datasets/master_product_suppliers.csv`

### Generator

- `tools/generate_master_data.py`

The generator validates the generated master data before writing the CSV files.

---

## Milestone 6 — Product Master Generation and Database Validation ✅

### Product Dataset

- Product master generated with 1,500 products
- Product IDs generated sequentially from 1 to 1,500
- SKUs validated as unique
- Product names validated as unique
- Brand references validated
- Sub-category references validated
- Base UOM references validated
- Product status values validated
- Product packaging definitions validated
- Base quantity per PAC validated as positive
- Packaging quantity normalization validated
- Product status distribution validated:
  - Active: 1,350
  - Inactive: 90
  - Discontinued: 60
- Brand distribution validated across 10 brands
- Sub-category distribution validated across 42 sub-categories

### PostgreSQL Load

- `datasets/master_products.csv` loaded into `master.products` using PostgreSQL from the pgAdmin Query Tool
- Product row count verified: 1,500
- Product ID range verified: 1 to 1,500
- Distinct product IDs verified: 1,500
- Distinct SKUs verified: 1,500
- Distinct product names verified: 1,500

### Database Validation

- Missing SKU values: 0
- Missing product names: 0
- Missing product status values: 0
- Invalid product status values: 0
- Invalid base quantities: 0
- Missing brand references: 0
- Missing sub-category references: 0
- Missing UOM references: 0
- Orphan brand references: 0
- Orphan sub-category references: 0
- Orphan UOM references: 0
- Packaging quantity mismatches: 0
- Packaging/UOM mismatches: 0
- Product primary key verified
- SKU unique constraint verified
- Product foreign keys verified
- Product status check constraint verified
- Product base quantity check constraint verified
- Required NOT NULL constraints verified
- Product identity sequence aligned after CSV load
- Next generated product ID verified to continue from 1,501

---

## Milestone 7 — Product-Supplier Relationship Generation and Validation ✅

### Product-Supplier Dataset

- Product-supplier relationships generated for all 1,500 products
- Total product-supplier relationships generated: 3,600
- Supplier count distribution validated:
  - 1 supplier: 300 products
  - 2 suppliers: 525 products
  - 3 suppliers: 450 products
  - 4 suppliers: 225 products
- All products have at least one supplier relationship
- Product-supplier relationship IDs generated sequentially from 1 to 3,600
- Product-supplier relationship pairs validated as unique
- Supplier product codes validated as unique within each supplier
- Purchase UOM references validated
- Supplier-specific purchase prices validated as positive
- Minimum order quantities validated as positive
- Supplier lead times validated as non-negative

### Supplier Sourcing Rules

- Active products use active supplier relationships
- Inactive and discontinued products use inactive supplier relationships
- Inactive suppliers do not have active relationships
- Inactive suppliers are not selected as primary sources
- Active products have one active primary supplier/source
- Inactive and discontinued products do not have a primary supplier
- Active relationships do not have an `effective_to` date
- Inactive relationships have an `effective_to` date
- Supplier relationship dates validated

### Purchase UOM Logic

- Packaged products use PAC as the purchase UOM
- Bulk liquid products use Litre as the purchase UOM
- Bulk grease products use Kilogram as the purchase UOM

### PostgreSQL Load

- `datasets/master_product_suppliers.csv` loaded into `master.product_suppliers`
- Product-supplier row count verified: 3,600
- Product references verified
- Supplier references verified
- Purchase UOM references verified
- Product-supplier relationship uniqueness verified
- Primary-source rule verified
- Product-supplier relationship status rules verified

---

## Milestone 8 — Complete Master Data Network ✅

### Completed

- Customer master dataset generated
- Customer location dataset generated
- Transporter master dataset generated
- Vehicle master dataset generated
- Employee master dataset generated
- Complete 15-master data network completed
- Customer and customer-location relationships validated
- Customer default ship-to rules validated
- Customer payment-term references validated
- Transporter and vehicle relationships validated
- Employee and warehouse relationships validated
- Vehicle registration state and transporter state consistency validated
- Master relationship validations completed across the complete master network

### Current Master Dataset Counts

- UOMs: 6
- Payment Terms: 8
- Brands: 10
- Categories: 8
- Sub-categories: 42
- Suppliers: 24
- Products: 1,500
- Product-Supplier Relationships: 3,600
- Customers: 180
- Customer Locations: 360
- Warehouses: 9
- Warehouse Locations: 500
- Transporters: 18
- Vehicles: 135
- Employees: 110

### Current Dataset Files

- `datasets/master_uoms.csv`
- `datasets/master_payment_terms.csv`
- `datasets/master_brands.csv`
- `datasets/master_categories.csv`
- `datasets/master_sub_categories.csv`
- `datasets/master_suppliers.csv`
- `datasets/master_warehouses.csv`
- `datasets/master_locations.csv`
- `datasets/master_products.csv`
- `datasets/master_product_suppliers.csv`
- `datasets/master_customers.csv`
- `datasets/master_customer_locations.csv`
- `datasets/master_transporters.csv`
- `datasets/master_vehicles.csv`
- `datasets/master_employees.csv`

### Generator Validation

- Python syntax validation passed
- Full master-data generation completed successfully
- UOM validation passed
- Payment-term validation passed
- Supplier validation passed
- Customer validation passed
- Customer-location validation passed
- Transporter validation passed
- Vehicle validation passed
- Brand validation passed
- Category validation passed
- Sub-category validation passed
- Product validation passed
- Product-supplier validation passed
- Warehouse validation passed
- Location validation passed
- Employee validation passed
- Master relationship validation passed

### PostgreSQL Master Data

- All 15 current master tables populated
- Master row counts verified against generated datasets
- Cross-master reference checks returned zero broken references
- Customer-location default rules verified
- Product-supplier sourcing rules verified
- Employee-warehouse references verified
- Vehicle-transporter references verified
- Warehouse-location references verified
- Complete master network verified before moving to transaction data generation

---

## Milestone 9 — Procurement Purchase Order Generation and Database Load ✅

### Purchase Order Generation

- Purchase order generation rules finalized
- Purchase order CSV generation added to the synthetic-data generator
- Purchase order item CSV generation added to the synthetic-data generator
- Procurement generation uses the existing master-data relationships
- Master-data generation logic remains reusable and deterministic
- Purchase order IDs generated sequentially from 1 to 1,500
- Purchase order item IDs generated sequentially from 1 to 6,534
- Unique PO numbers validated
- Product duplication within a PO prevented and validated
- Exact purchase order status distribution generated
- Exact purchase order line-count distribution generated

### Purchase Order Dataset

- Purchase orders generated: 1,500
- Purchase order items generated: 6,534
- PO date range: 2026-01-01 to 2026-06-30
- Expected dates generated from supplier lead-time logic
- Expected dates allowed to extend beyond the PO date range

### Status Distribution

- Draft: 60
- Approved: 120
- Sent: 150
- Partially Received: 300
- Received: 810
- Cancelled: 60

### Line Count Distribution

- 1 line: 300 purchase orders
- 2–3 lines: 450 purchase orders
- 4–6 lines: 450 purchase orders
- 7–10 lines: 225 purchase orders
- 11–15 lines: 75 purchase orders

### Quantity Model

- Packaged purchase relationships use PAC
- Bulk liquid purchase relationships use Litre
- Current active product-supplier relationships contain no active KG purchase-UOM relationships
- Ordered base quantity reconciles to ordered PAC quantity using `base_quantity_per_pac`
- Packaged and bulk minimum order quantities were validated

### CSV Validation

- Purchase order count validated: 1,500
- Purchase order item count validated: 6,534
- Status distribution validated
- Line-count distribution validated
- PO date range validated
- Expected date consistency validated
- PO numbers validated as unique
- Product uniqueness within each PO validated
- Purchase order line numbering validated
- Required values validated
- Sequential IDs validated

### Cross-Master Relational Validation

- Supplier references validated
- Warehouse references validated
- Payment-term references validated
- Supplier/payment-term consistency validated
- Product references validated
- Active product-supplier relationships validated
- Purchase UOM consistency validated
- Unit cost consistency validated
- PAC/base quantity reconciliation validated
- MOQ compliance validated
- Active supplier usage validated
- Active product usage validated

Total relational QA errors: 0

### PostgreSQL Purchase Order Load

- `datasets/procurement_purchase_orders.csv` loaded into `procurement.purchase_orders`
- `datasets/procurement_purchase_order_items.csv` loaded into `procurement.purchase_order_items`
- Purchase order database row count verified: 1,500
- Purchase order item database row count verified: 6,534
- Database foreign keys verified
- Database check constraints verified
- Database unique constraints verified
- PAC/base quantity rules verified
- Expected date rule verified
- Database-side consolidated QA returned zero errors
- PostgreSQL transaction committed successfully
- Post-commit row counts verified

### Current Procurement Status

Purchase orders and purchase order items are now generated, validated and loaded into PostgreSQL.

---

## Milestone 10 — Goods Receipt Generation and Database Load ✅

### Goods Receipt Generation

- Goods receipt generation rules finalized
- Goods receipt CSV generation added to the synthetic-data generator
- Goods receipt item CSV generation added to the synthetic-data generator
- Goods receipt generation uses the existing purchase order and purchase order item relationships
- Goods receipt dates follow the configured relationship to purchase order and expected dates
- Goods receipt generation remains deterministic under the existing generator seed
- Goods receipt IDs generated sequentially from 1 to 1,563
- Goods receipt item IDs generated sequentially from 1 to 6,655
- Unique GRN numbers validated
- Goods receipts generated only for eligible purchase orders
- Goods receipt warehouse matched to the purchase order warehouse
- Goods receipt items matched to their purchase order items

### Goods Receipt Dataset

- Goods receipts generated: 1,563
- Goods receipt items generated: 6,655
- Receipt status distribution validated
- Goods receipt dates validated
- Goods receipt references validated
- Goods receipt item product consistency validated
- Goods receipt item UOM consistency validated
- Batch-code generation validated

### Goods Receipt Quantity Model

- Received PAC quantity validated
- Accepted PAC quantity validated
- Rejected PAC quantity validated
- Received base quantity validated
- Accepted base quantity validated
- Rejected base quantity validated
- Accepted + rejected PAC quantity reconciles to received PAC quantity
- Accepted + rejected base quantity reconciles to received base quantity
- PAC/base quantity conversion validated using the product master definition
- Cumulative received quantity does not exceed ordered quantity
- Received purchase orders reconcile to ordered quantity
- Partially received purchase orders reconcile to a positive incomplete received quantity

### CSV Validation

- Purchase order dataset remained validated after goods receipt generation
- Goods receipt count validated: 1,563
- Goods receipt item count validated: 6,655
- Goods receipt IDs validated
- Goods receipt item IDs validated
- GRN numbers validated as unique
- Goods receipt references validated
- Goods receipt item references validated
- Goods receipt warehouse consistency validated
- Goods receipt product consistency validated
- Goods receipt UOM consistency validated
- Batch codes validated
- Line numbering validated
- PAC/base quantity reconciliation validated
- Cumulative receipt quantity validated
- Purchase order status reconciliation validated
- Independent goods receipt CSV QA passed

### PostgreSQL Goods Receipt Load

- `datasets/procurement_goods_receipts.csv` loaded into `procurement.goods_receipts`
- `datasets/procurement_goods_receipt_items.csv` loaded into `procurement.goods_receipt_items`
- Goods receipt database row count verified: 1,563
- Goods receipt item database row count verified: 6,655
- Goods receipt foreign keys verified
- Goods receipt item foreign keys verified
- Goods receipt unique constraints verified
- Goods receipt quantity checks verified
- Procurement end-to-end references verified
- Purchase order status reconciliation verified
- Identity sequences aligned after CSV load
- Final procurement database QA returned zero true errors
- Post-load row counts verified

### Current Procurement Status

Purchase orders, purchase order items, goods receipts and goods receipt items are now generated, validated and loaded into PostgreSQL.

The procurement inbound transaction flow is now complete through the goods receipt stage.

---

## Current Focus

Continue transaction-data generation from accepted goods receipts into the inventory and downstream operational flows.

### Next Transaction Focus

- Define inventory opening and movement generation rules
- Generate inventory stock data
- Generate inventory movement data
- Generate stock audit data
- Link accepted goods receipts to inventory stock and movement transactions
- Validate PAC/base quantities across inventory transactions
- Validate warehouse and physical-location relationships
- Load inventory datasets into PostgreSQL
- Verify procurement-to-inventory continuity
- Continue into warehouse transaction generation

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
- `database/migrations/04_add_batch_to_goods_receipt_items.sql` created and executed
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
- Delivery status rules verified
- Delivery item quantity check verified
- Delivery item line uniqueness verified
- Current logistics table count verified: 4
- Logistics tables verified before adding data

### Current Focus

Transport operations and delivery documentation design

### Next

- Define the required transport operations
- Define the required delivery documents
- Identify the logistics events needed for analysis

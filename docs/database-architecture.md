# Database Architecture

## Schemas

The database is divided into different business areas.

| Schema        | Purpose                                     |
| ------------- | ------------------------------------------- |
| `master`      | Core business master and reference data     |
| `inventory`   | Stock, stock movements and stock audits     |
| `procurement` | Purchase orders and goods receipts          |
| `warehouse`   | Warehouse operational activities            |
| `logistics`   | Transport, shipment and delivery activities |
| `sales`       | Customer orders and sales transactions      |
| `analytics`   | Reports, views and KPI calculations         |

---

## Master Schema

The `master` schema currently contains 15 master/reference tables:

- `brands`
- `categories`
- `sub_categories`
- `products`
- `uoms`
- `suppliers`
- `product_suppliers`
- `payment_terms`
- `customers`
- `customer_locations`
- `employees`
- `warehouses`
- `locations`
- `transporters`
- `vehicles`

The `master` schema provides the reference data used by transaction tables.

The `products` table stores material-level packaging attributes including pack type, pack size and the base quantity represented by one PAC.

---

## Synthetic Master Data

Synthetic master data has been generated for the current master model.

- 6 UOMs
- 8 payment terms
- 10 brands
- 8 categories
- 42 sub-categories
- 24 suppliers
- 1,500 products
- 9 warehouses
- 500 warehouse locations

The generated data is stored as CSV files under the `datasets/` directory.

The data-generation logic is maintained in:

`tools/generate_master_data.py`

The generator includes validation checks for master-data values and relationships.

---

## Procurement Schema

The `procurement` schema currently contains 4 transaction tables:

- `purchase_orders`
- `purchase_order_items`
- `goods_receipts`
- `goods_receipt_items`

The procurement flow is:

Purchase Order

→ Purchase Order Items

→ Goods Receipt

→ Goods Receipt Items

A purchase order can have multiple goods receipts.

Procurement transaction lines store both PAC quantity and base quantity.

Purchase order items store ordered PAC and base quantities.

Goods receipt items store received, accepted and rejected quantities in both PAC and base measures.

---

## Inventory Schema

The `inventory` schema currently contains 3 tables:

- `stock`
- `movements`
- `stock_audits`

The inventory layer stores current stock, stock movement history and physical stock audit results.

### Inventory Measurement

Inventory stock and movement records store:

- PAC quantity
- Base quantity
- SAP storage location code
- Physical warehouse location
- Batch
- Stock status

PAC quantity records the package count, while base quantity records the corresponding quantity in the product base UOM.

### Stock Location

The inventory model stores the SAP storage location code separately from the physical warehouse location.

`FGST` represents good finished stock and `RJCT` represents rejected stock.

Stock, movement and stock audit records keep the SAP storage location and physical warehouse location consistent with the selected warehouse.

### Stock Audits

Stock audits store system base quantity and separate physical quantities for good stock, damaged stock and leakage.

Variance is calculated as:

Variance = Physical Good + Physical Damaged + Physical Leakage - System Base Quantity

---

## Warehouse Schema

The `warehouse` schema currently contains 6 transaction tables:

- `putaways`
- `putaway_items`
- `pickings`
- `picking_items`
- `dispatches`
- `dispatch_items`

The putaway flow moves accepted stock from a receiving or staging location to a storage or picking location.

One putaway can contain multiple putaway items.

A goods receipt item can be split across multiple putaway items when stock is placed in more than one location.

The picking flow moves required stock from warehouse locations for outbound orders.

One picking can contain multiple picking items.

A picking can use stock from more than one location.

Picking items are linked to sales order allocations.

A picking item identifies the allocation being fulfilled and the inventory stock position being picked.

An allocation can be fulfilled through multiple picking items.

The picking item stock must match the stock assigned to its sales order allocation.

The picking source location must match the physical location of the selected stock.

The dispatch flow records warehouse loading and dispatch of picked stock.

One dispatch can contain multiple dispatch items.

A dispatch can contain items from more than one picking item.

Warehouse transaction lines store both PAC quantity and base quantity.

---

## Logistics Schema

The `logistics` schema currently contains 6 transaction tables:

- `shipments`
- `shipment_items`
- `deliveries`
- `delivery_items`
- `shipment_documents`
- `shipment_events`

The shipment flow connects warehouse dispatches to transport execution.

A shipment is linked to a warehouse dispatch, transporter and vehicle.

One shipment can contain multiple shipment items.

Shipment items are linked to dispatch items from the shipment dispatch to keep the outbound transaction flow consistent.

The delivery flow records the completion of a shipment at the delivery stage.

A delivery is linked to a shipment.

One delivery can contain multiple delivery items.

Delivery items are linked to shipment items from the delivery shipment to keep the delivery flow consistent.

Shipment documents store document references associated with shipments.

Supported document types include invoices, E-Way Bills, Lorry Receipts and proof of delivery.

Shipment events store the operational timeline of a shipment.

Supported shipment events include vehicle arrival, loading start, loading completion, departure and delivery completion.

The event timeline can support analysis of vehicle waiting time, loading time, dispatch turnaround time and transit time.

Logistics transaction lines store both PAC quantity and base quantity.

---

## Sales Schema

The `sales` schema currently contains 3 transaction tables:

- `sales_orders`
- `sales_order_items`
- `sales_order_allocations`

The sales order flow is:

Sales Order

→ Sales Order Items

→ Stock Allocation

A sales order is linked to a customer and a selected customer ship-to location.

A customer can have multiple ship-to locations.

The selected ship-to location must belong to the same customer as the sales order.

Sales order items are linked to products and store ordered PAC and base quantities.

Sales order items also store commercial rate information.

One sales order can contain multiple sales order items.

Sales order allocations link sales order items to specific inventory stock positions.

One sales order item can have multiple allocations.

Allocations store PAC and base quantities allocated from inventory stock.

The product in the sales order item must match the product in the allocated stock.

A sales order can be fulfilled from multiple warehouses through multiple stock allocations.

Sales order allocations are connected to warehouse picking items when allocated stock is picked.

---

## Schema Build Order

The current schema files define 37 business tables and 2 supporting schema files.

They should be created in the following order because some tables depend on others:

### Master Tables

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

16. `16_procurement_purchase_orders.sql`
17. `17_procurement_purchase_order_items.sql`
18. `18_procurement_goods_receipts.sql`
19. `19_procurement_goods_receipt_items.sql`

### Inventory Tables

20. `20_inventory_stock.sql`
21. `21_inventory_movements.sql`
22. `22_inventory_stock_audits.sql`

### Warehouse Tables

23. `23_warehouse_putaways.sql`
24. `24_warehouse_putaway_items.sql`
25. `25_warehouse_pickings.sql`
26. `26_warehouse_picking_items.sql`
27. `27_warehouse_dispatches.sql`
28. `28_warehouse_dispatch_items.sql`

### Logistics Tables

29. `29_logistics_shipments.sql`
30. `30_logistics_shipment_items.sql`
31. `31_logistics_deliveries.sql`
32. `32_logistics_delivery_items.sql`
33. `33_logistics_shipment_documents.sql`
34. `34_logistics_shipment_events.sql`

### Sales Tables

35. `35_sales_sales_orders.sql`
36. `36_sales_sales_order_items.sql`
37. `37_sales_sales_order_allocations.sql`

### Final Schema Links

38. `38_sales_allocations_to_picking.sql`

This file adds the sales order allocation reference to `warehouse.picking_items` after the sales allocation table has been created.

39. `39_transaction_integrity.sql`

This file adds consistency rules between related transaction records.

---

## Migrations

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

---

## Analytics Layer

Analytics will be added after the required transaction data is available.

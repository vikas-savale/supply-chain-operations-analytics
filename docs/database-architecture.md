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

### Stock Audits

Stock audits store system base quantity and separate physical quantities for good stock, damaged stock and leakage.

Variance is calculated as:

Physical Good

- Physical Damaged
- Physical Leakage

* System Base Quantity

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

Shipment items are linked to dispatch items to keep the outbound transaction flow traceable.

The delivery flow records the completion of a shipment at the delivery stage.

A delivery is linked to a shipment.

One delivery can contain multiple delivery items.

Delivery items are linked to shipment items to maintain quantity and transaction traceability.

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

Sales order items are linked to products and store ordered PAC and base quantities.

Sales order items also store commercial rate information.

One sales order can contain multiple sales order items.

Sales order allocations link sales order items to specific inventory stock positions.

One sales order item can have multiple allocations.

Allocations store PAC and base quantities allocated from inventory stock.

A sales order can be fulfilled from multiple warehouses through multiple stock allocations.

---

## Analytics Layer

Analytics will be added after the required transaction data is available.

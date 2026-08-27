# Data Model

## Master Data

### Product and Reference

- Brands
- Categories
- Sub Categories
- Products
- UOMs
- Suppliers
- Product Suppliers
- Payment Terms

### Customer and Operations

- Customers
- Customer Locations
- Employees

### Warehouse and Logistics

- Warehouses
- Locations
- Transporters
- Vehicles

---

## Current Relationships

- Brands → Products
- Categories → Sub Categories
- Sub Categories → Products
- UOMs → Products
- Products ↔ Suppliers through Product Suppliers
- Payment Terms → Customers
- Payment Terms → Suppliers
- Customers → Customer Locations
- Warehouses → Locations
- Warehouses → Employees
- Transporters → Vehicles

---

## Product Packaging

The product master stores packaging information for each stockable material.

- Material code identifies the stockable material and pack variant
- Pack type identifies the packaging form
- Pack size stores the descriptive pack configuration
- Base UOM defines the normalized measurement unit
- Base quantity per PAC stores the quantity represented by one PAC

PAC quantity is material-specific because different material codes can have different pack sizes.

---

## Procurement Transactions

### Purchase Orders

- Purchase Orders
- Purchase Order Items

### Goods Receipts

- Goods Receipts
- Goods Receipt Items

### Transaction Quantities

Procurement transaction lines store package quantity and normalized base quantity.

Purchase order items store:

- Ordered PAC quantity
- Ordered base quantity

Goods receipt items store:

- Received PAC quantity
- Accepted PAC quantity
- Rejected PAC quantity
- Received base quantity
- Accepted base quantity
- Rejected base quantity

Accepted and rejected quantities are tracked separately for both measures.

---

## Inventory

- Stock
- Inventory Movements
- Stock Audits

### Inventory Measures

Inventory transactions store both package quantity and normalized base quantity.

- PAC quantity stores the number of packages
- Base quantity stores the corresponding quantity in the product base UOM
- The product master defines the base quantity represented by one PAC

### Stock Location

Inventory stock stores the SAP storage location code along with the physical warehouse location.

- `FGST` represents good finished stock
- `RJCT` represents rejected stock

The SAP storage location and physical warehouse location are kept together in the stock model.

### Stock Audits

Stock audits store separate physical quantities for:

- Good stock
- Damaged stock
- Leakage

The variance is calculated from the physical quantities and the system base quantity.

Variance:

Physical Good

- Physical Damaged
- Physical Leakage

* System Base Quantity

---

## Warehouse Transactions

### Putaway

- Putaways
- Putaway Items

### Picking

- Pickings
- Picking Items

### Dispatch

- Dispatches
- Dispatch Items

### Warehouse Transaction Quantities

Warehouse transaction lines store both PAC quantity and base quantity.

- Putaway items store PAC and base quantities moved during putaway
- Picking items store PAC and base quantities picked from stock
- Dispatch items store PAC and base quantities loaded and dispatched

### Picking and Sales Allocation

Picking items are linked to sales order allocations.

A picking item identifies the allocation being fulfilled and the inventory stock position being picked.

An allocation can be fulfilled through multiple picking items.

The stock reference in the picking item is kept consistent with the allocation stock reference.

The picking source location is kept consistent with the selected stock location.

---

## Logistics Transactions

### Shipments

- Shipments
- Shipment Items

### Deliveries

- Deliveries
- Delivery Items

### Shipment Documents

- Shipment Documents

### Shipment Events

- Shipment Events

### Logistics Transaction Quantities

Logistics transaction lines store both PAC quantity and base quantity.

- Shipment items store PAC and base quantities shipped
- Delivery items store PAC and base quantities delivered

Shipment items are connected to dispatch items from the same warehouse dispatch.

Delivery items are connected to shipment items from the same shipment.

---

## Sales Transactions

### Sales Orders

- Sales Orders
- Sales Order Items

A sales order is created for a customer and a selected customer ship-to location.

A customer can have multiple ship-to locations.

The selected ship-to location must belong to the same customer as the sales order.

Sales order items store the ordered product, PAC quantity, base quantity and commercial rate information.

One sales order can contain multiple sales order items.

A sales order can be fulfilled from multiple warehouses through stock allocation.

### Sales Order Allocation

- Sales Order Allocations

Sales order allocations connect sales order items to specific inventory stock positions.

An allocation stores the stock position used for the allocation along with allocated PAC and base quantities.

The product in the sales order item must match the product in the allocated stock.

One sales order item can have multiple allocations.

A sales order can be fulfilled from multiple warehouses through multiple stock allocations.

Allocations are connected to warehouse picking items when allocated stock is picked.

---

## Data Consistency

The database includes consistency rules for related records.

- A customer order must use a ship-to location belonging to the same customer
- Inventory stock, movements and stock audits must use a location belonging to the same warehouse
- An allocation must use stock for the same product as the sales order item
- A picking item must use the stock assigned to its allocation
- A picking item must use the actual location of the selected stock
- A shipment item must use a dispatch item from the shipment dispatch
- A delivery item must use a shipment item from the delivery shipment

---

## Inbound Flow

Supplier

→ Purchase Order

→ Purchase Order Items

→ Goods Receipt

→ Goods Receipt Items

→ Receiving / Staging Inventory

→ Putaway

→ Storage / Picking Location

---

## Outbound Flow

Customer Order

→ Sales Order

→ Sales Order Items

→ Stock Allocation

→ Picking

→ Dispatch / Loading

→ Shipment

→ Delivery

→ Shipment Documents

---

## Shipment Event Timeline

Shipment

→ Vehicle Arrived

→ Loading Started

→ Loading Completed

→ Departed

→ Delivery Completed

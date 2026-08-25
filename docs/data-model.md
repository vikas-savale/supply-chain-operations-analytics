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

The product master stores the packaging information for each stockable material.

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

---

## Inventory

- Stock
- Inventory Movements
- Stock Audits

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
→ Allocation / Reserved Stock
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

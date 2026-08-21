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

## Main Flow

Supplier
→ Purchase Order
→ Purchase Order Items
→ Goods Receipt
→ Goods Receipt Items
→ Inventory

# Database Architecture

## Schemas

The database is divided into different business areas.

| Schema        | Purpose                                                       |
| ------------- | ------------------------------------------------------------- |
| `master`      | Core business master and reference data                       |
| `inventory`   | Inventory balances, stock movements and inventory adjustments |
| `procurement` | Purchase orders, purchase order items and goods receipts      |
| `warehouse`   | Warehouse operational activities                              |
| `logistics`   | Transport, shipment and delivery activities                   |
| `sales`       | Customer orders and sales transactions                        |
| `analytics`   | Reports, views and KPI calculations                           |

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

The master tables provide the basic data used by transaction tables.

---

## Transaction Tables

Transaction tables will be added based on the business process being implemented.

The immediate transaction focus is procurement:

- Purchase Orders
- Purchase Order Items
- Goods Receipts
- Goods Receipt Items

---

## Analytics Layer

Analytics will be added after the transaction data is ready.

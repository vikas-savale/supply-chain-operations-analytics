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

The master tables provide the basic data used by transaction tables.

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

---

## Inventory Schema

The `inventory` schema currently contains 3 tables:

- `stock`
- `movements`
- `stock_audits`

The inventory layer stores current stock, stock movement history and physical stock audit results.

---

## Warehouse Schema

The `warehouse` schema currently contains 2 transaction tables:

- `putaways`
- `putaway_items`

The putaway flow moves accepted stock from a receiving or staging location to a storage or picking location.

One putaway can contain multiple putaway items.

A goods receipt item can be split across multiple putaway items when stock is placed in more than one location.

---

## Logistics Schema

Logistics transaction tables will be added based on transport and delivery processes.

---

## Sales Schema

Sales transaction tables will be added after the required outbound processes are defined.

---

## Analytics Layer

Analytics will be added after the required transaction data is available.

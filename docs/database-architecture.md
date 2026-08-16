# Database Architecture

## Schemas

The database is divided into different business areas.

| Schema        | Purpose                                                       |
| ------------- | ------------------------------------------------------------- |
| `master`      | Core business master and reference data                       |
| `inventory`   | Inventory balances, stock movements and inventory adjustments |
| `procurement` | Purchase orders and goods receipts                            |
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

Inventory tables will be added after the receiving flow is complete.

---

## Warehouse Schema

Warehouse transaction tables will be added based on the warehouse processes being modeled.

---

## Logistics Schema

Logistics transaction tables will be added based on transport and delivery processes.

---

## Sales Schema

Sales transaction tables will be added after the required outbound processes are defined.

---

## Analytics Layer

Analytics will be added after the required transaction data is available.

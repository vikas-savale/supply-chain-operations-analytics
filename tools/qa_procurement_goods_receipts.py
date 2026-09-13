import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

BASE = Path("datasets")

PO_FILE = BASE / "procurement_purchase_orders.csv"
POI_FILE = BASE / "procurement_purchase_order_items.csv"
GR_FILE = BASE / "procurement_goods_receipts.csv"
GRI_FILE = BASE / "procurement_goods_receipt_items.csv"
PRODUCT_FILE = BASE / "master_products.csv"
VEHICLE_FILE = BASE / "master_vehicles.csv"
UOM_FILE = BASE / "master_uoms.csv"


EXPECTED_GR_COLUMNS = [
    "goods_receipt_id",
    "grn_number",
    "purchase_order_id",
    "warehouse_id",
    "vehicle_id",
    "receipt_date",
    "receipt_status",
    "notes",
    "created_date",
    "created_by",
    "updated_date",
    "updated_by",
]

EXPECTED_GRI_COLUMNS = [
    "goods_receipt_item_id",
    "goods_receipt_id",
    "purchase_order_item_id",
    "line_number",
    "product_id",
    "batch_code",
    "receipt_uom_id",
    "received_pac_quantity",
    "accepted_pac_quantity",
    "rejected_pac_quantity",
    "received_base_quantity",
    "accepted_base_quantity",
    "rejected_base_quantity",
    "notes",
    "created_date",
    "created_by",
    "updated_date",
    "updated_by",
]

ALLOWED_GR_STATUSES = {"partially_received", "received"}
EXPECTED_RECEIPT_STATUS = "received"


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def dec(value, field_name):
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise AssertionError(
            f"Invalid numeric value in {field_name}: {value!r}"
        )


def int_value(value, field_name):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise AssertionError(
            f"Invalid integer value in {field_name}: {value!r}"
        )


def parse_date(value, field_name):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        raise AssertionError(
            f"Invalid date in {field_name}: {value!r}"
        )


def normalize(value):
    return "" if value is None else str(value).strip()


def fail(errors, message):
    errors.append(message)


def main():
    errors = []

    # ------------------------------------------------------------
    # Load files
    # ------------------------------------------------------------
    po = read_csv(PO_FILE)
    poi = read_csv(POI_FILE)
    gr = read_csv(GR_FILE)
    gri = read_csv(GRI_FILE)
    products = read_csv(PRODUCT_FILE)
    vehicles = read_csv(VEHICLE_FILE)
    uoms = read_csv(UOM_FILE)

    print("Loaded:")
    print(f"  Purchase orders       : {len(po)}")
    print(f"  Purchase order items  : {len(poi)}")
    print(f"  Goods receipts        : {len(gr)}")
    print(f"  Goods receipt items   : {len(gri)}")
    print(f"  Products              : {len(products)}")
    print(f"  Vehicles              : {len(vehicles)}")
    print(f"  UOMs                  : {len(uoms)}")
    print()

    # ------------------------------------------------------------
    # Header checks
    # ------------------------------------------------------------
    if gr:
        if list(gr[0].keys()) != EXPECTED_GR_COLUMNS:
            fail(errors, "Goods receipt CSV header mismatch.")
    else:
        fail(errors, "Goods receipt CSV is empty.")

    if gri:
        if list(gri[0].keys()) != EXPECTED_GRI_COLUMNS:
            fail(errors, "Goods receipt item CSV header mismatch.")
    else:
        fail(errors, "Goods receipt item CSV is empty.")

    # ------------------------------------------------------------
    # Basic lookup structures
    # ------------------------------------------------------------
    po_by_id = {r["purchase_order_id"]: r for r in po}
    poi_by_id = {r["purchase_order_item_id"]: r for r in poi}
    product_by_id = {r["product_id"]: r for r in products}
    vehicle_by_id = {r["vehicle_id"]: r for r in vehicles}
    uom_by_id = {r["uom_id"]: r for r in uoms}

    po_items_by_po = defaultdict(list)
    for row in poi:
        po_items_by_po[row["purchase_order_id"]].append(row)

    gr_by_id = {r["goods_receipt_id"]: r for r in gr}

    gr_by_po = defaultdict(list)
    for row in gr:
        gr_by_po[row["purchase_order_id"]].append(row)

    gr_items_by_gr = defaultdict(list)
    for row in gri:
        gr_items_by_gr[row["goods_receipt_id"]].append(row)

    cumulative_received_pac = defaultdict(Decimal)
    cumulative_received_base = defaultdict(Decimal)

    # ------------------------------------------------------------
    # Expected row counts
    # ------------------------------------------------------------
    if len(po) != 1500:
        fail(errors, f"Expected 1500 POs, found {len(po)}.")

    if len(poi) != 6534:
        fail(errors, f"Expected 6534 PO items, found {len(poi)}.")

    if len(gr) != 1563:
        fail(errors, f"Expected 1563 GRs, found {len(gr)}.")

    if len(gri) != 6655:
        fail(errors, f"Expected 6655 GR items, found {len(gri)}.")

    # ------------------------------------------------------------
    # PO status checks
    # ------------------------------------------------------------
    status_counts = defaultdict(int)

    for row in po:
        status_counts[row["status"]] += 1

    expected_status_counts = {
        "draft": 60,
        "approved": 120,
        "sent": 150,
        "partially_received": 300,
        "received": 810,
        "cancelled": 60,
    }

    if dict(status_counts) != expected_status_counts:
        fail(
            errors,
            f"PO status distribution mismatch: "
            f"actual={dict(status_counts)}, "
            f"expected={expected_status_counts}",
        )

    # ------------------------------------------------------------
    # PO / PO item ID checks
    # ------------------------------------------------------------
    po_ids = [
        int_value(r["purchase_order_id"], "purchase_order_id")
        for r in po
    ]

    if len(po_ids) != len(set(po_ids)):
        fail(errors, "Duplicate purchase_order_id values.")

    if po_ids != list(range(1, 1501)):
        fail(
            errors,
            "Purchase order IDs are not sequential 1..1500.",
        )

    poi_ids = [
        int_value(
            r["purchase_order_item_id"],
            "purchase_order_item_id",
        )
        for r in poi
    ]

    if len(poi_ids) != len(set(poi_ids)):
        fail(
            errors,
            "Duplicate purchase_order_item_id values.",
        )

    if poi_ids != list(range(1, 6535)):
        fail(
            errors,
            "Purchase order item IDs are not sequential 1..6534.",
        )

    # ------------------------------------------------------------
    # GR / GR item ID checks
    # ------------------------------------------------------------
    gr_ids = [
        int_value(
            r["goods_receipt_id"],
            "goods_receipt_id",
        )
        for r in gr
    ]

    if len(gr_ids) != len(set(gr_ids)):
        fail(errors, "Duplicate goods_receipt_id values.")

    if gr_ids != list(range(1, len(gr) + 1)):
        fail(errors, "Goods receipt IDs are not sequential.")

    gri_ids = [
        int_value(
            r["goods_receipt_item_id"],
            "goods_receipt_item_id",
        )
        for r in gri
    ]

    if len(gri_ids) != len(set(gri_ids)):
        fail(
            errors,
            "Duplicate goods_receipt_item_id values.",
        )

    if gri_ids != list(range(1, len(gri) + 1)):
        fail(
            errors,
            "Goods receipt item IDs are not sequential.",
        )

    grn_numbers = [
        normalize(r["grn_number"])
        for r in gr
    ]

    if len(grn_numbers) != len(set(grn_numbers)):
        fail(errors, "Duplicate GRN numbers found.")

    if any(not x for x in grn_numbers):
        fail(errors, "Blank GRN number found.")

    # ------------------------------------------------------------
    # Vehicle reference checks
    # ------------------------------------------------------------
    for row in gr:
        vehicle_id = normalize(row["vehicle_id"])

        if vehicle_id == "":
            continue

        if vehicle_id not in vehicle_by_id:
            fail(
                errors,
                f"GR {row['goods_receipt_id']} references "
                f"unknown vehicle_id {vehicle_id}.",
            )

    # ------------------------------------------------------------
    # Goods receipt header validation
    # ------------------------------------------------------------
    for row in gr:
        gr_id = row["goods_receipt_id"]
        po_id = row["purchase_order_id"]

        if po_id not in po_by_id:
            fail(
                errors,
                f"GR {gr_id} references unknown PO {po_id}.",
            )
            continue

        po_row = po_by_id[po_id]

        # Eligibility
        if po_row["status"] not in ALLOWED_GR_STATUSES:
            fail(
                errors,
                f"GR {gr_id} belongs to ineligible PO {po_id} "
                f"with status {po_row['status']}.",
            )

        # Warehouse
        if row["warehouse_id"] != po_row["warehouse_id"]:
            fail(
                errors,
                f"Warehouse mismatch: GR {gr_id}, PO {po_id}.",
            )

        # Receipt status
        if row["receipt_status"] != EXPECTED_RECEIPT_STATUS:
            fail(
                errors,
                f"GR {gr_id} has receipt_status "
                f"{row['receipt_status']!r}, "
                f"expected 'received'.",
            )

        # Receipt date
        po_date = parse_date(
            po_row["po_date"],
            "po_date",
        )

        receipt_date = parse_date(
            row["receipt_date"],
            "receipt_date",
        )

        if receipt_date < po_date:
            fail(
                errors,
                f"GR {gr_id} receipt_date {receipt_date} "
                f"is before PO date {po_date}.",
            )

    # ------------------------------------------------------------
    # GR count per PO
    # ------------------------------------------------------------
    for po_id, po_row in po_by_id.items():
        status = po_row["status"]
        gr_count = len(gr_by_po.get(po_id, []))

        if status in ALLOWED_GR_STATUSES:
            if not 1 <= gr_count <= 3:
                fail(
                    errors,
                    f"PO {po_id} ({status}) has "
                    f"{gr_count} GRs; expected 1-3.",
                )
        else:
            if gr_count != 0:
                fail(
                    errors,
                    f"PO {po_id} ({status}) has "
                    f"{gr_count} GRs; expected 0.",
                )

    # ------------------------------------------------------------
    # Chronological GR dates and expected-date rules
    #
    # Generator business rule:
    # - First GR date = expected_date + offset between -2 and +2,
    #   never before po_date.
    # - Each subsequent GR date = previous GR date + 1 to 5 days.
    # ------------------------------------------------------------
    for po_id, rows in gr_by_po.items():
        po_row = po_by_id[po_id]

        po_date = parse_date(
            po_row["po_date"],
            "po_date",
        )

        expected_date = parse_date(
            po_row["expected_date"],
            "expected_date",
        )

        ordered = sorted(
            rows,
            key=lambda r: int_value(
                r["goods_receipt_id"],
                "goods_receipt_id",
            ),
        )

        receipt_dates = [
            parse_date(
                r["receipt_date"],
                "receipt_date",
            )
            for r in ordered
        ]

        # First receipt:
        # expected_date -2 to +2 days,
        # never before PO date.
        first_date = receipt_dates[0]
        first_delta = (first_date - expected_date).days

        if first_date < po_date:
            fail(
                errors,
                f"PO {po_id}: first GR date {first_date} "
                f"is before PO date {po_date}.",
            )

        if first_delta < -2 or first_delta > 2:
            fail(
                errors,
                f"PO {po_id}: first GR date differs from "
                f"expected date by {first_delta} days; "
                f"expected range is -2 to +2.",
            )

        # Subsequent receipts:
        # strictly chronological, 1-5 days apart.
        for index in range(1, len(receipt_dates)):
            previous_date = receipt_dates[index - 1]
            current_date = receipt_dates[index]

            gap_days = (
                current_date - previous_date
            ).days

            if gap_days < 1 or gap_days > 5:
                fail(
                    errors,
                    f"PO {po_id}: GR date gap between "
                    f"receipt {index} and {index + 1} "
                    f"is {gap_days} days; "
                    f"expected range is 1-5.",
                )

    # ------------------------------------------------------------
    # GR line numbering
    # ------------------------------------------------------------
    for gr_id, rows in gr_items_by_gr.items():
        line_numbers = [
            int_value(
                r["line_number"],
                "line_number",
            )
            for r in rows
        ]

        expected_lines = list(range(1, len(rows) + 1))

        if line_numbers != expected_lines:
            fail(
                errors,
                f"GR {gr_id} line numbering invalid: "
                f"{line_numbers} vs {expected_lines}.",
            )

    # ------------------------------------------------------------
    # GR item validation
    # ------------------------------------------------------------
    for row in gri:
        gri_id = row["goods_receipt_item_id"]
        gr_id = row["goods_receipt_id"]
        poi_id = row["purchase_order_item_id"]

        if gr_id not in gr_by_id:
            fail(
                errors,
                f"GR item {gri_id} references unknown "
                f"goods_receipt_id {gr_id}.",
            )
            continue

        if poi_id not in poi_by_id:
            fail(
                errors,
                f"GR item {gri_id} references unknown "
                f"PO item {poi_id}.",
            )
            continue

        gr_row = gr_by_id[gr_id]
        poi_row = poi_by_id[poi_id]

        po_id = gr_row["purchase_order_id"]

        # PO item must belong to the GR's PO
        if poi_row["purchase_order_id"] != po_id:
            fail(
                errors,
                f"GR item {gri_id}: PO item {poi_id} belongs "
                f"to PO {poi_row['purchase_order_id']}, "
                f"but GR {gr_id} belongs to PO {po_id}.",
            )

        # Product match
        if row["product_id"] != poi_row["product_id"]:
            fail(
                errors,
                f"GR item {gri_id}: product mismatch "
                f"with PO item {poi_id}.",
            )

        # UOM match
        if row["receipt_uom_id"] != poi_row["purchase_uom_id"]:
            fail(
                errors,
                f"GR item {gri_id}: receipt UOM mismatch "
                f"with PO item {poi_id}.",
            )

        # Product reference
        product_id = row["product_id"]

        if product_id not in product_by_id:
            fail(
                errors,
                f"GR item {gri_id} references unknown "
                f"product_id {product_id}.",
            )

        # UOM reference
        uom_id = row["receipt_uom_id"]

        if uom_id not in uom_by_id:
            fail(
                errors,
                f"GR item {gri_id} references unknown "
                f"receipt_uom_id {uom_id}.",
            )

        # Batch code
        if not normalize(row["batch_code"]):
            fail(
                errors,
                f"GR item {gri_id} has blank batch_code.",
            )

        # Quantity values
        received_pac = dec(
            row["received_pac_quantity"],
            "received_pac_quantity",
        )

        accepted_pac = dec(
            row["accepted_pac_quantity"],
            "accepted_pac_quantity",
        )

        rejected_pac = dec(
            row["rejected_pac_quantity"],
            "rejected_pac_quantity",
        )

        received_base = dec(
            row["received_base_quantity"],
            "received_base_quantity",
        )

        accepted_base = dec(
            row["accepted_base_quantity"],
            "accepted_base_quantity",
        )

        rejected_base = dec(
            row["rejected_base_quantity"],
            "rejected_base_quantity",
        )

        if received_pac <= 0:
            fail(
                errors,
                f"GR item {gri_id}: "
                f"received_pac_quantity must be > 0.",
            )

        if accepted_pac < 0 or rejected_pac < 0:
            fail(
                errors,
                f"GR item {gri_id}: accepted/rejected "
                f"PAC cannot be negative.",
            )

        if accepted_base < 0 or rejected_base < 0:
            fail(
                errors,
                f"GR item {gri_id}: accepted/rejected "
                f"base cannot be negative.",
            )

        if accepted_pac + rejected_pac != received_pac:
            fail(
                errors,
                f"GR item {gri_id}: accepted_pac + "
                f"rejected_pac != received_pac.",
            )

        if accepted_base + rejected_base != received_base:
            fail(
                errors,
                f"GR item {gri_id}: accepted_base + "
                f"rejected_base != received_base.",
            )

        if received_base <= 0:
            fail(
                errors,
                f"GR item {gri_id}: "
                f"received_base_quantity must be > 0.",
            )

        # Base quantity reconciliation
        if product_id in product_by_id:
            product = product_by_id[product_id]

            base_qty_per_pac_raw = product.get(
                "base_quantity_per_pac",
                "",
            )

            if normalize(base_qty_per_pac_raw) == "":
                fail(
                    errors,
                    f"Product {product_id}: missing "
                    f"base_quantity_per_pac.",
                )
            else:
                base_qty_per_pac = dec(
                    base_qty_per_pac_raw,
                    f"product {product_id} "
                    f"base_quantity_per_pac",
                )

                calculated_base = (
                    received_pac * base_qty_per_pac
                )

                if received_base != calculated_base:
                    fail(
                        errors,
                        f"GR item {gri_id}: "
                        f"received_base_quantity "
                        f"{received_base} != "
                        f"received_pac_quantity "
                        f"{received_pac} * "
                        f"base_quantity_per_pac "
                        f"{base_qty_per_pac} = "
                        f"{calculated_base}.",
                    )

                calculated_accepted_base = (
                    accepted_pac * base_qty_per_pac
                )

                calculated_rejected_base = (
                    rejected_pac * base_qty_per_pac
                )

                if accepted_base != calculated_accepted_base:
                    fail(
                        errors,
                        f"GR item {gri_id}: "
                        f"accepted_base_quantity mismatch.",
                    )

                if rejected_base != calculated_rejected_base:
                    fail(
                        errors,
                        f"GR item {gri_id}: "
                        f"rejected_base_quantity mismatch.",
                    )

        cumulative_received_pac[poi_id] += received_pac
        cumulative_received_base[poi_id] += received_base

    # ------------------------------------------------------------
    # No duplicate PO item within the same GR
    # ------------------------------------------------------------
    seen_gr_poi = set()

    for row in gri:
        key = (
            row["goods_receipt_id"],
            row["purchase_order_item_id"],
        )

        if key in seen_gr_poi:
            fail(
                errors,
                f"PO item {row['purchase_order_item_id']} "
                f"appears more than once in GR "
                f"{row['goods_receipt_id']}.",
            )

        seen_gr_poi.add(key)

    # ------------------------------------------------------------
    # Cumulative receipt <= ordered
    # ------------------------------------------------------------
    for poi_id, received_pac in cumulative_received_pac.items():
        poi_row = poi_by_id[poi_id]

        ordered_pac = dec(
            poi_row["ordered_pac_quantity"],
            "ordered_pac_quantity",
        )

        if received_pac > ordered_pac:
            fail(
                errors,
                f"PO item {poi_id}: cumulative received PAC "
                f"{received_pac} > ordered PAC {ordered_pac}.",
            )

    # ------------------------------------------------------------
    # PO-level receipt reconciliation
    # ------------------------------------------------------------
    for po_id, po_row in po_by_id.items():
        item_rows = po_items_by_po[po_id]

        ordered_total = sum(
            (
                dec(
                    r["ordered_pac_quantity"],
                    "ordered_pac_quantity",
                )
                for r in item_rows
            ),
            Decimal("0"),
        )

        received_total = Decimal("0")

        for item in item_rows:
            received_total += cumulative_received_pac.get(
                item["purchase_order_item_id"],
                Decimal("0"),
            )

        status = po_row["status"]

        if status == "received":
            if received_total != ordered_total:
                fail(
                    errors,
                    f"Received PO {po_id}: received total "
                    f"{received_total} != ordered total "
                    f"{ordered_total}.",
                )

            for item in item_rows:
                poi_id = item["purchase_order_item_id"]

                ordered = dec(
                    item["ordered_pac_quantity"],
                    "ordered_pac_quantity",
                )

                received = cumulative_received_pac.get(
                    poi_id,
                    Decimal("0"),
                )

                if received != ordered:
                    fail(
                        errors,
                        f"Received PO {po_id}, PO item {poi_id}: "
                        f"received {received} != "
                        f"ordered {ordered}.",
                    )

        elif status == "partially_received":
            if received_total <= 0:
                fail(
                    errors,
                    f"Partially received PO {po_id} "
                    f"has no received quantity.",
                )

            if received_total >= ordered_total:
                fail(
                    errors,
                    f"Partially received PO {po_id}: "
                    f"received total {received_total} >= "
                    f"ordered total {ordered_total}.",
                )

        else:
            if received_total != 0:
                fail(
                    errors,
                    f"Non-receiving PO {po_id} ({status}) "
                    f"has received quantity {received_total}.",
                )

    # ------------------------------------------------------------
    # GR receipt order follows chronological receipt dates
    # ------------------------------------------------------------
    for po_id, rows in gr_by_po.items():
        receipt_dates = [
            parse_date(
                r["receipt_date"],
                "receipt_date",
            )
            for r in rows
        ]

        if receipt_dates != sorted(receipt_dates):
            fail(
                errors,
                f"Receipt dates are not chronological "
                f"for PO {po_id}.",
            )

    # ------------------------------------------------------------
    # GR ↔ PO item coverage sanity
    # ------------------------------------------------------------
    for po_id, rows in gr_by_po.items():
        item_ids = {
            row["purchase_order_item_id"]
            for gr_row in rows
            for row in gr_items_by_gr[
                gr_row["goods_receipt_id"]
            ]
        }

        if not item_ids:
            fail(
                errors,
                f"PO {po_id} has GR headers but no GR items.",
            )

        valid_item_ids = {
            row["purchase_order_item_id"]
            for row in po_items_by_po[po_id]
        }

        invalid = item_ids - valid_item_ids

        if invalid:
            fail(
                errors,
                f"PO {po_id} has GR items outside its "
                f"PO item set: {sorted(invalid)}",
            )

    # ------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------
    gr_status_counts = defaultdict(int)

    for row in gr:
        gr_status_counts[row["receipt_status"]] += 1

    vehicle_used = sum(
        1
        for row in gr
        if normalize(row["vehicle_id"])
    )

    vehicle_null = len(gr) - vehicle_used

    print("GR receipt_status distribution:")

    for status, count in sorted(gr_status_counts.items()):
        print(f"  {status:10s}: {count}")

    print()
    print(f"GRs with vehicle   : {vehicle_used}")
    print(f"GRs without vehicle: {vehicle_null}")
    print()

    if errors:
        print("CSV QA: FAILED")
        print(f"Total errors: {len(errors)}")
        print()

        for i, error in enumerate(errors[:100], start=1):
            print(f"{i}. {error}")

        if len(errors) > 100:
            print()
            print(
                f"... and {len(errors) - 100} more errors."
            )

        raise SystemExit(1)

    print("CSV QA: PASSED")
    print(
        "All procurement GR/GR-item reconciliation checks passed."
    )


if __name__ == "__main__":
    main()
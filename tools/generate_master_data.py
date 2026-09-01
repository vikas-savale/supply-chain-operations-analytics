from datetime import datetime
from pathlib import Path
import csv


# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = Path("datasets")

DEFAULT_CREATED_BY = "system"
DEFAULT_UPDATED_BY = "system"

MASTER_DATA_DATE = datetime(2026, 1, 1, 0, 0, 0)

COMPANY_NAME = "Northridge Industrial Products"


# ============================================================
# UOM master definitions
# ============================================================

UOM_DEFINITIONS = [
    {
        "uom_id": 1,
        "uom_code": "L",
        "uom_name": "Litre",
        "uom_category": "volume",
        "is_active": True,
    },
    {
        "uom_id": 2,
        "uom_code": "ML",
        "uom_name": "Millilitre",
        "uom_category": "volume",
        "is_active": True,
    },
    {
        "uom_id": 3,
        "uom_code": "KG",
        "uom_name": "Kilogram",
        "uom_category": "weight",
        "is_active": True,
    },
    {
        "uom_id": 4,
        "uom_code": "G",
        "uom_name": "Gram",
        "uom_category": "weight",
        "is_active": True,
    },
    {
        "uom_id": 5,
        "uom_code": "EA",
        "uom_name": "Each",
        "uom_category": "quantity",
        "is_active": True,
    },
    {
        "uom_id": 6,
        "uom_code": "PAC",
        "uom_name": "Package",
        "uom_category": "quantity",
        "is_active": True,
    },
]


# ============================================================
# Payment term master definitions
# ============================================================

PAYMENT_TERM_DEFINITIONS = [
    {
        "payment_term_id": 1,
        "payment_term_code": "PT001",
        "payment_term_name": "Immediate",
        "payment_term_days": 0,
        "payment_term_description": "Payment due immediately.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 2,
        "payment_term_code": "PT002",
        "payment_term_name": "15 Days",
        "payment_term_days": 15,
        "payment_term_description": "Payment due within 15 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 3,
        "payment_term_code": "PT003",
        "payment_term_name": "30 Days",
        "payment_term_days": 30,
        "payment_term_description": "Payment due within 30 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 4,
        "payment_term_code": "PT004",
        "payment_term_name": "45 Days",
        "payment_term_days": 45,
        "payment_term_description": "Payment due within 45 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 5,
        "payment_term_code": "PT005",
        "payment_term_name": "60 Days",
        "payment_term_days": 60,
        "payment_term_description": "Payment due within 60 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 6,
        "payment_term_code": "PT006",
        "payment_term_name": "75 Days",
        "payment_term_days": 75,
        "payment_term_description": "Payment due within 75 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 7,
        "payment_term_code": "PT007",
        "payment_term_name": "90 Days",
        "payment_term_days": 90,
        "payment_term_description": "Payment due within 90 days.",
        "payment_term_status": "active",
    },
    {
        "payment_term_id": 8,
        "payment_term_code": "PT008",
        "payment_term_name": "120 Days",
        "payment_term_days": 120,
        "payment_term_description": "Payment due within 120 days.",
        "payment_term_status": "active",
    },
]


# ============================================================
# Brand master definitions
# ============================================================

BRAND_DEFINITIONS = [
    {
        "brand_id": 1,
        "brand_code": "BR001",
        "brand_name": "Northmark",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 2,
        "brand_code": "BR002",
        "brand_name": "Ironcrest",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 3,
        "brand_code": "BR003",
        "brand_name": "Redstone",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 4,
        "brand_code": "BR004",
        "brand_name": "Westmark",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 5,
        "brand_code": "BR005",
        "brand_name": "Crestfield",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 6,
        "brand_code": "BR006",
        "brand_name": "Stonebridge",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 7,
        "brand_code": "BR007",
        "brand_name": "Ridgewell",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 8,
        "brand_code": "BR008",
        "brand_name": "Millbrook",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 9,
        "brand_code": "BR009",
        "brand_name": "Highpoint",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
    {
        "brand_id": 10,
        "brand_code": "BR010",
        "brand_name": "Fieldmark",
        "brand_owner_company": COMPANY_NAME,
        "brand_status": "active",
    },
]


# ============================================================
# Category master definitions
# ============================================================

CATEGORY_DEFINITIONS = [
    {
        "category_id": 1,
        "category_code": "CAT001",
        "category_name": "Automotive Engine Oils",
        "category_status": "active",
    },
    {
        "category_id": 2,
        "category_code": "CAT002",
        "category_name": "Automotive & Drivetrain Fluids",
        "category_status": "active",
    },
    {
        "category_id": 3,
        "category_code": "CAT003",
        "category_name": "Industrial Lubricants",
        "category_status": "active",
    },
    {
        "category_id": 4,
        "category_code": "CAT004",
        "category_name": "Hydraulic & Equipment Fluids",
        "category_status": "active",
    },
    {
        "category_id": 5,
        "category_code": "CAT005",
        "category_name": "Greases",
        "category_status": "active",
    },
    {
        "category_id": 6,
        "category_code": "CAT006",
        "category_name": "Coolants & Maintenance Fluids",
        "category_status": "active",
    },
    {
        "category_id": 7,
        "category_code": "CAT007",
        "category_name": "Specialty & Process Fluids",
        "category_status": "active",
    },
    {
        "category_id": 8,
        "category_code": "CAT008",
        "category_name": "Agricultural & Off-Highway Lubricants",
        "category_status": "active",
    },
]


# ============================================================
# Sub-category master definitions
# ============================================================

SUB_CATEGORY_DEFINITIONS = [
    {
        "sub_category_id": 1,
        "category_id": 1,
        "sub_category_code": "SUB001",
        "sub_category_name": "Passenger Car Engine Oils",
        "description": "Engine oils for passenger cars.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 2,
        "category_id": 1,
        "sub_category_code": "SUB002",
        "sub_category_name": "Heavy-Duty Diesel Engine Oils",
        "description": "Engine oils for heavy-duty diesel applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 3,
        "category_id": 1,
        "sub_category_code": "SUB003",
        "sub_category_name": "Commercial Vehicle Engine Oils",
        "description": "Engine oils for commercial vehicle applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 4,
        "category_id": 1,
        "sub_category_code": "SUB004",
        "sub_category_name": "Motorcycle Engine Oils",
        "description": "Engine oils for motorcycle applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 5,
        "category_id": 1,
        "sub_category_code": "SUB005",
        "sub_category_name": "Natural Gas Engine Oils",
        "description": "Engine oils for natural gas engine applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 6,
        "category_id": 2,
        "sub_category_code": "SUB006",
        "sub_category_name": "Gear Oils",
        "description": "Lubricants for automotive gear systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 7,
        "category_id": 2,
        "sub_category_code": "SUB007",
        "sub_category_name": "Automatic Transmission Fluids",
        "description": "Fluids for automatic transmission systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 8,
        "category_id": 2,
        "sub_category_code": "SUB008",
        "sub_category_name": "Manual Transmission Fluids",
        "description": "Fluids for manual transmission systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 9,
        "category_id": 2,
        "sub_category_code": "SUB009",
        "sub_category_name": "Differential Oils",
        "description": "Lubricants for vehicle differential systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 10,
        "category_id": 2,
        "sub_category_code": "SUB010",
        "sub_category_name": "Axle & Final Drive Oils",
        "description": "Lubricants for axle and final drive systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 11,
        "category_id": 3,
        "sub_category_code": "SUB011",
        "sub_category_name": "Industrial Gear Oils",
        "description": "Gear oils for industrial equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 12,
        "category_id": 3,
        "sub_category_code": "SUB012",
        "sub_category_name": "Compressor Oils",
        "description": "Lubricants for compressor equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 13,
        "category_id": 3,
        "sub_category_code": "SUB013",
        "sub_category_name": "Turbine Oils",
        "description": "Lubricants for turbine equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 14,
        "category_id": 3,
        "sub_category_code": "SUB014",
        "sub_category_name": "Circulating Oils",
        "description": "Circulating oils for industrial machinery.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 15,
        "category_id": 3,
        "sub_category_code": "SUB015",
        "sub_category_name": "Slideway Oils",
        "description": "Lubricants for machine tool slideways.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 16,
        "category_id": 3,
        "sub_category_code": "SUB016",
        "sub_category_name": "Machine Tool Oils",
        "description": "Lubricants for machine tool applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 17,
        "category_id": 4,
        "sub_category_code": "SUB017",
        "sub_category_name": "Hydraulic Oils",
        "description": "Hydraulic fluids for industrial and mobile equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 18,
        "category_id": 4,
        "sub_category_code": "SUB018",
        "sub_category_name": "Hydraulic Transmission Fluids",
        "description": "Fluids for combined hydraulic and transmission systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 19,
        "category_id": 4,
        "sub_category_code": "SUB019",
        "sub_category_name": "Tractor Hydraulic Fluids",
        "description": "Hydraulic fluids for tractor systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 20,
        "category_id": 4,
        "sub_category_code": "SUB020",
        "sub_category_name": "Construction Equipment Fluids",
        "description": "Fluids for construction equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 21,
        "category_id": 4,
        "sub_category_code": "SUB021",
        "sub_category_name": "Agricultural Equipment Fluids",
        "description": "Fluids for agricultural equipment.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 22,
        "category_id": 5,
        "sub_category_code": "SUB022",
        "sub_category_name": "Multipurpose Greases",
        "description": "General-purpose greases for multiple applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 23,
        "category_id": 5,
        "sub_category_code": "SUB023",
        "sub_category_name": "EP Greases",
        "description": "Extreme-pressure greases for demanding loads.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 24,
        "category_id": 5,
        "sub_category_code": "SUB024",
        "sub_category_name": "High Temperature Greases",
        "description": "Greases designed for high-temperature applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 25,
        "category_id": 5,
        "sub_category_code": "SUB025",
        "sub_category_name": "Lithium Greases",
        "description": "Lithium-based greases for industrial and automotive use.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 26,
        "category_id": 5,
        "sub_category_code": "SUB026",
        "sub_category_name": "Calcium Greases",
        "description": "Calcium-based greases for suitable applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 27,
        "category_id": 5,
        "sub_category_code": "SUB027",
        "sub_category_name": "Special Purpose Greases",
        "description": "Greases for specialised operating conditions.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 28,
        "category_id": 6,
        "sub_category_code": "SUB028",
        "sub_category_name": "Engine Coolants",
        "description": "Coolants for engine cooling systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 29,
        "category_id": 6,
        "sub_category_code": "SUB029",
        "sub_category_name": "Long Life Coolants",
        "description": "Extended-life engine coolant products.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 30,
        "category_id": 6,
        "sub_category_code": "SUB030",
        "sub_category_name": "Ready-to-Use Coolants",
        "description": "Pre-mixed coolants ready for use.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 31,
        "category_id": 6,
        "sub_category_code": "SUB031",
        "sub_category_name": "Antifreeze Concentrates",
        "description": "Concentrated antifreeze products.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 32,
        "category_id": 6,
        "sub_category_code": "SUB032",
        "sub_category_name": "Radiator Fluids",
        "description": "Fluids for radiator and cooling-system maintenance.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 33,
        "category_id": 7,
        "sub_category_code": "SUB033",
        "sub_category_name": "Cutting Fluids",
        "description": "Fluids used in metal cutting operations.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 34,
        "category_id": 7,
        "sub_category_code": "SUB034",
        "sub_category_name": "Metalworking Fluids",
        "description": "Process fluids used in metalworking applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 35,
        "category_id": 7,
        "sub_category_code": "SUB035",
        "sub_category_name": "Heat Transfer Fluids",
        "description": "Fluids used in heat transfer systems.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 36,
        "category_id": 7,
        "sub_category_code": "SUB036",
        "sub_category_name": "Rust Preventive Fluids",
        "description": "Fluids used to protect metal surfaces against corrosion.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 37,
        "category_id": 7,
        "sub_category_code": "SUB037",
        "sub_category_name": "Electrical Insulating Oils",
        "description": "Insulating oils for electrical applications.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 38,
        "category_id": 8,
        "sub_category_code": "SUB038",
        "sub_category_name": "Tractor Engine Oils",
        "description": "Engine oils for tractors.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 39,
        "category_id": 8,
        "sub_category_code": "SUB039",
        "sub_category_name": "Tractor Transmission Oils",
        "description": "Transmission oils for tractors.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 40,
        "category_id": 8,
        "sub_category_code": "SUB040",
        "sub_category_name": "Tractor Differential Oils",
        "description": "Differential oils for tractors.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 41,
        "category_id": 8,
        "sub_category_code": "SUB041",
        "sub_category_name": "Agricultural Machinery Oils",
        "description": "Lubricants for agricultural machinery.",
        "sub_category_status": "active",
    },
    {
        "sub_category_id": 42,
        "category_id": 8,
        "sub_category_code": "SUB042",
        "sub_category_name": "Off-Highway Engine Oils",
        "description": "Engine oils for off-highway equipment.",
        "sub_category_status": "active",
    },
]


# ============================================================
# Warehouse master definitions
# ============================================================

WAREHOUSE_DEFINITIONS = [
    {
        "warehouse_id": 1,
        "warehouse_code": "WH001",
        "warehouse_name": "Pune Central Distribution Centre",
        "warehouse_type": "central",
        "address_line1": "MIDC Logistics Park, Block A",
        "address_line2": "Bhosari Industrial Area",
        "city": "Pune",
        "state": "Maharashtra",
        "postal_code": "411026",
        "country": "India",
        "total_capacity_ltr": 650000,
        "usable_capacity_ltr": 560000,
        "storage_mode": "mixed",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 2,
        "warehouse_code": "WH002",
        "warehouse_name": "Bhiwandi Regional Warehouse",
        "warehouse_type": "regional",
        "address_line1": "Distribution Estate, Plot 14",
        "address_line2": "Wada Road",
        "city": "Bhiwandi",
        "state": "Maharashtra",
        "postal_code": "421302",
        "country": "India",
        "total_capacity_ltr": 450000,
        "usable_capacity_ltr": 390000,
        "storage_mode": "covered",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 3,
        "warehouse_code": "WH003",
        "warehouse_name": "Ahmedabad Regional Warehouse",
        "warehouse_type": "regional",
        "address_line1": "Industrial Distribution Park, Plot 22",
        "address_line2": "Changodar Area",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "postal_code": "382213",
        "country": "India",
        "total_capacity_ltr": 420000,
        "usable_capacity_ltr": 360000,
        "storage_mode": "covered",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 4,
        "warehouse_code": "WH004",
        "warehouse_name": "Indore Regional Warehouse",
        "warehouse_type": "regional",
        "address_line1": "Industrial Storage Complex, Unit 7",
        "address_line2": "Pithampur Road",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "postal_code": "453001",
        "country": "India",
        "total_capacity_ltr": 350000,
        "usable_capacity_ltr": 300000,
        "storage_mode": "mixed",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 5,
        "warehouse_code": "WH005",
        "warehouse_name": "Bengaluru Regional Warehouse",
        "warehouse_type": "regional",
        "address_line1": "Industrial Logistics Park, Phase 2",
        "address_line2": "Hoskote Road",
        "city": "Bengaluru",
        "state": "Karnataka",
        "postal_code": "562114",
        "country": "India",
        "total_capacity_ltr": 360000,
        "usable_capacity_ltr": 310000,
        "storage_mode": "covered",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 6,
        "warehouse_code": "WH006",
        "warehouse_name": "Hyderabad Regional Warehouse",
        "warehouse_type": "regional",
        "address_line1": "Industrial Logistics Estate, Plot 18",
        "address_line2": "Medchal Road",
        "city": "Hyderabad",
        "state": "Telangana",
        "postal_code": "501401",
        "country": "India",
        "total_capacity_ltr": 320000,
        "usable_capacity_ltr": 275000,
        "storage_mode": "mixed",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 7,
        "warehouse_code": "WH007",
        "warehouse_name": "Nagpur Distribution Depot",
        "warehouse_type": "depot",
        "address_line1": "Regional Storage Yard, Unit 4",
        "address_line2": "Butibori Industrial Area",
        "city": "Nagpur",
        "state": "Maharashtra",
        "postal_code": "441122",
        "country": "India",
        "total_capacity_ltr": 220000,
        "usable_capacity_ltr": 190000,
        "storage_mode": "mixed",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 8,
        "warehouse_code": "WH008",
        "warehouse_name": "Nashik Distribution Depot",
        "warehouse_type": "depot",
        "address_line1": "Industrial Storage Yard, Unit 3",
        "address_line2": "Ambad Industrial Area",
        "city": "Nashik",
        "state": "Maharashtra",
        "postal_code": "422010",
        "country": "India",
        "total_capacity_ltr": 180000,
        "usable_capacity_ltr": 155000,
        "storage_mode": "mixed",
        "warehouse_status": "active",
    },
    {
        "warehouse_id": 9,
        "warehouse_code": "WH009",
        "warehouse_name": "Sanand Cross-Dock Facility",
        "warehouse_type": "cross_dock",
        "address_line1": "Industrial Transit Park, Dock 6",
        "address_line2": "Sanand Industrial Area",
        "city": "Sanand",
        "state": "Gujarat",
        "postal_code": "382110",
        "country": "India",
        "total_capacity_ltr": 160000,
        "usable_capacity_ltr": 80000,
        "storage_mode": "covered",
        "warehouse_status": "active",
    },
]


# ============================================================
# Location distribution
# ============================================================

LOCATION_TYPE_COUNTS = {
    1: {
        "receiving": 5,
        "storage": 55,
        "picking": 20,
        "dispatch": 5,
        "quarantine": 4,
        "returns": 3,
        "damage": 3,
        "staging": 5,
    },
    2: {
        "receiving": 4,
        "storage": 42,
        "picking": 14,
        "dispatch": 4,
        "quarantine": 3,
        "returns": 2,
        "damage": 2,
        "staging": 4,
    },
    3: {
        "receiving": 4,
        "storage": 36,
        "picking": 12,
        "dispatch": 4,
        "quarantine": 2,
        "returns": 2,
        "damage": 2,
        "staging": 3,
    },
    4: {
        "receiving": 3,
        "storage": 30,
        "picking": 10,
        "dispatch": 3,
        "quarantine": 2,
        "returns": 2,
        "damage": 2,
        "staging": 3,
    },
    5: {
        "receiving": 3,
        "storage": 30,
        "picking": 10,
        "dispatch": 3,
        "quarantine": 2,
        "returns": 2,
        "damage": 2,
        "staging": 3,
    },
    6: {
        "receiving": 3,
        "storage": 27,
        "picking": 9,
        "dispatch": 3,
        "quarantine": 2,
        "returns": 2,
        "damage": 2,
        "staging": 2,
    },
    7: {
        "receiving": 2,
        "storage": 18,
        "picking": 6,
        "dispatch": 2,
        "quarantine": 2,
        "returns": 1,
        "damage": 1,
        "staging": 3,
    },
    8: {
        "receiving": 2,
        "storage": 15,
        "picking": 5,
        "dispatch": 2,
        "quarantine": 1,
        "returns": 1,
        "damage": 1,
        "staging": 3,
    },
    9: {
        "receiving": 3,
        "storage": 8,
        "picking": 5,
        "dispatch": 5,
        "quarantine": 2,
        "returns": 1,
        "damage": 1,
        "staging": 10,
    },
}


# ============================================================
# Location capacity allocation
# ============================================================

LOCATION_CAPACITY_SHARES = {
    "storage": 0.50,
    "picking": 0.18,
    "receiving": 0.08,
    "dispatch": 0.05,
    "staging": 0.07,
    "quarantine": 0.05,
    "returns": 0.035,
    "damage": 0.035,
}

LOCATION_CAPACITY_UTILIZATION = 0.95


# ============================================================
# Location generation rules
# ============================================================

LOCATION_TYPE_ORDER = [
    "receiving",
    "storage",
    "picking",
    "dispatch",
    "quarantine",
    "returns",
    "damage",
    "staging",
]


# ============================================================
# Common helpers
# ============================================================

def format_timestamp(value: datetime) -> str:
    """Return a PostgreSQL-friendly timestamp string."""

    return value.strftime("%Y-%m-%d %H:%M:%S")


def add_audit_columns(row: dict) -> dict:
    """Add standard audit fields to a master-data row."""

    timestamp = format_timestamp(MASTER_DATA_DATE)

    return {
        **row,
        "created_date": timestamp,
        "created_by": DEFAULT_CREATED_BY,
        "updated_date": timestamp,
        "updated_by": DEFAULT_UPDATED_BY,
    }


def get_warehouse_by_id(warehouse_id: int) -> dict:
    """Return a warehouse definition by ID."""

    for warehouse in WAREHOUSE_DEFINITIONS:
        if warehouse["warehouse_id"] == warehouse_id:
            return warehouse

    raise ValueError(
        f"Warehouse not found: {warehouse_id}"
    )


# ============================================================
# UOM validation
# ============================================================

def validate_uoms(uoms: list[dict]) -> None:
    """Validate UOM master data."""

    if not uoms:
        raise ValueError("UOM data is empty.")

    required_fields = {
        "uom_id",
        "uom_code",
        "uom_name",
        "uom_category",
        "is_active",
    }

    for row in uoms:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing UOM fields: {sorted(missing_fields)}"
            )

    uom_ids = [row["uom_id"] for row in uoms]
    uom_codes = [row["uom_code"] for row in uoms]
    uom_names = [row["uom_name"] for row in uoms]

    if len(uom_ids) != len(set(uom_ids)):
        raise ValueError("Duplicate uom_id found.")

    if len(uom_codes) != len(set(uom_codes)):
        raise ValueError("Duplicate uom_code found.")

    if len(uom_names) != len(set(uom_names)):
        raise ValueError("Duplicate uom_name found.")

    if uom_ids != sorted(uom_ids):
        raise ValueError("UOM IDs are not in ascending order.")

    allowed_categories = {
        "volume",
        "weight",
        "quantity",
        "length",
        "area",
    }

    for row in uoms:
        if row["uom_category"] not in allowed_categories:
            raise ValueError(
                f"Invalid UOM category: {row['uom_category']}"
            )

        if not isinstance(row["is_active"], bool):
            raise ValueError(
                f"is_active must be boolean for UOM: {row['uom_code']}"
            )

        if row["uom_id"] <= 0:
            raise ValueError(
                f"uom_id must be positive: {row['uom_id']}"
            )


# ============================================================
# Payment term validation
# ============================================================

def validate_payment_terms(payment_terms: list[dict]) -> None:
    """Validate payment term master data."""

    if not payment_terms:
        raise ValueError("Payment term data is empty.")

    required_fields = {
        "payment_term_id",
        "payment_term_code",
        "payment_term_name",
        "payment_term_days",
        "payment_term_description",
        "payment_term_status",
    }

    for row in payment_terms:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing payment term fields: {sorted(missing_fields)}"
            )

    payment_term_ids = [
        row["payment_term_id"]
        for row in payment_terms
    ]

    payment_term_codes = [
        row["payment_term_code"]
        for row in payment_terms
    ]

    payment_term_names = [
        row["payment_term_name"]
        for row in payment_terms
    ]

    if len(payment_term_ids) != len(set(payment_term_ids)):
        raise ValueError("Duplicate payment_term_id found.")

    if len(payment_term_codes) != len(set(payment_term_codes)):
        raise ValueError("Duplicate payment_term_code found.")

    if len(payment_term_names) != len(set(payment_term_names)):
        raise ValueError("Duplicate payment_term_name found.")

    if payment_term_ids != sorted(payment_term_ids):
        raise ValueError(
            "Payment term IDs are not in ascending order."
        )

    allowed_statuses = {
        "active",
        "inactive",
    }

    for row in payment_terms:
        if row["payment_term_id"] <= 0:
            raise ValueError(
                f"payment_term_id must be positive: "
                f"{row['payment_term_id']}"
            )

        if row["payment_term_days"] < 0:
            raise ValueError(
                f"payment_term_days cannot be negative: "
                f"{row['payment_term_code']}"
            )

        if row["payment_term_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid payment term status: "
                f"{row['payment_term_status']}"
            )

        if not row["payment_term_code"].strip():
            raise ValueError(
                f"Payment term code cannot be empty: "
                f"{row['payment_term_id']}"
            )

        if not row["payment_term_name"].strip():
            raise ValueError(
                f"Payment term name cannot be empty: "
                f"{row['payment_term_id']}"
            )


# ============================================================
# Brand validation
# ============================================================

def validate_brands(brands: list[dict]) -> None:
    """Validate brand master data."""

    if not brands:
        raise ValueError("Brand data is empty.")

    required_fields = {
        "brand_id",
        "brand_code",
        "brand_name",
        "brand_owner_company",
        "brand_status",
    }

    for row in brands:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing brand fields: {sorted(missing_fields)}"
            )

    brand_ids = [row["brand_id"] for row in brands]
    brand_codes = [row["brand_code"] for row in brands]
    brand_names = [row["brand_name"] for row in brands]

    if len(brand_ids) != len(set(brand_ids)):
        raise ValueError("Duplicate brand_id found.")

    if len(brand_codes) != len(set(brand_codes)):
        raise ValueError("Duplicate brand_code found.")

    if len(brand_names) != len(set(brand_names)):
        raise ValueError("Duplicate brand_name found.")

    if brand_ids != sorted(brand_ids):
        raise ValueError("Brand IDs are not in ascending order.")

    allowed_statuses = {
        "active",
        "inactive",
    }

    for row in brands:
        if row["brand_id"] <= 0:
            raise ValueError(
                f"brand_id must be positive: {row['brand_id']}"
            )

        if not row["brand_code"].strip():
            raise ValueError(
                f"Brand code cannot be empty: {row['brand_id']}"
            )

        if not row["brand_name"].strip():
            raise ValueError(
                f"Brand name cannot be empty: {row['brand_id']}"
            )

        if row["brand_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid brand status: {row['brand_status']}"
            )

        if row["brand_owner_company"] != COMPANY_NAME:
            raise ValueError(
                f"Unexpected brand owner: {row['brand_name']}"
            )


# ============================================================
# Category validation
# ============================================================

def validate_categories(categories: list[dict]) -> None:
    """Validate category master data."""

    if not categories:
        raise ValueError("Category data is empty.")

    required_fields = {
        "category_id",
        "category_code",
        "category_name",
        "category_status",
    }

    for row in categories:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing category fields: {sorted(missing_fields)}"
            )

    category_ids = [row["category_id"] for row in categories]
    category_codes = [row["category_code"] for row in categories]
    category_names = [row["category_name"] for row in categories]

    if len(category_ids) != len(set(category_ids)):
        raise ValueError("Duplicate category_id found.")

    if len(category_codes) != len(set(category_codes)):
        raise ValueError("Duplicate category_code found.")

    if len(category_names) != len(set(category_names)):
        raise ValueError("Duplicate category_name found.")

    if category_ids != sorted(category_ids):
        raise ValueError(
            "Category IDs are not in ascending order."
        )

    allowed_statuses = {
        "active",
        "inactive",
    }

    for row in categories:
        if row["category_id"] <= 0:
            raise ValueError(
                f"category_id must be positive: "
                f"{row['category_id']}"
            )

        if not row["category_code"].strip():
            raise ValueError(
                f"Category code cannot be empty: "
                f"{row['category_id']}"
            )

        if not row["category_name"].strip():
            raise ValueError(
                f"Category name cannot be empty: "
                f"{row['category_id']}"
            )

        if row["category_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid category status: "
                f"{row['category_status']}"
            )


# ============================================================
# Sub-category validation
# ============================================================

def validate_sub_categories(
    sub_categories: list[dict],
    categories: list[dict],
) -> None:
    """Validate sub-category data and category relationships."""

    if not sub_categories:
        raise ValueError("Sub-category data is empty.")

    required_fields = {
        "sub_category_id",
        "category_id",
        "sub_category_code",
        "sub_category_name",
        "description",
        "sub_category_status",
    }

    for row in sub_categories:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing sub-category fields: "
                f"{sorted(missing_fields)}"
            )

    category_ids = {
        row["category_id"]
        for row in categories
    }

    sub_category_ids = [
        row["sub_category_id"]
        for row in sub_categories
    ]

    sub_category_codes = [
        row["sub_category_code"]
        for row in sub_categories
    ]

    if len(sub_category_ids) != len(set(sub_category_ids)):
        raise ValueError(
            "Duplicate sub_category_id found."
        )

    if len(sub_category_codes) != len(set(sub_category_codes)):
        raise ValueError(
            "Duplicate sub_category_code found."
        )

    if sub_category_ids != sorted(sub_category_ids):
        raise ValueError(
            "Sub-category IDs are not in ascending order."
        )

    allowed_statuses = {
        "active",
        "inactive",
    }

    category_name_pairs = set()

    for row in sub_categories:
        if row["sub_category_id"] <= 0:
            raise ValueError(
                f"sub_category_id must be positive: "
                f"{row['sub_category_id']}"
            )

        if row["category_id"] not in category_ids:
            raise ValueError(
                f"Invalid category_id {row['category_id']} "
                f"for sub-category {row['sub_category_code']}"
            )

        if not row["sub_category_code"].strip():
            raise ValueError(
                f"Sub-category code cannot be empty: "
                f"{row['sub_category_id']}"
            )

        if not row["sub_category_name"].strip():
            raise ValueError(
                f"Sub-category name cannot be empty: "
                f"{row['sub_category_id']}"
            )

        if row["sub_category_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid sub-category status: "
                f"{row['sub_category_status']}"
            )

        category_name_key = (
            row["category_id"],
            row["sub_category_name"],
        )

        if category_name_key in category_name_pairs:
            raise ValueError(
                "Duplicate sub-category name within category: "
                f"{category_name_key}"
            )

        category_name_pairs.add(category_name_key)


# ============================================================
# Warehouse validation
# ============================================================

def validate_warehouses(
    warehouses: list[dict],
) -> None:
    """Validate warehouse master data."""

    if not warehouses:
        raise ValueError("Warehouse data is empty.")

    required_fields = {
        "warehouse_id",
        "warehouse_code",
        "warehouse_name",
        "warehouse_type",
        "address_line1",
        "city",
        "state",
        "postal_code",
        "country",
        "total_capacity_ltr",
        "usable_capacity_ltr",
        "storage_mode",
        "warehouse_status",
    }

    for row in warehouses:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing warehouse fields: "
                f"{sorted(missing_fields)}"
            )

    warehouse_ids = [
        row["warehouse_id"]
        for row in warehouses
    ]

    warehouse_codes = [
        row["warehouse_code"]
        for row in warehouses
    ]

    warehouse_names = [
        row["warehouse_name"]
        for row in warehouses
    ]

    if len(warehouse_ids) != len(set(warehouse_ids)):
        raise ValueError(
            "Duplicate warehouse_id found."
        )

    if len(warehouse_codes) != len(set(warehouse_codes)):
        raise ValueError(
            "Duplicate warehouse_code found."
        )

    if len(warehouse_names) != len(set(warehouse_names)):
        raise ValueError(
            "Duplicate warehouse_name found."
        )

    if warehouse_ids != sorted(warehouse_ids):
        raise ValueError(
            "Warehouse IDs are not in ascending order."
        )

    allowed_types = {
        "central",
        "regional",
        "depot",
        "cross_dock",
    }

    allowed_storage_modes = {
        "ambient",
        "covered",
        "mixed",
        "controlled",
    }

    allowed_statuses = {
        "active",
        "inactive",
    }

    for row in warehouses:
        if row["warehouse_id"] <= 0:
            raise ValueError(
                f"warehouse_id must be positive: "
                f"{row['warehouse_id']}"
            )

        if row["warehouse_type"] not in allowed_types:
            raise ValueError(
                f"Invalid warehouse type: "
                f"{row['warehouse_type']}"
            )

        if row["storage_mode"] not in allowed_storage_modes:
            raise ValueError(
                f"Invalid storage mode: "
                f"{row['storage_mode']}"
            )

        if row["warehouse_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid warehouse status: "
                f"{row['warehouse_status']}"
            )

        if row["total_capacity_ltr"] < 0:
            raise ValueError(
                f"Negative total capacity: "
                f"{row['warehouse_code']}"
            )

        if row["usable_capacity_ltr"] < 0:
            raise ValueError(
                f"Negative usable capacity: "
                f"{row['warehouse_code']}"
            )

        if (
            row["usable_capacity_ltr"]
            > row["total_capacity_ltr"]
        ):
            raise ValueError(
                f"Usable capacity exceeds total capacity: "
                f"{row['warehouse_code']}"
            )


# ============================================================
# Location generation
# ============================================================

def generate_locations(
    warehouses: list[dict],
) -> list[dict]:
    """Generate deterministic warehouse locations."""

    locations = []

    location_id = 1

    for warehouse in warehouses:
        warehouse_id = warehouse["warehouse_id"]
        usable_capacity = warehouse["usable_capacity_ltr"]

        if warehouse_id not in LOCATION_TYPE_COUNTS:
            raise ValueError(
                f"Missing location distribution for warehouse "
                f"{warehouse_id}"
            )

        location_type_counts = LOCATION_TYPE_COUNTS[
            warehouse_id
        ]

        expected_count = sum(
            location_type_counts.values()
        )

        allocated_capacity = (
            usable_capacity
            * LOCATION_CAPACITY_UTILIZATION
        )

        for location_type in LOCATION_TYPE_ORDER:
            count = location_type_counts.get(
                location_type,
                0,
            )

            if count == 0:
                continue

            share = LOCATION_CAPACITY_SHARES[
                location_type
            ]

            type_capacity = (
                allocated_capacity
                * share
            )

            capacity_per_location = round(
                type_capacity / count,
                2,
            )

            if capacity_per_location <= 0:
                raise ValueError(
                    f"Invalid location capacity for "
                    f"{warehouse['warehouse_code']} "
                    f"{location_type}"
                )

            for sequence in range(1, count + 1):
                if location_type == "receiving":
                    location_code = (
                        f"REC-{sequence:02d}"
                    )
                    location_name = (
                        f"Receiving Bay {sequence:02d}"
                    )
                    zone_code = "REC"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                elif location_type == "storage":
                    zone_number = (
                        ((sequence - 1) // 20) + 1
                    )
                    aisle_number = (
                        ((sequence - 1) % 20) // 5
                    ) + 1
                    rack_number = (
                        ((sequence - 1) % 5) + 1
                    )
                    bin_number = 1

                    zone_code = f"Z{zone_number:02d}"
                    aisle_no = f"A{aisle_number:02d}"
                    rack_no = f"R{rack_number:02d}"
                    bin_no = f"B{bin_number:02d}"

                    location_code = (
                        f"{zone_code}-"
                        f"{aisle_no}-"
                        f"{rack_no}-"
                        f"{bin_no}"
                    )

                    location_name = (
                        f"Storage {zone_code} "
                        f"{aisle_no} "
                        f"{rack_no} "
                        f"{bin_no}"
                    )

                elif location_type == "picking":
                    zone_number = (
                        ((sequence - 1) // 10) + 1
                    )
                    aisle_number = (
                        ((sequence - 1) % 10) // 5
                    ) + 1
                    rack_number = (
                        ((sequence - 1) % 5) + 1
                    )
                    bin_number = 1

                    zone_code = f"P{zone_number:02d}"
                    aisle_no = f"A{aisle_number:02d}"
                    rack_no = f"R{rack_number:02d}"
                    bin_no = f"B{bin_number:02d}"

                    location_code = (
                        f"{zone_code}-"
                        f"{aisle_no}-"
                        f"{rack_no}-"
                        f"{bin_no}"
                    )

                    location_name = (
                        f"Picking {zone_code} "
                        f"{aisle_no} "
                        f"{rack_no} "
                        f"{bin_no}"
                    )

                elif location_type == "dispatch":
                    location_code = (
                        f"DSP-{sequence:02d}"
                    )
                    location_name = (
                        f"Dispatch Staging {sequence:02d}"
                    )
                    zone_code = "DSP"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                elif location_type == "quarantine":
                    location_code = (
                        f"QTN-{sequence:02d}"
                    )
                    location_name = (
                        f"Quarantine Area {sequence:02d}"
                    )
                    zone_code = "QTN"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                elif location_type == "returns":
                    location_code = (
                        f"RET-{sequence:02d}"
                    )
                    location_name = (
                        f"Returns Area {sequence:02d}"
                    )
                    zone_code = "RET"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                elif location_type == "damage":
                    location_code = (
                        f"DMG-{sequence:02d}"
                    )
                    location_name = (
                        f"Damage Hold Area {sequence:02d}"
                    )
                    zone_code = "DMG"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                elif location_type == "staging":
                    location_code = (
                        f"STG-{sequence:02d}"
                    )
                    location_name = (
                        f"Staging Area {sequence:02d}"
                    )
                    zone_code = "STG"
                    aisle_no = ""
                    rack_no = ""
                    bin_no = ""

                else:
                    raise ValueError(
                        f"Unsupported location type: "
                        f"{location_type}"
                    )

                location_storage_mode = (
                    warehouse["storage_mode"]
                )

                if location_type in {
                    "receiving",
                    "dispatch",
                    "staging",
                    "quarantine",
                    "returns",
                    "damage",
                }:
                    location_storage_mode = "covered"

                locations.append(
                    {
                        "location_id": location_id,
                        "warehouse_id": warehouse_id,
                        "location_code": location_code,
                        "location_name": location_name,
                        "zone_code": zone_code,
                        "aisle_no": aisle_no,
                        "rack_no": rack_no,
                        "bin_no": bin_no,
                        "location_type": location_type,
                        "storage_mode": location_storage_mode,
                        "max_capacity_ltr": capacity_per_location,
                        "location_status": "active",
                    }
                )

                location_id += 1

        actual_count = sum(
            1
            for location in locations
            if location["warehouse_id"] == warehouse_id
        )

        if actual_count != expected_count:
            raise ValueError(
                f"Location count mismatch for "
                f"{warehouse['warehouse_code']}: "
                f"expected {expected_count}, "
                f"generated {actual_count}"
            )

    return locations


# ============================================================
# Location validation
# ============================================================

def validate_locations(
    locations: list[dict],
    warehouses: list[dict],
) -> None:
    """Validate generated warehouse locations."""

    if not locations:
        raise ValueError("Location data is empty.")

    warehouse_ids = {
        row["warehouse_id"]
        for row in warehouses
    }

    warehouse_capacity_map = {
        row["warehouse_id"]: row["usable_capacity_ltr"]
        for row in warehouses
    }

    required_fields = {
        "location_id",
        "warehouse_id",
        "location_code",
        "location_name",
        "zone_code",
        "aisle_no",
        "rack_no",
        "bin_no",
        "location_type",
        "storage_mode",
        "max_capacity_ltr",
        "location_status",
    }

    for row in locations:
        missing_fields = required_fields - row.keys()

        if missing_fields:
            raise ValueError(
                f"Missing location fields: "
                f"{sorted(missing_fields)}"
            )

    location_ids = [
        row["location_id"]
        for row in locations
    ]

    if len(location_ids) != len(set(location_ids)):
        raise ValueError(
            "Duplicate location_id found."
        )

    allowed_types = {
        "receiving",
        "storage",
        "picking",
        "dispatch",
        "quarantine",
        "returns",
        "damage",
        "staging",
    }

    allowed_storage_modes = {
        "ambient",
        "covered",
        "mixed",
        "controlled",
    }

    allowed_statuses = {
        "active",
        "inactive",
    }

    warehouse_location_pairs = set()

    capacity_by_warehouse = {}

    for row in locations:
        warehouse_id = row["warehouse_id"]

        if warehouse_id not in warehouse_ids:
            raise ValueError(
                f"Invalid warehouse_id for location: "
                f"{row['location_code']}"
            )

        if row["location_type"] not in allowed_types:
            raise ValueError(
                f"Invalid location type: "
                f"{row['location_type']}"
            )

        if row["storage_mode"] not in allowed_storage_modes:
            raise ValueError(
                f"Invalid location storage mode: "
                f"{row['storage_mode']}"
            )

        if row["location_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid location status: "
                f"{row['location_status']}"
            )

        if row["max_capacity_ltr"] <= 0:
            raise ValueError(
                f"Location capacity must be positive: "
                f"{row['location_code']}"
            )

        pair = (
            warehouse_id,
            row["location_code"],
        )

        if pair in warehouse_location_pairs:
            raise ValueError(
                "Duplicate location code within warehouse: "
                f"{pair}"
            )

        warehouse_location_pairs.add(pair)

        capacity_by_warehouse[warehouse_id] = (
            capacity_by_warehouse.get(
                warehouse_id,
                0,
            )
            + row["max_capacity_ltr"]
        )

    expected_total = sum(
        sum(counts.values())
        for counts in LOCATION_TYPE_COUNTS.values()
    )

    if len(locations) != expected_total:
        raise ValueError(
            f"Total location count mismatch: "
            f"expected {expected_total}, "
            f"generated {len(locations)}"
        )

    for warehouse_id, expected_counts in (
        LOCATION_TYPE_COUNTS.items()
    ):
        expected_count = sum(
            expected_counts.values()
        )

        actual_count = sum(
            1
            for location in locations
            if location["warehouse_id"] == warehouse_id
        )

        if actual_count != expected_count:
            warehouse = get_warehouse_by_id(
                warehouse_id
            )

            raise ValueError(
                f"Location count mismatch for "
                f"{warehouse['warehouse_code']}: "
                f"expected {expected_count}, "
                f"generated {actual_count}"
            )

        location_capacity = (
            capacity_by_warehouse.get(
                warehouse_id,
                0,
            )
        )

        usable_capacity = warehouse_capacity_map[
            warehouse_id
        ]

        if location_capacity > usable_capacity:
            warehouse = get_warehouse_by_id(
                warehouse_id
            )

            raise ValueError(
                f"Location capacity exceeds usable "
                f"warehouse capacity for "
                f"{warehouse['warehouse_code']}: "
                f"locations={location_capacity:.2f}, "
                f"usable={usable_capacity:.2f}"
            )


# ============================================================
# Cross-master validation
# ============================================================

def validate_master_relationships(
    categories: list[dict],
    sub_categories: list[dict],
    warehouses: list[dict],
    locations: list[dict],
) -> None:
    """Validate relationships between generated masters."""

    category_ids = {
        row["category_id"]
        for row in categories
    }

    referenced_category_ids = {
        row["category_id"]
        for row in sub_categories
    }

    missing_categories = (
        referenced_category_ids - category_ids
    )

    if missing_categories:
        raise ValueError(
            "Sub-categories reference missing categories: "
            f"{sorted(missing_categories)}"
        )

    warehouse_ids = {
        row["warehouse_id"]
        for row in warehouses
    }

    referenced_warehouse_ids = {
        row["warehouse_id"]
        for row in locations
    }

    missing_warehouses = (
        referenced_warehouse_ids - warehouse_ids
    )

    if missing_warehouses:
        raise ValueError(
            "Locations reference missing warehouses: "
            f"{sorted(missing_warehouses)}"
        )


# ============================================================
# Generic CSV writer
# ============================================================

def write_csv(
    rows: list[dict],
    filename: str,
    fieldnames: list[str],
) -> Path:
    """Write master data rows to a CSV file."""

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = OUTPUT_DIR / filename

    with output_file.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        for row in rows:
            writer.writerow(
                add_audit_columns(row)
            )

    return output_file


# ============================================================
# CSV writers
# ============================================================

def write_uoms_csv(
    uoms: list[dict],
) -> Path:
    """Write UOM master data."""

    return write_csv(
        rows=uoms,
        filename="master_uoms.csv",
        fieldnames=[
            "uom_id",
            "uom_code",
            "uom_name",
            "uom_category",
            "is_active",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_payment_terms_csv(
    payment_terms: list[dict],
) -> Path:
    """Write payment term master data."""

    return write_csv(
        rows=payment_terms,
        filename="master_payment_terms.csv",
        fieldnames=[
            "payment_term_id",
            "payment_term_code",
            "payment_term_name",
            "payment_term_days",
            "payment_term_description",
            "payment_term_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_brands_csv(
    brands: list[dict],
) -> Path:
    """Write brand master data."""

    return write_csv(
        rows=brands,
        filename="master_brands.csv",
        fieldnames=[
            "brand_id",
            "brand_code",
            "brand_name",
            "brand_owner_company",
            "brand_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_categories_csv(
    categories: list[dict],
) -> Path:
    """Write category master data."""

    return write_csv(
        rows=categories,
        filename="master_categories.csv",
        fieldnames=[
            "category_id",
            "category_code",
            "category_name",
            "category_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_sub_categories_csv(
    sub_categories: list[dict],
) -> Path:
    """Write sub-category master data."""

    return write_csv(
        rows=sub_categories,
        filename="master_sub_categories.csv",
        fieldnames=[
            "sub_category_id",
            "category_id",
            "sub_category_code",
            "sub_category_name",
            "description",
            "sub_category_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_warehouses_csv(
    warehouses: list[dict],
) -> Path:
    """Write warehouse master data."""

    return write_csv(
        rows=warehouses,
        filename="master_warehouses.csv",
        fieldnames=[
            "warehouse_id",
            "warehouse_code",
            "warehouse_name",
            "warehouse_type",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal_code",
            "country",
            "total_capacity_ltr",
            "usable_capacity_ltr",
            "storage_mode",
            "warehouse_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_locations_csv(
    locations: list[dict],
) -> Path:
    """Write warehouse location master data."""

    return write_csv(
        rows=locations,
        filename="master_locations.csv",
        fieldnames=[
            "location_id",
            "warehouse_id",
            "location_code",
            "location_name",
            "zone_code",
            "aisle_no",
            "rack_no",
            "bin_no",
            "location_type",
            "storage_mode",
            "max_capacity_ltr",
            "location_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


# ============================================================
# Main
# ============================================================

def main() -> None:
    """Generate and validate current master datasets."""

    try:
        uoms = UOM_DEFINITIONS
        payment_terms = PAYMENT_TERM_DEFINITIONS
        brands = BRAND_DEFINITIONS
        categories = CATEGORY_DEFINITIONS
        sub_categories = SUB_CATEGORY_DEFINITIONS
        warehouses = WAREHOUSE_DEFINITIONS

        locations = generate_locations(
            warehouses
        )

        # ----------------------------------------------------
        # Validation
        # ----------------------------------------------------

        validate_uoms(uoms)
        print("UOM validation: PASSED")

        validate_payment_terms(payment_terms)
        print("Payment term validation: PASSED")

        validate_brands(brands)
        print("Brand validation: PASSED")

        validate_categories(categories)
        print("Category validation: PASSED")

        validate_sub_categories(
            sub_categories,
            categories,
        )
        print("Sub-category validation: PASSED")

        validate_warehouses(
            warehouses
        )
        print("Warehouse validation: PASSED")

        validate_locations(
            locations,
            warehouses,
        )
        print("Location validation: PASSED")

        validate_master_relationships(
            categories,
            sub_categories,
            warehouses,
            locations,
        )
        print("Master relationship validation: PASSED")

        # ----------------------------------------------------
        # CSV generation
        # ----------------------------------------------------

        uom_file = write_uoms_csv(uoms)

        payment_term_file = (
            write_payment_terms_csv(payment_terms)
        )

        brand_file = write_brands_csv(brands)

        category_file = write_categories_csv(
            categories
        )

        sub_category_file = (
            write_sub_categories_csv(
                sub_categories
            )
        )

        warehouse_file = write_warehouses_csv(
            warehouses
        )

        location_file = write_locations_csv(
            locations
        )

        # ----------------------------------------------------
        # Output summary
        # ----------------------------------------------------

        print(f"Created: {uom_file}")
        print(f"Rows: {len(uoms)}")

        print(f"Created: {payment_term_file}")
        print(f"Rows: {len(payment_terms)}")

        print(f"Created: {brand_file}")
        print(f"Rows: {len(brands)}")

        print(f"Created: {category_file}")
        print(f"Rows: {len(categories)}")

        print(f"Created: {sub_category_file}")
        print(f"Rows: {len(sub_categories)}")

        print(f"Created: {warehouse_file}")
        print(f"Rows: {len(warehouses)}")

        print(f"Created: {location_file}")
        print(f"Rows: {len(locations)}")

    except (OSError, ValueError) as error:
        print(f"Generation failed: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
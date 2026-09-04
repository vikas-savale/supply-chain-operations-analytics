from datetime import date, datetime, timedelta
from pathlib import Path
import csv
import re


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
# Supplier master definitions
# ============================================================

SUPPLIER_DEFINITIONS = [
    {
        "supplier_id": 1,
        "supplier_code": "SUP001",
        "supplier_name": "Novera Lubricant Manufacturing",
        "supplier_type": "manufacturer",
        "contact_person": "Rohan Mehta",
        "phone": "020-4108-2637",
        "email": "commercial@noveralu.example",
        "gstin": "27QRTPL4821M1Z8",
        "state_code": "27",
        "address_line1": "Plot 12, Industrial Estate",
        "address_line2": "Bhosari MIDC",
        "city": "Pune",
        "state": "Maharashtra",
        "postal_code": "411026",
        "country": "India",
        "lead_time_days": 7,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 2,
        "supplier_code": "SUP002",
        "supplier_name": "Brightshore Industrial Oils",
        "supplier_type": "manufacturer",
        "contact_person": "Anil Sharma",
        "phone": "079-4682-3154",
        "email": "commercial@brightshoreoils.example",
        "gstin": "24NVMRK7316D1Z4",
        "state_code": "24",
        "address_line1": "Survey 44, GIDC Industrial Area",
        "address_line2": "Vatva Phase II",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "postal_code": "382445",
        "country": "India",
        "lead_time_days": 10,
        "payment_term_id": 4,
        "supplier_status": "active",
    },
    {
        "supplier_id": 3,
        "supplier_code": "SUP003",
        "supplier_name": "Crestline Petrochem Supplies",
        "supplier_type": "manufacturer",
        "contact_person": "Neeraj Kapoor",
        "phone": "080-4179-2638",
        "email": "sales@crestlinepetrochem.example",
        "gstin": "29LHTPS5842C1Z7",
        "state_code": "29",
        "address_line1": "Block 7, Industrial Layout",
        "address_line2": "Peenya",
        "city": "Bengaluru",
        "state": "Karnataka",
        "postal_code": "560058",
        "country": "India",
        "lead_time_days": 9,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 4,
        "supplier_code": "SUP004",
        "supplier_name": "Delta Automotive Fluids",
        "supplier_type": "manufacturer",
        "contact_person": "Sanjay Patel",
        "phone": "020-4631-7284",
        "email": "sales@deltafluids.example",
        "gstin": "27XQFRE2168K1Z3",
        "state_code": "27",
        "address_line1": "Unit 18, Industrial Park",
        "address_line2": "Chakan MIDC",
        "city": "Pune",
        "state": "Maharashtra",
        "postal_code": "410501",
        "country": "India",
        "lead_time_days": 6,
        "payment_term_id": 5,
        "supplier_status": "active",
    },
    {
        "supplier_id": 5,
        "supplier_code": "SUP005",
        "supplier_name": "Eastern Gear Lubricants",
        "supplier_type": "manufacturer",
        "contact_person": "Arindam Bose",
        "phone": "033-4018-5263",
        "email": "sales@easterngl.example",
        "gstin": "19BKMTA9054R1Z6",
        "state_code": "19",
        "address_line1": "Industrial Plot 31",
        "address_line2": "Dankuni Industrial Zone",
        "city": "Kolkata",
        "state": "West Bengal",
        "postal_code": "712311",
        "country": "India",
        "lead_time_days": 12,
        "payment_term_id": 6,
        "supplier_status": "active",
    },
    {
        "supplier_id": 6,
        "supplier_code": "SUP006",
        "supplier_name": "Frontier Hydraulic Oils",
        "supplier_type": "manufacturer",
        "contact_person": "Vivek Joshi",
        "phone": "0731-4917-2635",
        "email": "commercial@frontierhydraulic.example",
        "gstin": "23CPNVD3471H1Z9",
        "state_code": "23",
        "address_line1": "Plot 8, Sector C",
        "address_line2": "Pithampur Industrial Area",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "postal_code": "454775",
        "country": "India",
        "lead_time_days": 8,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 7,
        "supplier_code": "SUP007",
        "supplier_name": "Greenfield Grease Works",
        "supplier_type": "manufacturer",
        "contact_person": "Manish Verma",
        "phone": "0120-4186-2735",
        "email": "sales@greenfieldgrease.example",
        "gstin": "09RSLKG6285P1Z2",
        "state_code": "09",
        "address_line1": "Plot 22, Industrial Estate",
        "address_line2": "Site IV",
        "city": "Ghaziabad",
        "state": "Uttar Pradesh",
        "postal_code": "201010",
        "country": "India",
        "lead_time_days": 11,
        "payment_term_id": 5,
        "supplier_status": "active",
    },
    {
        "supplier_id": 8,
        "supplier_code": "SUP008",
        "supplier_name": "Highland Industrial Fluids",
        "supplier_type": "manufacturer",
        "contact_person": "Kiran Desai",
        "phone": "022-4928-3164",
        "email": "commercial@highlandfluids.example",
        "gstin": "27TDMQJ4137A1Z5",
        "state_code": "27",
        "address_line1": "Warehouse Road Industrial Plot",
        "address_line2": "Taloja MIDC",
        "city": "Navi Mumbai",
        "state": "Maharashtra",
        "postal_code": "410208",
        "country": "India",
        "lead_time_days": 10,
        "payment_term_id": 4,
        "supplier_status": "active",
    },
    {
        "supplier_id": 9,
        "supplier_code": "SUP009",
        "supplier_name": "Metro Lubricants Distribution",
        "supplier_type": "authorized_distributor",
        "contact_person": "Rahul Nair",
        "phone": "080-4612-7358",
        "email": "sales@metrolubricants.example",
        "gstin": "29VKRNB7624S1Z8",
        "state_code": "29",
        "address_line1": "23 Logistics Park Road",
        "address_line2": "Hosur Road",
        "city": "Bengaluru",
        "state": "Karnataka",
        "postal_code": "560068",
        "country": "India",
        "lead_time_days": 5,
        "payment_term_id": 2,
        "supplier_status": "active",
    },
    {
        "supplier_id": 10,
        "supplier_code": "SUP010",
        "supplier_name": "Pioneer Mobility Components",
        "supplier_type": "authorized_distributor",
        "contact_person": "Akash Malhotra",
        "phone": "011-4286-3157",
        "email": "commercial@pioneermobility.example",
        "gstin": "07HPCWL5389N1Z4",
        "state_code": "07",
        "address_line1": "Shed 14, Industrial Park",
        "address_line2": "Patparganj",
        "city": "New Delhi",
        "state": "Delhi",
        "postal_code": "110092",
        "country": "India",
        "lead_time_days": 4,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 11,
        "supplier_code": "SUP011",
        "supplier_name": "Western Auto Fluids Distribution",
        "supplier_type": "authorized_distributor",
        "contact_person": "Harish Shah",
        "phone": "02522-463817",
        "email": "sales@westernfluids.example",
        "gstin": "27MZTRF1846Q1Z7",
        "state_code": "27",
        "address_line1": "Unit 6, Industrial Estate",
        "address_line2": "Bhiwandi Logistics Zone",
        "city": "Thane",
        "state": "Maharashtra",
        "postal_code": "421302",
        "country": "India",
        "lead_time_days": 6,
        "payment_term_id": 4,
        "supplier_status": "active",
    },
    {
        "supplier_id": 12,
        "supplier_code": "SUP012",
        "supplier_name": "Southline Lubricant Supply",
        "supplier_type": "authorized_distributor",
        "contact_person": "Joseph Mathew",
        "phone": "0484-4162-7351",
        "email": "commercial@southlinelubes.example",
        "gstin": "32DPLKS9072E1Z3",
        "state_code": "32",
        "address_line1": "Plot 9, Logistics Industrial Area",
        "address_line2": "Kalamassery",
        "city": "Kochi",
        "state": "Kerala",
        "postal_code": "683104",
        "country": "India",
        "lead_time_days": 7,
        "payment_term_id": 5,
        "supplier_status": "active",
    },
    {
        "supplier_id": 13,
        "supplier_code": "SUP013",
        "supplier_name": "Central Fleet Lubricants",
        "supplier_type": "authorized_distributor",
        "contact_person": "Pankaj Soni",
        "phone": "0731-4628-3159",
        "email": "sales@centralfleetlubes.example",
        "gstin": "23GWNHC6158V1Z6",
        "state_code": "23",
        "address_line1": "Depot 4, Industrial Corridor",
        "address_line2": "Rau",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "postal_code": "453331",
        "country": "India",
        "lead_time_days": 5,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 14,
        "supplier_code": "SUP014",
        "supplier_name": "Deccan Equipment Fluids",
        "supplier_type": "authorized_distributor",
        "contact_person": "Swapnil Kulkarni",
        "phone": "0253-4187-2634",
        "email": "commercial@deccanequipment.example",
        "gstin": "27RKDPS3429L1Z8",
        "state_code": "27",
        "address_line1": "Shop 12, Industrial Service Road",
        "address_line2": "Satpur MIDC",
        "city": "Nashik",
        "state": "Maharashtra",
        "postal_code": "422007",
        "country": "India",
        "lead_time_days": 4,
        "payment_term_id": 2,
        "supplier_status": "active",
    },
    {
        "supplier_id": 15,
        "supplier_code": "SUP015",
        "supplier_name": "Northwest Regional Oils",
        "supplier_type": "regional_distributor",
        "contact_person": "Gaurav Bansal",
        "phone": "0141-4672-3158",
        "email": "sales@northwestoils.example",
        "gstin": "08FQMBT7815C1Z4",
        "state_code": "08",
        "address_line1": "Plot 19, Transport Nagar",
        "address_line2": "Sitapura",
        "city": "Jaipur",
        "state": "Rajasthan",
        "postal_code": "302022",
        "country": "India",
        "lead_time_days": 6,
        "payment_term_id": 4,
        "supplier_status": "active",
    },
    {
        "supplier_id": 16,
        "supplier_code": "SUP016",
        "supplier_name": "Vidarbha Industrial Distribution",
        "supplier_type": "regional_distributor",
        "contact_person": "Suresh Patil",
        "phone": "0712-4816-2734",
        "email": "commercial@vidarbhadist.example",
        "gstin": "27JVLNR5036T1Z9",
        "state_code": "27",
        "address_line1": "Plot 5, Logistics Hub",
        "address_line2": "Hingna Road",
        "city": "Nagpur",
        "state": "Maharashtra",
        "postal_code": "440016",
        "country": "India",
        "lead_time_days": 5,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 17,
        "supplier_code": "SUP017",
        "supplier_name": "Varnex Industrial Supply",
        "supplier_type": "regional_distributor",
        "contact_person": "Ramesh Rao",
        "phone": "040-4637-2815",
        "email": "sales@varnexindustrial.example",
        "gstin": "36KPBRS4261F1Z5",
        "state_code": "36",
        "address_line1": "Shed 8, Industrial Estate",
        "address_line2": "Jeedimetla",
        "city": "Hyderabad",
        "state": "Telangana",
        "postal_code": "500055",
        "country": "India",
        "lead_time_days": 7,
        "payment_term_id": 5,
        "supplier_status": "active",
    },
    {
        "supplier_id": 18,
        "supplier_code": "SUP018",
        "supplier_name": "Gujarat Regional Lubricants",
        "supplier_type": "regional_distributor",
        "contact_person": "Dhruv Trivedi",
        "phone": "079-4518-3264",
        "email": "commercial@gujaratregional.example",
        "gstin": "24WDTMG8593A1Z7",
        "state_code": "24",
        "address_line1": "Warehouse 3, GIDC Estate",
        "address_line2": "Sanand",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "postal_code": "382170",
        "country": "India",
        "lead_time_days": 5,
        "payment_term_id": 3,
        "supplier_status": "active",
    },
    {
        "supplier_id": 19,
        "supplier_code": "SUP019",
        "supplier_name": "Southwest Industrial Traders",
        "supplier_type": "regional_distributor",
        "contact_person": "Nitin Shetty",
        "phone": "080-4926-3175",
        "email": "sales@southwesttraders.example",
        "gstin": "29SCQHV2148M1Z3",
        "state_code": "29",
        "address_line1": "Plot 17, Industrial Area",
        "address_line2": "Bommasandra",
        "city": "Bengaluru",
        "state": "Karnataka",
        "postal_code": "560099",
        "country": "India",
        "lead_time_days": 6,
        "payment_term_id": 4,
        "supplier_status": "inactive",
    },
    {
        "supplier_id": 20,
        "supplier_code": "SUP020",
        "supplier_name": "Global Base Oil Imports",
        "supplier_type": "importer",
        "contact_person": "Amit Khanna",
        "phone": "022-4691-2853",
        "email": "commercial@globalbaseoil.example",
        "gstin": "27BFRNK6705P1Z8",
        "state_code": "27",
        "address_line1": "Tank Farm Road, Plot 2",
        "address_line2": "Nhava Sheva",
        "city": "Navi Mumbai",
        "state": "Maharashtra",
        "postal_code": "400707",
        "country": "India",
        "lead_time_days": 24,
        "payment_term_id": 7,
        "supplier_status": "active",
    },
    {
        "supplier_id": 21,
        "supplier_code": "SUP021",
        "supplier_name": "International Additives India",
        "supplier_type": "importer",
        "contact_person": "Rajiv Menon",
        "phone": "044-4186-3725",
        "email": "sales@intladditives.example",
        "gstin": "33NQXLD3917R1Z4",
        "state_code": "33",
        "address_line1": "Warehouse 11, Port Logistics Park",
        "address_line2": "Manali Industrial Area",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "postal_code": "600068",
        "country": "India",
        "lead_time_days": 28,
        "payment_term_id": 8,
        "supplier_status": "active",
    },
    {
        "supplier_id": 22,
        "supplier_code": "SUP022",
        "supplier_name": "Coastal Specialty Chemicals",
        "supplier_type": "importer",
        "contact_person": "Faizal Ahmed",
        "phone": "02641-467218",
        "email": "commercial@coastalspecialty.example",
        "gstin": "24HVMCP7452K1Z9",
        "state_code": "24",
        "address_line1": "Plot 4, Port Industrial Zone",
        "address_line2": "Dahej",
        "city": "Bharuch",
        "state": "Gujarat",
        "postal_code": "392130",
        "country": "India",
        "lead_time_days": 21,
        "payment_term_id": 7,
        "supplier_status": "active",
    },
    {
        "supplier_id": 23,
        "supplier_code": "SUP023",
        "supplier_name": "Bulk Industrial Supply Co",
        "supplier_type": "bulk_supplier",
        "contact_person": "Prakash Yadav",
        "phone": "0120-4527-3168",
        "email": "sales@bulkindustrial.example",
        "gstin": "09ZTRFS2864D1Z6",
        "state_code": "09",
        "address_line1": "Bulk Storage Yard 6",
        "address_line2": "Dadri Industrial Area",
        "city": "Greater Noida",
        "state": "Uttar Pradesh",
        "postal_code": "201306",
        "country": "India",
        "lead_time_days": 13,
        "payment_term_id": 6,
        "supplier_status": "active",
    },
    {
        "supplier_id": 24,
        "supplier_code": "SUP024",
        "supplier_name": "Industrial Fluids Bulk Services",
        "supplier_type": "bulk_supplier",
        "contact_person": "Deepak Agarwal",
        "phone": "011-4726-3185",
        "email": "commercial@industrialbulk.example",
        "gstin": "07PLQVB6183H1Z2",
        "state_code": "07",
        "address_line1": "Yard 3, Logistics Cluster",
        "address_line2": "Narela Industrial Area",
        "city": "New Delhi",
        "state": "Delhi",
        "postal_code": "110040",
        "country": "India",
        "lead_time_days": 14,
        "payment_term_id": 6,
        "supplier_status": "inactive",
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
# Product master generation
# ============================================================

PRODUCT_MASTER_COUNT = 1500
PRODUCT_RANDOM_SEED = 20260101

CATEGORY_PRODUCT_TARGETS = {
    1: 300,
    2: 200,
    3: 250,
    4: 220,
    5: 170,
    6: 130,
    7: 100,
    8: 130,
}

SUB_CATEGORY_PRODUCT_TARGETS = {
    # Automotive Engine Oils
    1: 70,
    2: 65,
    3: 60,
    4: 55,
    5: 50,
    # Automotive & Drivetrain Fluids
    6: 50,
    7: 40,
    8: 40,
    9: 35,
    10: 35,
    # Industrial Lubricants
    11: 45,
    12: 45,
    13: 40,
    14: 40,
    15: 40,
    16: 40,
    # Hydraulic & Equipment Fluids
    17: 50,
    18: 45,
    19: 45,
    20: 40,
    21: 40,
    # Greases
    22: 30,
    23: 30,
    24: 30,
    25: 30,
    26: 25,
    27: 25,
    # Coolants & Maintenance Fluids
    28: 30,
    29: 30,
    30: 25,
    31: 25,
    32: 20,
    # Specialty & Process Fluids
    33: 25,
    34: 20,
    35: 20,
    36: 20,
    37: 15,
    # Agricultural & Off-Highway Lubricants
    38: 30,
    39: 25,
    40: 25,
    41: 25,
    42: 25,
}

PRODUCT_BRAND_TARGET = 150

PRODUCT_STATUS_TARGETS = {
    "active": 1350,
    "inactive": 90,
    "discontinued": 60,
}

CATEGORY_SKU_PREFIXES = {
    1: "AEO",
    2: "ADF",
    3: "ILO",
    4: "HEF",
    5: "GRS",
    6: "CMF",
    7: "SPF",
    8: "AOL",
}


# Product families are synthetic and tied to the business meaning
# of the corresponding sub-category.
PRODUCT_FAMILY_STEMS = {
    1: ["RoadShield", "DriveCore", "EngineMax", "AutoPrime"],
    2: ["FleetGuard", "DieselCore", "HaulPro", "TorqueShield"],
    3: ["FleetLine", "CargoForce", "RoadHaul", "TransitCore"],
    4: ["MotoDrive", "RiderCore", "StreetForce", "MotoGuard"],
    5: ["GasCore", "CleanBurn", "StationPro", "GasGuard"],
    6: ["GearShield", "TorqueLine", "DriveGear", "AxleGuard"],
    7: ["TransFlow", "ShiftCore", "AutoShift", "TransGuard"],
    8: ["ManualCore", "ShiftForce", "GearFlow", "DriveShift"],
    9: ["DiffShield", "AxleCore", "DriveDiff", "FinalGuard"],
    10: ["FinalDrive", "AxleForce", "PowerAxle", "DriveLoad"],
    11: ["PlantGear", "IndustrialGear", "MachDrive", "GearWorks"],
    12: ["CompressorCore", "AirGuard", "CompressPro", "AirFlow"],
    13: ["TurbineCore", "RotorGuard", "PowerTurb", "TurbineLine"],
    14: ["CircuCore", "MachineFlow", "LoopGuard", "CircuLine"],
    15: ["SlideGuard", "WayCore", "MachineWay", "SlideForce"],
    16: ["ToolCore", "MachinePro", "ToolGuard", "MachLube"],
    17: ["HydraCore", "HydroForce", "PowerHyd", "HydraFlow"],
    18: ["HydraShift", "TransHyd", "PowerUTTO", "HydroDrive"],
    19: ["TractorHyd", "AgriHydro", "FieldFlow", "FarmHyd"],
    20: ["SiteHyd", "BuildForce", "EarthMove", "EquipHyd"],
    21: ["AgriFlow", "FarmPower", "FieldHyd", "CropForce"],
    22: ["MultiGrease", "GeneralLube", "AllRoundGrease", "MultiGuard"],
    23: ["EPShield", "LoadGuard", "ExtremeLube", "EPForce"],
    24: ["ThermoGrease", "HeatGuard", "TempForce", "HeatShield"],
    25: ["LithoGuard", "LithoForce", "BearingLube", "LithoPro"],
    26: ["CalciCore", "CalciGuard", "CalciForce", "CalciLube"],
    27: ["SpecialGrease", "LoadSpecial", "MotionGuard", "PurposeLube"],
    28: ["CoolGuard", "EngineCool", "ThermoCool", "CoolFlow", "RadiantCore"],
    29: [
        "LongLifeCool",
        "EnduraCool",
        "LifeGuardCool",
        "ExtendedCool",
        "LongRunCool",
    ],
    30: [
        "ReadyCool",
        "PremixGuard",
        "ReadyFlow",
        "InstantCool",
        "UseReadyCool",
    ],
    31: [
        "FreezeGuard",
        "AntifreezeCore",
        "ColdShield",
        "FrostProtect",
        "WinterGuard",
    ],
    32: [
        "RadiatorGuard",
        "RadFlow",
        "CoolingCore",
        "RadShield",
        "ThermoGuard",
    ],
    33: ["CutFlow", "MetalCut", "MachCut", "ToolCool", "CutGuard"],
    34: [
        "MetalCore",
        "ProcessFlow",
        "WorkshopCool",
        "MetalGuard",
        "ProcessLube",
    ],
    35: [
        "HeatFlow",
        "ThermoProcess",
        "HeatCore",
        "ThermalGuard",
        "ProcessTherm",
    ],
    36: [
        "RustGuard",
        "CorroShield",
        "MetalProtect",
        "RustBlock",
        "SurfaceGuard",
    ],
    37: [
        "InsulCore",
        "VoltGuard",
        "DielectricPro",
        "TransformShield",
        "InsulFlow",
    ],
    38: ["TractorDrive", "FieldEngine", "AgriEngine", "FarmPowerOil"],
    39: ["TractorGear", "FarmTransmission", "FieldGear", "AgriDrive"],
    40: ["TractorDiff", "FarmAxle", "AgriFinal", "FieldDiff"],
    41: ["MachineryCore", "AgriMach", "FieldMach", "FarmLube"],
    42: ["OffRoadPower", "EarthEngine", "SiteEngine", "RuggedCore"],
}

PRODUCT_GRADE_OPTIONS = {
    1: ["0W-20", "5W-30", "5W-40", "10W-40"],
    2: ["10W-30", "15W-40", "20W-40", "20W-50"],
    3: ["10W-40", "15W-40", "20W-50"],
    4: ["5W-30", "10W-30", "10W-40", "20W-40"],
    5: ["10W-40", "15W-40", "20W-40"],
    6: ["75W-90", "80W-90", "85W-140"],
    7: ["ATF Multi-Vehicle", "ATF Low-Viscosity", "ATF Synthetic"],
    8: ["75W-80", "75W-90", "80W"],
    9: ["75W-90", "80W-90", "85W-140"],
    10: ["80W-90", "85W-140", "75W-140"],
    11: ["AGMA 4", "AGMA 5", "AGMA 6"],
    12: ["ISO VG 32", "ISO VG 46", "ISO VG 68", "ISO VG 100"],
    13: ["ISO VG 32", "ISO VG 46", "ISO VG 68"],
    14: ["ISO VG 32", "ISO VG 46", "ISO VG 68", "ISO VG 100"],
    15: ["ISO VG 68", "ISO VG 100", "ISO VG 220"],
    16: ["ISO VG 32", "ISO VG 46", "ISO VG 68"],
    17: ["ISO VG 32", "ISO VG 46", "ISO VG 68"],
    18: ["UTTO 10W-30", "UTTO 20W-30", "UTTO 20W-40"],
    19: ["UTTO 10W-30", "UTTO 20W-30", "UTTO 20W-40"],
    20: ["10W", "10W-30", "15W-40"],
    21: ["UTTO 10W-30", "STOU 10W-30", "15W-40"],
    22: ["NLGI 1", "NLGI 2", "NLGI 3"],
    23: ["NLGI 1", "NLGI 2", "NLGI 3"],
    24: ["NLGI 2", "NLGI 3"],
    25: ["NLGI 1", "NLGI 2", "NLGI 3"],
    26: ["NLGI 2", "NLGI 3"],
    27: ["NLGI 1", "NLGI 2", "NLGI 3"],
    28: [None],
    29: [None],
    30: [None],
    31: [None],
    32: [None],
    33: [None],
    34: [None],
    35: [None],
    36: [None],
    37: [None],
    38: ["10W-30", "15W-40", "20W-50"],
    39: ["80W-90", "85W-140", "75W-90"],
    40: ["80W-90", "85W-140", "75W-140"],
    41: ["15W-40", "20W-40", "20W-50"],
    42: ["10W-40", "15W-40", "20W-50"],
}

PRODUCT_PACKAGE_GROUP = {
    **{
        sub_category_id: "automotive_liquid"
        for sub_category_id in range(1, 11)
    },
    **{
        sub_category_id: "industrial_liquid"
        for sub_category_id in range(11, 22)
    },
    **{
        sub_category_id: "grease"
        for sub_category_id in range(22, 28)
    },
    **{
        sub_category_id: "coolant"
        for sub_category_id in range(28, 33)
    },
    **{
        sub_category_id: "specialty_liquid"
        for sub_category_id in range(33, 38)
    },
    **{
        sub_category_id: "industrial_liquid"
        for sub_category_id in range(38, 43)
    },
}

PRODUCT_PACKAGE_DEFINITIONS = {
    "automotive_liquid": [
        ("Bottle", "800 ML", 0.8, 1),
        ("Bottle", "1 L", 1, 1),
        ("Bottle", "1.2 L", 1.2, 1),
        ("Bottle", "3 L", 3, 1),
        ("Bucket", "5 L", 5, 1),
        ("Bucket", "10 L", 10, 1),
        ("Bucket", "15 L", 15, 1),
        ("Bucket", "20 L", 20, 1),
        ("Bucket", "25 L", 25, 1),
        ("Bucket", "30 L", 30, 1),
        ("Drum", "50 L", 50, 1),
        ("Drum", "55 L", 55, 1),
        ("Drum", "180 L", 180, 1),
        ("Barrel", "210 L", 210, 1),
        ("Bulk", "1000 L", 1000, 1),
    ],
    "industrial_liquid": [
        ("Can", "3 L", 3, 1),
        ("Bucket", "5 L", 5, 1),
        ("Bucket", "10 L", 10, 1),
        ("Bucket", "15 L", 15, 1),
        ("Bucket", "20 L", 20, 1),
        ("Bucket", "25 L", 25, 1),
        ("Bucket", "30 L", 30, 1),
        ("Drum", "50 L", 50, 1),
        ("Drum", "55 L", 55, 1),
        ("Drum", "180 L", 180, 1),
        ("Barrel", "210 L", 210, 1),
        ("Bulk", "500 L", 500, 1),
        ("Bulk", "1000 L", 1000, 1),
        ("Bulk", "2000 L", 2000, 1),
    ],
    "grease": [
        ("Cartridge", "400 G", 0.4, 3),
        ("Tub", "500 G", 0.5, 3),
        ("Tub", "1 KG", 1, 3),
        ("Tub", "2 KG", 2, 3),
        ("Tub", "5 KG", 5, 3),
        ("Pail", "10 KG", 10, 3),
        ("Pail", "18 KG", 18, 3),
        ("Drum", "50 KG", 50, 3),
        ("Drum", "180 KG", 180, 3),
    ],
    "coolant": [
        ("Bottle", "1 L", 1, 1),
        ("Bottle", "3 L", 3, 1),
        ("Can", "5 L", 5, 1),
        ("Bucket", "10 L", 10, 1),
        ("Bucket", "20 L", 20, 1),
        ("Drum", "55 L", 55, 1),
        ("Barrel", "210 L", 210, 1),
        ("Bulk", "1000 L", 1000, 1),
    ],
    "specialty_liquid": [
        ("Bottle", "1 L", 1, 1),
        ("Can", "5 L", 5, 1),
        ("Bucket", "20 L", 20, 1),
        ("Drum", "55 L", 55, 1),
        ("Drum", "180 L", 180, 1),
        ("Barrel", "210 L", 210, 1),
        ("Bulk", "1000 L", 1000, 1),
        ("Bulk", "2000 L", 2000, 1),
    ],
}


PRODUCT_CATEGORY_NAMES = {
    row["category_id"]: row["category_name"]
    for row in CATEGORY_DEFINITIONS
}

BRAND_NAMES_BY_ID = {
    row["brand_id"]: row["brand_name"]
    for row in BRAND_DEFINITIONS
}

SUB_CATEGORY_BY_ID = {
    row["sub_category_id"]: row
    for row in SUB_CATEGORY_DEFINITIONS
}

UOM_CODES_BY_ID = {
    row["uom_id"]: row["uom_code"]
    for row in UOM_DEFINITIONS
}


# ============================================================
# Product-supplier relationship generation
# ============================================================

PRODUCT_SUPPLIER_RANDOM_SEED = 20260102

PRODUCT_SUPPLIER_COUNT_TARGETS = {
    1: 300,
    2: 525,
    3: 450,
    4: 225,
}

SUPPLIER_CATEGORY_CAPABILITIES = {
    "manufacturer": {
        1, 2, 3, 4, 5, 6, 7, 8,
    },
    "authorized_distributor": {
        1, 2, 3, 4, 5, 6, 8,
    },
    "regional_distributor": {
        1, 2, 3, 4, 5, 6, 8,
    },
    "importer": {
        2, 3, 4, 6, 7,
    },
    "bulk_supplier": {
        3, 4, 6, 7, 8,
    },
}

SUPPLIER_SELECTION_WEIGHTS = {
    "manufacturer": 3.0,
    "authorized_distributor": 2.4,
    "regional_distributor": 1.7,
    "importer": 1.1,
    "bulk_supplier": 0.9,
}

INACTIVE_SUPPLIER_SELECTION_FACTOR = 0.20

SUPPLIER_PRICE_MULTIPLIER_RANGES = {
    "manufacturer": (0.94, 1.05),
    "authorized_distributor": (1.02, 1.14),
    "regional_distributor": (1.05, 1.18),
    "importer": (1.08, 1.24),
    "bulk_supplier": (0.91, 1.02),
}

SUPPLIER_MOQ_MULTIPLIERS = {
    "manufacturer": 1.00,
    "authorized_distributor": 1.15,
    "regional_distributor": 1.25,
    "importer": 0.90,
    "bulk_supplier": 0.85,
}

CATEGORY_PURCHASE_PRICE_PER_BASE_UOM = {
    1: 240.0,
    2: 220.0,
    3: 190.0,
    4: 210.0,
    5: 360.0,
    6: 140.0,
    7: 320.0,
    8: 210.0,
}

CATEGORY_LEAD_TIME_ADJUSTMENT = {
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 0,
    6: 0,
    7: 2,
    8: 1,
}

PACKAGE_MOQ_BASE = {
    "Bottle": 12,
    "Can": 12,
    "Bucket": 6,
    "Drum": 2,
    "Barrel": 1,
    "Bulk": 1,
    "Cartridge": 24,
    "Tub": 12,
    "Pail": 4,
}

PACKAGE_CATEGORY_PRICE_DISCOUNT = {
    180: 0.95,
    500: 0.91,
}

PRODUCT_SUPPLIER_EFFECTIVE_FROM = date(2026, 1, 1)
PRODUCT_SUPPLIER_LEGACY_FROM = date(2024, 1, 1)
PRODUCT_SUPPLIER_LEGACY_TO = date(2025, 12, 31)

PRODUCT_SUPPLIER_ACTIVE_HISTORY_DAYS = 730
PRODUCT_SUPPLIER_INACTIVE_MAX_HISTORY_DAYS = 730
PRODUCT_SUPPLIER_INACTIVE_MIN_DURATION_DAYS = 60
PRODUCT_SUPPLIER_INACTIVE_MAX_DURATION_DAYS = 540

PACKAGED_PRODUCT_TYPES = {
    "Bottle",
    "Can",
    "Bucket",
    "Drum",
    "Barrel",
    "Cartridge",
    "Tub",
    "Pail",
}


def build_product_supplier_count_map(
    products: list[dict],
) -> dict[int, int]:
    """Assign deterministic supplier counts across products."""

    import random

    rng = random.Random(PRODUCT_SUPPLIER_RANDOM_SEED)

    product_ids = [
        row["product_id"]
        for row in products
    ]

    rng.shuffle(product_ids)

    expected_total_products = sum(
        PRODUCT_SUPPLIER_COUNT_TARGETS.values()
    )

    if len(product_ids) != expected_total_products:
        raise ValueError(
            "Product supplier count targets do not cover "
            f"the current product count: "
            f"expected {expected_total_products}, "
            f"got {len(product_ids)}"
        )

    count_map = {}
    cursor = 0

    for relationship_count in sorted(
        PRODUCT_SUPPLIER_COUNT_TARGETS
    ):
        product_count = PRODUCT_SUPPLIER_COUNT_TARGETS[
            relationship_count
        ]

        for product_id in product_ids[
            cursor:cursor + product_count
        ]:
            count_map[product_id] = relationship_count

        cursor += product_count

    return count_map


def _weighted_sample_without_replacement(
    rng,
    candidates: list[dict],
    weights: list[float],
    sample_size: int,
) -> list[dict]:
    """Sample unique candidates using deterministic weighted selection."""

    if sample_size > len(candidates):
        raise ValueError(
            "Cannot sample more suppliers than available "
            "eligible suppliers."
        )

    remaining_candidates = list(candidates)
    remaining_weights = list(weights)
    selected = []

    for _ in range(sample_size):
        total_weight = sum(remaining_weights)

        if total_weight <= 0:
            raise ValueError(
                "Supplier selection weights must contain "
                "a positive total."
            )

        threshold = rng.random() * total_weight
        cumulative = 0.0
        selected_index = None

        for index, weight in enumerate(
            remaining_weights
        ):
            cumulative += weight

            if threshold <= cumulative:
                selected_index = index
                break

        if selected_index is None:
            selected_index = len(remaining_candidates) - 1

        selected.append(
            remaining_candidates.pop(selected_index)
        )
        remaining_weights.pop(selected_index)

    return selected


def _get_product_category_id(
    product: dict,
) -> int:
    """Return the category ID associated with a product."""

    sub_category = SUB_CATEGORY_BY_ID[
        product["sub_category_id"]
    ]

    return sub_category["category_id"]


def _get_supplier_candidates(
    product: dict,
    suppliers: list[dict],
) -> list[dict]:
    """Return suppliers eligible for the product."""

    category_id = _get_product_category_id(product)

    eligible = []

    for supplier in suppliers:
        supplier_type = supplier["supplier_type"]

        allowed_categories = (
            SUPPLIER_CATEGORY_CAPABILITIES[
                supplier_type
            ]
        )

        if category_id not in allowed_categories:
            continue

        # Active products can only use active suppliers.
        if (
            product["product_status"] == "active"
            and supplier["supplier_status"] != "active"
        ):
            continue

        eligible.append(supplier)

    return eligible


def _get_purchase_uom_id(
    product: dict,
) -> int:
    """
    Determine the purchasing UOM from the product packaging.

    Packaged products are purchased by package.
    Bulk liquid products are purchased by litre.
    Bulk grease products are purchased by kilogram.
    """

    pack_type = product["pack_type"]
    base_uom_id = product["base_uom_id"]

    if pack_type in PACKAGED_PRODUCT_TYPES:
        return 6

    if pack_type == "Bulk":
        if base_uom_id == 1:
            return 1

        if base_uom_id == 3:
            return 3

        raise ValueError(
            "Bulk product must use a litre or kilogram base UOM: "
            f"product_id={product['product_id']}, "
            f"base_uom_id={base_uom_id}"
        )

    raise ValueError(
        "Unsupported product pack type for purchasing UOM: "
        f"product_id={product['product_id']}, "
        f"pack_type={pack_type}"
    )


def _build_supplier_product_name(
    product: dict,
) -> str:
    """Build a clean supplier-facing product name with package size in brackets."""

    product_name = product["product_name"].strip()
    pack_size = product["pack_size"].strip()

    if not product_name.endswith(pack_size):
        raise ValueError(
            "Product name does not end with its package size: "
            f"product_id={product['product_id']}"
        )

    base_name = product_name[
        :len(product_name) - len(pack_size)
    ].rstrip()

    supplier_product_name = (
        f"{base_name} ({pack_size})"
    )

    return supplier_product_name[:150]


def _calculate_unit_purchase_price(
    product: dict,
    supplier: dict,
    rng,
) -> float:
    """Calculate supplier-specific purchase price in the purchase UOM."""

    category_id = _get_product_category_id(product)

    base_price_per_uom = (
        CATEGORY_PURCHASE_PRICE_PER_BASE_UOM[
            category_id
        ]
    )

    base_quantity_per_pac = float(
        product["base_quantity_per_pac"]
    )

    purchase_uom_id = _get_purchase_uom_id(
        product
    )

    package_discount = 1.0

    for threshold, discount in sorted(
        PACKAGE_CATEGORY_PRICE_DISCOUNT.items()
    ):
        if base_quantity_per_pac >= threshold:
            package_discount = discount

    supplier_type = supplier["supplier_type"]

    minimum_multiplier, maximum_multiplier = (
        SUPPLIER_PRICE_MULTIPLIER_RANGES[
            supplier_type
        ]
    )

    supplier_multiplier = rng.uniform(
        minimum_multiplier,
        maximum_multiplier,
    )

    grade_multiplier = 1.0

    viscosity_grade = product["viscosity_grade"]

    if viscosity_grade == "ATF Synthetic":
        grade_multiplier = 1.08

    if viscosity_grade == "AGMA 6":
        grade_multiplier = 1.06

    if purchase_uom_id == 6:
        price = (
            base_price_per_uom
            * base_quantity_per_pac
            * package_discount
            * supplier_multiplier
            * grade_multiplier
        )

    elif purchase_uom_id in {1, 3}:
        price = (
            base_price_per_uom
            * package_discount
            * supplier_multiplier
            * grade_multiplier
        )

    else:
        raise ValueError(
            "Unsupported purchase UOM for purchase price: "
            f"product_id={product['product_id']}, "
            f"purchase_uom_id={purchase_uom_id}"
        )

    return round(
        max(price, 0.01),
        2,
    )


def _calculate_minimum_order_quantity(
    product: dict,
    supplier: dict,
    rng,
) -> float:
    """Calculate supplier MOQ in the purchase UOM."""

    pack_type = product["pack_type"]
    supplier_type = supplier["supplier_type"]

    supplier_multiplier = (
        SUPPLIER_MOQ_MULTIPLIERS[
            supplier_type
        ]
    )

    purchase_uom_id = _get_purchase_uom_id(
        product
    )

    if purchase_uom_id == 6:
        base_moq = PACKAGE_MOQ_BASE[
            pack_type
        ]

        variation = rng.uniform(
            0.85,
            1.20,
        )

        quantity = round(
            base_moq
            * supplier_multiplier
            * variation
        )

        return float(
            max(
                int(quantity),
                1,
            )
        )

    if purchase_uom_id in {1, 3}:
        base_quantity_per_pac = float(
            product["base_quantity_per_pac"]
        )

        variation = rng.uniform(
            0.80,
            1.25,
        )

        raw_quantity = (
            base_quantity_per_pac
            * supplier_multiplier
            * variation
        )

        # Bulk ordering is expressed in practical lot sizes.
        lot_size = 50.0

        quantity = (
            round(
                raw_quantity / lot_size
            )
            * lot_size
        )

        return round(
            max(
                quantity,
                lot_size,
            ),
            3,
        )

    raise ValueError(
        "Unsupported purchase UOM for MOQ: "
        f"product_id={product['product_id']}, "
        f"purchase_uom_id={purchase_uom_id}"
    )


def _calculate_relationship_lead_time(
    product: dict,
    supplier: dict,
    rng,
) -> int:
    """Calculate product-specific sourcing lead time."""

    category_id = _get_product_category_id(product)

    supplier_baseline = supplier["lead_time_days"]

    category_adjustment = (
        CATEGORY_LEAD_TIME_ADJUSTMENT[
            category_id
        ]
    )

    package_adjustment = 0

    if float(product["base_quantity_per_pac"]) >= 180:
        package_adjustment = 1

    variation = rng.randint(
        -2,
        3,
    )

    lead_time = (
        supplier_baseline
        + category_adjustment
        + package_adjustment
        + variation
    )

    return max(
        int(lead_time),
        0,
    )


def _calculate_relationship_dates(
    relationship_status: str,
    rng,
) -> tuple[date, date | None]:
    """Generate deterministic business-valid relationship effective dates."""

    if relationship_status == "active":
        effective_from = (
            PRODUCT_SUPPLIER_EFFECTIVE_FROM
            - timedelta(
                days=rng.randint(
                    0,
                    PRODUCT_SUPPLIER_ACTIVE_HISTORY_DAYS,
                )
            )
        )

        return (
            effective_from,
            None,
        )

    if relationship_status == "inactive":
        effective_to = (
            PRODUCT_SUPPLIER_LEGACY_TO
            - timedelta(
                days=rng.randint(
                    0,
                    364,
                )
            )
        )

        duration_days = rng.randint(
            PRODUCT_SUPPLIER_INACTIVE_MIN_DURATION_DAYS,
            PRODUCT_SUPPLIER_INACTIVE_MAX_DURATION_DAYS,
        )

        effective_from = (
            effective_to
            - timedelta(days=duration_days)
        )

        minimum_allowed_from = (
            PRODUCT_SUPPLIER_LEGACY_FROM
            - timedelta(
                days=PRODUCT_SUPPLIER_INACTIVE_MAX_HISTORY_DAYS
            )
        )

        if effective_from < minimum_allowed_from:
            effective_from = minimum_allowed_from

        if effective_from >= effective_to:
            effective_from = (
                effective_to
                - timedelta(
                    days=PRODUCT_SUPPLIER_INACTIVE_MIN_DURATION_DAYS
                )
            )

        return (
            effective_from,
            effective_to,
        )

    raise ValueError(
        "Unsupported product-supplier relationship status: "
        f"{relationship_status}"
    )


def _select_primary_supplier(
    relationship_candidates: list[dict],
    rng,
) -> int:
    """Select one active primary supplier without always choosing the cheapest."""

    if not relationship_candidates:
        raise ValueError(
            "Cannot select a primary supplier from an empty set."
        )

    if len(relationship_candidates) == 1:
        return relationship_candidates[0][
            "supplier_id"
        ]

    minimum_price = min(
        row["unit_purchase_price"]
        for row in relationship_candidates
    )

    minimum_lead_time = min(
        row["lead_time_days"]
        for row in relationship_candidates
    )

    scored = []

    for row in relationship_candidates:
        supplier_type = row[
            "_supplier_type"
        ]

        supplier_preference = (
            1.0
            / SUPPLIER_SELECTION_WEIGHTS[
                supplier_type
            ]
        )

        price_ratio = (
            row["unit_purchase_price"]
            / minimum_price
        )

        lead_ratio = (
            row["lead_time_days"]
            / max(
                minimum_lead_time,
                1,
            )
        )

        score = (
            0.55 * price_ratio
            + 0.30 * lead_ratio
            + 0.15 * supplier_preference
            + rng.uniform(0.0, 0.03)
        )

        scored.append(
            (
                score,
                row,
            )
        )

    scored.sort(
        key=lambda item: item[0]
    )

    top_candidates = [
        item[1]
        for item in scored[:3]
    ]

    if len(top_candidates) == 1:
        return top_candidates[0][
            "supplier_id"
        ]

    selection_weights = []

    for index in range(
        len(top_candidates)
    ):
        if index == 0:
            selection_weights.append(0.60)
        elif index == 1:
            selection_weights.append(0.25)
        else:
            selection_weights.append(0.15)

    total_weight = sum(
        selection_weights
    )

    threshold = (
        rng.random()
        * total_weight
    )

    cumulative = 0.0

    for index, weight in enumerate(
        selection_weights
    ):
        cumulative += weight

        if threshold <= cumulative:
            return top_candidates[index][
                "supplier_id"
            ]

    return top_candidates[-1][
        "supplier_id"
    ]


def generate_product_suppliers(
    products: list[dict],
    suppliers: list[dict],
) -> list[dict]:
    """Generate deterministic product-supplier relationships."""

    import random

    rng = random.Random(
        PRODUCT_SUPPLIER_RANDOM_SEED
    )

    relationship_count_map = (
        build_product_supplier_count_map(
            products
        )
    )

    relationship_rows = []

    for product in products:
        product_id = product["product_id"]

        relationship_count = (
            relationship_count_map[
                product_id
            ]
        )

        candidates = _get_supplier_candidates(
            product,
            suppliers,
        )

        if len(candidates) < relationship_count:
            raise ValueError(
                "Insufficient eligible suppliers for "
                f"product {product['sku']}: "
                f"required={relationship_count}, "
                f"available={len(candidates)}"
            )

        weights = []

        for supplier in candidates:
            supplier_type = supplier[
                "supplier_type"
            ]

            weight = SUPPLIER_SELECTION_WEIGHTS[
                supplier_type
            ]

            if (
                supplier["supplier_status"]
                != "active"
            ):
                weight *= (
                    INACTIVE_SUPPLIER_SELECTION_FACTOR
                )

            weights.append(weight)

        selected_suppliers = (
            _weighted_sample_without_replacement(
                rng,
                candidates,
                weights,
                relationship_count,
            )
        )

        candidate_relationships = []

        for supplier in selected_suppliers:
            relationship_status = (
                "active"
                if product["product_status"]
                == "active"
                else "inactive"
            )

            purchase_uom_id = _get_purchase_uom_id(
                product
            )

            purchase_price = (
                _calculate_unit_purchase_price(
                    product,
                    supplier,
                    rng,
                )
            )

            minimum_order_quantity = (
                _calculate_minimum_order_quantity(
                    product,
                    supplier,
                    rng,
                )
            )

            lead_time_days = (
                _calculate_relationship_lead_time(
                    product,
                    supplier,
                    rng,
                )
            )

            category_prefix = (
                CATEGORY_SKU_PREFIXES[
                    _get_product_category_id(product)
                ]
            )

            supplier_product_code = (
                f"{supplier['supplier_code']}-"
                f"{category_prefix}-"
                f"{product_id:04d}"
            )

            supplier_product_name = (
                _build_supplier_product_name(
                    product
                )
            )

            effective_from, effective_to = (
                _calculate_relationship_dates(
                    relationship_status,
                    rng,
                )
            )

            candidate_relationships.append(
                {
                    "product_id": product_id,
                    "supplier_id": supplier[
                        "supplier_id"
                    ],
                    "supplier_product_code": (
                        supplier_product_code
                    ),
                    "supplier_product_name": (
                        supplier_product_name
                    ),
                    "purchase_uom_id": (
                        purchase_uom_id
                    ),
                    "unit_purchase_price": (
                        purchase_price
                    ),
                    "minimum_order_quantity": (
                        minimum_order_quantity
                    ),
                    "lead_time_days": (
                        lead_time_days
                    ),
                    "is_primary_source": False,
                    "relationship_status": (
                        relationship_status
                    ),
                    "effective_from": (
                        effective_from.isoformat()
                    ),
                    "effective_to": (
                        effective_to.isoformat()
                        if effective_to
                        else None
                    ),
                    "_supplier_type": supplier[
                        "supplier_type"
                    ],
                }
            )

        if product["product_status"] == "active":
            primary_supplier_id = (
                _select_primary_supplier(
                    candidate_relationships,
                    rng,
                )
            )

            for row in candidate_relationships:
                row["is_primary_source"] = (
                    row["supplier_id"]
                    == primary_supplier_id
                )

        for row in candidate_relationships:
            row.pop(
                "_supplier_type",
                None,
            )

            row["product_supplier_id"] = (
                len(relationship_rows) + 1
            )

            relationship_rows.append(
                row
            )

    expected_relationship_count = (
        sum(
            relationship_count
            * product_count
            for relationship_count,
            product_count
            in PRODUCT_SUPPLIER_COUNT_TARGETS.items()
        )
    )

    if len(relationship_rows) != (
        expected_relationship_count
    ):
        raise ValueError(
            "Product-supplier relationship count mismatch: "
            f"expected {expected_relationship_count}, "
            f"generated {len(relationship_rows)}"
        )

    return relationship_rows


def validate_product_suppliers(
    product_suppliers: list[dict],
    products: list[dict],
    suppliers: list[dict],
) -> None:
    """Validate product-supplier relationships and sourcing rules."""

    expected_relationship_count = (
        sum(
            relationship_count
            * product_count
            for relationship_count,
            product_count
            in PRODUCT_SUPPLIER_COUNT_TARGETS.items()
        )
    )

    if len(product_suppliers) != (
        expected_relationship_count
    ):
        raise ValueError(
            "Product-supplier relationship count mismatch: "
            f"expected {expected_relationship_count}, "
            f"got {len(product_suppliers)}"
        )

    required_fields = {
        "product_supplier_id",
        "product_id",
        "supplier_id",
        "supplier_product_code",
        "supplier_product_name",
        "purchase_uom_id",
        "unit_purchase_price",
        "minimum_order_quantity",
        "lead_time_days",
        "is_primary_source",
        "relationship_status",
        "effective_from",
        "effective_to",
    }

    for row in product_suppliers:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                "Missing product-supplier fields: "
                f"{sorted(missing_fields)}"
            )

    product_map = {
        row["product_id"]: row
        for row in products
    }

    supplier_map = {
        row["supplier_id"]: row
        for row in suppliers
    }

    relationship_ids = [
        row["product_supplier_id"]
        for row in product_suppliers
    ]

    if relationship_ids != list(
        range(
            1,
            expected_relationship_count + 1,
        )
    ):
        raise ValueError(
            "Product-supplier IDs are not sequential."
        )

    relationship_pairs = [
        (
            row["product_id"],
            row["supplier_id"],
        )
        for row in product_suppliers
    ]

    if len(relationship_pairs) != len(
        set(relationship_pairs)
    ):
        raise ValueError(
            "Duplicate product-supplier relationship found."
        )

    supplier_codes = [
        (
            row["supplier_id"],
            row["supplier_product_code"],
        )
        for row in product_suppliers
    ]

    if len(supplier_codes) != len(
        set(supplier_codes)
    ):
        raise ValueError(
            "Duplicate supplier product code found "
            "within supplier."
        )

    relationship_count_by_product = {}

    for row in product_suppliers:
        product_id = row["product_id"]
        supplier_id = row["supplier_id"]

        if product_id not in product_map:
            raise ValueError(
                "Product-supplier relationship references "
                f"unknown product_id: {product_id}"
            )

        if supplier_id not in supplier_map:
            raise ValueError(
                "Product-supplier relationship references "
                f"unknown supplier_id: {supplier_id}"
            )

        supplier = supplier_map[
            supplier_id
        ]

        product = product_map[
            product_id
        ]

        expected_purchase_uom_id = (
            _get_purchase_uom_id(
                product
            )
        )

        if row["purchase_uom_id"] != (
            expected_purchase_uom_id
        ):
            raise ValueError(
                "Unexpected product-supplier purchase UOM: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}, "
                f"expected={expected_purchase_uom_id}, "
                f"got={row['purchase_uom_id']}"
            )

        if (
            row["purchase_uom_id"]
            not in UOM_CODES_BY_ID
        ):
            raise ValueError(
                "Unknown purchase UOM ID: "
                f"{row['purchase_uom_id']}"
            )

        if row["unit_purchase_price"] <= 0:
            raise ValueError(
                "Unit purchase price must be positive: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if row["minimum_order_quantity"] <= 0:
            raise ValueError(
                "Minimum order quantity must be positive: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if row["lead_time_days"] < 0:
            raise ValueError(
                "Lead time cannot be negative: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if row["relationship_status"] not in {
            "active",
            "inactive",
        }:
            raise ValueError(
                "Invalid product-supplier relationship status: "
                f"{row['relationship_status']}"
            )

        if not row["supplier_product_code"].strip():
            raise ValueError(
                "Supplier product code cannot be empty: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        expected_supplier_product_name = (
            _build_supplier_product_name(
                product
            )
        )

        if (
            row["supplier_product_name"]
            != expected_supplier_product_name
        ):
            raise ValueError(
                "Supplier product name format mismatch: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if (
            len(
                row["supplier_product_name"]
            )
            > 150
        ):
            raise ValueError(
                "Supplier product name exceeds 150 characters: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if (
            row["supplier_product_name"]
            .endswith("Supply Pack")
        ):
            raise ValueError(
                "Supplier product name contains the deprecated "
                "Supply Pack suffix: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if supplier["supplier_code"] in (
            row["supplier_product_name"]
        ):
            raise ValueError(
                "Supplier product name contains a supplier code: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if not (
            row["supplier_product_name"]
            .endswith(
                f"({product['pack_size']})"
            )
        ):
            raise ValueError(
                "Supplier product name must end with "
                "the package size in brackets: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        effective_from = date.fromisoformat(
            row["effective_from"]
        )

        effective_to = None

        if row["effective_to"] is not None:
            effective_to = date.fromisoformat(
                row["effective_to"]
            )

            if effective_to < effective_from:
                raise ValueError(
                    "effective_to cannot be before "
                    "effective_from."
                )

        if (
            effective_from
            > PRODUCT_SUPPLIER_EFFECTIVE_FROM
        ):
            raise ValueError(
                "effective_from cannot be in the future "
                "relative to the master data date: "
                f"product_id={product_id}, "
                f"supplier_id={supplier_id}"
            )

        if (
            row["relationship_status"]
            == "active"
        ):
            if supplier["supplier_status"] != "active":
                raise ValueError(
                    "Inactive supplier cannot have "
                    "an active relationship: "
                    f"supplier_id={supplier_id}"
                )

            if product["product_status"] != "active":
                raise ValueError(
                    "Non-active product cannot have "
                    "an active supplier relationship: "
                    f"product_id={product_id}"
                )

            if effective_to is not None:
                raise ValueError(
                    "Active relationship must not have "
                    "an effective_to date."
                )

        else:
            if row["is_primary_source"]:
                raise ValueError(
                    "Inactive relationship cannot be primary."
                )

            if effective_to is None:
                raise ValueError(
                    "Inactive relationship must have "
                    "an effective_to date."
                )

            if effective_to >= PRODUCT_SUPPLIER_EFFECTIVE_FROM:
                raise ValueError(
                    "Inactive relationship must end before "
                    "the active master-data date: "
                    f"product_id={product_id}, "
                    f"supplier_id={supplier_id}"
                )

        if supplier["supplier_status"] == "inactive":
            if (
                row["relationship_status"]
                == "active"
            ):
                raise ValueError(
                    "Inactive supplier cannot be active."
                )

            if row["is_primary_source"]:
                raise ValueError(
                    "Inactive supplier cannot be primary."
                )

        relationship_count_by_product[
            product_id
        ] = (
            relationship_count_by_product.get(
                product_id,
                0,
            )
            + 1
        )

    if set(relationship_count_by_product) != set(
        product_map
    ):
        missing_products = (
            set(product_map)
            - set(relationship_count_by_product)
        )

        raise ValueError(
            "Products without supplier relationships: "
            f"{sorted(missing_products)[:20]}"
        )

    expected_count_map = (
        build_product_supplier_count_map(
            products
        )
    )

    if (
        relationship_count_by_product
        != expected_count_map
    ):
        raise ValueError(
            "Product-supplier relationship count "
            "distribution mismatch."
        )

    primary_count_by_product = {}

    active_relationship_count_by_product = {}

    for row in product_suppliers:
        product_id = row["product_id"]

        if row["is_primary_source"]:
            primary_count_by_product[
                product_id
            ] = (
                primary_count_by_product.get(
                    product_id,
                    0,
                )
                + 1
            )

        if row["relationship_status"] == "active":
            active_relationship_count_by_product[
                product_id
            ] = (
                active_relationship_count_by_product.get(
                    product_id,
                    0,
                )
                + 1
            )

    for product in products:
        product_id = product[
            "product_id"
        ]

        primary_count = (
            primary_count_by_product.get(
                product_id,
                0,
            )
        )

        active_relationship_count = (
            active_relationship_count_by_product.get(
                product_id,
                0,
            )
        )

        if product["product_status"] == "active":
            if active_relationship_count < 1:
                raise ValueError(
                    "Active product has no active supplier relationship: "
                    f"product_id={product_id}"
                )

            if primary_count != 1:
                raise ValueError(
                    "Active product must have exactly "
                    "one active primary supplier: "
                    f"product_id={product_id}"
                )

        else:
            if active_relationship_count != 0:
                raise ValueError(
                    "Inactive/discontinued product cannot "
                    "have active supplier relationships: "
                    f"product_id={product_id}"
                )

            if primary_count != 0:
                raise ValueError(
                    "Inactive/discontinued product cannot "
                    "have a primary supplier: "
                    f"product_id={product_id}"
                )

    relationship_count_distribution = {}

    for count in relationship_count_by_product.values():
        relationship_count_distribution[count] = (
            relationship_count_distribution.get(
                count,
                0,
            )
            + 1
        )

    if (
        relationship_count_distribution
        != PRODUCT_SUPPLIER_COUNT_TARGETS
    ):
        raise ValueError(
            "Supplier-per-product distribution mismatch: "
            f"{relationship_count_distribution}"
        )


def generate_products() -> list[dict]:
    """Generate the large product master deterministically."""

    import random

    rng = random.Random(PRODUCT_RANDOM_SEED)
    product_rows = []

    category_sequences = {
        category_id: 0
        for category_id in CATEGORY_PRODUCT_TARGETS
    }

    global_index = 0

    status_pool = (
        ["active"] * PRODUCT_STATUS_TARGETS["active"]
        + ["inactive"] * PRODUCT_STATUS_TARGETS["inactive"]
        + ["discontinued"] * PRODUCT_STATUS_TARGETS["discontinued"]
    )

    rng.shuffle(status_pool)

    for sub_category_id in sorted(SUB_CATEGORY_PRODUCT_TARGETS):
        target_count = SUB_CATEGORY_PRODUCT_TARGETS[sub_category_id]
        sub_category = SUB_CATEGORY_BY_ID[sub_category_id]
        category_id = sub_category["category_id"]
        category_prefix = CATEGORY_SKU_PREFIXES[category_id]

        families = PRODUCT_FAMILY_STEMS[sub_category_id]
        grades = PRODUCT_GRADE_OPTIONS[sub_category_id]
        package_group = PRODUCT_PACKAGE_GROUP[sub_category_id]
        packages = PRODUCT_PACKAGE_DEFINITIONS[package_group]

        for local_index in range(target_count):
            brand_id = (
                global_index
                % len(BRAND_DEFINITIONS)
            ) + 1

            family = families[
                local_index % len(families)
            ]

            grade = grades[
                (local_index // len(families))
                % len(grades)
            ]

            package = packages[
                (
                    local_index
                    + sub_category_id * 2
                )
                % len(packages)
            ]

            (
                pack_type,
                pack_size,
                base_quantity,
                base_uom_id,
            ) = package

            category_sequences[category_id] += 1

            category_sequence = (
                category_sequences[
                    category_id
                ]
            )

            sku = (
                f"NR-{category_prefix}-"
                f"{category_sequence:04d}"
            )

            name_parts = [
                BRAND_NAMES_BY_ID[brand_id],
                family,
            ]

            if grade is not None:
                name_parts.append(grade)

            name_parts.append(pack_size)

            product_rows.append(
                {
                    "product_id": global_index + 1,
                    "sku": sku,
                    "product_name": " ".join(
                        name_parts
                    ),
                    "brand_id": brand_id,
                    "sub_category_id": (
                        sub_category_id
                    ),
                    "base_uom_id": base_uom_id,
                    "pack_type": pack_type,
                    "pack_size": pack_size,
                    "base_quantity_per_pac": (
                        base_quantity
                    ),
                    "viscosity_grade": grade,
                    "product_status": (
                        status_pool[global_index]
                    ),
                }
            )

            global_index += 1

    if len(product_rows) != PRODUCT_MASTER_COUNT:
        raise ValueError(
            f"Expected {PRODUCT_MASTER_COUNT} products, "
            f"generated {len(product_rows)}"
        )

    return product_rows


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

    return value.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def add_audit_columns(row: dict) -> dict:
    """Add standard audit fields to a master-data row."""

    timestamp = format_timestamp(
        MASTER_DATA_DATE
    )

    return {
        **row,
        "created_date": timestamp,
        "created_by": DEFAULT_CREATED_BY,
        "updated_date": timestamp,
        "updated_by": DEFAULT_UPDATED_BY,
    }


def get_warehouse_by_id(
    warehouse_id: int,
) -> dict:
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

def validate_uoms(
    uoms: list[dict],
) -> None:
    """Validate UOM master data."""

    if not uoms:
        raise ValueError(
            "UOM data is empty."
        )

    required_fields = {
        "uom_id",
        "uom_code",
        "uom_name",
        "uom_category",
        "is_active",
    }

    for row in uoms:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing UOM fields: "
                f"{sorted(missing_fields)}"
            )

    uom_ids = [
        row["uom_id"]
        for row in uoms
    ]

    uom_codes = [
        row["uom_code"]
        for row in uoms
    ]

    uom_names = [
        row["uom_name"]
        for row in uoms
    ]

    if len(uom_ids) != len(
        set(uom_ids)
    ):
        raise ValueError(
            "Duplicate uom_id found."
        )

    if len(uom_codes) != len(
        set(uom_codes)
    ):
        raise ValueError(
            "Duplicate uom_code found."
        )

    if len(uom_names) != len(
        set(uom_names)
    ):
        raise ValueError(
            "Duplicate uom_name found."
        )

    if uom_ids != sorted(uom_ids):
        raise ValueError(
            "UOM IDs are not in ascending order."
        )

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
                f"Invalid UOM category: "
                f"{row['uom_category']}"
            )

        if not isinstance(
            row["is_active"],
            bool,
        ):
            raise ValueError(
                f"is_active must be boolean for UOM: "
                f"{row['uom_code']}"
            )

        if row["uom_id"] <= 0:
            raise ValueError(
                f"uom_id must be positive: "
                f"{row['uom_id']}"
            )


# ============================================================
# Payment term validation
# ============================================================

def validate_payment_terms(
    payment_terms: list[dict],
) -> None:
    """Validate payment term master data."""

    if not payment_terms:
        raise ValueError(
            "Payment term data is empty."
        )

    required_fields = {
        "payment_term_id",
        "payment_term_code",
        "payment_term_name",
        "payment_term_days",
        "payment_term_description",
        "payment_term_status",
    }

    for row in payment_terms:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing payment term fields: "
                f"{sorted(missing_fields)}"
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

    if len(payment_term_ids) != len(
        set(payment_term_ids)
    ):
        raise ValueError(
            "Duplicate payment_term_id found."
        )

    if len(payment_term_codes) != len(
        set(payment_term_codes)
    ):
        raise ValueError(
            "Duplicate payment_term_code found."
        )

    if len(payment_term_names) != len(
        set(payment_term_names)
    ):
        raise ValueError(
            "Duplicate payment_term_name found."
        )

    if payment_term_ids != sorted(
        payment_term_ids
    ):
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
# Supplier validation
# ============================================================

SUPPLIER_EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

SUPPLIER_PHONE_PATTERN = re.compile(
    r"^[0-9()+\-\s]{8,25}$"
)

SUPPLIER_GSTIN_PATTERN = re.compile(
    r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9]Z[A-Z0-9]$"
)


def validate_suppliers(
    suppliers: list[dict],
    payment_terms: list[dict],
) -> None:
    """Validate supplier master data."""

    if not suppliers:
        raise ValueError(
            "Supplier data is empty."
        )

    required_fields = {
        "supplier_id",
        "supplier_code",
        "supplier_name",
        "supplier_type",
        "contact_person",
        "phone",
        "email",
        "gstin",
        "state_code",
        "address_line1",
        "address_line2",
        "city",
        "state",
        "postal_code",
        "country",
        "lead_time_days",
        "payment_term_id",
        "supplier_status",
    }

    for row in suppliers:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing supplier fields: "
                f"{sorted(missing_fields)}"
            )

    supplier_ids = [
        row["supplier_id"]
        for row in suppliers
    ]

    supplier_codes = [
        row["supplier_code"]
        for row in suppliers
    ]

    supplier_names = [
        row["supplier_name"]
        for row in suppliers
    ]

    supplier_phones = [
        row["phone"]
        for row in suppliers
    ]

    supplier_emails = [
        row["email"].lower()
        for row in suppliers
    ]

    supplier_gstins = [
        row["gstin"].upper()
        for row in suppliers
    ]

    if len(supplier_ids) != len(
        set(supplier_ids)
    ):
        raise ValueError(
            "Duplicate supplier_id found."
        )

    if len(supplier_codes) != len(
        set(supplier_codes)
    ):
        raise ValueError(
            "Duplicate supplier_code found."
        )

    if len(supplier_names) != len(
        set(supplier_names)
    ):
        raise ValueError(
            "Duplicate supplier_name found."
        )

    if len(supplier_phones) != len(
        set(supplier_phones)
    ):
        raise ValueError(
            "Duplicate supplier phone found."
        )

    if len(supplier_emails) != len(
        set(supplier_emails)
    ):
        raise ValueError(
            "Duplicate supplier email found."
        )

    if len(supplier_gstins) != len(
        set(supplier_gstins)
    ):
        raise ValueError(
            "Duplicate supplier GSTIN found."
        )

    if supplier_ids != sorted(
        supplier_ids
    ):
        raise ValueError(
            "Supplier IDs are not in ascending order."
        )

    allowed_supplier_types = {
        "manufacturer",
        "authorized_distributor",
        "regional_distributor",
        "importer",
        "bulk_supplier",
    }

    allowed_statuses = {
        "active",
        "inactive",
    }

    payment_term_ids = {
        row["payment_term_id"]
        for row in payment_terms
    }

    for row in suppliers:
        code = row["supplier_code"]

        if row["supplier_id"] <= 0:
            raise ValueError(
                f"supplier_id must be positive: "
                f"{row['supplier_id']}"
            )

        if not row["supplier_code"].strip():
            raise ValueError(
                f"Supplier code cannot be empty: "
                f"{row['supplier_id']}"
            )

        if not row["supplier_name"].strip():
            raise ValueError(
                f"Supplier name cannot be empty: "
                f"{row['supplier_id']}"
            )

        if row["supplier_type"] not in allowed_supplier_types:
            raise ValueError(
                f"Invalid supplier type: "
                f"{row['supplier_type']}"
            )

        if not row["contact_person"].strip():
            raise ValueError(
                f"Supplier contact_person cannot be empty: "
                f"{code}"
            )

        phone = row["phone"].strip()

        if not SUPPLIER_PHONE_PATTERN.fullmatch(
            phone
        ):
            raise ValueError(
                f"Invalid supplier phone format: {code}"
            )

        phone_digits = re.sub(
            r"\D",
            "",
            phone,
        )

        if len(phone_digits) < 8:
            raise ValueError(
                f"Supplier phone has too few digits: {code}"
            )

        if len(set(phone_digits)) == 1:
            raise ValueError(
                f"Supplier phone looks like a placeholder: {code}"
            )

        email = row["email"].strip()

        if (
            not email
            or not SUPPLIER_EMAIL_PATTERN.fullmatch(
                email
            )
        ):
            raise ValueError(
                f"Invalid supplier email format: {code}"
            )

        email_domain = email.rsplit(
            "@",
            1,
        )[1].lower()

        blocked_email_tokens = {
            "test",
            "demo",
            "dummy",
            "sample",
            "localhost",
            "invalid",
        }

        if any(
            token in email_domain
            for token in blocked_email_tokens
        ):
            raise ValueError(
                f"Supplier email domain looks like a placeholder: {code}"
            )

        gstin = row["gstin"].strip().upper()

        if not SUPPLIER_GSTIN_PATTERN.fullmatch(
            gstin
        ):
            raise ValueError(
                f"Invalid supplier GSTIN format: {code}"
            )

        state_code = row["state_code"].strip()

        if (
            not state_code
            or gstin[:2] != state_code
        ):
            raise ValueError(
                f"Supplier GSTIN/state_code mismatch: {code}"
            )

        if row["lead_time_days"] < 0:
            raise ValueError(
                f"Negative supplier lead time: {code}"
            )

        if row["payment_term_id"] not in payment_term_ids:
            raise ValueError(
                f"Invalid payment_term_id "
                f"{row['payment_term_id']} for {code}"
            )

        if row["supplier_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid supplier status: "
                f"{row['supplier_status']}"
            )

        for field in (
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal_code",
            "country",
        ):
            if not row[field].strip():
                raise ValueError(
                    f"Supplier {field} cannot be empty: "
                    f"{code}"
                )


# ============================================================
# Brand validation
# ============================================================

def validate_brands(
    brands: list[dict],
) -> None:
    """Validate brand master data."""

    if not brands:
        raise ValueError(
            "Brand data is empty."
        )

    required_fields = {
        "brand_id",
        "brand_code",
        "brand_name",
        "brand_owner_company",
        "brand_status",
    }

    for row in brands:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing brand fields: "
                f"{sorted(missing_fields)}"
            )

    brand_ids = [
        row["brand_id"]
        for row in brands
    ]

    brand_codes = [
        row["brand_code"]
        for row in brands
    ]

    brand_names = [
        row["brand_name"]
        for row in brands
    ]

    if len(brand_ids) != len(
        set(brand_ids)
    ):
        raise ValueError(
            "Duplicate brand_id found."
        )

    if len(brand_codes) != len(
        set(brand_codes)
    ):
        raise ValueError(
            "Duplicate brand_code found."
        )

    if len(brand_names) != len(
        set(brand_names)
    ):
        raise ValueError(
            "Duplicate brand_name found."
        )

    if brand_ids != sorted(brand_ids):
        raise ValueError(
            "Brand IDs are not in ascending order."
        )

    allowed_statuses = {
        "active",
        "inactive",
    }

    for row in brands:
        if row["brand_id"] <= 0:
            raise ValueError(
                f"brand_id must be positive: "
                f"{row['brand_id']}"
            )

        if not row["brand_code"].strip():
            raise ValueError(
                f"Brand code cannot be empty: "
                f"{row['brand_id']}"
            )

        if not row["brand_name"].strip():
            raise ValueError(
                f"Brand name cannot be empty: "
                f"{row['brand_id']}"
            )

        if row["brand_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid brand status: "
                f"{row['brand_status']}"
            )

        if row["brand_owner_company"] != COMPANY_NAME:
            raise ValueError(
                f"Unexpected brand owner: "
                f"{row['brand_name']}"
            )


# ============================================================
# Category validation
# ============================================================

def validate_categories(
    categories: list[dict],
) -> None:
    """Validate category master data."""

    if not categories:
        raise ValueError(
            "Category data is empty."
        )

    required_fields = {
        "category_id",
        "category_code",
        "category_name",
        "category_status",
    }

    for row in categories:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing category fields: "
                f"{sorted(missing_fields)}"
            )

    category_ids = [
        row["category_id"]
        for row in categories
    ]

    category_codes = [
        row["category_code"]
        for row in categories
    ]

    category_names = [
        row["category_name"]
        for row in categories
    ]

    if len(category_ids) != len(
        set(category_ids)
    ):
        raise ValueError(
            "Duplicate category_id found."
        )

    if len(category_codes) != len(
        set(category_codes)
    ):
        raise ValueError(
            "Duplicate category_code found."
        )

    if len(category_names) != len(
        set(category_names)
    ):
        raise ValueError(
            "Duplicate category_name found."
        )

    if category_ids != sorted(
        category_ids
    ):
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
        raise ValueError(
            "Sub-category data is empty."
        )

    required_fields = {
        "sub_category_id",
        "category_id",
        "sub_category_code",
        "sub_category_name",
        "description",
        "sub_category_status",
    }

    for row in sub_categories:
        missing_fields = (
            required_fields - row.keys()
        )

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

    if len(sub_category_ids) != len(
        set(sub_category_ids)
    ):
        raise ValueError(
            "Duplicate sub_category_id found."
        )

    if len(sub_category_codes) != len(
        set(sub_category_codes)
    ):
        raise ValueError(
            "Duplicate sub_category_code found."
        )

    if sub_category_ids != sorted(
        sub_category_ids
    ):
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
                f"Invalid category_id "
                f"{row['category_id']} "
                f"for sub-category "
                f"{row['sub_category_code']}"
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
                "Duplicate sub-category name "
                "within category: "
                f"{category_name_key}"
            )

        category_name_pairs.add(
            category_name_key
        )


# ============================================================
# Product validation
# ============================================================

def validate_products(
    products: list[dict],
) -> None:
    """Validate product master data and reference integrity."""

    if len(products) != PRODUCT_MASTER_COUNT:
        raise ValueError(
            f"Product count mismatch: expected "
            f"{PRODUCT_MASTER_COUNT}, got {len(products)}"
        )

    required_fields = {
        "product_id",
        "sku",
        "product_name",
        "brand_id",
        "sub_category_id",
        "base_uom_id",
        "pack_type",
        "pack_size",
        "base_quantity_per_pac",
        "viscosity_grade",
        "product_status",
    }

    for row in products:
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing product fields: "
                f"{sorted(missing_fields)}"
            )

    product_ids = [
        row["product_id"]
        for row in products
    ]

    skus = [
        row["sku"]
        for row in products
    ]

    product_names = [
        row["product_name"]
        for row in products
    ]

    if product_ids != list(
        range(
            1,
            PRODUCT_MASTER_COUNT + 1,
        )
    ):
        raise ValueError(
            "Product IDs are not sequential from 1 "
            f"to {PRODUCT_MASTER_COUNT}."
        )

    if len(skus) != len(
        set(skus)
    ):
        raise ValueError(
            "Duplicate product SKU found."
        )

    if len(product_names) != len(
        set(product_names)
    ):
        raise ValueError(
            "Duplicate product_name found."
        )

    brand_ids = {
        row["brand_id"]
        for row in BRAND_DEFINITIONS
    }

    sub_category_map = {
        row["sub_category_id"]: row
        for row in SUB_CATEGORY_DEFINITIONS
    }

    uom_ids = {
        row["uom_id"]
        for row in UOM_DEFINITIONS
    }

    target_sub_category_ids = set(
        SUB_CATEGORY_PRODUCT_TARGETS
    )

    if set(sub_category_map) != (
        target_sub_category_ids
    ):
        raise ValueError(
            "Sub-category definitions and product targets "
            "do not cover the same IDs."
        )

    if set(PRODUCT_FAMILY_STEMS) != (
        target_sub_category_ids
    ):
        raise ValueError(
            "Product family definitions do not cover "
            "all product target sub-categories."
        )

    if set(PRODUCT_GRADE_OPTIONS) != (
        target_sub_category_ids
    ):
        raise ValueError(
            "Product grade definitions do not cover "
            "all product target sub-categories."
        )

    if set(PRODUCT_PACKAGE_GROUP) != (
        target_sub_category_ids
    ):
        raise ValueError(
            "Product package groups do not cover "
            "all product target sub-categories."
        )

    if set(CATEGORY_SKU_PREFIXES) != set(
        CATEGORY_PRODUCT_TARGETS
    ):
        raise ValueError(
            "SKU prefixes do not cover all product target categories."
        )

    if (
        sum(
            SUB_CATEGORY_PRODUCT_TARGETS.values()
        )
        != PRODUCT_MASTER_COUNT
    ):
        raise ValueError(
            "Sub-category product targets do not sum "
            f"to {PRODUCT_MASTER_COUNT}."
        )

    if (
        sum(
            CATEGORY_PRODUCT_TARGETS.values()
        )
        != PRODUCT_MASTER_COUNT
    ):
        raise ValueError(
            "Category product targets do not sum "
            f"to {PRODUCT_MASTER_COUNT}."
        )

    if (
        sum(
            PRODUCT_STATUS_TARGETS.values()
        )
        != PRODUCT_MASTER_COUNT
    ):
        raise ValueError(
            "Product status targets do not sum "
            f"to {PRODUCT_MASTER_COUNT}."
        )

    expected_brand_total = (
        len(BRAND_DEFINITIONS)
        * PRODUCT_BRAND_TARGET
    )

    if expected_brand_total != PRODUCT_MASTER_COUNT:
        raise ValueError(
            "Brand distribution target does not reconcile "
            f"to {PRODUCT_MASTER_COUNT}."
        )

    category_ids = set(
        CATEGORY_PRODUCT_TARGETS
    )

    if category_ids != set(
        PRODUCT_CATEGORY_NAMES
    ):
        raise ValueError(
            "Category product targets and category definitions "
            "do not cover the same IDs."
        )

    sub_category_totals_by_category = {
        category_id: 0
        for category_id in CATEGORY_PRODUCT_TARGETS
    }

    for sub_category_id, target in (
        SUB_CATEGORY_PRODUCT_TARGETS.items()
    ):
        category_id = sub_category_map[
            sub_category_id
        ]["category_id"]

        sub_category_totals_by_category[
            category_id
        ] += target

    if (
        sub_category_totals_by_category
        != CATEGORY_PRODUCT_TARGETS
    ):
        raise ValueError(
            "Sub-category product targets do not reconcile "
            "to category product targets."
        )

    allowed_statuses = set(
        PRODUCT_STATUS_TARGETS
    )

    category_counts = {
        category_id: 0
        for category_id in CATEGORY_PRODUCT_TARGETS
    }

    sub_category_counts = {
        sub_category_id: 0
        for sub_category_id in SUB_CATEGORY_PRODUCT_TARGETS
    }

    brand_counts = {
        brand_id: 0
        for brand_id in brand_ids
    }

    status_counts = {
        status: 0
        for status in allowed_statuses
    }

    for row in products:
        product_label = row["sku"]
        sub_category_id = row["sub_category_id"]

        if row["brand_id"] not in brand_ids:
            raise ValueError(
                f"Invalid brand_id {row['brand_id']} "
                f"for {product_label}"
            )

        if sub_category_id not in sub_category_map:
            raise ValueError(
                f"Invalid sub_category_id "
                f"{sub_category_id} for {product_label}"
            )

        if row["base_uom_id"] not in uom_ids:
            raise ValueError(
                f"Invalid base_uom_id "
                f"{row['base_uom_id']} for {product_label}"
            )

        package_group = PRODUCT_PACKAGE_GROUP[
            sub_category_id
        ]

        valid_packages = PRODUCT_PACKAGE_DEFINITIONS.get(
            package_group
        )

        if not valid_packages:
            raise ValueError(
                "No package definitions found for "
                f"package group {package_group} "
                f"assigned to {product_label}"
            )

        package = (
            row["pack_type"],
            row["pack_size"],
            row["base_quantity_per_pac"],
            row["base_uom_id"],
        )

        if package not in valid_packages:
            raise ValueError(
                "Invalid package for sub-category "
                f"{sub_category_id}: "
                f"{product_label}: {package}"
            )

        if row["base_quantity_per_pac"] <= 0:
            raise ValueError(
                "base_quantity_per_pac must be positive: "
                f"{product_label}"
            )

        valid_grades = PRODUCT_GRADE_OPTIONS[
            sub_category_id
        ]

        if row["viscosity_grade"] not in valid_grades:
            raise ValueError(
                "Invalid viscosity/grade value for "
                f"sub-category {sub_category_id}: "
                f"{product_label}: "
                f"{row['viscosity_grade']}"
            )

        if row["product_status"] not in allowed_statuses:
            raise ValueError(
                f"Invalid product_status for "
                f"{product_label}: "
                f"{row['product_status']}"
            )

        if not row["sku"].strip():
            raise ValueError(
                "SKU cannot be empty: "
                f"product_id={row['product_id']}"
            )

        if not row["product_name"].strip():
            raise ValueError(
                "Product name cannot be empty: "
                f"product_id={row['product_id']}"
            )

        expected_category_id = sub_category_map[
            sub_category_id
        ]["category_id"]

        category_counts[
            expected_category_id
        ] += 1

        sub_category_counts[
            sub_category_id
        ] += 1

        brand_counts[
            row["brand_id"]
        ] += 1

        status_counts[
            row["product_status"]
        ] += 1

    if category_counts != CATEGORY_PRODUCT_TARGETS:
        raise ValueError(
            "Category product distribution mismatch: "
            f"{category_counts}"
        )

    if (
        sub_category_counts
        != SUB_CATEGORY_PRODUCT_TARGETS
    ):
        raise ValueError(
            "Sub-category product distribution mismatch: "
            f"{sub_category_counts}"
        )

    expected_brand_counts = {
        brand_id: PRODUCT_BRAND_TARGET
        for brand_id in brand_ids
    }

    if brand_counts != expected_brand_counts:
        raise ValueError(
            "Brand product distribution mismatch: "
            f"{brand_counts}"
        )

    if status_counts != PRODUCT_STATUS_TARGETS:
        raise ValueError(
            "Product status distribution mismatch: "
            f"{status_counts}"
        )

    for category_id, target in (
        CATEGORY_PRODUCT_TARGETS.items()
    ):
        if category_id not in PRODUCT_CATEGORY_NAMES:
            raise ValueError(
                "Product target references unknown category: "
                f"{category_id}"
            )

        if target <= 0:
            raise ValueError(
                "Product target must be positive: "
                f"category {category_id}"
            )

    for sub_category_id, target in (
        SUB_CATEGORY_PRODUCT_TARGETS.items()
    ):
        if target <= 0:
            raise ValueError(
                "Product target must be positive: "
                f"sub-category {sub_category_id}"
            )

        if not PRODUCT_FAMILY_STEMS[
            sub_category_id
        ]:
            raise ValueError(
                "Product family definitions cannot be empty "
                f"for sub-category {sub_category_id}"
            )

        if not PRODUCT_GRADE_OPTIONS[
            sub_category_id
        ]:
            raise ValueError(
                "Product grade definitions cannot be empty "
                f"for sub-category {sub_category_id}"
            )

        package_group = PRODUCT_PACKAGE_GROUP[
            sub_category_id
        ]

        if package_group not in PRODUCT_PACKAGE_DEFINITIONS:
            raise ValueError(
                f"Unknown package group {package_group} "
                f"for sub-category {sub_category_id}"
            )


# ============================================================
# Warehouse validation
# ============================================================

def validate_warehouses(
    warehouses: list[dict],
) -> None:
    """Validate warehouse master data."""

    if not warehouses:
        raise ValueError(
            "Warehouse data is empty."
        )

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
        missing_fields = (
            required_fields - row.keys()
        )

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

    if len(warehouse_ids) != len(
        set(warehouse_ids)
    ):
        raise ValueError(
            "Duplicate warehouse_id found."
        )

    if len(warehouse_codes) != len(
        set(warehouse_codes)
    ):
        raise ValueError(
            "Duplicate warehouse_code found."
        )

    if len(warehouse_names) != len(
        set(warehouse_names)
    ):
        raise ValueError(
            "Duplicate warehouse_name found."
        )

    if warehouse_ids != sorted(
        warehouse_ids
    ):
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
        usable_capacity = warehouse[
            "usable_capacity_ltr"
        ]

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

            for sequence in range(
                1,
                count + 1,
            ):
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

                    zone_code = (
                        f"Z{zone_number:02d}"
                    )
                    aisle_no = (
                        f"A{aisle_number:02d}"
                    )
                    rack_no = (
                        f"R{rack_number:02d}"
                    )
                    bin_no = (
                        f"B{bin_number:02d}"
                    )

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

                    zone_code = (
                        f"P{zone_number:02d}"
                    )
                    aisle_no = (
                        f"A{aisle_number:02d}"
                    )
                    rack_no = (
                        f"R{rack_number:02d}"
                    )
                    bin_no = (
                        f"B{bin_number:02d}"
                    )

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
        raise ValueError(
            "Location data is empty."
        )

    warehouse_ids = {
        row["warehouse_id"]
        for row in warehouses
    }

    warehouse_capacity_map = {
        row["warehouse_id"]: row[
            "usable_capacity_ltr"
        ]
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
        missing_fields = (
            required_fields - row.keys()
        )

        if missing_fields:
            raise ValueError(
                f"Missing location fields: "
                f"{sorted(missing_fields)}"
            )

    location_ids = [
        row["location_id"]
        for row in locations
    ]

    if len(location_ids) != len(
        set(location_ids)
    ):
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

        warehouse_location_pairs.add(
            pair
        )

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
            if location["warehouse_id"]
            == warehouse_id
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

        usable_capacity = (
            warehouse_capacity_map[
                warehouse_id
            ]
        )

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
        referenced_category_ids
        - category_ids
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
        referenced_warehouse_ids
        - warehouse_ids
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

    output_file = (
        OUTPUT_DIR
        / filename
    )

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


def write_suppliers_csv(
    suppliers: list[dict],
) -> Path:
    """Write supplier master data."""

    return write_csv(
        rows=suppliers,
        filename="master_suppliers.csv",
        fieldnames=[
            "supplier_id",
            "supplier_code",
            "supplier_name",
            "supplier_type",
            "contact_person",
            "phone",
            "email",
            "gstin",
            "state_code",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal_code",
            "country",
            "lead_time_days",
            "payment_term_id",
            "supplier_status",
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


def write_products_csv(
    products: list[dict],
) -> Path:
    """Write product master data."""

    return write_csv(
        rows=products,
        filename="master_products.csv",
        fieldnames=[
            "product_id",
            "sku",
            "product_name",
            "brand_id",
            "sub_category_id",
            "base_uom_id",
            "pack_type",
            "pack_size",
            "base_quantity_per_pac",
            "viscosity_grade",
            "product_status",
            "created_date",
            "created_by",
            "updated_date",
            "updated_by",
        ],
    )


def write_product_suppliers_csv(
    product_suppliers: list[dict],
) -> Path:
    """Write product-supplier relationship data."""

    return write_csv(
        rows=product_suppliers,
        filename="master_product_suppliers.csv",
        fieldnames=[
            "product_supplier_id",
            "product_id",
            "supplier_id",
            "supplier_product_code",
            "supplier_product_name",
            "purchase_uom_id",
            "unit_purchase_price",
            "minimum_order_quantity",
            "lead_time_days",
            "is_primary_source",
            "relationship_status",
            "effective_from",
            "effective_to",
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
        suppliers = SUPPLIER_DEFINITIONS
        brands = BRAND_DEFINITIONS
        categories = CATEGORY_DEFINITIONS
        sub_categories = SUB_CATEGORY_DEFINITIONS
        warehouses = WAREHOUSE_DEFINITIONS

        products = generate_products()

        product_suppliers = generate_product_suppliers(
            products,
            suppliers,
        )

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

        validate_suppliers(
            suppliers,
            payment_terms,
        )
        print("Supplier validation: PASSED")

        validate_brands(brands)
        print("Brand validation: PASSED")

        validate_categories(categories)
        print("Category validation: PASSED")

        validate_sub_categories(
            sub_categories,
            categories,
        )
        print(
            "Sub-category validation: PASSED"
        )

        validate_products(products)
        print("Product validation: PASSED")

        validate_product_suppliers(
            product_suppliers,
            products,
            suppliers,
        )
        print(
            "Product-supplier validation: PASSED"
        )

        validate_warehouses(
            warehouses
        )
        print(
            "Warehouse validation: PASSED"
        )

        validate_locations(
            locations,
            warehouses,
        )
        print(
            "Location validation: PASSED"
        )

        validate_master_relationships(
            categories,
            sub_categories,
            warehouses,
            locations,
        )
        print(
            "Master relationship validation: PASSED"
        )

        # ----------------------------------------------------
        # CSV generation
        # ----------------------------------------------------

        uom_file = write_uoms_csv(
            uoms
        )

        payment_term_file = (
            write_payment_terms_csv(
                payment_terms
            )
        )

        supplier_file = write_suppliers_csv(
            suppliers
        )

        brand_file = write_brands_csv(
            brands
        )

        category_file = write_categories_csv(
            categories
        )

        sub_category_file = (
            write_sub_categories_csv(
                sub_categories
            )
        )

        product_file = write_products_csv(
            products
        )

        product_supplier_file = (
            write_product_suppliers_csv(
                product_suppliers
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

        print(
            f"Created: {uom_file}"
        )
        print(
            f"Rows: {len(uoms)}"
        )

        print(
            f"Created: {payment_term_file}"
        )
        print(
            f"Rows: {len(payment_terms)}"
        )

        print(
            f"Created: {supplier_file}"
        )
        print(
            f"Rows: {len(suppliers)}"
        )

        print(
            f"Created: {brand_file}"
        )
        print(
            f"Rows: {len(brands)}"
        )

        print(
            f"Created: {category_file}"
        )
        print(
            f"Rows: {len(categories)}"
        )

        print(
            f"Created: {sub_category_file}"
        )
        print(
            f"Rows: {len(sub_categories)}"
        )

        print(
            f"Created: {product_file}"
        )
        print(
            f"Rows: {len(products)}"
        )

        print(
            f"Created: {product_supplier_file}"
        )
        print(
            f"Rows: {len(product_suppliers)}"
        )

        print(
            f"Created: {warehouse_file}"
        )
        print(
            f"Rows: {len(warehouses)}"
        )

        print(
            f"Created: {location_file}"
        )
        print(
            f"Rows: {len(locations)}"
        )

    except (
        OSError,
        ValueError,
    ) as error:
        print(
            f"Generation failed: {error}"
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()
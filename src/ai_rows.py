import random
from typing import Callable, Dict, List

from generators import (
    TYPES_TO_GENERATORS,
    customer_plan,
    fake,
    product_attributes,
    product_category,
    product_name,
    review_sample,
    support_priority,
    support_ticket_sample,
    target_language,
)

SUPPORT_CATEGORIES = ["Billing", "Bug", "Feature Request", "Account Access", "Data Import", "Performance", "Other"]
SENTIMENTS = ["Positive", "Neutral", "Negative", "Mixed"]
REVIEW_TOPICS = ["Pricing", "Support", "Product Quality", "Delivery", "Usability", "Features", "Other"]
ICP_FITS = ["Strong", "Medium", "Poor", "Unclear"]
SCORE_BANDS = ["High", "Medium", "Low"]
RESEARCH_OUTPUT_TYPES = ["Company Summary", "ICP Fit", "Pricing Evidence", "Hiring Signal", "Technology Mention", "Competitor Mention"]
PAGE_TYPES = ["Homepage", "Product Page", "Pricing Page", "Case Study", "Blog Post", "Directory Listing"]
TRANSLATION_TARGET_LANGUAGES = ["French", "Spanish", "German", "Italian", "Portuguese", "Dutch", "Japanese", "Swedish"]

REAL_COMPANY_PROFILES = [
    {
        "name": "OpenAI",
        "domain": "openai.com",
        "website": "https://openai.com/",
        "country": "United States",
        "industry": "Artificial Intelligence",
        "description": "OpenAI builds AI models and products including ChatGPT, API models, and tools for developers and businesses.",
        "pricing_url": "https://openai.com/api/pricing/",
        "careers_url": "https://openai.com/careers/",
    },
    {
        "name": "Stripe",
        "domain": "stripe.com",
        "website": "https://stripe.com/",
        "country": "United States",
        "industry": "Payments",
        "description": "Stripe provides payment infrastructure for online businesses, marketplaces, subscriptions, and embedded finance products.",
        "pricing_url": "https://stripe.com/pricing",
        "careers_url": "https://stripe.com/jobs",
    },
    {
        "name": "Shopify",
        "domain": "shopify.com",
        "website": "https://www.shopify.com/",
        "country": "Canada",
        "industry": "Ecommerce",
        "description": "Shopify provides commerce software for online stores, point of sale, payments, fulfillment, and merchant growth.",
        "pricing_url": "https://www.shopify.com/pricing",
        "careers_url": "https://www.shopify.com/careers",
    },
    {
        "name": "HubSpot",
        "domain": "hubspot.com",
        "website": "https://www.hubspot.com/",
        "country": "United States",
        "industry": "CRM Software",
        "description": "HubSpot offers CRM, marketing, sales, service, content, operations, and commerce software for growing businesses.",
        "pricing_url": "https://www.hubspot.com/pricing",
        "careers_url": "https://www.hubspot.com/careers",
    },
    {
        "name": "Salesforce",
        "domain": "salesforce.com",
        "website": "https://www.salesforce.com/",
        "country": "United States",
        "industry": "CRM Software",
        "description": "Salesforce provides cloud software for sales, service, marketing, commerce, analytics, integration, and AI workflows.",
        "pricing_url": "https://www.salesforce.com/products/sales-cloud/pricing/",
        "careers_url": "https://www.salesforce.com/company/careers/",
    },
    {
        "name": "Atlassian",
        "domain": "atlassian.com",
        "website": "https://www.atlassian.com/",
        "country": "Australia",
        "industry": "Collaboration Software",
        "description": "Atlassian builds collaboration and software development tools including Jira, Confluence, Trello, and Bitbucket.",
        "pricing_url": "https://www.atlassian.com/software/jira/pricing",
        "careers_url": "https://www.atlassian.com/company/careers",
    },
    {
        "name": "Notion",
        "domain": "notion.so",
        "website": "https://www.notion.so/",
        "country": "United States",
        "industry": "Productivity Software",
        "description": "Notion provides a connected workspace for documents, wikis, projects, notes, databases, and AI-assisted work.",
        "pricing_url": "https://www.notion.so/pricing",
        "careers_url": "https://www.notion.so/careers",
    },
    {
        "name": "Datadog",
        "domain": "datadoghq.com",
        "website": "https://www.datadoghq.com/",
        "country": "United States",
        "industry": "Observability",
        "description": "Datadog provides monitoring, security, logging, tracing, infrastructure observability, and application performance tools.",
        "pricing_url": "https://www.datadoghq.com/pricing/",
        "careers_url": "https://www.datadoghq.com/careers/",
    },
    {
        "name": "Cloudflare",
        "domain": "cloudflare.com",
        "website": "https://www.cloudflare.com/",
        "country": "United States",
        "industry": "Internet Infrastructure",
        "description": "Cloudflare provides CDN, DNS, DDoS protection, Zero Trust security, developer platform, and network services.",
        "pricing_url": "https://www.cloudflare.com/plans/",
        "careers_url": "https://www.cloudflare.com/careers/",
    },
    {
        "name": "Twilio",
        "domain": "twilio.com",
        "website": "https://www.twilio.com/",
        "country": "United States",
        "industry": "Customer Engagement",
        "description": "Twilio provides communications APIs, messaging, voice, email, authentication, customer data, and engagement tools.",
        "pricing_url": "https://www.twilio.com/en-us/pricing",
        "careers_url": "https://www.twilio.com/en-us/company/jobs",
    },
]

REAL_WEB_PAGES = [
    {
        "url": "https://stripe.com/pricing",
        "title": "Stripe pricing",
        "text": "Stripe publishes pricing for online card payments, in-person payments, billing, invoicing, fraud prevention, and other payment products. The page is useful for extracting plan names, transaction fees, and product-specific pricing notes.",
        "task": "Extract product names and pricing signals from the page text.",
    },
    {
        "url": "https://www.shopify.com/pricing",
        "title": "Shopify pricing",
        "text": "Shopify lists commerce plans for merchants that want to sell online, in person, and across channels. The page is useful for comparing plan names, monthly prices, and included commerce features.",
        "task": "Extract plan names, prices, and commerce features from the page text.",
    },
    {
        "url": "https://www.hubspot.com/pricing",
        "title": "HubSpot pricing",
        "text": "HubSpot publishes pricing for its customer platform, including marketing, sales, service, content, operations, and commerce products. The page is useful for extracting product hubs, editions, and pricing structure.",
        "task": "Extract software products, editions, and pricing structure from the page text.",
    },
    {
        "url": "https://www.atlassian.com/software/jira",
        "title": "Jira project management software",
        "text": "Atlassian presents Jira as software for planning, tracking, and managing work across software, IT, and business teams. The page is useful for extracting product positioning, target users, and core use cases.",
        "task": "Extract the product name, target users, and main use cases from the page text.",
    },
    {
        "url": "https://www.notion.so/product",
        "title": "Notion product",
        "text": "Notion describes its workspace as a place for docs, wikis, projects, databases, and AI-assisted work. The page is useful for extracting product categories, collaboration features, and workflow examples.",
        "task": "Extract collaboration features and workflow categories from the page text.",
    },
    {
        "url": "https://www.datadoghq.com/product/",
        "title": "Datadog products",
        "text": "Datadog groups products around infrastructure monitoring, logs, APM, security, digital experience, software delivery, and cloud cost management. The page is useful for extracting product families and observability use cases.",
        "task": "Extract product families and observability use cases from the page text.",
    },
    {
        "url": "https://www.cloudflare.com/application-services/",
        "title": "Cloudflare application services",
        "text": "Cloudflare describes application services for performance, security, DDoS protection, bot management, and traffic acceleration. The page is useful for extracting security capabilities and infrastructure benefits.",
        "task": "Extract security capabilities and infrastructure benefits from the page text.",
    },
    {
        "url": "https://www.twilio.com/en-us/messaging",
        "title": "Twilio messaging",
        "text": "Twilio presents messaging products for SMS, MMS, WhatsApp, conversational messaging, verification, and customer engagement workflows. The page is useful for extracting communication channels and API use cases.",
        "task": "Extract communication channels and API use cases from the page text.",
    },
]

COUNTRY_ISO_CODES = {
    "Australia": "AU",
    "Canada": "CA",
    "United States": "US",
}

MESSY_CRM_SOURCE_SYSTEMS = [
    "Salesforce import 2018",
    "HubSpot sync",
    "Pipedrive migration",
    "Manual entry",
    "CSV upload",
    "Legacy CRM",
    "Event list",
    "Partner spreadsheet",
    "Website form",
    "Unknown",
]

MESSY_LIFECYCLE_STAGES = [
    "lead",
    "Lead",
    "LEAD",
    "prospect",
    "customer",
    "Customer - Active",
    "churned",
    "Closed Won",
    "n/a",
    "",
]

MESSY_EMPLOYEE_COUNTS = [
    "unknown",
    "n/a",
    "1-10",
    "11-50",
    "51-200",
    "201-500",
    "500+",
    "1,000+",
]

MESSY_REVENUE_VALUES = [
    "",
    "unknown",
    "n/a",
    "$1M-$5M",
    "$10M+",
    "€2.5m",
    "5000000",
    "12,000,000 USD",
    "4.2M",
    "approx. 900k",
    "Confidential",
    "USD 250000",
]

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

MESSY_LEAD_SCORES = [
    "",
    "unknown",
    "hot",
    "warm",
    "cold",
    "A",
    "B+",
    "high intent",
    "needs review",
]


def messy_date_value() -> str:
    year = random.randrange(2015, 2027)
    month = random.randrange(1, 13)
    day = random.randrange(1, 29)
    hour = random.randrange(0, 24)
    minute = random.randrange(0, 60)
    return random.choice([
        f"{year}-{month:02d}-{day:02d}",
        f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00Z",
        f"{month:02d}/{day:02d}/{year}",
        f"{day:02d}/{month:02d}/{year}",
        f"{MONTH_NAMES[month - 1]} {day}, {year}",
        f"{day} {MONTH_NAMES[month - 1]} {str(year)[2:]}",
        f"Q{((month - 1) // 3) + 1} {year}",
        str(random.randrange(42005, 47000)),
        "last contacted Q4",
        "",
    ])


def messy_employee_count() -> str:
    return random.choice(MESSY_EMPLOYEE_COUNTS + [
        str(TYPES_TO_GENERATORS["company_number_employees"]()),
        f"~{random.randrange(50, 5000)}",
        f"{random.randrange(10, 200)} employees",
        f"{random.randrange(1, 20)}k",
    ])


def messy_lead_score() -> str:
    score = random.randrange(0, 101)
    return random.choice(MESSY_LEAD_SCORES + [
        str(score),
        f"{score}/100",
        f"{score}%",
        f"{score} points",
        f"{random.randrange(1, 6)} stars",
    ])


def messy_open_opportunities() -> str:
    return random.choice([
        "",
        "none",
        "0",
        str(random.randrange(1, 12)),
        f"{random.randrange(1, 8)} open",
        f"{random.randrange(1, 5)} deals",
        "multiple",
    ])

TRANSLATION_PRODUCTS = [
    {
        "category": "Kitchen Appliances",
        "adjectives": ["Compact", "Smart", "Stainless Steel", "Family-Size", "Quiet"],
        "products": ["Air Fryer", "Espresso Machine", "Rice Cooker", "Hand Blender", "Food Processor"],
        "materials": ["brushed steel", "heat-resistant glass", "BPA-free plastic", "ceramic coating"],
        "audiences": ["small kitchens", "busy families", "meal prep", "home cooks"],
        "benefits": ["cuts cooking time", "keeps cleanup simple", "uses less counter space", "delivers consistent results"],
        "features": ["dishwasher-safe parts", "digital timer", "cool-touch handle", "preset cooking modes"],
    },
    {
        "category": "Fitness Equipment",
        "adjectives": ["Adjustable", "Foldable", "Low-Impact", "Heavy-Duty", "Travel-Ready"],
        "products": ["Resistance Band Set", "Yoga Mat", "Exercise Bike", "Foam Roller", "Dumbbell Kit"],
        "materials": ["natural rubber", "powder-coated steel", "high-density foam", "textured silicone"],
        "audiences": ["home workouts", "small apartments", "recovery sessions", "daily training"],
        "benefits": ["supports full-body training", "stores easily", "protects joints", "helps improve mobility"],
        "features": ["non-slip grip", "quick adjustment dial", "carry strap", "sweat-resistant surface"],
    },
    {
        "category": "Home Office",
        "adjectives": ["Ergonomic", "Minimalist", "Height-Adjustable", "Cable-Friendly", "Compact"],
        "products": ["Laptop Stand", "Desk Lamp", "Monitor Arm", "Keyboard Tray", "Standing Desk Converter"],
        "materials": ["anodized aluminum", "solid beechwood", "recycled ABS", "matte steel"],
        "audiences": ["remote work", "shared desks", "student rooms", "focused writing sessions"],
        "benefits": ["reduces desk clutter", "improves screen position", "keeps cables tidy", "fits tight workspaces"],
        "features": ["tool-free setup", "warm and cool light modes", "weighted base", "smooth height adjustment"],
    },
    {
        "category": "Outdoor Gear",
        "adjectives": ["Weatherproof", "Lightweight", "Trail-Ready", "Insulated", "Packable"],
        "products": ["Hiking Backpack", "Camping Lantern", "Rain Jacket", "Water Bottle", "Travel Towel"],
        "materials": ["ripstop nylon", "double-wall stainless steel", "recycled polyester", "soft microfiber"],
        "audiences": ["weekend hikes", "camping trips", "daily commuting", "travel packing"],
        "benefits": ["keeps essentials dry", "packs down small", "stays comfortable for long days", "handles changing weather"],
        "features": ["sealed seams", "side-access pocket", "USB-C rechargeable battery", "leakproof lid"],
    },
    {
        "category": "Baby Products",
        "adjectives": ["Soft", "Organic", "Easy-Clean", "Adjustable", "Lightweight"],
        "products": ["Baby Blanket", "Changing Mat", "Silicone Bib", "Bottle Warmer", "Sleep Sack"],
        "materials": ["organic cotton", "food-grade silicone", "quilted microfiber", "soft bamboo viscose"],
        "audiences": ["new parents", "nursery routines", "travel days", "night feeds"],
        "benefits": ["feels gentle on skin", "cleans quickly", "saves space in a diaper bag", "helps keep routines simple"],
        "features": ["machine-washable fabric", "snap closure", "roll-up design", "temperature indicator"],
    },
    {
        "category": "Pet Supplies",
        "adjectives": ["Washable", "Chew-Resistant", "Travel-Friendly", "Calming", "Adjustable"],
        "products": ["Dog Harness", "Cat Bed", "Treat Pouch", "Pet Water Bottle", "Grooming Brush"],
        "materials": ["breathable mesh", "soft fleece", "stainless steel", "recycled nylon"],
        "audiences": ["daily walks", "training sessions", "road trips", "small pets"],
        "benefits": ["keeps pets comfortable", "makes cleanup faster", "helps organize essentials", "reduces pulling on walks"],
        "features": ["reflective trim", "quick-release buckle", "removable liner", "one-hand dispenser"],
    },
    {
        "category": "Beauty & Personal Care",
        "adjectives": ["Gentle", "Hydrating", "Fragrance-Free", "Travel-Size", "Fast-Absorbing"],
        "products": ["Face Cleanser", "Body Lotion", "Hair Mask", "Hand Cream", "Sunscreen Stick"],
        "materials": ["aloe vera", "shea butter", "ceramide blend", "plant-based oils"],
        "audiences": ["daily skincare", "sensitive skin", "gym bags", "travel kits"],
        "benefits": ["absorbs without a greasy feel", "helps skin feel soft", "fits easily in a pouch", "works for morning routines"],
        "features": ["dermatologist-tested formula", "flip-top cap", "recyclable tube", "non-sticky finish"],
    },
    {
        "category": "Consumer Electronics",
        "adjectives": ["Wireless", "Portable", "Noise-Reducing", "Fast-Charging", "Compact"],
        "products": ["Bluetooth Speaker", "USB-C Charger", "Wireless Earbuds", "Power Bank", "Webcam"],
        "materials": ["aluminum shell", "braided cable", "soft-touch plastic", "scratch-resistant glass"],
        "audiences": ["video calls", "travel days", "desk setups", "commuting"],
        "benefits": ["connects quickly", "saves charging time", "fits in a small bag", "keeps audio clear"],
        "features": ["LED battery display", "dual-device pairing", "foldable stand", "water-resistant casing"],
    },
]

TRANSLATION_PRODUCT_ITEMS = [
    {
        "category": "Kitchen Appliances",
        "adjectives": ["Compact", "Smart", "Family-Size", "Quiet"],
        "product": "Air Fryer",
        "materials": ["ceramic non-stick basket", "stainless steel drawer"],
        "audiences": ["small kitchens", "busy families", "weeknight meals"],
        "benefits": ["cooks frozen snacks with less oil", "keeps cleanup simple", "reheats leftovers without making them soggy"],
        "features": ["dishwasher-safe basket", "digital timer", "preset cooking modes"],
    },
    {
        "category": "Kitchen Appliances",
        "adjectives": ["Stainless Steel", "Compact", "Barista-Style"],
        "product": "Espresso Machine",
        "materials": ["brushed steel housing", "removable water tank"],
        "audiences": ["morning coffee routines", "small kitchens", "home baristas"],
        "benefits": ["pulls a rich shot without taking much counter space", "warms up quickly", "keeps milk steaming simple"],
        "features": ["15-bar pump", "steam wand", "removable drip tray"],
    },
    {
        "category": "Fitness Equipment",
        "adjectives": ["Adjustable", "Foldable", "Heavy-Duty"],
        "product": "Exercise Bike",
        "materials": ["powder-coated steel frame", "padded seat"],
        "audiences": ["home workouts", "small apartments", "low-impact cardio"],
        "benefits": ["supports steady cardio training", "stores neatly after a session", "keeps rides quiet enough for shared spaces"],
        "features": ["magnetic resistance", "quick adjustment dial", "LCD training display"],
    },
    {
        "category": "Fitness Equipment",
        "adjectives": ["Non-Slip", "Cushioned", "Travel-Ready"],
        "product": "Yoga Mat",
        "materials": ["natural rubber surface", "textured foam base"],
        "audiences": ["daily stretching", "studio classes", "home workouts"],
        "benefits": ["adds grip during poses", "cushions knees and wrists", "rolls tightly for easy storage"],
        "features": ["non-slip texture", "carry strap", "closed-cell surface"],
    },
    {
        "category": "Home Office",
        "adjectives": ["Ergonomic", "Minimalist", "Height-Adjustable"],
        "product": "Laptop Stand",
        "materials": ["anodized aluminum frame", "silicone grip pads"],
        "audiences": ["remote work", "shared desks", "student rooms"],
        "benefits": ["raises the screen to a more comfortable height", "reduces desk clutter", "folds flat for travel"],
        "features": ["tool-free setup", "ventilated platform", "foldable design"],
    },
    {
        "category": "Home Office",
        "adjectives": ["Dimmable", "Minimalist", "USB-C"],
        "product": "Desk Lamp",
        "materials": ["matte steel arm", "frosted LED panel"],
        "audiences": ["focused writing sessions", "late-night study", "compact workspaces"],
        "benefits": ["softens glare on the desk", "switches from warm to cool light", "keeps a phone charged while working"],
        "features": ["warm and cool light modes", "touch dimmer", "USB-C charging port"],
    },
    {
        "category": "Outdoor Gear",
        "adjectives": ["Weatherproof", "Lightweight", "Trail-Ready"],
        "product": "Hiking Backpack",
        "materials": ["ripstop nylon shell", "breathable mesh back panel"],
        "audiences": ["weekend hikes", "day trips", "daily commuting"],
        "benefits": ["keeps essentials organized", "sits comfortably on long walks", "protects gear during light rain"],
        "features": ["sealed front pocket", "side-access bottle sleeve", "padded shoulder straps"],
    },
    {
        "category": "Outdoor Gear",
        "adjectives": ["Insulated", "Leakproof", "Trail-Ready"],
        "product": "Water Bottle",
        "materials": ["double-wall stainless steel body", "BPA-free lid"],
        "audiences": ["gym bags", "hiking trails", "daily commuting"],
        "benefits": ["keeps drinks cold for hours", "prevents leaks in a bag", "fits most car cup holders"],
        "features": ["leakproof lid", "wide-mouth opening", "powder-coated finish"],
    },
    {
        "category": "Baby Products",
        "adjectives": ["Soft", "Organic", "Lightweight"],
        "product": "Baby Blanket",
        "materials": ["organic cotton muslin", "soft stitched border"],
        "audiences": ["new parents", "stroller naps", "nursery routines"],
        "benefits": ["feels gentle on skin", "layers easily without bulk", "washes well after daily use"],
        "features": ["machine-washable fabric", "breathable weave", "generous square size"],
    },
    {
        "category": "Baby Products",
        "adjectives": ["Easy-Clean", "Adjustable", "Soft"],
        "product": "Silicone Bib",
        "materials": ["food-grade silicone", "soft adjustable neck strap"],
        "audiences": ["first meals", "travel days", "busy kitchens"],
        "benefits": ["catches crumbs before they reach clothing", "wipes clean in seconds", "rolls up inside a diaper bag"],
        "features": ["deep front pocket", "adjustable closure", "dishwasher-safe material"],
    },
    {
        "category": "Pet Supplies",
        "adjectives": ["Adjustable", "Reflective", "Comfort-Fit"],
        "product": "Dog Harness",
        "materials": ["breathable mesh panels", "recycled nylon straps"],
        "audiences": ["daily walks", "training sessions", "road trips"],
        "benefits": ["reduces pulling on walks", "keeps pressure away from the neck", "dries quickly after wet weather"],
        "features": ["reflective trim", "quick-release buckle", "front and back leash clips"],
    },
    {
        "category": "Pet Supplies",
        "adjectives": ["Washable", "Calming", "Soft"],
        "product": "Cat Bed",
        "materials": ["soft fleece lining", "supportive foam base"],
        "audiences": ["small pets", "quiet corners", "apartment living"],
        "benefits": ["creates a warm resting spot", "keeps loose fur in one place", "fits neatly beside a sofa"],
        "features": ["removable liner", "non-slip bottom", "machine-washable cover"],
    },
    {
        "category": "Beauty & Personal Care",
        "adjectives": ["Gentle", "Fragrance-Free", "Daily"],
        "product": "Face Cleanser",
        "materials": ["aloe vera formula", "ceramide blend"],
        "audiences": ["daily skincare", "sensitive skin", "morning routines"],
        "benefits": ["removes buildup without a tight feeling", "rinses clean with warm water", "prepares skin for moisturizer"],
        "features": ["dermatologist-tested formula", "flip-top cap", "non-stripping texture"],
    },
    {
        "category": "Beauty & Personal Care",
        "adjectives": ["Hydrating", "Fast-Absorbing", "Travel-Size"],
        "product": "Hand Cream",
        "materials": ["shea butter blend", "plant-based oils"],
        "audiences": ["dry hands", "desk drawers", "travel kits"],
        "benefits": ["absorbs without a greasy feel", "softens rough patches", "fits easily in a small pouch"],
        "features": ["recyclable tube", "non-sticky finish", "lightweight texture"],
    },
    {
        "category": "Consumer Electronics",
        "adjectives": ["Wireless", "Portable", "Water-Resistant"],
        "product": "Bluetooth Speaker",
        "materials": ["rubberized outer shell", "woven speaker grille"],
        "audiences": ["picnics", "desk setups", "weekend travel"],
        "benefits": ["connects quickly to a phone", "keeps audio clear at low and medium volume", "slides easily into a backpack"],
        "features": ["dual-device pairing", "USB-C charging", "water-resistant casing"],
    },
    {
        "category": "Consumer Electronics",
        "adjectives": ["Fast-Charging", "Compact", "Travel-Ready"],
        "product": "Power Bank",
        "materials": ["aluminum shell", "scratch-resistant display"],
        "audiences": ["commuting", "travel days", "conference bags"],
        "benefits": ["charges a phone during long days", "shows remaining battery at a glance", "fits in a jacket pocket"],
        "features": ["LED battery display", "USB-C input and output", "compact 10,000 mAh body"],
    },
]

BRAND_PREFIXES = ["Northline", "CasaPro", "UrbanNest", "Luma", "EverTrail", "Milo & Co", "Aster", "BluePeak"]
TRANSLATION_TONES = [
    "Use natural ecommerce language. Keep the copy clear and customer friendly.",
    "Translate for a product listing. Keep measurements, model names, and brand names unchanged.",
    "Use a concise retail tone. Avoid adding claims that are not in the source text.",
    "Translate for an online store. Keep the benefit-led structure and preserve line breaks.",
]
GLOSSARY_TERMS = [
    "non-slip grip; leakproof lid; USB-C",
    "organic cotton; snap closure; machine-washable",
    "preset modes; dishwasher-safe; cool-touch",
    "height-adjustable; cable tray; tool-free",
    "water-resistant; sealed seams; side-access pocket",
    "dermatologist-tested; fragrance-free; recyclable tube",
    "dual-device pairing; fast-charging; LED display",
]

PRODUCT_MEASUREMENTS = {
    "Air Fryer": ["5 L", "6 qt", "1,500 W"],
    "Espresso Machine": ["15 bar", "1.2 L", "1,350 W"],
    "Exercise Bike": ["120 kg max load", "18 kg flywheel", "110 x 50 cm"],
    "Yoga Mat": ["183 x 61 cm", "6 mm", "1.2 kg"],
    "Laptop Stand": ["13-16 in", "1.1 kg", "26 cm width"],
    "Desk Lamp": ["15 W", "45 cm arm", "1.8 m cable"],
    "Hiking Backpack": ["24 L", "48 cm height", "900 g"],
    "Water Bottle": ["500 ml", "750 ml", "24 oz"],
    "Baby Blanket": ["120 x 120 cm", "47 x 47 in", "300 g"],
    "Silicone Bib": ["one size", "25 x 30 cm", "90 g"],
    "Dog Harness": ["Size M", "45-60 cm chest", "120 g"],
    "Cat Bed": ["45 cm diameter", "60 cm diameter", "800 g"],
    "Face Cleanser": ["150 ml", "5 fl oz", "100 ml"],
    "Hand Cream": ["75 ml", "2.5 fl oz", "50 ml"],
    "Bluetooth Speaker": ["10 W", "12-hour battery", "450 g"],
    "Power Bank": ["10,000 mAh", "20 W", "180 g"],
}


def product_measurement(product: str) -> str:
    return random.choice(PRODUCT_MEASUREMENTS[product])


def support_ticket_row() -> List[str]:
    subject, text = support_ticket_sample()
    return [
        TYPES_TO_GENERATORS["id"](),
        customer_plan(),
        subject,
        text,
        support_priority(),
    ]


def customer_review_row() -> List[str]:
    review, score = review_sample()
    return [
        TYPES_TO_GENERATORS["id"](),
        product_name(),
        score,
        review,
    ]


def messy_company_data_row() -> List[str]:
    company = random.choice(REAL_COMPANY_PROFILES)
    clean_name = company["name"]
    suffix = random.choice([" Inc.", " LLC", " ltd", " GmbH", " SAS", " PLC", "  "])
    raw_name = random.choice([
        clean_name.upper(),
        clean_name.lower(),
        f"  {clean_name}{suffix}",
        f"The {clean_name}",
        f"{clean_name}, {suffix.strip()}",
        f"{clean_name} - old account",
        f"{clean_name} ({random.choice(['HQ', 'US', 'EMEA', 'old CRM'])})",
    ])
    domain = company["domain"]
    website = random.choice([
        domain,
        f"www.{domain}",
        company["website"],
        company["website"].rstrip("/"),
        f"http://{domain}",
        f"https://www.{domain}/",
        f"https://{domain}/pricing",
        f"https://{domain}/about-us",
        f"https://{domain}/contact?utm_source=crm",
        f" {domain.upper()} ",
    ])
    country = random.choice([
        company["country"],
        COUNTRY_ISO_CODES[company["country"]],
        company["country"].upper(),
        company["country"].lower(),
        f" {COUNTRY_ISO_CODES[company['country']]} ",
        "",
    ])
    source_system = random.choice(MESSY_CRM_SOURCE_SYSTEMS)
    owner = random.choice([
        TYPES_TO_GENERATORS["full_name"](),
        TYPES_TO_GENERATORS["email"](),
        "unassigned",
        "sales-admin",
        "",
    ])
    created_date = messy_date_value()
    last_activity = messy_date_value()
    renewal_date = messy_date_value()
    lifecycle_stage = random.choice(MESSY_LIFECYCLE_STAGES)
    employee_count = messy_employee_count()
    revenue = random.choice(MESSY_REVENUE_VALUES)
    lead_score = messy_lead_score()
    open_opportunities = messy_open_opportunities()
    notes = random.choice([
        f"Imported from {source_system}; verify website before enrichment.",
        f"Possible duplicate of {clean_name}; owner changed during migration.",
        f"Sales note: talked to procurement, country field may be outdated.",
        f"Old CRM row. Website copied from email signature. Stage={lifecycle_stage or 'blank'}.",
        f"Manual update requested by {owner or 'unknown owner'}; keep original company name for audit.",
    ])
    return [
        TYPES_TO_GENERATORS["id"](),
        raw_name,
        website,
        company["description"],
        country,
        source_system,
        owner,
        created_date,
        last_activity,
        renewal_date,
        lifecycle_stage,
        employee_count,
        revenue,
        lead_score,
        open_opportunities,
        notes,
    ]


def product_catalog_ai_row() -> List[str]:
    category = product_category()
    title = product_name()
    attributes = product_attributes()
    description = f"{title} by {fake.company()} is a {attributes} product for customers shopping in {category}."
    return [
        TYPES_TO_GENERATORS["id"](),
        title,
        description,
        fake.company(),
        category,
        target_language(),
    ]


def product_translation_ai_row() -> List[str]:
    product_item = random.choice(TRANSLATION_PRODUCT_ITEMS)
    adjective = random.choice(product_item["adjectives"])
    product = product_item["product"]
    brand = random.choice(BRAND_PREFIXES)
    material = random.choice(product_item["materials"])
    audience = random.choice(product_item["audiences"])
    benefit = random.choice(product_item["benefits"])
    secondary_benefit = random.choice([item for item in product_item["benefits"] if item != benefit])
    features = random.sample(product_item["features"], k=3)
    target_language = random.choice(TRANSLATION_TARGET_LANGUAGES)
    product_name = f"{brand} {adjective} {product}"
    model = f"Model {random.choice(['A12', 'Pro 4', 'Lite 2', 'X100'])}"
    measurement = product_measurement(product)
    description = (
        f"The {product_name} is designed for {audience}. "
        f"It is made with {material} and {benefit}, so customers can use it every day without extra effort. "
        f"The {model} version uses a {measurement} format for consistent catalog data. "
        f"The product also {secondary_benefit}, making it a practical choice for repeat purchases and localized ecommerce listings."
    )
    bullets = " | ".join([
        f"{features[0]} for everyday use",
        f"{features[1]} for simple setup with {model}",
        f"{features[2]} for a better customer experience",
    ])
    seo_title = f"{product_name} for {audience.title()}"
    do_not_translate = f"{brand}; {product_name}; {model}; {measurement}"

    return [
        TYPES_TO_GENERATORS["id"](),
        product_name,
        product_item["category"],
        "English",
        target_language,
        description,
        bullets,
        seo_title,
        random.choice(TRANSLATION_TONES),
        f"{features[0]}; {features[1]}; {material}",
        do_not_translate,
    ]


def lead_scoring_ai_row() -> List[str]:
    company = random.choice(REAL_COMPANY_PROFILES)
    notes = f"{company['name']} works in {company['industry']}. Recent notes mention {random.choice(['growth hiring', 'budget review', 'new software rollout', 'unclear buying intent'])}."
    return [
        TYPES_TO_GENERATORS["id"](),
        TYPES_TO_GENERATORS["first_name"](),
        TYPES_TO_GENERATORS["last_name"](),
        TYPES_TO_GENERATORS["job"](),
        company["name"],
        company["website"],
        company["industry"],
        notes,
    ]


def web_page_extraction_ai_row() -> List[str]:
    page = random.choice(REAL_WEB_PAGES)
    return [
        TYPES_TO_GENERATORS["id"](),
        page["url"],
        page["title"],
        page["text"],
        page["task"],
    ]


def research_questions_ai_row() -> List[str]:
    company = random.choice(REAL_COMPANY_PROFILES)
    question, source_url = random.choice([
        ("Summarize the company in one sentence using the official website.", company["website"]),
        ("Find whether this company has a public pricing page and return the URL.", company["pricing_url"]),
        ("Find the official careers page and summarize what teams it hires for.", company["careers_url"]),
        ("Identify the main product categories described on the official website.", company["website"]),
        ("Find one signal that the company sells to businesses.", company["website"]),
    ])
    return [
        TYPES_TO_GENERATORS["id"](),
        company["name"],
        company["domain"],
        question,
        source_url,
    ]


AI_ROW_FACTORIES: Dict[str, Callable[[], List[str]]] = {
    "support_tickets": support_ticket_row,
    "customer_reviews": customer_review_row,
    "messy_company_data": messy_company_data_row,
    "product_catalog_ai": product_catalog_ai_row,
    "product_translation_ai": product_translation_ai_row,
    "lead_scoring_ai": lead_scoring_ai_row,
    "web_page_extraction_ai": web_page_extraction_ai_row,
    "research_questions_ai": research_questions_ai_row,
}

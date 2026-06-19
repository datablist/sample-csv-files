import random
import string
import json
import secrets
from pathlib import Path
from faker import Faker

fake = Faker(use_weighting=False)
product_names_json = Path(__file__).parent / "data/product_names.json"
with open(product_names_json, "r") as f:
    product_names = json.load(f)

def random_string(string_length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(string_length))

def number():
    return random.randrange(-1000, 1000)

def small_positive_integer():
    return random.randrange(1, 100)

def positive_integer():
    return random.randrange(10, 1000)

def number_employees():
    return random.randrange(1, 10000)

def long_text():
    return fake.paragraph(nb_sentences=1)


_very_long_text_cache = []
def very_long_text() -> str:
    if not _very_long_text_cache:
        for _ in range(20):
            _very_long_text_cache.append(fake.paragraph(nb_sentences=30))
    return random.choice(_very_long_text_cache)

def username():
    return fake.user_name()

def full_name():
    return "{} {}".format(fake.first_name(), fake.last_name())

def sex():
    return random.choice(['Male', 'Female'])

def brand():
    return fake.company()

def department():
    # https://www.quora.com/What-are-the-main-departments-in-a-company
    return random.choice([
        "Marketing & Proposals Department",
        "sales Department",
        "Project Department",
        "Designing Department",
        "Production Department",
        "Maintenance Department",
        "Store Department",
        "Procurement Department",
        "Quality Department",
        "Inspection department",
        "Packaging Department",
        "Finance Department",
        "Dispatch Department",
        "Account Department",
        "Research & Development Department",
        "Information Technology Department",
        "Human Resource Department",
        "Security Department",
        "Administration department"
    ])

def deal_stage():
    values = [
        "New Lead",
        "Contacted",
        "Qualified",
        "Proposal Sent",
        "Negotiation",
        "Closed Won",
        "Closed Lost",
        "Re-engagement",
        "On Hold",
        "Disqualified",
    ]
    return random.choice(values)

def color():
    return fake.color_name()

def size():
    clothing_sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    generic_sizes = ["Small", "Medium", "Large", "Extra Large"]
    dimensions = [
        "10x10 cm", "15x20 cm", "30x40 cm", "50x70 cm",
        "100x200 mm", "5x7 in", "8x10 in", "12x18 in"
    ]
    
    size_pool = clothing_sizes + generic_sizes + dimensions
    return random.choice(size_pool)

def availability():
    statuses = [
        "in_stock",
        "out_of_stock",
        "pre_order",
        "discontinued",
        "limited_stock",
        "backorder"
    ]
    return random.choice(statuses)

def product_name():
    adjectives = [
        "Smart", "Ultra", "Eco", "Wireless", "Portable", "Pro", "Mini", "Advanced", "Digital",
        "Compact", "Premium", "Rechargeable", "Smart", "Fast", "Silent", "Clean", "Automatic"
    ]
    
    extra = [
        "Max", "X", "Go", "One", "360", "Plus", "Edge", "Prime", "Lite", "Air", "Touch", "Sense"
    ]
    
    word_count = random.randint(1, 5)
    name_parts = []

    if word_count >= 2:
        name_parts.append(random.choice(adjectives))
        name_parts.append(random.choice(product_names))
        word_count -= 2
    else:
        name_parts.append(random.choice(product_names))
        word_count -= 1

    for _ in range(word_count):
        name_parts.append(random.choice(extra + adjectives))

    return " ".join(name_parts)


def deal_source():
    values = [
        "Website Form",
        "Cold Email",
        "Cold Call", 
        "Referral",
        "Social Media",
        "LinkedIn Outreach",
        "Google Ads",
        "Facebook Ads", 
        "Organic Search (SEO)",
        "Content Marketing",
        "Webinars",
        "Trade Show",
        "Networking Event",
        "Purchased List",
        "Partner Program",
        "Chatbot",
        "Direct Traffic",
        "Retargeting Ads",
        "Podcast",
        "Other"
    ]
    return random.choice(values)

def product_category():
    values = [
        "Clothing & Apparel",
        "Home & Kitchen", 
        "Beauty & Personal Care",
        "Health & Wellness",
        "Sports & Outdoors",
        "Toys & Games",
        "Automotive",
        "Books & Stationery",
        "Office Supplies",
        "Smartphones",
        "Laptops & Computers",
        "Smartwatches",
        "Headphones & Earbuds",
        "Cameras & Accessories",
        "Men's Clothing",
        "Women's Clothing",
        "Kids' Clothing",
        "Shoes & Footwear",
        "Accessories (Bags, Hats, Belts)",
        "Furniture",
        "Kitchen Appliances",
        "Bedding & Bath",
        "Home Decor",
        "Cleaning Supplies",
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrances",
        "Grooming Tools",
        "Fitness Equipment",
        "Camping & Hiking",
        "Cycling",
        "Team Sports",
        "Fishing & Hunting"
    ]
    return random.choice(values)

def currency():
    return 'USD'

def industry():
    # https://gist.github.com/mbejda/19012b99a12e9d014389
    return random.choice(["Accounting",
"Airlines / Aviation",
"Alternative Dispute Resolution",
"Alternative Medicine",
"Animation",
"Apparel / Fashion",
"Architecture / Planning",
"Arts / Crafts",
"Automotive",
"Aviation / Aerospace",
"Banking / Mortgage",
"Biotechnology / Greentech",
"Broadcast Media",
"Building Materials",
"Business Supplies / Equipment",
"Capital Markets / Hedge Fund / Private Equity",
"Chemicals",
"Civic / Social Organization",
"Civil Engineering",
"Commercial Real Estate",
"Computer Games",
"Computer Hardware",
"Computer Networking",
"Computer Software / Engineering",
"Computer / Network Security",
"Construction",
"Consumer Electronics",
"Consumer Goods",
"Consumer Services",
"Cosmetics",
"Dairy",
"Defense / Space",
"Design",
"E - Learning",
"Education Management",
"Electrical / Electronic Manufacturing",
"Entertainment / Movie Production",
"Environmental Services",
"Events Services",
"Executive Office",
"Facilities Services",
"Farming",
"Financial Services",
"Fine Art",
"Fishery",
"Food Production",
"Food / Beverages",
"Fundraising",
"Furniture",
"Gambling / Casinos",
"Glass / Ceramics / Concrete",
"Government Administration",
"Government Relations",
"Graphic Design / Web Design",
"Health / Fitness",
"Higher Education / Acadamia",
"Hospital / Health Care",
"Hospitality",
"Human Resources / HR",
"Import / Export",
"Individual / Family Services",
"Industrial Automation",
"Information Services",
"Information Technology / IT",
"Insurance",
"International Affairs",
"International Trade / Development",
"Internet",
"Investment Banking / Venture",
"Investment Management / Hedge Fund / Private Equity",
"Judiciary",
"Law Enforcement",
"Law Practice / Law Firms",
"Legal Services",
"Legislative Office",
"Leisure / Travel",
"Library",
"Logistics / Procurement",
"Luxury Goods / Jewelry",
"Machinery",
"Management Consulting",
"Maritime",
"Market Research",
"Marketing / Advertising / Sales",
"Mechanical or Industrial Engineering",
"Media Production",
"Medical Equipment",
"Medical Practice",
"Mental Health Care",
"Military Industry",
"Mining / Metals",
"Motion Pictures / Film",
"Museums / Institutions",
"Music",
"Nanotechnology",
"Newspapers / Journalism",
"Non - Profit / Volunteering",
"Oil / Energy / Solar / Greentech",
"Online Publishing",
"Other Industry",
"Outsourcing / Offshoring",
"Package / Freight Delivery",
"Packaging / Containers",
"Paper / Forest Products",
"Performing Arts",
"Pharmaceuticals",
"Philanthropy",
"Photography",
"Plastics",
"Political Organization",
"Primary / Secondary Education",
"Printing",
"Professional Training",
"Program Development",
"Public Relations / PR",
"Public Safety",
"Publishing Industry",
"Railroad Manufacture",
"Ranching",
"Real Estate / Mortgage",
"Recreational Facilities / Services",
"Religious Institutions",
"Renewables / Environment",
"Research Industry",
"Restaurants",
"Retail Industry",
"Security / Investigations",
"Semiconductors",
"Shipbuilding",
"Sporting Goods",
"Sports",
"Staffing / Recruiting",
"Supermarkets",
"Telecommunications",
"Textiles",
"Think Tanks",
"Tobacco",
"Translation / Localization",
"Transportation",
"Utilities",
"Venture Capital / VC",
"Veterinary",
"Warehousing",
"Wholesale",
"Wine / Spirits",
"Wireless",
"Writing / Editing"])


def rating():
    return random.randrange(1, 6)

def customer_plan():
    return random.choice(["Free", "Starter", "Pro", "Business", "Enterprise"])

def support_priority():
    return random.choice(["Low", "Medium", "High", "Urgent"])

def sentiment():
    return random.choice(["Positive", "Neutral", "Negative", "Mixed"])

def support_ticket_category():
    return random.choice(["Billing", "Bug", "Feature Request", "Account Access", "Data Import", "Performance", "Other"])

def review_topic():
    return random.choice(["Pricing", "Support", "Product Quality", "Delivery", "Usability", "Features", "Other"])

def target_language():
    return random.choice(["French", "Spanish", "German", "Italian", "Portuguese", "Dutch"])

def product_attributes():
    attributes = ["portable", "wireless", "waterproof", "rechargeable", "eco-friendly", "compact", "premium", "lightweight"]
    return "; ".join(random.sample(attributes, k=random.randrange(2, 5)))

def icp_fit():
    return random.choice(["Strong", "Medium", "Poor", "Unclear"])

def score_band():
    return random.choice(["High", "Medium", "Low"])

def page_type():
    return random.choice(["Homepage", "Product Page", "Pricing Page", "Case Study", "Blog Post", "Directory Listing"])

def research_output_type():
    return random.choice(["Company Summary", "ICP Fit", "Pricing Evidence", "Hiring Signal", "Technology Mention", "Competitor Mention"])

def domain():
    return fake.domain_name()

def page_title():
    return random.choice([
        f"{fake.company()} | {fake.catch_phrase()}",
        f"{product_name()} - Features and Pricing",
        f"How {fake.company()} improved operations",
        f"About {fake.company()}",
    ])

def research_question():
    return random.choice([
        "Does this company sell to ecommerce brands?",
        "Find the pricing page and summarize the packaging.",
        "Does the website mention Shopify, Salesforce, or HubSpot?",
        "Find one recent hiring signal for this company.",
        "Summarize the main product and target customer.",
    ])

SUPPORT_TICKET_SCENARIOS = [
    {
        "subjects": ["CSV columns shifted after upload", "Rows split into extra columns", "Commas broke my import"],
        "objects": ["a customer export", "a vendor list", "a product catalog", "a CRM backup", "a lead file", "an order history file", "a supplier spreadsheet", "a webinar attendee list"],
        "details": ["commas in the notes field", "line breaks inside addresses", "quoted values from Excel", "empty columns near the end", "semicolon delimiters from our ERP", "tabs copied from Google Sheets", "unescaped quotes in product descriptions"],
        "asks": ["repair the import", "identify the failed rows", "recover the original columns", "upload the file safely", "normalize the delimiter", "keep multiline notes in one column"],
    },
    {
        "subjects": ["Broken accents after import", "Special characters look wrong", "Encoding issue in names"],
        "objects": ["French customer names", "Spanish addresses", "German company names", "currency symbols", "smart quotes", "Nordic characters", "Portuguese product descriptions", "Italian city names"],
        "details": ["UTF-8 worked in Excel but not after upload", "the file may be Windows-1252", "some rows came from an old CRM export", "the export was saved on a Windows laptop", "the file mixes old and new rows"],
        "asks": ["fix the encoding", "detect the right file encoding", "keep accents readable", "re-export the file correctly", "convert the file to clean UTF-8", "list the characters that changed"],
    },
    {
        "subjects": ["Invoice has extra seats", "Billing amount looks wrong", "Unexpected charge on invoice"],
        "objects": ["two removed users", "an old workspace", "a trial account", "a canceled add-on", "a duplicate subscription", "an annual plan upgrade"],
        "details": ["the change was made last month", "the renewal date is tomorrow", "the invoice was already sent to finance", "the card was charged this morning", "the receipt does not match our purchase order"],
        "asks": ["correct the invoice", "explain the charge", "update billing before renewal", "send a revised receipt", "confirm the active seats", "apply the credit to the next invoice"],
    },
    {
        "subjects": ["Cannot access workspace", "Password reset did not work", "Locked out after email change"],
        "objects": ["my admin account", "a teammate account", "our shared workspace", "a new SSO user", "a contractor login", "the owner account"],
        "details": ["the reset email never arrived", "SSO redirects to the wrong workspace", "the old email is no longer active", "the invite link has expired", "the browser shows a permission error"],
        "asks": ["restore access", "update the login email", "check the SSO configuration", "send a recovery link", "transfer ownership", "resend the invitation"],
    },
    {
        "subjects": ["Large export is slow", "Export has been running too long", "Need CSV export before meeting"],
        "objects": ["a 200k-row collection", "a filtered contact list", "a full product table", "a deduplicated lead list", "a 1M-row CSV", "an enriched company table"],
        "details": ["the progress bar has not moved", "the download link expired", "the export must include all columns", "the browser tab was closed by mistake", "the file is needed for a scheduled import"],
        "asks": ["speed up the export", "send a fresh download link", "confirm whether the export is still running", "help me split the file", "export only visible columns", "retry the job"],
    },
    {
        "subjects": ["Reusable prompt templates", "Save AI prompts for the team", "Prompt library request"],
        "objects": ["classification prompts", "translation prompts", "cleaning prompts", "research prompts", "lead scoring prompts", "support triage prompts"],
        "details": ["we run the same prompt every week", "different teammates need the same instructions", "we want fewer copy-paste mistakes", "we test several LLM providers", "we need approvals before changing prompts"],
        "asks": ["save reusable templates", "share prompts with the workspace", "track prompt versions", "apply a template to new files", "lock approved prompts", "compare prompt outputs"],
    },
    {
        "subjects": ["Duplicates are not detected", "Need help merging duplicate rows", "Company matching missed records"],
        "objects": ["companies with legal suffixes", "contacts with two emails", "domains with tracking parameters", "names with typos", "accounts from two CRMs", "leads from event lists"],
        "details": ["some rows have empty phone numbers", "the duplicate groups look too strict", "one source has old values", "the same company appears with local branches", "some URLs include tracking parameters"],
        "asks": ["tune the matching rules", "merge the best values", "preview duplicate groups", "export a change log", "keep the newest value", "ignore empty fields during merge"],
    },
    {
        "subjects": ["Webhook failed during enrichment", "Auto-run stopped processing rows", "Scheduled enrichment did not finish"],
        "objects": ["new leads", "company domains", "LinkedIn URLs", "email addresses", "phone numbers", "website URLs"],
        "details": ["only some rows were processed", "the run stopped overnight", "the log shows a timeout", "credits were consumed before the failure", "auto-run did not pick up new rows"],
        "asks": ["restart the run", "show failed rows", "explain the error", "avoid duplicate charges", "resume from the failed rows", "disable auto-run temporarily"],
    },
]

SUPPORT_TICKET_OPENERS = [
    "We ran into an issue with {object}: {detail}.",
    "Our team is working on {object}, and we found {detail}.",
    "A teammate checked {object} and found {detail}.",
    "During a cleanup involving {object}, we found {detail}.",
    "After checking {object}, we saw that {detail}.",
    "While preparing {object} for a deadline, we found {detail}.",
    "The workflow related to {object} reported {detail}.",
    "I need help with {object} because we found {detail}.",
]

SUPPORT_TICKET_URGENCY = [
    "This is blocking today's cleanup work.",
    "We need this before a customer meeting.",
    "It is not urgent, but it affects several users.",
    "Finance is waiting for an answer.",
    "We can work around it today, but need a reliable fix.",
    "The sales team is waiting for the cleaned file.",
    "We are testing this on a small file before running the full import.",
    "The issue affects one workspace, but not another.",
    "I can share a sample row if needed.",
    "The same workflow worked last week.",
]

SUPPORT_TICKET_CLOSERS = [
    "Can you help us {ask}?",
    "Please {ask} and let me know the next step.",
    "What is the safest way to {ask}?",
    "Could you help us {ask}?",
    "Is there a way to {ask}?",
    "Can you confirm whether you can {ask}?",
    "What should we check before we {ask}?",
]

SUPPORT_TICKET_CONTEXT = [
    "The file has {row_count} rows and {column_count} columns.",
    "This started after we exported from {source_system}.",
    "The affected rows are mostly from {region}.",
    "We are using {browser} on {os_name}.",
    "The upload file is a {file_type} created {timeframe}.",
    "The workspace has {seat_count} active users.",
]

SUPPORT_TICKET_SOURCE_SYSTEMS = ["Salesforce", "HubSpot", "Pipedrive", "Airtable", "Excel", "Google Sheets", "Shopify", "an internal admin tool"]
SUPPORT_TICKET_REGIONS = ["France", "Spain", "Germany", "the United States", "Canada", "the United Kingdom", "Brazil", "multiple EMEA offices"]
SUPPORT_TICKET_BROWSERS = ["Chrome", "Safari", "Edge", "Firefox"]
SUPPORT_TICKET_OS = ["macOS", "Windows", "Ubuntu", "iPadOS"]
SUPPORT_TICKET_FILE_TYPES = ["CSV", "UTF-8 CSV", "semicolon CSV", "Excel export", "tab-separated file"]
SUPPORT_TICKET_TIMEFRAMES = ["this morning", "yesterday", "last Friday", "after a scheduled sync", "from a nightly export", "during a migration test"]

def _support_context_values():
    return {
        "row_count": random.choice(["480", "1,200", "8,500", "24,000", "100,000", "250,000", "1,000,000"]),
        "column_count": random.choice(["12", "28", "47", "86", "120"]),
        "source_system": random.choice(SUPPORT_TICKET_SOURCE_SYSTEMS),
        "region": random.choice(SUPPORT_TICKET_REGIONS),
        "browser": random.choice(SUPPORT_TICKET_BROWSERS),
        "os_name": random.choice(SUPPORT_TICKET_OS),
        "file_type": random.choice(SUPPORT_TICKET_FILE_TYPES),
        "timeframe": random.choice(SUPPORT_TICKET_TIMEFRAMES),
        "seat_count": random.choice(["3", "7", "14", "26", "58"]),
    }

def support_ticket_sample():
    scenario = random.choice(SUPPORT_TICKET_SCENARIOS)
    subject = random.choice(scenario["subjects"])
    values = {
        "object": random.choice(scenario["objects"]),
        "detail": random.choice(scenario["details"]),
        "ask": random.choice(scenario["asks"]),
    }
    context_values = _support_context_values()
    context_sentences = random.sample(SUPPORT_TICKET_CONTEXT, k=random.choice([1, 1, 2]))
    text = " ".join([
        random.choice(SUPPORT_TICKET_OPENERS).format(**values),
        *[sentence.format(**context_values) for sentence in context_sentences],
        random.choice(SUPPORT_TICKET_URGENCY),
        random.choice(SUPPORT_TICKET_CLOSERS).format(**values),
    ])
    return subject, text

def support_ticket_subject():
    return support_ticket_sample()[0]

def support_ticket_text():
    return support_ticket_sample()[1]

REVIEW_SCENARIOS = [
    {
        "ratings": [4, 5],
        "openers": ["Setup was straightforward", "The build quality feels solid", "The product worked well out of the box", "Support answered quickly", "The first run went better than expected", "The design feels practical"],
        "details": ["the instructions were clear", "the packaging was careful", "the main feature worked as described", "the app connected on the first try", "the controls were easy to understand", "the materials feel durable"],
        "closers": ["I would buy it again.", "It feels like good value.", "It solved the problem I bought it for.", "I recommended it to a teammate.", "I will keep it in our regular workflow.", "It is one of the better options I have tried."],
    },
    {
        "ratings": [1, 2],
        "openers": ["Delivery was late", "The setup process was frustrating", "The product stopped working after a few days", "Support took too long to answer", "The item did not match the listing", "The first impression was disappointing"],
        "details": ["the box arrived damaged", "the instructions skipped important steps", "the feature I needed was unreliable", "the replacement process was unclear", "the size was different from the description", "the finish scratched during normal use"],
        "closers": ["I would not order it again.", "It was not worth the price.", "I expected better quality.", "I had to switch to another option.", "I asked for a refund.", "I would wait for a better version."],
    },
    {
        "ratings": [3],
        "openers": ["The product is fine for basic use", "There are useful features, but the experience is uneven", "It works, but it took longer than expected", "The value is acceptable for the price", "I have mixed feelings after using it", "It does the job, but not smoothly"],
        "details": ["the setup guide could be clearer", "support eventually solved the issue", "some parts feel durable and others do not", "the advanced options are hard to find", "the default settings were not ideal", "the result depends a lot on how you use it"],
        "closers": ["I might keep using it.", "I would compare alternatives before buying again.", "It is okay for small teams.", "It needs a few improvements.", "I would recommend it only for simple needs.", "It is acceptable, but not impressive."],
    },
]

REVIEW_CONTEXTS = [
    "after two weeks of use",
    "for a small team",
    "during a busy launch week",
    "as a replacement for an older product",
    "for daily work",
    "while traveling",
    "for a first-time user",
    "with several people sharing it",
    "after a month of testing",
    "for a client project",
    "during onboarding",
    "in a busy household",
    "for a remote team",
    "in a small office",
    "on a tight budget",
]

REVIEW_PRODUCTS = [
    "the starter kit",
    "the mobile app",
    "the replacement part",
    "the premium plan",
    "the travel case",
    "the dashboard",
    "the compact model",
    "the new version",
    "the subscription",
    "the accessory bundle",
]

REVIEW_SPECIFICS = [
    "Battery life lasted {duration}.",
    "The first setup took {duration}.",
    "I used it with {team_size} people.",
    "The order arrived in {delivery_time}.",
    "I contacted support {support_count}.",
    "The price was {price_comment}.",
    "The main issue appeared after {duration}.",
    "The package included {package_item}.",
]

REVIEW_OPTIONAL_NOTES = [
    "I also liked that the documentation used plain language.",
    "The photos on the product page were accurate.",
    "The return policy made the purchase less risky.",
    "The comparison chart helped me choose the right option.",
    "The email updates were clear.",
    "I had to search the help center to finish setup.",
    "A short video tutorial would have helped.",
    "The product page should mention this limitation earlier.",
]

def _review_specific_values():
    return {
        "duration": random.choice(["one day", "three days", "a week", "two weeks", "about a month", "less than an hour", "most of the afternoon"]),
        "team_size": random.choice(["2", "4", "6", "12", "25"]),
        "delivery_time": random.choice(["two days", "four days", "one week", "ten days", "less than 48 hours"]),
        "support_count": random.choice(["once", "twice", "three times", "several times"]),
        "price_comment": random.choice(["fair for the quality", "higher than expected", "reasonable during the sale", "hard to justify for light use"]),
        "package_item": random.choice(["a quick-start guide", "extra screws", "a carrying pouch", "a charging cable", "replacement pads"]),
    }

def review_sample():
    scenario = random.choice(REVIEW_SCENARIOS)
    values = _review_specific_values()
    specific_sentences = random.sample(REVIEW_SPECIFICS, k=random.choice([1, 1, 2]))
    optional_notes = random.sample(REVIEW_OPTIONAL_NOTES, k=random.choice([0, 1, 1, 2]))
    text = " ".join([
        f"{random.choice(scenario['openers'])} {random.choice(REVIEW_CONTEXTS)}.",
        f"I tested {random.choice(REVIEW_PRODUCTS)}.",
        f"Overall, {random.choice(scenario['details'])}.",
        *[sentence.format(**values) for sentence in specific_sentences],
        *optional_notes,
        random.choice(scenario["closers"]),
    ])
    return text, random.choice(scenario["ratings"])

def review_text():
    return review_sample()[0]

def messy_company_name():
    base_name = fake.company().replace(',', '')
    prefix = random.choice(["", "  ", "THE "])
    suffix = random.choice(["", " Inc.", " LLC", " ltd", " GmbH", "  "])
    return f"{prefix}{base_name}{suffix}"

TYPES_TO_GENERATORS = {
    'id': random_string,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'full_name': full_name, # fake.name,
    'username': username,
    'company': fake.company,
    'industry': industry,
    'business_department': department,
    'company_desc': fake.catch_phrase,
    'company_number_employees': number_employees,
    'city': fake.city,
    'country': fake.country,
    'sex': sex,
    'ean': fake.ean,
    'url': fake.url,
    'email': fake.email,
    'currency': currency,
    'availability': availability,
    'size': size,
    'color': color,
    'business_email': fake.company_email,
    'website': fake.url,
    'job': fake.job,
    'number': number,
    'small_positive_integer': small_positive_integer,
    'positive_integer': positive_integer,
    'product_name': product_name,
    'brand': brand,
    'product_category': product_category,
    'deal_stage': deal_stage,
    'deal_source': deal_source,
    'date': fake.date,
    'year': fake.year,
    'datetime': fake.date_time,
    'date_this_decade': fake.date_this_decade,
    'date_of_birth': fake.date_of_birth,
    'long_text': long_text,
    'very_long_text': very_long_text,
    'address': fake.address,
    'phone': fake.phone_number,
    'rating': rating,
    'customer_plan': customer_plan,
    'support_priority': support_priority,
    'sentiment': sentiment,
    'support_ticket_category': support_ticket_category,
    'review_topic': review_topic,
    'target_language': target_language,
    'product_attributes': product_attributes,
    'icp_fit': icp_fit,
    'score_band': score_band,
    'page_type': page_type,
    'research_output_type': research_output_type,
    'domain': domain,
    'page_title': page_title,
    'research_question': research_question,
    'support_ticket_subject': support_ticket_subject,
    'support_ticket_text': support_ticket_text,
    'review_text': review_text,
    'messy_company_name': messy_company_name
}

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
    return random.randrange(1, 1000)

def number_employees():
    return random.randrange(1, 10000)

def long_text():
    return fake.paragraph(nb_sentences=1)

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
    'address': fake.address,
    'phone': fake.phone_number
}

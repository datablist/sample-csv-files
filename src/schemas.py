from typing import Dict, TypedDict, List, Literal, Tuple

class SchemaField(TypedDict):
    name: str
    type: str
    unique: bool

CUSTOMERS_SCHEMA: List[SchemaField] = [{
    "name": "Customer Id",
    "type": 'id',
    "unique": True
}, {
    "name": "First Name",
    "type": 'first_name'
}, {
    "name": "Last Name",
    "type": "last_name"
}, {
    "name": "Company",
    "type": "company"
}, {
    "name": "City",
    "type": "city",
}, {
    "name": "Country",
    "type": "country",
}, {
    "name": "Phone 1",
    "type": "phone"
}, {
    "name": "Phone 2",
    "type": "phone"
}, {
    "name": "Email",
    "type": "business_email",
    "unique": True
}, {
    "name": "Subscription Date",
    "type": "date_this_decade"
}, {
    "name": "Website",
    "type": "website"
}]

LEADS_SCHEMA =[{
    "name": "Account Id",
    "type": 'id',
    "unique": True
}, {
    "name": "Lead Owner",
    "type": 'full_name'
}, {
    "name": "First Name",
    "type": 'first_name'
}, {
    "name": "Last Name",
    "type": "last_name"
}, {
    "name": "Company",
    "type": "company"
}, {
    "name": "Phone 1",
    "type": "phone"
}, {
    "name": "Phone 2",
    "type": "phone"
}, {
    "name": "Email 1",
    "type": "business_email"
}, {
    "name": "Email 2",
    "type": "business_email"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Source",
    "type": "deal_source"
}, {
    "name": "Deal Stage",
    "type": "deal_stage"
}, {
    "name": "Notes",
    "type": "long_text"
}]

PEOPLE_SCHEMA = [{
    "name": "User Id",
    "type": 'id',
    "unique": True
}, {
    "name": "First Name",
    "type": 'first_name'
}, {
    "name": "Last Name",
    "type": "last_name"
}, {
    "name": "Sex",
    "type": "sex"
}, {
    "name": "Email",
    "type": "email",
    "unique": True
}, {
    "name": "Phone",
    "type": "phone"
}, {
    "name": "Date of birth",
    "type": "date_of_birth"
}, {
    "name": "Job Title",
    "type": "job"
}]

ORGANIZATIONS_SCHEMA = [{
    "name": "Organization Id",
    "type": 'id',
    "unique": True
}, {
    "name": "Name",
    "type": "company"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Country",
    "type": "country"
}, {
    "name": "Description",
    "type": "company_desc"
}, {
    "name": "Founded",
    "type": "year"
}, {
    "name": "Industry",
    "type": "industry"
}, {
    "name": "Number of employees",
    "type": "company_number_employees"
}]


PRODUCTS_SCHEMA = [{
    "name": "Name",
    "type": "product_name"
}, {
    "name": "Description",
    "type": "long_text"
}, {
    "name": "Brand",
    "type": "company"
}, {
    "name": "Category",
    "type": "product_category"
}, {
    "name": "Price",
    "type": "positive_integer"
}, {
    "name": "Currency",
    "type": "currency"
}, {
    "name": "Stock",
    "type": "positive_integer"
}, {
    "name": "EAN",
    "type": "ean",
    "unique": True
}, {
    "name": "Color",
    "type": "color"
}, {
    "name": "Size",
    "type": "size"
}, {
    'name': 'Availability',
    'type': 'availability'
}, {
    "name": "Internal ID",
    "type": "id",
    "unique": True
}]

OFFERS_SCHEMA = [{
    "name": "EAN",
    "type": "ean",
    "unique": True
}, {
    "name": "Internal ID",
    "type": "id",
    "unique": True
}, {
    "name": "Stock",
    "type": "positive_integer"
}, {
    "name": "Price",
    "type": "positive_integer"
}]

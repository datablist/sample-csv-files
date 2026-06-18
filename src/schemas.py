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
}, {
    "name": "UpdatedAt",
    "type": "datetime",
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
    "name": "Added Date",
    "type": "date",
    "unique": False
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

ENTERPRISE_CUSTOMERS_SCHEMA: List[SchemaField] = [{
    "name": "Customer ID",
    "type": "id",
    "unique": True
}, {
    "name": "Company Name",
    "type": "company"
}, {
    "name": "Primary Contact First Name",
    "type": "first_name"
}, {
    "name": "Primary Contact Last Name",
    "type": "last_name"
}, {
    "name": "Secondary Contact First Name",
    "type": "first_name"
}, {
    "name": "Secondary Contact Last Name",
    "type": "last_name"
}, {
    "name": "Email Primary",
    "type": "business_email",
    "unique": True
}, {
    "name": "Email Secondary",
    "type": "business_email"
}, {
    "name": "Phone Primary",
    "type": "phone"
}, {
    "name": "Phone Secondary",
    "type": "phone"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Industry",
    "type": "industry"
}, {
    "name": "Company Description",
    "type": "very_long_text"
}, {
    "name": "Number of Employees",
    "type": "company_number_employees"
}, {
    "name": "Annual Revenue",
    "type": "positive_integer"
}, {
    "name": "Address",
    "type": "address"
}, {
    "name": "City",
    "type": "city"
}, {
    "name": "Country",
    "type": "country"
}, {
    "name": "Account Manager",
    "type": "full_name"
}, {
    "name": "Department",
    "type": "business_department"
}, {
    "name": "Contract Start Date",
    "type": "date_this_decade"
}, {
    "name": "Contract End Date",
    "type": "date"
}, {
    "name": "Contract Value",
    "type": "positive_integer"
}, {
    "name": "Payment Terms",
    "type": "very_long_text"
}, {
    "name": "Special Requirements",
    "type": "very_long_text"
}, {
    "name": "Support Level",
    "type": "deal_stage"
}, {
    "name": "Lead Source",
    "type": "deal_source"
}, {
    "name": "Last Contact Date",
    "type": "date"
}, {
    "name": "Next Follow Up Date",
    "type": "date"
}, {
    "name": "Customer Since",
    "type": "year"
}, {
    "name": "Notes",
    "type": "very_long_text"
}, {
    "name": "History",
    "type": "very_long_text"
}, {
    "name": "Messages",
    "type": "very_long_text"
}, {
    "name": "Implementation Instructions",
    "type": "very_long_text"
}]

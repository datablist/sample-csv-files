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


SUPPORT_TICKETS_SCHEMA: List[SchemaField] = [{
    "name": "Ticket ID",
    "type": "id",
    "unique": True
}, {
    "name": "Customer Plan",
    "type": "customer_plan"
}, {
    "name": "Ticket Subject",
    "type": "support_ticket_subject"
}, {
    "name": "Ticket Text",
    "type": "support_ticket_text"
}, {
    "name": "Priority Hint",
    "type": "support_priority"
}]

CUSTOMER_REVIEWS_SCHEMA: List[SchemaField] = [{
    "name": "Review ID",
    "type": "id",
    "unique": True
}, {
    "name": "Product Name",
    "type": "product_name"
}, {
    "name": "Rating",
    "type": "rating"
}, {
    "name": "Review Text",
    "type": "review_text"
}]

MESSY_COMPANY_DATA_SCHEMA: List[SchemaField] = [{
    "name": "Row ID",
    "type": "id",
    "unique": True
}, {
    "name": "Raw Company Name",
    "type": "messy_company_name"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Company Description",
    "type": "long_text"
}, {
    "name": "Country",
    "type": "country"
}, {
    "name": "Source System",
    "type": "deal_source"
}, {
    "name": "Account Owner",
    "type": "full_name"
}, {
    "name": "Created Date",
    "type": "date"
}, {
    "name": "Last Activity Date",
    "type": "date"
}, {
    "name": "Renewal Date",
    "type": "date"
}, {
    "name": "Lifecycle Stage",
    "type": "deal_stage"
}, {
    "name": "Employee Count",
    "type": "company_number_employees"
}, {
    "name": "Annual Revenue",
    "type": "positive_integer"
}, {
    "name": "Lead Score",
    "type": "number"
}, {
    "name": "Open Opportunities",
    "type": "number"
}, {
    "name": "CRM Notes",
    "type": "long_text"
}]

PRODUCT_CATALOG_AI_SCHEMA: List[SchemaField] = [{
    "name": "Product ID",
    "type": "id",
    "unique": True
}, {
    "name": "Product Title",
    "type": "product_name"
}, {
    "name": "Raw Description",
    "type": "long_text"
}, {
    "name": "Brand",
    "type": "company"
}, {
    "name": "Category",
    "type": "product_category"
}, {
    "name": "Target Language",
    "type": "target_language"
}]

PRODUCT_TRANSLATION_AI_SCHEMA: List[SchemaField] = [{
    "name": "Translation ID",
    "type": "id",
    "unique": True
}, {
    "name": "Product Name",
    "type": "product_name"
}, {
    "name": "Category",
    "type": "product_category"
}, {
    "name": "Source Language",
    "type": "target_language"
}, {
    "name": "Target Language",
    "type": "target_language"
}, {
    "name": "Product Description",
    "type": "long_text"
}, {
    "name": "Feature Bullets",
    "type": "long_text"
}, {
    "name": "SEO Title",
    "type": "product_name"
}, {
    "name": "Translation Instructions",
    "type": "long_text"
}, {
    "name": "Glossary Terms",
    "type": "product_attributes"
}, {
    "name": "Do Not Translate",
    "type": "long_text"
}]

LEAD_SCORING_AI_SCHEMA: List[SchemaField] = [{
    "name": "Lead ID",
    "type": "id",
    "unique": True
}, {
    "name": "First Name",
    "type": "first_name"
}, {
    "name": "Last Name",
    "type": "last_name"
}, {
    "name": "Job Title",
    "type": "job"
}, {
    "name": "Company",
    "type": "company"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Industry",
    "type": "industry"
}, {
    "name": "Company Notes",
    "type": "long_text"
}]

WEB_PAGE_EXTRACTION_AI_SCHEMA: List[SchemaField] = [{
    "name": "Page ID",
    "type": "id",
    "unique": True
}, {
    "name": "URL",
    "type": "website"
}, {
    "name": "Page Title",
    "type": "page_title"
}, {
    "name": "Page Text",
    "type": "very_long_text"
}, {
    "name": "Extraction Task",
    "type": "long_text"
}]

RESEARCH_QUESTIONS_AI_SCHEMA: List[SchemaField] = [{
    "name": "Research ID",
    "type": "id",
    "unique": True
}, {
    "name": "Entity Name",
    "type": "company"
}, {
    "name": "Domain",
    "type": "domain"
}, {
    "name": "Research Question",
    "type": "research_question"
}, {
    "name": "Source URL",
    "type": "website"
}]



CUSTOMERS_SCHEMA = [{
    "name": "Customer Id",
    "type": 'id'
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
    "type": "business_email"
}, {
    "name": "Subscription Date",
    "type": "date_this_decade"
}, {
    "name": "Website",
    "type": "website"
}]

LEADS_SCHEMA =[{
    "name": "Account Id",
    "type": 'id'
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
    "name": "Email",
    "type": "business_email"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Notes",
    "type": "long_text"
}]

PEOPLE_SCHEMA = [{
    "name": "User Id",
    "type": 'id'
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
    "type": "email"
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
    "type": 'id'
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
    "name": "EAN",
    "type": "ean"
}, {
    "name": "Internal ID",
    "type": "small_positive_integer"
}]

OFFERS_SCHEMA = [{
    "name": "EAN",
    "type": "ean"
}, {
    "name": "Internal ID",
    "type": "small_positive_integer"
}, {
    "name": "Stock",
    "type": "positive_integer"
}, {
    "name": "Price",
    "type": "positive_integer"
}]

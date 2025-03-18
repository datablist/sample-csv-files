from typing import List, Dict
import csv
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2
import random

from generators import TYPES_TO_GENERATORS, long_text, username

from schemas import (
    CUSTOMERS_SCHEMA,
    PEOPLE_SCHEMA,
    ORGANIZATIONS_SCHEMA,
    PRODUCTS_SCHEMA,
    OFFERS_SCHEMA,
    LEADS_SCHEMA
)

SCHEMA_TO_DICT = {
    'customers': CUSTOMERS_SCHEMA,
    'leads': LEADS_SCHEMA,
    'people': PEOPLE_SCHEMA,
    'organizations': ORGANIZATIONS_SCHEMA,
    'products': PRODUCTS_SCHEMA,
    'offers': OFFERS_SCHEMA
}

def find_index(list_values: List[Dict], name: str) -> int:
    possible = [i for i, elem in enumerate(list_values) if elem.get("name") == name]
    if len(possible) == 0:
        raise IndexError("No index found for {}".format(name))
    return possible[0] + 1 # Add 1 because we added the "index" column to the schema columns

def add_small_variation_to_duplicates(row: List, schema: str) -> List:
    """
    Add a small variation to the row to make it unique.
    """
    if schema != 'leads':
        return row
    
    last_name_index = find_index(LEADS_SCHEMA, "Last Name")
    website_index = find_index(LEADS_SCHEMA, "Website")
    email_1_index = find_index(LEADS_SCHEMA, "Email 1")
    email_2_index = find_index(LEADS_SCHEMA, "Email 2")
    phone_1_index = find_index(LEADS_SCHEMA, "Phone 1")
    phone_2_index = find_index(LEADS_SCHEMA, "Phone 2")
    note_index = find_index(LEADS_SCHEMA, "Notes")
    
    new_row = row.copy()

    lucky_number = random.randrange(1, 5)
    lucky_number_2 = random.randrange(1, 5)

    # Change Name
    if lucky_number <= 2:
        last_name = new_row[last_name_index]
        last_name_changed = "{}.".format(last_name[:1]) # Only the letter

        new_row[last_name_index] = last_name_changed

    # Add a small variation to the Website
    website = new_row[website_index]
    if lucky_number == 3:
        if "www" in website:
            website = website.replace("www.", "")
        elif "https" in website:
            website = website.replace("https", "http")
        elif "http" in website:
            website = website.replace("http", "https")
        
        new_row[website_index] = website

    # Inverse Emails
    if lucky_number <= 2:
        email1 = new_row[email_1_index]
        email2 = new_row[email_2_index]

        new_row[email_1_index] = email2
        new_row[email_2_index] = email1
    
    # Add a small variation to the Email
    if lucky_number_2 >= 3:
        email_to_change_index = random.choice([email_1_index, email_2_index])
        email_to_change = new_row[email_to_change_index]

        email_parts = email_to_change.split('@')

        new_row[email_to_change_index] = "".join([
            email_parts[0],
            "+",
            username(),
            "@",
            email_parts[1]
        ])

    # Inverse Phones
    if 2<= lucky_number <= 4:
        phone1 = new_row[phone_1_index]
        phone2 = new_row[phone_2_index]
        new_row[phone_1_index] = phone2
        new_row[phone_2_index] = phone1

    # New Note
    if lucky_number >= 3:
        new_row[note_index] = long_text()

    return new_row


def generate_file(
    schema='customers',
    name="customers",
    count=1000000,
    duplicate_ratio=0.0
):
    if duplicate_ratio > 0:
        name = "{}-duplicates-{}".format(name, duplicate_ratio)

    print("Generating file for: {} - {} - {}".format(schema, name, count, duplicate_ratio))

    p = Path(__file__).parent / "../files/{}".format(schema)
    p.mkdir(parents=True, exist_ok=True)

    file_name = "{}.csv".format(name)
    file_path = p / file_name

    if not file_path.exists():
        schema_dict = SCHEMA_TO_DICT[schema]

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Headers
            headers = [elem['name'] for elem in schema_dict]
            headers.insert(0, "Index") # Add an Index header
            writer.writerow(headers)

            # Content
            data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]
            rows = []
            generated_rows = []

            for index in range(1, count+1):
                random_pick = random.random()
                add_randomness = random_pick < duplicate_ratio
                if duplicate_ratio > 0 and len(generated_rows) > 0 and  add_randomness:
                    row = random.choice(generated_rows)  # Pick a random existing row
                    row = [index] + row[1:]  # Keep a unique index
                    row = add_small_variation_to_duplicates(row, schema)
                else:
                    row = [gen() for gen in data_generators]
                    row.insert(0, index)

                    generated_rows.append(row)
                
                rows.append(row)

                if index % 1000 == 0:
                    writer.writerows(rows)
                    rows = []

                if index % 10000 == 0:
                    print("{}/{}".format(index, count))

            writer.writerows(rows)
    else:
        print("{} already exists".format(file_path))

    # Create a zip version
    file_name_zip = "{}.zip".format(name)
    file_path_zip = p / file_name_zip
    if not file_path_zip.exists():
        with ZipFile(file_path_zip, 'w', ZIP_BZIP2) as zipObj:
            zipObj.write(filename=file_path, arcname=file_name)




if __name__ == '__main__':
    generate_file('customers', 'customers-100', 100)
    generate_file('customers', 'customers-1000', 1000)
    generate_file('customers', 'customers-10000', 10000)
    generate_file('customers', 'customers-100000', 100000)
    generate_file('customers', 'customers-500000', 500000)
    generate_file('customers', 'customers-1000000', 1000000)
    generate_file('customers', 'customers-2000000', 2000000)

    generate_file('leads', 'leads-100', 100)
    generate_file('leads', 'leads-1000', 1000)
    generate_file('leads', 'leads-10000', 10000)
    generate_file('leads', 'leads-100000', 100000)

    # With Duplicates
    generate_file('leads', 'leads-10000', 10000, 0.4)

    generate_file('people', 'people-100', 100)
    generate_file('people', 'people-1000', 1000)
    generate_file('people', 'people-10000', 10000)
    generate_file('people', 'people-100000', 100000)
    generate_file('people', 'people-500000', 500000)
    generate_file('people', 'people-1000000', 1000000)
    generate_file('people', 'people-2000000', 2000000)

    generate_file('organizations', 'organizations-100', 100)
    generate_file('organizations', 'organizations-1000', 1000)
    generate_file('organizations', 'organizations-10000', 10000)
    generate_file('organizations', 'organizations-100000', 100000)
    generate_file('organizations', 'organizations-500000', 500000)
    generate_file('organizations', 'organizations-1000000', 1000000)
    generate_file('organizations', 'organizations-2000000', 2000000)

    generate_file('products', 'products-100', 100)
    generate_file('products', 'products-1000', 1000)
    generate_file('products', 'products-10000', 10000)
    generate_file('products', 'products-100000', 100000)
    generate_file('products', 'products-500000', 500000)
    generate_file('products', 'products-1000000', 1000000)
    generate_file('products', 'products-2000000', 2000000)

    generate_file('offers', 'offers-100', 100)
    generate_file('offers', 'offers-1000', 1000)
    generate_file('offers', 'offers-10000', 10000)
    generate_file('offers', 'offers-100000', 100000)
    generate_file('offers', 'offers-500000', 500000)
    generate_file('offers', 'offers-1000000', 1000000)
    generate_file('offers', 'offers-2000000', 2000000)

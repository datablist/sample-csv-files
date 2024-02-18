import csv
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2

from generators import TYPES_TO_GENERATORS
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


def generate_file(schema='customers', name="customers", count=1000000):
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
            for index in range(1, count+1):
                row = [gen() for gen in data_generators]
                row.insert(0, index)
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

    generate_file('products', 'products-5000', 5000)
    generate_file('offers', 'offers-5000', 5000)

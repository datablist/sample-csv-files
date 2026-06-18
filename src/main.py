from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, List, Optional
import csv
import json
import random
from zipfile import ZIP_BZIP2, ZipFile

from ai_rows import AI_ROW_FACTORIES
from generators import TYPES_TO_GENERATORS
from schemas import (
    CUSTOMERS_SCHEMA,
    PEOPLE_SCHEMA,
    ORGANIZATIONS_SCHEMA,
    PRODUCTS_SCHEMA,
    OFFERS_SCHEMA,
    LEADS_SCHEMA,
    ENTERPRISE_CUSTOMERS_SCHEMA,
    SUPPORT_TICKETS_SCHEMA,
    CUSTOMER_REVIEWS_SCHEMA,
    MESSY_COMPANY_DATA_SCHEMA,
    PRODUCT_CATALOG_AI_SCHEMA,
    PRODUCT_TRANSLATION_AI_SCHEMA,
    LEAD_SCORING_AI_SCHEMA,
    WEB_PAGE_EXTRACTION_AI_SCHEMA,
    RESEARCH_QUESTIONS_AI_SCHEMA,
)

SCHEMA_TO_DICT = {
    'customers': CUSTOMERS_SCHEMA,
    'leads': LEADS_SCHEMA,
    'people': PEOPLE_SCHEMA,
    'organizations': ORGANIZATIONS_SCHEMA,
    'products': PRODUCTS_SCHEMA,
    'offers': OFFERS_SCHEMA,
    'enterprise_customers': ENTERPRISE_CUSTOMERS_SCHEMA,
    'support_tickets': SUPPORT_TICKETS_SCHEMA,
    'customer_reviews': CUSTOMER_REVIEWS_SCHEMA,
    'messy_company_data': MESSY_COMPANY_DATA_SCHEMA,
    'product_catalog_ai': PRODUCT_CATALOG_AI_SCHEMA,
    'product_translation_ai': PRODUCT_TRANSLATION_AI_SCHEMA,
    'lead_scoring_ai': LEAD_SCORING_AI_SCHEMA,
    'web_page_extraction_ai': WEB_PAGE_EXTRACTION_AI_SCHEMA,
    'research_questions_ai': RESEARCH_QUESTIONS_AI_SCHEMA,
}

AI_SCHEMAS = set(AI_ROW_FACTORIES.keys())
DEFAULT_ROW_COUNTS = (100, 1000, 10000)


@dataclass(frozen=True)
class GenerationScenario:
    schema: str
    slug: str
    counts: tuple[int, ...]
    use_case: str
    duplicate_ratio: float = 0.0
    output_folder: Optional[str] = None


def find_index(list_values: List[Dict], name: str) -> int:
    possible = [i for i, elem in enumerate(list_values) if elem.get("name") == name]
    if len(possible) == 0:
        raise IndexError("No index found for {}".format(name))
    return possible[0] + 1


def generate_company_variation(company_name: str) -> str:
    business_suffixes = [
        "Inc.", "Corp", "LLC", "Ltd.", "Incorporated", "Company", "Co.", "PLC",
        "GmbH", "S.A.", "Pty Ltd", "BV", "SAS", "LLP", "Limited", "AG", "AB",
    ]
    already_with_suffix = any(suffix in company_name for suffix in business_suffixes)
    geography_suffixes = [
        "Europe", "Asia", "USA", "Global", "International", "Canada", "UK",
        "India", "Pacific", "Americas", "Nordics", "EMEA", "DACH", "France",
        "Germany", "Japan", "Australia", "Africa",
    ]
    industry_terms = [
        "Systems", "Holdings", "Solutions", "Group", "Technologies", "Enterprises",
        "Partners", "Ventures", "Labs", "Studios", "Network", "Services", "Dynamics",
        "Industries", "Capital", "Investments", "Works", "Development", "Platform",
        "Innovations", "Consulting", "Digital", "Logistics", "Software", "Media",
        "Cloud", "Data", "Analytics", "Resources", "Design", "Security",
    ]
    variations = [
        f"{company_name} {random.choice(geography_suffixes)}",
        f"{company_name} {random.choice(industry_terms)}",
    ]
    if not already_with_suffix:
        variations.append(f"{company_name} {random.choice(business_suffixes)}")
    return random.choice(variations)


def add_small_variation_to_duplicates(row: List, schema: str) -> List:
    if schema not in ['leads', 'products', 'organizations']:
        return row

    if schema == 'products':
        new_row = row.copy()
        new_row[find_index(PRODUCTS_SCHEMA, "Stock")] = TYPES_TO_GENERATORS['positive_integer']()
        new_row[find_index(PRODUCTS_SCHEMA, "Added Date")] = TYPES_TO_GENERATORS['date']()
        return new_row

    if schema == 'organizations':
        new_row = row.copy()
        new_row[find_index(ORGANIZATIONS_SCHEMA, "Name")] = generate_company_variation(row[find_index(ORGANIZATIONS_SCHEMA, "Name")])
        new_row[find_index(ORGANIZATIONS_SCHEMA, "UpdatedAt")] = TYPES_TO_GENERATORS['datetime']()
        new_row[find_index(ORGANIZATIONS_SCHEMA, "Description")] = TYPES_TO_GENERATORS['long_text']()
        return new_row

    new_row = row.copy()
    last_name_index = find_index(LEADS_SCHEMA, "Last Name")
    website_index = find_index(LEADS_SCHEMA, "Website")
    email_1_index = find_index(LEADS_SCHEMA, "Email 1")
    email_2_index = find_index(LEADS_SCHEMA, "Email 2")
    phone_1_index = find_index(LEADS_SCHEMA, "Phone 1")
    phone_2_index = find_index(LEADS_SCHEMA, "Phone 2")
    note_index = find_index(LEADS_SCHEMA, "Notes")
    lucky_number = random.randrange(1, 5)
    lucky_number_2 = random.randrange(1, 5)

    if lucky_number <= 2:
        last_name = new_row[last_name_index]
        new_row[last_name_index] = f"{last_name[:1]}."

    website = new_row[website_index]
    if lucky_number == 3:
        if "https" in website:
            website = website.replace("https", "http", 1)
        elif "http" in website:
            website = website.replace("http", "https", 1)
        new_row[website_index] = website

    if lucky_number <= 2:
        new_row[email_1_index], new_row[email_2_index] = new_row[email_2_index], new_row[email_1_index]

    if lucky_number_2 >= 3:
        email_to_change_index = random.choice([email_1_index, email_2_index])
        email_parts = new_row[email_to_change_index].split('@')
        new_row[email_to_change_index] = f"{email_parts[0]}+{TYPES_TO_GENERATORS['username']()}@{email_parts[1]}"

    if 2 <= lucky_number <= 4:
        new_row[phone_1_index], new_row[phone_2_index] = new_row[phone_2_index], new_row[phone_1_index]

    if lucky_number >= 3:
        new_row[note_index] = TYPES_TO_GENERATORS['long_text']()

    return new_row


def _build_standard_row(schema_dict: List[Dict], data_generators: List[Callable], unique_fields: List[bool], generated_unique_values: Dict[int, set]) -> List:
    row = []
    for field_index, gen in enumerate(data_generators):
        gen_value = gen()
        if unique_fields[field_index]:
            while gen_value in generated_unique_values[field_index]:
                gen_value = gen()
            generated_unique_values[field_index].add(gen_value)
        row.append(gen_value)
    return row


def generate_file(
    schema='customers',
    name="customers",
    count=1000000,
    duplicate_ratio=0.0,
    output_root: Optional[Path] = None,
    output_folder: Optional[str] = None,
    overwrite: bool = False,
) -> Dict[str, str]:
    if duplicate_ratio > 0 and "duplicate" not in name:
        name = f"{name}-duplicates-{duplicate_ratio}"
    print(f"Generating file for: {schema} - {name} - {count} - {duplicate_ratio}")

    base_output = output_root or (Path(__file__).parent / "../files")
    folder_name = output_folder or schema
    output_dir = base_output / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    file_name = f"{name}.csv"
    file_path = output_dir / file_name

    schema_dict = SCHEMA_TO_DICT[schema]
    headers = [elem['name'] for elem in schema_dict]
    headers.insert(0, "Index")

    if overwrite or not file_path.exists():
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]
            unique_fields = [elem.get('unique', False) for elem in schema_dict]
            generated_rows = []
            generated_unique_values = {field_index: set() for field_index, is_unique in enumerate(unique_fields) if is_unique}
            rows = []
            row_factory = AI_ROW_FACTORIES.get(schema)

            for row_number in range(1, count + 1):
                if duplicate_ratio > 0 and generated_rows and random.random() < duplicate_ratio:
                    row = random.choice(generated_rows)
                    row = [row_number] + row[1:]
                    row = add_small_variation_to_duplicates(row, schema)
                else:
                    values = row_factory() if row_factory else _build_standard_row(schema_dict, data_generators, unique_fields, generated_unique_values)
                    row = [row_number] + values
                    generated_rows.append(row)

                rows.append(row)
                if row_number % 1000 == 0:
                    writer.writerows(rows)
                    rows = []
                if row_number % 10000 == 0:
                    print(f"{row_number}/{count}")
            writer.writerows(rows)
    else:
        print(f"{file_path} already exists")

    file_name_zip = f"{name}.zip"
    file_path_zip = output_dir / file_name_zip
    if overwrite or not file_path_zip.exists():
        with ZipFile(file_path_zip, 'w', ZIP_BZIP2) as zip_obj:
            zip_obj.write(filename=file_path, arcname=file_name)

    return {
        "schema": schema,
        "output_folder": folder_name,
        "name": name,
        "count": str(count),
        "csv_path": str(file_path),
        "zip_path": str(file_path_zip),
    }


def build_generation_scenarios() -> List[GenerationScenario]:
    return [
        GenerationScenario("customers", "customers", DEFAULT_ROW_COUNTS, "CRM import and customer table testing"),
        GenerationScenario("people", "people", DEFAULT_ROW_COUNTS, "Person records, contact fields, dates, and job titles"),
        GenerationScenario("organizations", "organizations", DEFAULT_ROW_COUNTS, "Company enrichment, domains, and account records"),
        GenerationScenario("leads", "leads", DEFAULT_ROW_COUNTS, "Sales pipeline, CRM cleanup, and lead imports"),
        GenerationScenario("products", "products", DEFAULT_ROW_COUNTS, "Ecommerce catalog, stock, price, and category testing"),
        GenerationScenario("offers", "offers", DEFAULT_ROW_COUNTS, "Inventory feed and product join tests"),
        GenerationScenario("enterprise_customers", "enterprise-customers", DEFAULT_ROW_COUNTS, "Wide CRM exports with long text fields"),
        GenerationScenario("leads", "leads-duplicates", DEFAULT_ROW_COUNTS, "Duplicate lead merge testing", 0.4),
        GenerationScenario("organizations", "organizations-duplicates", DEFAULT_ROW_COUNTS, "Duplicate company matching and normalization", 0.3),
        GenerationScenario("products", "products-duplicates", DEFAULT_ROW_COUNTS, "Duplicate product and inventory merge testing", 0.5),
        GenerationScenario("support_tickets", "support-tickets", DEFAULT_ROW_COUNTS, "AI ticket classification and priority routing"),
        GenerationScenario("customer_reviews", "customer-reviews", DEFAULT_ROW_COUNTS, "AI sentiment analysis and topic classification"),
        GenerationScenario("messy_company_data", "messy-company-data", DEFAULT_ROW_COUNTS, "AI data cleaning and company normalization"),
        GenerationScenario("product_catalog_ai", "product-catalog-ai", DEFAULT_ROW_COUNTS, "AI ecommerce classification and translation prompt testing"),
        GenerationScenario("product_translation_ai", "product-translation-ai", (1000,), "AI translation testing with realistic product copy"),
        GenerationScenario("lead_scoring_ai", "lead-scoring-ai", DEFAULT_ROW_COUNTS, "AI lead scoring and ICP fit testing"),
        GenerationScenario("web_page_extraction_ai", "web-page-extraction-ai", DEFAULT_ROW_COUNTS, "AI structured extraction from page text"),
        GenerationScenario("research_questions_ai", "research-questions-ai", DEFAULT_ROW_COUNTS, "AI agent web research prompt testing"),
    ]


def generate_scenarios(scenarios: Optional[List[GenerationScenario]] = None, output_root: Optional[Path] = None, overwrite: bool = False) -> List[Dict[str, str]]:
    generated = []
    for scenario in scenarios or build_generation_scenarios():
        for count in scenario.counts:
            result = generate_file(
                schema=scenario.schema,
                name=f"{scenario.slug}-{count}",
                count=count,
                duplicate_ratio=scenario.duplicate_ratio,
                output_root=output_root,
                output_folder=scenario.output_folder or scenario.slug,
                overwrite=overwrite,
            )
            generated.append({
                **result,
                "use_case": scenario.use_case,
                "duplicate_ratio": str(scenario.duplicate_ratio),
                "google_drive_csv_id": "",
                "google_drive_zip_id": "",
            })
    return generated


def write_upload_manifest(generated: List[Dict[str, str]], output_root: Optional[Path] = None) -> Path:
    base_output = output_root or (Path(__file__).parent / "../files")
    manifest_path = base_output / "google_drive_upload_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(generated, indent=2), encoding='utf-8')
    return manifest_path


if __name__ == '__main__':
    generated_files = generate_scenarios()
    manifest = write_upload_manifest(generated_files)
    print(f"Wrote upload manifest: {manifest}")

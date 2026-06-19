import csv
import random
from pathlib import Path
from zipfile import ZipFile

from ai_rows import REAL_COMPANY_PROFILES, REAL_WEB_PAGES, TRANSLATION_TARGET_LANGUAGES
from main import AI_SCHEMAS, GenerationScenario, SCHEMA_TO_DICT, add_small_variation_to_duplicates, build_generation_scenarios, generate_file, generate_scenarios


def read_csv(path: Path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))


def test_generate_file_writes_rows_headers_and_zip(tmp_path):
    result = generate_file('customers', 'customers-test', 10, output_root=tmp_path)
    rows = read_csv(Path(result['csv_path']))
    expected_headers = ['Index'] + [field['name'] for field in SCHEMA_TO_DICT['customers']]
    assert rows[0] == expected_headers
    assert len(rows) == 11
    assert [int(row[0]) for row in rows[1:]] == list(range(1, 11))
    with ZipFile(result['zip_path']) as zip_file:
        assert zip_file.namelist() == ['customers-test.csv']


def test_generate_file_does_not_overwrite_existing_file(tmp_path):
    result = generate_file('customers', 'customers-test', 10, output_root=tmp_path)
    csv_path = Path(result['csv_path'])
    csv_path.write_text('sentinel\n', encoding='utf-8')
    generate_file('customers', 'customers-test', 10, output_root=tmp_path)
    assert csv_path.read_text(encoding='utf-8') == 'sentinel\n'


def test_generation_scenarios_have_standalone_output_folders():
    scenarios = build_generation_scenarios()
    folders = [scenario.output_folder or scenario.slug for scenario in scenarios]
    assert len(folders) == len(set(folders))


def test_duplicate_scenarios_do_not_overwrite_standard_scenarios(tmp_path):
    scenarios = [
        GenerationScenario("leads", "leads", (10,), "standard leads"),
        GenerationScenario("leads", "leads-duplicates", (10,), "duplicate leads", 0.4),
        GenerationScenario("organizations", "organizations", (10,), "standard organizations"),
        GenerationScenario("organizations", "organizations-duplicates", (10,), "duplicate organizations", 0.3),
        GenerationScenario("products", "products", (10,), "standard products"),
        GenerationScenario("products", "products-duplicates", (10,), "duplicate products", 0.5),
    ]
    generated = generate_scenarios(scenarios, output_root=tmp_path)
    csv_paths = [Path(result['csv_path']) for result in generated]
    zip_paths = [Path(result['zip_path']) for result in generated]

    assert len(csv_paths) == len(set(csv_paths))
    assert len(zip_paths) == len(set(zip_paths))
    assert {path.parent.name for path in csv_paths} == {
        "leads",
        "leads-duplicates",
        "organizations",
        "organizations-duplicates",
        "products",
        "products-duplicates",
    }


def test_duplicate_generation_keeps_unique_index(tmp_path):
    result = generate_file('products', 'products-test', 50, duplicate_ratio=0.8, output_root=tmp_path)
    rows = read_csv(Path(result['csv_path']))
    indexes = [row[0] for row in rows[1:]]
    assert len(indexes) == len(set(indexes)) == 50


def test_duplicate_variation_changes_supported_rows():
    product_row = ['1'] + ['value'] * len(SCHEMA_TO_DICT['products'])
    changed_product = add_small_variation_to_duplicates(product_row, 'products')
    assert changed_product != product_row

    organization_row = ['1'] + ['Acme'] * len(SCHEMA_TO_DICT['organizations'])
    changed_organization = add_small_variation_to_duplicates(organization_row, 'organizations')
    assert changed_organization != organization_row

    lead_row = ['1'] + ['lead@example.com'] * len(SCHEMA_TO_DICT['leads'])
    changed_lead = add_small_variation_to_duplicates(lead_row, 'leads')
    assert changed_lead != lead_row


def test_ai_schema_generation_works_for_100_rows(tmp_path):
    scenarios = [GenerationScenario(schema, schema.replace('_', '-'), (100,), 'test') for schema in sorted(AI_SCHEMAS)]
    generated = generate_scenarios(scenarios, output_root=tmp_path)
    assert len(generated) == len(AI_SCHEMAS)
    for result in generated:
        rows = read_csv(Path(result['csv_path']))
        assert len(rows) == 101
        assert all(any(cell for cell in row[1:]) for row in rows[1:])


def test_support_and_review_ai_samples_have_many_text_variations(tmp_path):
    random.seed(123)
    scenarios = [
        GenerationScenario('support_tickets', 'support-tickets', (10000,), 'test'),
        GenerationScenario('customer_reviews', 'customer-reviews', (10000,), 'test'),
    ]
    generated = generate_scenarios(scenarios, output_root=tmp_path)
    thresholds = {
        'support_tickets': ('Ticket Text', 9500),
        'customer_reviews': ('Review Text', 9000),
    }
    for result in generated:
        rows = read_csv(Path(result['csv_path']))
        header, minimum_unique = thresholds[result['schema']]
        text_index = rows[0].index(header)
        unique_texts = {row[text_index] for row in rows[1:]}
        assert len(unique_texts) >= minimum_unique


def test_ai_schemas_do_not_emit_expected_columns(tmp_path):
    scenarios = [GenerationScenario(schema, schema.replace('_', '-'), (100,), 'test') for schema in sorted(AI_SCHEMAS)]
    generated = generate_scenarios(scenarios, output_root=tmp_path)
    for result in generated:
        rows = read_csv(Path(result['csv_path']))
        assert all(not header.startswith('Expected') for header in rows[0])


def test_research_and_web_ai_rows_use_real_urls(tmp_path):
    scenarios = [
        GenerationScenario('research_questions_ai', 'research-questions-ai', (100,), 'test'),
        GenerationScenario('web_page_extraction_ai', 'web-page-extraction-ai', (100,), 'test'),
        GenerationScenario('messy_company_data', 'messy-company-data', (1000,), 'test'),
        GenerationScenario('lead_scoring_ai', 'lead-scoring-ai', (100,), 'test'),
    ]
    generated = generate_scenarios(scenarios, output_root=tmp_path)
    real_domains = {company['domain'] for company in REAL_COMPANY_PROFILES}
    real_company_websites = {company['website'] for company in REAL_COMPANY_PROFILES}
    real_research_urls = {
        url
        for company in REAL_COMPANY_PROFILES
        for url in (company['website'], company['pricing_url'], company['careers_url'])
    }
    real_web_page_urls = {page['url'] for page in REAL_WEB_PAGES}

    for result in generated:
        rows = read_csv(Path(result['csv_path']))
        headers = rows[0]
        if result['schema'] == 'research_questions_ai':
            domain_index = headers.index('Domain')
            source_url_index = headers.index('Source URL')
            assert {row[domain_index] for row in rows[1:]} <= real_domains
            assert {row[source_url_index] for row in rows[1:]} <= real_research_urls
        if result['schema'] == 'web_page_extraction_ai':
            url_index = headers.index('URL')
            assert {row[url_index] for row in rows[1:]} <= real_web_page_urls
        if result['schema'] == 'messy_company_data':
            website_index = headers.index('Website')
            country_index = headers.index('Country')
            created_date_index = headers.index('Created Date')
            last_activity_index = headers.index('Last Activity Date')
            renewal_date_index = headers.index('Renewal Date')
            employee_count_index = headers.index('Employee Count')
            revenue_index = headers.index('Annual Revenue')
            lead_score_index = headers.index('Lead Score')
            websites = [row[website_index] for row in rows[1:]]
            countries = [row[country_index] for row in rows[1:]]
            date_values = [row[index] for row in rows[1:] for index in (created_date_index, last_activity_index, renewal_date_index)]
            employee_counts = [row[employee_count_index] for row in rows[1:]]
            revenues = [row[revenue_index] for row in rows[1:]]
            lead_scores = [row[lead_score_index] for row in rows[1:]]
            assert any(website.startswith(('http://', 'https://')) for website in websites)
            assert any(website and not website.strip().startswith(('http://', 'https://')) for website in websites)
            assert any('/' in website.replace('https://', '').replace('http://', '') for website in websites)
            assert any(country.strip() in {'US', 'CA', 'AU'} for country in countries)
            assert any(country in {'United States', 'Canada', 'Australia'} for country in countries)
            assert any('T' in value and value.endswith('Z') for value in date_values)
            assert any('/' in value for value in date_values)
            assert any(value.startswith('Q') for value in date_values)
            assert any(value.isdigit() and len(value) == 5 for value in date_values)
            assert any('-' in value for value in employee_counts)
            assert any(value.endswith('+') for value in employee_counts)
            assert any(value.isdigit() for value in employee_counts)
            assert any(value.startswith(('$', '€', 'USD')) for value in revenues)
            assert any(value in {'unknown', 'n/a', 'Confidential', ''} for value in revenues)
            assert any('/100' in value for value in lead_scores)
            assert any(value.endswith('%') for value in lead_scores)
            assert any(value in {'hot', 'warm', 'cold', 'high intent', 'needs review'} for value in lead_scores)
        if result['schema'] == 'lead_scoring_ai':
            website_index = headers.index('Website')
            assert {row[website_index] for row in rows[1:]} <= real_company_websites


def test_product_translation_ai_has_realistic_copy_for_translation(tmp_path):
    result = generate_file('product_translation_ai', 'product-translation-ai-test', 1000, output_root=tmp_path)
    rows = read_csv(Path(result['csv_path']))
    headers = rows[0]
    description_index = headers.index('Product Description')
    bullets_index = headers.index('Feature Bullets')
    product_name_index = headers.index('Product Name')
    seo_title_index = headers.index('SEO Title')
    source_language_index = headers.index('Source Language')
    target_language_index = headers.index('Target Language')
    instructions_index = headers.index('Translation Instructions')
    do_not_translate_index = headers.index('Do Not Translate')

    assert len(rows) == 1001
    for row in rows[1:]:
        description = row[description_index]
        source_text = " ".join([
            row[product_name_index],
            row[description_index],
            row[bullets_index],
            row[seo_title_index],
        ])
        assert row[source_language_index] == 'English'
        assert row[target_language_index] in TRANSLATION_TARGET_LANGUAGES
        assert len(description.split()) >= 30
        assert description.count('.') >= 2
        assert ' | ' in row[bullets_index]
        assert 'Translate' in row[instructions_index] or 'Use' in row[instructions_index]
        assert ';' in row[do_not_translate_index]
        protected_terms = [term.strip() for term in row[do_not_translate_index].split(';')]
        assert all(term in source_text for term in protected_terms)

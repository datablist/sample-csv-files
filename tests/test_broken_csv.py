import csv
from pathlib import Path

import pytest

from broken_csv import generate_broken_csv_fixtures


def test_broken_csv_manifest_matches_generated_files(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    assert len(manifest) == 12
    for item in manifest:
        assert Path(item['broken_path']).exists()
        assert item['issue_type']
        assert item['expected_parser_symptom']
        assert item['suggested_repair']
        if item['has_expected_fixed_file']:
            assert Path(item['expected_fixed_path']).exists()


def test_expected_fixed_files_parse_with_csv_module(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    for item in manifest:
        if not item['has_expected_fixed_file']:
            continue
        with open(item['expected_fixed_path'], newline='', encoding='utf-8') as f:
            rows = list(csv.reader(f))
        assert len(rows) >= 2
        width = len(rows[0])
        assert all(len(row) == width for row in rows)


def test_encoding_fixtures_fail_when_decoded_as_utf8(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    by_name = {item['file_name']: item for item in manifest}
    for name in ['broken-encoding-windows-1252.csv', 'broken-encoding-latin1.csv']:
        with pytest.raises(UnicodeDecodeError):
            Path(by_name[name]['broken_path']).read_text(encoding='utf-8')


def test_ragged_rows_show_row_length_mismatch(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    by_name = {item['file_name']: item for item in manifest}
    for name in ['ragged-rows-extra-columns.csv', 'ragged-rows-missing-columns.csv', 'mixed-delimiters.csv']:
        with open(by_name[name]['broken_path'], newline='', encoding='utf-8') as f:
            rows = list(csv.reader(f))
        width = len(rows[0])
        assert any(len(row) != width for row in rows[1:])


def test_missing_closing_quote_errors_in_strict_parser(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    item = next(entry for entry in manifest if entry['file_name'] == 'missing-closing-quote.csv')
    with open(item['broken_path'], newline='', encoding='utf-8') as f:
        reader = csv.reader(f, strict=True)
        with pytest.raises(csv.Error):
            list(reader)


def test_duplicate_headers_fixture_has_duplicate_header(tmp_path):
    manifest = generate_broken_csv_fixtures(tmp_path)
    item = next(entry for entry in manifest if entry['file_name'] == 'duplicate-headers.csv')
    with open(item['broken_path'], newline='', encoding='utf-8') as f:
        header = next(csv.reader(f))
    assert len(header) != len(set(header))

from pathlib import Path
from typing import Dict, List, Optional
import csv
import json

BROKEN_FIXTURE_DIR = "broken_csv"
EXPECTED_FIXED_DIR = "expected-fixed"


def _write_text(path: Path, text: str, encoding: str = "utf-8", newline: Optional[str] = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding=encoding, newline=newline) as f:
        f.write(text)


def _write_bytes(path: Path, content: str, encoding: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content.encode(encoding))


def _write_fixed(path: Path, rows: List[List[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def _fixture_definitions() -> List[Dict]:
    return [
        {
            "file_name": "broken-encoding-windows-1252.csv",
            "issue_type": "windows_1252_encoding",
            "expected_parser_symptom": "Opening as UTF-8 raises UnicodeDecodeError or shows mojibake for smart quotes and euro signs.",
            "suggested_repair": "Decode as Windows-1252 and re-export as UTF-8.",
            "content": "id,name,city,notes\n1,François,Montréal,“Premium” customer €\n2,Anaïs,Zürich,Renews in Q4\n",
            "encoding": "cp1252",
            "fixed_rows": [["id", "name", "city", "notes"], ["1", "François", "Montréal", "“Premium” customer €"], ["2", "Anaïs", "Zürich", "Renews in Q4"]],
        },
        {
            "file_name": "broken-encoding-latin1.csv",
            "issue_type": "latin1_encoding",
            "expected_parser_symptom": "Opening as UTF-8 raises UnicodeDecodeError or corrupts accented Western European names.",
            "suggested_repair": "Decode as ISO-8859-1 and re-export as UTF-8.",
            "content": "id,name,country\n1,José,España\n2,André,France\n3,Müller,Deutschland\n",
            "encoding": "iso-8859-1",
            "fixed_rows": [["id", "name", "country"], ["1", "José", "España"], ["2", "André", "France"], ["3", "Müller", "Deutschland"]],
        },
        {
            "file_name": "mixed-delimiters.csv",
            "issue_type": "mixed_delimiters",
            "expected_parser_symptom": "Some rows parse into one column or the wrong number of columns.",
            "suggested_repair": "Detect row-level delimiters and normalize all rows to commas.",
            "content": "id,name,email\n1,Alice,alice@example.com\n2;Bob;bob@example.com\n3\tCara\tcara@example.com\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", "bob@example.com"], ["3", "Cara", "cara@example.com"]],
        },
        {
            "file_name": "wrong-delimiter-semicolon.csv",
            "issue_type": "semicolon_delimiter",
            "expected_parser_symptom": "Parsing as comma CSV returns one column per row.",
            "suggested_repair": "Detect semicolon as delimiter or let the user select it.",
            "content": "id;name;email\n1;Alice;alice@example.com\n2;Bob;bob@example.com\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", "bob@example.com"]],
        },
        {
            "file_name": "unescaped-quotes.csv",
            "issue_type": "unescaped_quotes",
            "expected_parser_symptom": "Quotes inside a value are not doubled and can corrupt parsing in strict CSV readers.",
            "suggested_repair": "Escape inner quotes by doubling them.",
            "content": 'id,company,notes\n1,Datablist,"He said "clean the file first" yesterday"\n2,Example Corp,Valid row\n',
            "fixed_rows": [["id", "company", "notes"], ["1", "Datablist", "He said \"clean the file first\" yesterday"], ["2", "Example Corp", "Valid row"]],
        },
        {
            "file_name": "missing-closing-quote.csv",
            "issue_type": "missing_closing_quote",
            "expected_parser_symptom": "Strict CSV parsing raises a quote error or merges following lines into one field.",
            "suggested_repair": "Find unterminated quoted fields and close or escape the value.",
            "content": 'id,name,notes\n1,Alice,"Started import yesterday\n2,Bob,Valid row\n',
            "fixed_rows": [["id", "name", "notes"], ["1", "Alice", "Started import yesterday"], ["2", "Bob", "Valid row"]],
        },
        {
            "file_name": "newline-inside-unquoted-field.csv",
            "issue_type": "newline_inside_unquoted_field",
            "expected_parser_symptom": "A single record is split into several rows.",
            "suggested_repair": "Quote multiline text fields or join continuation lines.",
            "content": "id,name,notes\n1,Alice,First line\nsecond line should be same field\n2,Bob,Valid row\n",
            "fixed_rows": [["id", "name", "notes"], ["1", "Alice", "First line\nsecond line should be same field"], ["2", "Bob", "Valid row"]],
        },
        {
            "file_name": "ragged-rows-extra-columns.csv",
            "issue_type": "extra_columns",
            "expected_parser_symptom": "Some rows have more fields than the header.",
            "suggested_repair": "Detect delimiter inside unquoted values or map overflow columns.",
            "content": "id,name,email\n1,Alice,alice@example.com\n2,Bob,bob@example.com,unexpected\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", "bob@example.com"]],
        },
        {
            "file_name": "ragged-rows-missing-columns.csv",
            "issue_type": "missing_columns",
            "expected_parser_symptom": "Some rows have fewer fields than the header.",
            "suggested_repair": "Pad missing trailing fields with empty values or reject incomplete rows.",
            "content": "id,name,email\n1,Alice,alice@example.com\n2,Bob\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", ""]],
        },
        {
            "file_name": "bom-and-whitespace-headers.csv",
            "issue_type": "bom_and_whitespace_headers",
            "expected_parser_symptom": "First header contains a BOM and headers include invisible leading or trailing spaces.",
            "suggested_repair": "Strip UTF-8 BOM and trim header names.",
            "content": "\ufeff id , name , email \n1,Alice,alice@example.com\n2,Bob,bob@example.com\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", "bob@example.com"]],
        },
        {
            "file_name": "mixed-line-endings.csv",
            "issue_type": "mixed_line_endings",
            "expected_parser_symptom": "Line counting and parsers can disagree because LF, CRLF, and CR are mixed.",
            "suggested_repair": "Normalize line endings to LF or CRLF.",
            "content": "id,name,email\n1,Alice,alice@example.com\r\n2,Bob,bob@example.com\r3,Cara,cara@example.com\n",
            "fixed_rows": [["id", "name", "email"], ["1", "Alice", "alice@example.com"], ["2", "Bob", "bob@example.com"], ["3", "Cara", "cara@example.com"]],
        },
        {
            "file_name": "duplicate-headers.csv",
            "issue_type": "duplicate_headers",
            "expected_parser_symptom": "Column mapping is ambiguous because two columns share the same name.",
            "suggested_repair": "Rename duplicate headers with stable suffixes such as Email 1 and Email 2.",
            "content": "id,name,Email,Email\n1,Alice,alice@example.com,alice@work.com\n2,Bob,bob@example.com,bob@work.com\n",
            "fixed_rows": [["id", "name", "Email 1", "Email 2"], ["1", "Alice", "alice@example.com", "alice@work.com"], ["2", "Bob", "bob@example.com", "bob@work.com"]],
        },
    ]


def generate_broken_csv_fixtures(output_root: Optional[Path] = None, overwrite: bool = False) -> List[Dict[str, object]]:
    base_output = output_root or (Path(__file__).parent / "../files")
    fixture_dir = base_output / BROKEN_FIXTURE_DIR
    fixed_dir = fixture_dir / EXPECTED_FIXED_DIR
    manifest = []

    for fixture in _fixture_definitions():
        broken_path = fixture_dir / fixture["file_name"]
        if overwrite or not broken_path.exists():
            if fixture.get("encoding"):
                _write_bytes(broken_path, fixture["content"], fixture["encoding"])
            else:
                _write_text(broken_path, fixture["content"], encoding="utf-8", newline="")

        fixed_path = None
        if fixture.get("fixed_rows"):
            fixed_path = fixed_dir / fixture["file_name"]
            if overwrite or not fixed_path.exists():
                _write_fixed(fixed_path, fixture["fixed_rows"])

        manifest.append({
            "file_name": fixture["file_name"],
            "issue_type": fixture["issue_type"],
            "expected_parser_symptom": fixture["expected_parser_symptom"],
            "suggested_repair": fixture["suggested_repair"],
            "broken_path": str(broken_path),
            "expected_fixed_path": str(fixed_path) if fixed_path else "",
            "has_expected_fixed_file": bool(fixed_path),
            "google_drive_broken_csv_id": "",
            "google_drive_fixed_csv_id": "",
        })

    manifest_path = fixture_dir / "broken_csv_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    generate_broken_csv_fixtures()

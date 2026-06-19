from generators import TYPES_TO_GENERATORS
from main import SCHEMA_TO_DICT


def test_schema_fields_have_name_and_type():
    for schema_name, fields in SCHEMA_TO_DICT.items():
        for field in fields:
            assert field.get("name"), f"{schema_name} field missing name"
            assert field.get("type"), f"{schema_name} field missing type"


def test_schema_types_have_generators():
    missing = []
    for schema_name, fields in SCHEMA_TO_DICT.items():
        for field in fields:
            if field["type"] not in TYPES_TO_GENERATORS:
                missing.append((schema_name, field["name"], field["type"]))
    assert missing == []


def test_schema_field_names_are_unique():
    for schema_name, fields in SCHEMA_TO_DICT.items():
        names = [field["name"] for field in fields]
        assert len(names) == len(set(names)), schema_name


def test_unique_generators_do_not_collide_on_small_sample():
    for schema_name, fields in SCHEMA_TO_DICT.items():
        for field in fields:
            if not field.get("unique"):
                continue
            generator = TYPES_TO_GENERATORS[field["type"]]
            values = {generator() for _ in range(25)}
            assert len(values) == 25, f"{schema_name}.{field['name']} generated duplicate values"

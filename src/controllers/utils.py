import jsonschema
from src.errors import ValidationError


def validate_schema(data: dict, schema: dict):
    # NOTE: we are simply mapping jsonschema exceptions
    # to internally defined ones
    try:
        jsonschema.validate(data, schema)
    except jsonschema.ValidationError as e:
        raise ValidationError(e.message)

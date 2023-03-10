from jsonschema import validate
from API_test_v2.src.enums.global_enums import GlobalEnumError


class SampleApiCharacters:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_schema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self


    def __str__(self):
        return f'\nStatus code: {self.response_status_code}' \
               f'\nRequsted url: {self.response.url}'
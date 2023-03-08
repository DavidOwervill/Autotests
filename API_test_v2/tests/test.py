import requests
from API_test_v2.src.schemas.schema_sampleapi import CHARACTER_SCHEMA
from API_test_v2.base_classes.sampleapis_characters import SampleApiCharacters


class TestSampleApi:
    def test_get_characters(self):
        """
        Функция работает с сайтом sampleapis раздел персонажи, проверяет статус код и валидацию схемы, написанной вручную
        """
        response = requests.get("https://api.sampleapis.com/rickandmorty/characters")
        SampleApiCharacters(response).assert_status_code(200)
        SampleApiCharacters(response).validate_schema(CHARACTER_SCHEMA)


if __name__ == "__main__":
    requests.Session()
    TestSampleApi.test_get_characters()

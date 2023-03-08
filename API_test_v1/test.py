import requests
from src.enums.global_enums import GlobalEnumError


class TestSwagger:
    def test_pet_find_by_status(self):
        pass

    def test_pet_find_by_tags(self):
        pass

    def test_get_auth(self):
        response = requests.get("https://httpbin.org/status/200")
        assert response.status_code == 200, GlobalEnumError.WRONG_STATUS_CODE
        # assert response.json().get("authenticated") == "true"
        # assert response.json().get('user') == "Test"
        print(response.text)


if __name__ == "__main__":
    requests.Session()
    TestSwagger().test_get_auth()

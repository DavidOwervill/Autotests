import requests



class TestSwagger:
    def test_pet_find_by_status(self):
        pass

    def test_pet_find_by_tags(self):
        pass

    def test_get_auth(self):
        response = requests.get("https://httpbin.org/basic-auth/test/test")
        assert response.status_code == 401
        assert response.json().get("authenticated") == "true"
        assert response.json().get('user') == "Test"
        print(response.text)



if __name__ == "__main__":
    requests.Session()
    TestSwagger().test_get_auth()

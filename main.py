import pytest
import requests


class TestRegres:

    def test_ListUsers(self):
        self.response = requests.get('https://reqres.in/api/users?page=2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_SingleUser(self):
        self.response = requests.get('https://reqres.in/api/users/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_SingleUserNotFound(self):
        self.response = requests.get('https://reqres.in/api/users/23')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404

    def test_ListResource(self):
        self.response = requests.get('https://reqres.in/api/unknown')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_SingleResource(self):
        self.response = requests.get('https://reqres.in/api/unknown/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_SingleResourceNotFound(self):
        self.response = requests.get('https://reqres.in/api/unknown/23')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404


    @pytest.mark.parametrize("name,job",[("morpheus","leader")])
    def test_Create(self, name,job):
        url = 'https://reqres.in/api/users'
        json = {
            "name":name,
            "job":job
        }
        self.response = requests.post(url,json=json)
        assert self.response.status_code == 201


    @pytest.mark.parametrize("name,job",[("morpheus","zion resident")])
    def test_Update(self, name,job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "name":name,
            "job":job
        }
        self.response = requests.put(url,json=json)
        assert self.response.status_code == 200

    @pytest.mark.parametrize("name,job", [("morpheus", "zion resident")])
    def test_PatchUpdate(self, name, job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "name": name,
            "job": job
        }
        self.response = requests.patch(url, json=json)
        assert self.response.status_code == 200


    def test_DELETE(self):
        response = self.requests.delete('https://reqres.in/api/users/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 204

    @pytest.mark.parametrize("email,password", [("eve.holt@reqres.in", "pistol"), ("sydney@fife")])
    def test_Register(self, email, password):
        url = 'https://reqres.in/api/register'
        json = {
            "email": email,
            "password": password
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 200

    @pytest.mark.parametrize("email,password", [("eve.holt@reqres.in", "cityslicka"), ("peter@klaven")])
    def test_Login(self, email, password):
        url = 'https://reqres.in/api/login'
        json = {
            "email": email,
            "password": password
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 200

    def test_DelayedResponse(self):
        self.response = requests.get('https://reqres.in/api/users?delay=3')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
import requests
from requests.auth import HTTPBasicAuth

URL = "http://demo.universosigma.com.br/api/login?dbid=20"


def login(username: str, password: str):
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        URL, auth=HTTPBasicAuth(username, password), headers=headers
    )
    response_data = response.json()

    return response_data.get("success")


username = "teste@email.com"
password = "12345"

print(login(username, password))

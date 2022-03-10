import requests
from http import HTTPStatus
from scripts.helpers.env_to_dict import use_env
from shared.utils.constants import SERVER_URL

env = use_env()

headers = {
    'Authorization': env.secret_key
}

def main():
    response = requests.get(SERVER_URL, headers=headers)
    if response.status_code == HTTPStatus.OK:
        print('The server is healthy!')
    else:
        print('The server is not healthy! (Status Code : %d)' % response.status_code)

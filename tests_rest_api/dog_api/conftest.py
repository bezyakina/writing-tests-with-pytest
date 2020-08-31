import io
import json
import os
import re

import pytest
import requests
from PIL import Image


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(
            url=url, params=params, data=data, headers=headers
        )

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)


@pytest.fixture(scope="session")
def api_client(request):
    # base_url = request.config.getoption("--url")
    return APIClient(base_address="https://dog.ceo/api")


@pytest.fixture(scope="function")
def get_expected_response():
    tests_folder = os.path.dirname(os.path.abspath(__file__))
    responses_folder = os.path.join(tests_folder, "responses")

    def get_response_body(file_name):
        with open(os.path.join(responses_folder, file_name + ".json")) as f:
            response_body = json.load(f)
            return response_body

    return get_response_body


@pytest.fixture(scope="function")
def get_image_info():
    regex = r"https:[/|.|\w|\s|-]*\.(?:jpg|gif|png)"

    def get_image_info_from_response(response_body):
        image_urls = re.findall(regex, json.dumps(response_body))
        for image_url in image_urls:
            r = requests.get(image_url)
            image_bytes = io.BytesIO(r.content)
            image = Image.open(image_bytes)
            return image_url, image.format

    return get_image_info_from_response

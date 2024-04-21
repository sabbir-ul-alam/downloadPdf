import pytest
import json
from selenium import webdriver

@pytest.fixture()
def path():
    with open("../config.json","r") as config_file:
        config = json.load(config_file)
    yield config['base_url'],config['pdf_path']

@pytest.fixture
def browser():
    with open("../config.json","r") as config_file:
        config = json.load(config_file)

    if config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception (f'Broswer "{config["browser"]}" is not supported')

    yield driver

    driver.quit()
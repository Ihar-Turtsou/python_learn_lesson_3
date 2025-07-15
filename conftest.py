import pytest
from selenium import webdriver
from selene import Browser, Config

@pytest.fixture(scope='function', autouse=True)
def browser():
    driver = webdriver.Chrome()
    config = Config(
        driver=driver,
        base_url='https://www.ecosia.org',
        window_width=1280,
        window_height=800,
    )
    browser = Browser(config)
    yield browser
    browser.quit()
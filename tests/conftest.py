from datetime import datetime

import pytest
from selene import browser
from selenium import webdriver



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



@pytest.fixture(scope="function", autouse=True)
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    # driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options
    browser.config.type_by_js = True

    browser.config.window_height = 2500
    browser.config.window_width = 1400

    browser.config.base_url = "https://demoqa.com/automation-practice-form"

    yield

    browser.quit()


@pytest.fixture(scope="function")
def today_date():
    c = datetime.now()
    current_time = c.strftime("%d %B, %Y")
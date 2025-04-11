import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_site(setup):
    driver = setup
    driver.get("https://www.ajio.com/")

    element = driver.find_element(By.XPATH, "//span[@aria-label='MEN']")
    element.click()

    allure.attach("Test Passed Successfully", name="Test Result", attachment_type=allure.attachment_type.TEXT)




# allure generate allure-results --clean -o docs
# pytest test_check.py --alluredir=allure-results


# pytest test_main.py --alluredir=allure-results




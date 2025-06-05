import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("XEED_Ventures_Login_Page")
def test_site(setup):
    driver = setup

    with allure.step("Open Xeed Ventures Login Page"):
        driver.get("http://157.15.202.244:88/authentication/login")

    with allure.step("Click on username field"):
        element = driver.find_element(By.XPATH, "//input[@id='username']")
        element.click()

    with allure.step("Type in the username"):
        element.send_keys("Rohit")

    with allure.step("Click on password field"):
        element = driver.find_element(By.XPATH, "//input[@id='password']")
        element.send_keys("Erp@123")
        element.click()

    with allure.step("Press Login"):
        element = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        element.click()


    allure.attach("Test Passed Successfully", name="Test Result", attachment_type=allure.attachment_type.TEXT)


# Follow these

# pytest test_check.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "First Commit"
# git push origin main

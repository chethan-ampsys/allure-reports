import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    wait = WebDriverWait(driver, 10)  # 10 seconds explicit wait

    with allure.step("Open Xeed Ventures Login Page"):
        driver.get("http://157.15.202.244:88/authentication/login")

    with allure.step("Wait for and click on username field"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
        element.click()

    with allure.step("Type in the username"):
        element.send_keys("Rohit")

    with allure.step("Wait for and click on password field"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.click()
        element.send_keys("Erp@123")

    with allure.step("Wait for and press Login button"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        element.click()

    time.sleep(10)

    allure.attach("Test Passed Successfully", name="Test Result", attachment_type=allure.attachment_type.TEXT)

# Follow these

# pytest Xeed_Login_Page/Test_TC001.py --alluredir=allure-results
# pytest test_check.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "First Commit"
# git push origin main

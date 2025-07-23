import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

__all__ = ["allure", "time", "By", "WebDriverWait", "EC"]

@pytest.fixture(params=["firefox", "chrome", "edge"])
def setup(request):
    browser = request.param
    if browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def punk(setup):  # setup is your driver
    def _punk(allure_text, xpath, keys, wait_time=10):
        with allure.step(allure_text):
            wait = WebDriverWait(setup, wait_time)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            if keys:  # only send_keys if non-empty string is passed
                element.send_keys(keys)
    return _punk

@pytest.fixture
def login_user(punk, setup):
    def _login():
        setup.get("http://157.15.202.244:99/authentication/login")

        punk("Waiting until the username field is displayed and it is clicked", "//input[@id='email']", "Sk12@gmail.com")
        punk("Waiting until the password field is displayed", "//input[@id='password']", "Sk@123")
        punk("Clicking the login button", "//button[normalize-space()='Login']", "")

        WebDriverWait(setup, 10).until(EC.url_contains("/dashboard"))
        assert "/dashboard" in setup.current_url, "Login failed — dashboard not reached."

    return _login




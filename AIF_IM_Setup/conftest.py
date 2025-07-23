import pytest
import allure
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
def textfield(setup):
    def _textfield(allure_text, xpath, keys, wait_time=10):
        with allure.step(allure_text):
            wait = WebDriverWait(setup, wait_time)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            if keys:
                element.send_keys(keys)
    return _textfield

@pytest.fixture
def dropdown(setup):
    def _dropdown(allure_text, select_xpath, option_text, wait_time=10):
        with allure.step(allure_text):
            wait = WebDriverWait(setup, wait_time)
            dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, select_xpath)))
            select = Select(dropdown_element)
            select.select_by_visible_text(option_text)
    return _dropdown

@pytest.fixture
def calendar(setup):
    def _calendar(allure_text, input_xpath, date_str, wait_time=10):
        with allure.step(allure_text):
            wait = WebDriverWait(setup, wait_time)
            date_input = wait.until(EC.element_to_be_clickable((By.XPATH, input_xpath)))
            date_input.clear()
            date_input.send_keys(date_str)  # Format: yyyy-mm-dd
    return _calendar

@pytest.fixture
def clicker(setup):
    def _clicker(allure_text, xpath, wait_time=10):
        with allure.step(allure_text):
            wait = WebDriverWait(setup, wait_time)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
    return _clicker

@pytest.fixture
def login(textfield, setup):
    def _login():
        setup.get("http://157.15.202.244:99/authentication/login")

        textfield("Waiting until the username field is displayed", "//input[@id='email']", "Sk12@gmail.com")
        textfield("Waiting until the password field is displayed", "//input[@id='password']", "Sk@123")
        textfield("Clicking the login button", "//button[normalize-space()='Login']", "")

        WebDriverWait(setup, 10).until(EC.url_contains("/dashboard"))
        assert "/dashboard" in setup.current_url, "Login failed — dashboard not reached."

    return _login

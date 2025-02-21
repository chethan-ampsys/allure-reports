import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAutomation:

    @allure.feature('Login Tests')
    @allure.story('Test login functionality with credentials')
    def test_login(self):
        # Hardcoded credentials for testing
        username = "abccompany"
        password = "abc1234$"

        allure.attach(f"Testing with Username: {username} and Password: {password}", name="Login Test Parameters", attachment_type=allure.attachment_type.TEXT)
        allure.attach("Testcase: Username: abccompany, password: abc1234$")

        self.driver.get("http://157.15.202.244:81/")

        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))

        self.wait.until(EC.visibility_of_element_located((By.ID, "ctrl_Userlogin_txtLoginId"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.ID, "ctrl_Userlogin_txtPassword"))).send_keys(password)
        self.wait.until(EC.visibility_of_element_located((By.ID, "ctrl_Userlogin_btnSignIn"))).click()





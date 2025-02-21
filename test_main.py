import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

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
    def test_login(self):
        self.driver.get("http://157.15.202.244:81/")
        print("Page Title:", self.driver.title)
        print("Current URL:", self.driver.current_url)

        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_txtLoginId']"))).send_keys("abccompany")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_txtPassword']"))).send_keys("abc1234$")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_btnSignIn']"))).click()

        time.sleep(5)
        self.driver.save_screenshot("login_success.png")
        print("Login Successful")

    def test_addcustomer(self):
        self.test_login()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))

        client_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ctrl_IFAAdminMainDashboard_imgClientsClick']")))
        self.driver.execute_script("arguments[0].click();", client_button)
        time.sleep(15)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='leftframe']"))))

        add_customer_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add Customer')]")))
        self.driver.execute_script("arguments[0].click();", add_customer_button)
        time.sleep(6)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))

        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_rbtnNonIndividual"))).click()
        time.sleep(6)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_rbtnIndividual"))).click()
        time.sleep(2)

        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlAdviserBranchList")).select_by_visible_text('RASHMITA')
        time.sleep(2)
        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlAdviseRMList")).select_by_visible_text('Amar Singh')
        time.sleep(2)
        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlCustomerSubType")).select_by_visible_text('Resident')
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtPanNumber"))).send_keys("BDJPC1234Z")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_chkdummypan"))).click()
        time.sleep(2)

        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlSalutation")).select_by_visible_text('Mr.')
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtFirstName"))).send_keys("John")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtLastName"))).send_keys("Wick")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtEmail"))).send_keys("johnwickmustang@gmail.com")
        time.sleep(2)

        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlCustomerCategory")).select_by_visible_text('super hni')
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtDpName1"))).send_keys("John Wick")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtDpId1"))).send_keys("87524695")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.NAME, "ctrl_CustomerType$txtBeneficiaryNo1"))).send_keys("5246389574265")
        time.sleep(2)

        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlDepositoryName1")).select_by_visible_text('CDSL')
        time.sleep(2)
        Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlDpCategory1")).select_by_visible_text('PMS')
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_btnSubmit"))).click()
        time.sleep(15)

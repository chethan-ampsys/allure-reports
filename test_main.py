import pytest
import allure
import av
import threading
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import subprocess

VIDEO_FILE = "test_execution.mp4"
recording = True
ffmpeg_process = None

def start_recording():
    global recording, ffmpeg_process
    command = [
        "ffmpeg", "-y", "-video_size", "1920x1080", "-framerate", "30",
        "-f", "gdigrab", "-i", "desktop",
        "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        VIDEO_FILE
]
    ffmpeg_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    while recording:
        time.sleep(1)

def stop_recording():
    global ffmpeg_process
    if ffmpeg_process:
        try:
            ffmpeg_process.stdin.write(b"q\n")
            ffmpeg_process.stdin.flush()
        except Exception as e:
            print(f"Error sending 'q' to FFmpeg: {e}")
        ffmpeg_process.wait()
        time.sleep(2)
        ffmpeg_process = None


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global recording
    recording = True

    recorder_thread = threading.Thread(target=start_recording, daemon=True)
    recorder_thread.start()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    with allure.step("Opening the login page"):
        driver.get("http://157.15.202.244:81/")

    with allure.step("Logging into the application"):
        driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))

        login_details = {
            "Username": "abccompany",
            "Password": "abc1234$"
        }
        allure.attach(json.dumps(login_details, indent=4), name="Login Parameters", attachment_type=allure.attachment_type.JSON)

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_txtLoginId']"))).send_keys(login_details["Username"])
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_txtPassword']"))).send_keys(login_details["Password"])
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ctrl_Userlogin_btnSignIn']"))).click()

    time.sleep(5)
    screenshot_path = "login_success.png"
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

    yield

    driver.quit()
    recording = False
    stop_recording()

    allure.attach.file(VIDEO_FILE, name="Test Execution Video", attachment_type=allure.attachment_type.MP4)

@pytest.mark.usefixtures("setup")
class TestAutomation:

    @allure.title("Test to Add a New Customer")
    def test_addcustomer(self):
        with allure.step("Navigating to 'Add Customer' page"):
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))
            client_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ctrl_IFAAdminMainDashboard_imgClientsClick']")))
            self.driver.execute_script("arguments[0].click();", client_button)
            time.sleep(10)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='leftframe']"))))
            add_customer_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add Customer')]")))
            self.driver.execute_script("arguments[0].click();", add_customer_button)
            time.sleep(6)

        customer_details = {
            "Branch": "RASHMITA",
            "Relationship Manager": "Amar Singh",
            "Customer Subtype": "Resident",
            "PAN Number": "BWRGE1234Z",
            "Salutation": "Mr.",
            "First Name": "John",
            "Last Name": "Wick",
            "Email": "johnwickmustang@gmail.com",
            "Customer Category": "super hni",
            "Demat Name" : "John Wick",
            "DP ID" : '14785236',
            "Beneficiary Acc No" : "1478523691234",
            "Depository": 'CDSL',
            "Equity": "PMS"
        }
        allure.attach(json.dumps(customer_details, indent=4), name="Customer Details", attachment_type=allure.attachment_type.JSON)

        with allure.step("Filling out the customer details form"):
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mainframe']"))))

            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_rbtnNonIndividual"))).click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_rbtnIndividual"))).click()
            time.sleep(2)

            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlAdviserBranchList")).select_by_visible_text(customer_details["Branch"])
            time.sleep(2)
            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlAdviseRMList")).select_by_visible_text(customer_details["Relationship Manager"])
            time.sleep(2)
            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlCustomerSubType")).select_by_visible_text(customer_details["Customer Subtype"])
            time.sleep(2)

            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtPanNumber"))).send_keys(customer_details["PAN Number"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_chkdummypan"))).click()
            time.sleep(2)

            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlSalutation")).select_by_visible_text(customer_details["Salutation"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtFirstName"))).send_keys(customer_details["First Name"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtLastName"))).send_keys(customer_details["Last Name"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtEmail"))).send_keys(customer_details["Email"])
            time.sleep(2)
            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlCustomerCategory")).select_by_visible_text(customer_details["Customer Category"])
            time.sleep(2)

            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtDpName1"))).send_keys(customer_details["Demat Name"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtDpId1"))).send_keys(customer_details["DP ID"])
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_txtBeneficiaryNo1"))).send_keys(customer_details["Beneficiary Acc No"])
            time.sleep(2)

            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlDepositoryName1")).select_by_visible_text(customer_details["Depository"])
            time.sleep(2)

            Select(self.driver.find_element(By.NAME, "ctrl_CustomerType$ddlDpCategory1")).select_by_visible_text(customer_details["Equity"])
            time.sleep(2)

        with allure.step("Finalizing and Submitting the Form"):
            self.wait.until(EC.element_to_be_clickable((By.ID, "ctrl_CustomerType_btnSubmit"))).click()
            time.sleep(10)

        screenshot_path = "add_customer_success.png"
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Add Customer Screenshot", attachment_type=allure.attachment_type.PNG)

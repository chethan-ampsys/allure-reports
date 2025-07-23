from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC011 - Validating 'Passwords do not match' text for mismatched inputs")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**  
Verify that the system displays the message **Passwords do not match** when the values in the **New Password** and **Confirm Password** fields are different.

**Expected Result**  
An appropriate error message should be shown, and the password should not be reset.

**How it is evaluated**  
The test checks if the 'Passwords do not match' message is displayed on the screen.

**Test will pass if**  
The system correctly shows the 'Passwords do not match' error message and prevents password reset.
""")
def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Locating email input in the popup"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        element.click()

    with allure.step("Entering the email"):
        element.send_keys("Sk11@gmail.com")

    with allure.step("Locating new password input"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='newPassword']")))

    with allure.step("Entering the new password"):
        element.send_keys("Sk@123")

    with allure.step("Locating confirm password input"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='confirmPassword']")))

    with allure.step("Entering a different password"):
        element.send_keys("Sk@125")

    with allure.step("Clicking the Submit button"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
        element.click()

    with allure.step("Validating 'Passwords do not match' error message is displayed"):
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'error') and contains(text(), 'Passwords do not match')]")
        ))
        assert "Passwords do not match" in element.text
        allure.attach(element.text, name="Displayed Message", attachment_type=allure.attachment_type.TEXT)

#pytest Xeed_Login_Page/Test_TC011.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

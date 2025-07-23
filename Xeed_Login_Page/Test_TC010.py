from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC010 - Validating 'Password Reset Failed' for invalid email")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**  
Verify that the system displays the 'Password Reset Failed' message when an invalid email is used to reset the password.

**Expected Result**  
The password should not be changed, and an appropriate error message should be shown.

**How it is evaluated**  
The test checks if the 'Password Reset Failed' message is visible on the screen.

**Test will pass if**  
The password is not reset and the 'Password Reset Failed' message is displayed correctly.
""")
def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Reaching the email input in the Forgot Password popup"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        element.click()

    with allure.step("Entering an invalid email"):
        element.send_keys("Sk11@gmail.com")

    with allure.step("Reaching the new password input"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='newPassword']")))

    with allure.step("Entering a new password"):
        element.send_keys("Sk@123")

    with allure.step("Reaching the confirm password input"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='confirmPassword']")))

    with allure.step("Entering the same password for confirmation"):
        element.send_keys("Sk@123")

    with allure.step("Clicking the Submit button"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
        element.click()

    with allure.step("Validating the error message 'Password Reset Failed' is displayed"):
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Password Reset Failed']")))
        assert "Password Reset Failed" in element.text, "Expected error message not found"
        allure.attach(element.text, name="Displayed Message", attachment_type=allure.attachment_type.TEXT)

#pytest Xeed_Login_Page/Test_TC010.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main


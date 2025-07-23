from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC009 - Verify login is not allowed using old password after reset")
@allure.description("""
**Test Type**  
Functional and cross-browser

**Test Scenario**  
After resetting the password using the 'Forgot Password' feature, try logging in with the old password to ensure it no longer works.

**Expected Result**  
The user should not be able to log in using the old password.

**How it is evaluated**  
After attempting login with the old password, the system should display a snack bar message: `'Login failed: Invalid credentials'`.

**Test will pass if**  
The login fails and the appropriate error message is displayed on the screen.
""")

def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Opening the Login Page"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Entering email in the forgot password popup"):
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        email_field.click()
        email_field.send_keys("Sk12@gmail.com")

    with allure.step("Entering a new password"):
        new_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='newPassword']")))
        new_password_field.send_keys("Sk@123")

    with allure.step("Confirming the new password"):
        confirm_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='confirmPassword']")))
        confirm_password_field.send_keys("Sk@123")

    with allure.step("Submitting the password reset form"):
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
        submit_button.click()

    with allure.step("Closing the successful password reset popup"):
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[@role='img']")))
        close_button.click()

    with allure.step("Entering login email"):
        login_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        login_email.click()
        login_email.send_keys("Sk12@gmail.com")

    with allure.step("Entering the old password"):
        login_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        login_password.send_keys("Sk@123654")

    with allure.step("Clicking on 'Login' button"):
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        login_button.click()

    with allure.step("Validating login failure message on snack bar"):
        snack_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']")))
        assert "Login failed: Invalid credentials" in snack_bar.text
        allure.attach(snack_bar.text, name="Error Message", attachment_type=allure.attachment_type.TEXT)

#pytest Xeed_Login_Page/Test_TC009.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

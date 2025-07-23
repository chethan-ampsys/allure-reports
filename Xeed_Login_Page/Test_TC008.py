from conftest import allure, By, WebDriverWait, EC, time

@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC008 - Verify Forgot Password Functionality")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**  
Reset the password using the 'Forgot Password' functionality, and then attempt to log in with the newly set password.

**Expected Result**  
The user should be able to log in successfully with the new password created via the 'Forgot Password' feature.

**How it is evaluated**  
After resetting the password, the test will attempt to log in with the updated credentials. Success is confirmed by checking whether the user is redirected to the dashboard URL.

**Test will pass if**  
The system accepts the new password and successfully redirects the user to the dashboard.
""")

def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Opening the Login Page"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Entering email in the popup"):
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
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close-button']")))
        close_button.click()

    with allure.step("Entering login email"):
        login_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        login_email.click()
        login_email.send_keys("Sk12@gmail.com")

    with allure.step("Entering the new password"):
        login_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        login_password.send_keys("Sk@123")

    with allure.step("Clicking on 'Login' button"):
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        login_button.click()

    with allure.step("Waiting for navigation to Dashboard"):
        try:
            wait.until(EC.url_contains("/dashboard"))
        except:
            allure.attach(driver.current_url, name="Current URL on Failure", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Login failed — URL did not change to Dashboard.")

    with allure.step("Test Passed"):
        allure.attach("User successfully logged in with the new password.", name="Test Result", attachment_type=allure.attachment_type.TEXT)

#pytest Xeed_Login_Page/Test_TC008.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

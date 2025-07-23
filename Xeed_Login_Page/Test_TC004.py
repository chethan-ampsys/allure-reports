from conftest import allure, By, WebDriverWait, EC, time

@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC004 - Login with Invalid Credentials")
@allure.description("""
**Test Scenario:**  
Attempt to log in using an invalid credentials  
Username: Ohitr
Password: 9902@KM

**Expected Result:**  
User should not be able to log in.

**How it is evaluated:**  
The login is considered failed if a snackbar displays the message **Login failed: Invalid credentials**.
""")

def test_site(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is Opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Entering invalid email"):
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        email_field.click()
        email_field.send_keys("Ohitr")

    with allure.step("Entering the invalid password"):
        password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_field.click()
        password_field.send_keys("9902@KM")

    with allure.step("Clicking the Login button"):
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        login_button.click()

    with allure.step("Validating error message for failed login"):
        snackbar = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']")))
        assert "Login failed: Invalid credentials" in snackbar.text
        allure.attach(snackbar.text, name="Login failed", attachment_type=allure.attachment_type.TEXT)


# pytest Xeed_Login_Page/Test_TC004.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

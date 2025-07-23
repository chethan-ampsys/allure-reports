from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC015 - Testing the Passwords do not match text")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**
Entering the email, new password but entering different password in confirm password field and waiting till the **Passwords do not match text**

**Input data**
Email: Sk12@gmail.com
New Password: cpktnwt
Confirm Password: chethan

**Test passes if**
The **Valid email is required** text is displayed when confirm password field is entered and waited.
""")

def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password?' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Entering the Email"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        element.click()
        element.send_keys("Sk12@gmail.com")

    with allure.step("Entering the NewPassword"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='newPassword']")))
        element.click()
        element.send_keys("cpktnwt")

    with allure.step("Entering the password in Confirm Password field"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='confirmPassword']")))
        element.click()
        element.send_keys("chethan")

    with allure.step("Validating 'Passwords do not match' error is shown"):
        try:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error ng-star-inserted']")))
            assert element.is_displayed(), "Expected 'Passwords do not match' message not visible"
            allure.attach(element.text, name= "Text displayed", attachment_type=allure.attachment_type.TEXT )

        except:
            pytest.fail("Element not found within the wait time")

# pytest Xeed_Login_Page/Test_TC014.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

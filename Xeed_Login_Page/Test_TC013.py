from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC014 – Validating ‘Please enter valid email’ message on incorrect email format in Forgot Password popup")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**  
Will type in the invalid email and move on to the next field and check the visibility of **Valid email is required** text displayed or not

**Input data**
Email: cpktnwt

**Test passes if**
The **Valid email is required** text is displayed.
""")

def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password?' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Checking the visibility of email field and entering invalid email"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        element.click()
        element.send_keys("cpktnwt")

    with allure.step("Checking the visibility of the new password field and clicking on it"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='newPassword']")))
        element.click()

    with allure.step("Checking the visibility of the **Valid email is required** text is displayed"):
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Valid email is required']")))
        assert element.is_displayed(), "Expected validation message is not visible"
        allure.attach(element.text, name= "Text displayed", attachment_type=allure.attachment_type.TEXT )

# pytest Xeed_Login_Page/Test_TC013.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

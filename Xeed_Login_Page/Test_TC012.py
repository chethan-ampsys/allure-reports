from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC012 - Checking visibility and enablement of Submit button with unfilled fields")
@allure.description("""
**Test Type**  
Functional and cross-browser testing

**Test Scenario**  
Verify that the 'Submit' button in the Forgot Password pop-up is not visible or not enabled when required fields are left empty.

**Expected Result**  
The Submit button should NOT be clickable if any of the form fields (email, new password, confirm password) are empty.

**Test Passes When**  
- The Submit button is either **not visible**, or  
- The Submit button is visible but **not enabled** (disabled)
""")

def test_suite(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Clicking on 'Forgot Password?' link"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Password?']")))
        element.click()

    with allure.step("Checking Submit button state with empty fields"):
        try:
            submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            is_displayed = submit_button.is_displayed()
            is_enabled = submit_button.is_enabled()

            allure.attach(f"Submit Button - Displayed: {is_displayed}, Enabled: {is_enabled}",
                          name="Submit Button State", attachment_type=allure.attachment_type.TEXT)

        except NoSuchElementException:
            allure.attach("Submit button not found (not displayed)",
                          name="Submit Button State", attachment_type=allure.attachment_type.TEXT)

#pytest Xeed_Login_Page/Test_TC012.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

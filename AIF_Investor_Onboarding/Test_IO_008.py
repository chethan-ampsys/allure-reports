import pytest
from conftest import allure, time, EC, WebDriverWait

user_data_map = {
    "chrome": {
        "first_name": "Jaggesh",
        "email": "jaggesh.patel@testmail.com",
        "pan": "KWEPS4321D",
        "mobile": "9889956780"
    },
    "firefox": {
        "first_name": "Michael",
        "email": "michael.mishra@testmail.com",
        "pan": "AJHMR9876F",
        "mobile": "7988776655"
    },
    "edge": {
        "first_name": "Maeby",
        "email": "maeby.ram@testmail.com",
        "pan": "SJUPT6543Q",
        "mobile": "9006543212"
    }
}

@allure.feature("AIF Investor Onboarding")
@allure.title("Positive_TC_IO_008 - Initial Verification of a New Investor with filling all fields")
@allure.description("""
**Test Scenario:**  
All the fields will be filled and form is submitted.

**Expected Result:**  
It should redirect to the Investor Profile page.

**How it is evaluated:**  
Verified by checking if URL changes to `/InvestorProfile`.
""")
def test_site(setup, login_user, click_element, type_into_field, select_dropdown_option, request):
    driver, browser = setup

    user_data = user_data_map.get(browser, user_data_map["chrome"])

    login_user(driver)

    click_element(driver, "Navigating to Investor Node", "//span[normalize-space()='Investors']")
    click_element(driver, "Clicking Add Investor", "//button[normalize-space()='Add Investor']")
    click_element(driver, "Selecting Investor Type: Individual", "//div[@class='radio-group']//div[2]//input[1]")
    time.sleep(5)
    select_dropdown_option(driver, "Selecting Investor Sub Type: Directors", "//select[@name='customerSubType']", "Directors")

    type_into_field(driver, "Entering First Name", "//input[@placeholder='e.g., Rajesh']", user_data["first_name"])
    type_into_field(driver, "Entering Middle Name", "//input[@placeholder='e.g., Kumar']","vikas" )
    type_into_field(driver, "Entering Last Name", "//input[@placeholder='e.g., Sharma']", "Singh")
    type_into_field(driver, "Entering First Name", "//input[@placeholder='e.g., Rajesh']", user_data["first_name"])
    type_into_field(driver, "Entering PAN", "//input[@placeholder='(e.g., ABCDE1234F)']", user_data["pan"])
    type_into_field(driver, "Entering Email", "//input[@placeholder='e.g., rajesh.sharma@gmail.com']", user_data["email"])
    type_into_field(driver, "Entering Mobile Number", "//input[@placeholder='e.g., 9876543210']", user_data["mobile"])

    click_element(driver, "Clicking Submit", "//button[normalize-space()='Submit']")

    with allure.step("Test Passed: User successfully redirected to '/InvestorProfile' after submission"):
        WebDriverWait(driver, 10).until(EC.url_contains("/InvestorProfile"))
        assert "/InvestorProfile" in driver.current_url, "Test Failed: Redirection to /InvestorProfile did not happen as expected."

# pytest AIF_Investor_Onboarding/Test_IO_008.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "Updated Allure report"
# git push origin main

# pytest AIF_Investor_Onboarding/Test_IO_008.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "Updated Allure report"; git push origin main
import pytest
from conftest import allure, time, EC, WebDriverWait

user_data_map = {
    "chrome": {
        "email": "jaggesh.patel@testmail.com",
        "pan": "KWEPS4321D",
        "mobile": "9889956780"
    },
    "firefox": {
        "email": "michael.mishra@testmail.com",
        "pan": "AJHMR9876F",
        "mobile": "7988776655"
    },
    "edge": {
        "email": "maeby.ram@testmail.com",
        "pan": "SJUPT6543Q",
        "mobile": "9006543212"
    }
}

@allure.feature("AIF Investor Onboarding")
@allure.title("Negative_TC_IO_005 - Initial Verification of a New Investor without First Name")
@allure.description("""
**Test Scenario:**  
First Name Mandatory field will be left empty and submitted.

**Expected Result:**  
It should not redirect to the Investor Profile page.

**How it is evaluated:**  
Verified by checking  URL & it should not changes to `/InvestorProfile'.
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

    type_into_field(driver, "Entering PAN", "//input[@placeholder='(e.g., ABCDE1234F)']", user_data["pan"])
    type_into_field(driver, "Entering Email", "//input[@placeholder='e.g., rajesh.sharma@gmail.com']", user_data["email"])
    type_into_field(driver, "Entering Mobile Number", "//input[@placeholder='e.g., 9876543210']", user_data["mobile"])

    click_element(driver, "Clicking Submit", "//button[normalize-space()='Submit']")

    with allure.step("Test Passed: No redirection occurred as First Name was missing"):
        assert "/InvestorProfile" not in driver.current_url, "Unexpected redirection occurred despite missing First Name"

# pytest AIF_Investor_Onboarding/Test_IO_005.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "Updated Allure report"
# git push origin main

# pytest AIF_Investor_Onboarding/Test_IO_005.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "Updated Allure report"; git push origin main

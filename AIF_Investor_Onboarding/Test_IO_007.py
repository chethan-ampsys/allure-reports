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
@allure.title("Negative_TC_IO_007 - Initial Verification of a New Investor without selecting Investor Type")
@allure.description("""
**Test Scenario:**  
Investor Type Mandatory field will be left empty and submitted.

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

    type_into_field(driver, "Entering First Name", "//input[@placeholder='e.g., Rajesh']", user_data["first_name"])
    type_into_field(driver, "Entering PAN", "//input[@placeholder='(e.g., ABCDE1234F)']", user_data["pan"])
    type_into_field(driver, "Entering Email", "//input[@placeholder='e.g., rajesh.sharma@gmail.com']", user_data["email"])
    type_into_field(driver, "Entering Mobile Number", "//input[@placeholder='e.g., 9876543210']", user_data["mobile"])

    click_element(driver, "Clicking Submit", "//button[normalize-space()='Submit']")

    with allure.step("Test Passed: No redirection occurred as Investor Type was missing"):
        assert "/InvestorProfile" not in driver.current_url, "Unexpected redirection occurred despite missing Investor Type"

# pytest AIF_Investor_Onboarding/Test_IO_007.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "Updated Allure report"
# git push origin main

# # pytest AIF_Investor_Onboarding/Test_IO_007.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "Updated Allure report"; git push origin main

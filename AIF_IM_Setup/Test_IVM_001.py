from conftest import allure, EC, time, By, WebDriverWait

@allure.feature("AIF_IM_Setup")
@allure.title("TC_IVM_001 - Adding an IM")
@allure.description("""
**Test Scenario:**
Entering all the fields with correct input to check how it works

**Expected Result:**
IM should be added and visible in IM Setup

**How it is evaluated:**
Users will be thrown to IM List page
""")
def test_site(login, textfield, dropdown, calendar, clicker, setup):
    login()

    clicker("Clicking on the IM Management page", "//span[contains(text(),'IM Management')]")
    clicker("Clicking on IM Setup tab", "//div[@class='tab']")

    # --- IM Profile ---
    textfield("Entering Entity Name as FinEdge Capital Advisors Pvt. Ltd", "//input[@placeholder='e.g., Acme Corporation Ltd.']", "FinEdge Capital Advisors Pvt. Ltd")
    textfield("Entering First Name as Sachin", "//input[@placeholder='e.g., Rahul']", "Sachin")
    textfield("Entering Middle Name as Kumar", "//input[@placeholder='e.g., Kumar']", "Kumar")
    textfield("Entering Last Name as Menon", "//input[@placeholder='e.g., Sharma or Mary Jane']", "Menon")
    textfield("Entering Address Line 1 as 801, Phoenix Towers, MG Road", "//textarea[@placeholder='e.g., 123 MG Road, Prestige Towers']", "801, Phoenix Towers, MG Road")
    textfield("Entering Address Line 2 as 5th Floor, Opp. Metro Station", "//textarea[@placeholder='e.g., 4th Floor, Near Trinity Metro Station']", "5th Floor, Opp. Metro Station")
    textfield("Entering Address Line 3 as Indiranagar, Bengaluru", "//input[@placeholder='e.g., Ashok Nagar, Bengaluru']", "Indiranagar, Bengaluru")
    textfield("Entering City as Bengaluru", "//input[@placeholder='e.g., Mumbai']", "Bengaluru")
    textfield("Entering State as Karnataka", "//input[@placeholder='e.g., Maharashtra']", "Karnataka")
    textfield("Entering Country as India", "//input[@placeholder='e.g., India']", "India")
    textfield("Entering Pincode as 560038", "//input[@placeholder='e.g., 560001']", "560038")
    textfield("Entering Email as rajesh.meon@finedge.com", "//input[@placeholder='e.g., you@example.com']", "rajesh.meon@finedge.com")
    textfield("Entering Mobile as 9876543210", "//input[@placeholder='e.g., 9123456789']", "9876543210")
    textfield("Entering Login ID as 42524", "//input[@placeholder='e.g., user.user123 or user@email.com']", "85245")
    textfield("Entering Landline as 08022334455", "//input[@placeholder='e.g., 12345678']", "08022334455")
    dropdown("Selecting Category as Gold", "//select[@name='Category']", "Gold")
    calendar("Selecting Activation Date as 2025-07-01", "//input[@name='ActivationDate']", "2025-07-01")
    dropdown("Selecting Status as Active", "//select[@name='Status']", "Active")
    clicker("Selecting Multi-branch as Yes", "//input[@id='confirmationYes']")
    textfield("Entering Master ID as 54753", "//input[@placeholder='e.g., 12345']", "54753")

    clicker("Clicking Save and Continue to move to subscription page", "//button[normalize-space()='Save & Continue']")

    try:
        # Assert modal appeared with correct message
        WebDriverWait(setup, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'popup-card')]//p[normalize-space()='IM Added Successfully']"))
        )
        print("[SUCCESS] Success modal found")
    except Exception as e:
        allure.attach(setup.get_screenshot_as_png(), name="SuccessModalError", attachment_type=allure.attachment_type.PNG)
        allure.attach(setup.page_source, name="HTMLAfterSave", attachment_type=allure.attachment_type.HTML)
        raise AssertionError("Success modal did not appear as expected")

    # Click close button after confirming popup
    clicker("Closing the Modal Dialog", "//button[contains(@class, 'close-button')]")


    # --- IM Subscription ---
    calendar("Selecting Trial Start Date as 2025-07-01", "//input[@name='TrialStartDate']", "2025-07-01")
    calendar("Selecting Trial End Date as 2025-07-31", "//input[@name='TrialEndDate']", "2025-07-31")
    calendar("Selecting Subscription Start Date as 2025-08-01", "//input[@name='SubscriptionStartDate']", "2025-08-01")
    calendar("Selecting Subscription End Date as 2026-07-31", "//input[@name='SubscriptionEndDate']", "2026-07-31")
    clicker("Selecting Opt For Tenant App/DB as Yes", "//input[@id='optTenant']")
    textfield("Entering No Of Branches as 25", "//input[@placeholder='e.g., 25']", "25")
    textfield("Entering No of Staff Logins as 50", "//input[@placeholder='e.g., 50']", "50")
    textfield("Entering No of Customer Logins as 100000", "//input[@placeholder='e.g., 100000']", "100000")
    textfield("Entering SMS's Bought as 50000", "//input[@placeholder='e.g., 50000']", "50000")
    textfield("Entering Vault Default Size as 1000", "//input[@placeholder='e.g., 1000']", "1000")
    textfield("Entering Vault Paid Size as 5000", "//input[@placeholder='e.g., 5000']", "5000")
    textfield("Entering Vault Balance Storage as 2500.50", "//input[@placeholder='e.g., 2500.50']", "2500.50")
    textfield("Entering Vault Used Storage as 1249.50", "//input[@placeholder='e.g., 1249.50']", "1249.50")
    clicker("Selecting Send Login Info as Yes", "//input[@name='SendLoginInfo']")
    dropdown("Selecting Pick a Plan as AIF Manager", "//select[@name='selectedPlan']", "AIF Manager")
    textfield("Entering Comment as Enabled dashboard access for client.", "//textarea[@placeholder='Enter any comments about the selected plan or modules...']", "Enabled dashboard access for client.")

    clicker("Clicking Save & Continue", "//button[normalize-space()='Save & Continue']")

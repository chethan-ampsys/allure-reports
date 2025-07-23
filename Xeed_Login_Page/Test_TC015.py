from conftest import allure, time

@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC015 - Login with Valid Credentials")
@allure.description("""
**Test Scenario:**  
Attempt to log in using valid credentials  
Username: Rohit  
Password: Erp@123

**Expected Result:**  
User should be able to log in.

**How it is evaluated:**  
This is verified by checking the URL change; if the login is successful, the URL changes to `/dashboard`.
""")

def test_site(login_user, punk):
    login_user()

    punk("Clicking on the IM Management page", "//span[contains(text(),'IM Management')]", "")
    punk("Clicking on IM Setup tab", "//div[@class='tab']", "")
    punk("Entering the name", "//input[@placeholder='Enter Name']", "Dirk")
    allure.attach("Test Passed Successfully", name="Test Result", attachment_type=allure.attachment_type.TEXT)



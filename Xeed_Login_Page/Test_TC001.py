from conftest import allure, By, WebDriverWait, EC, time
@allure.feature("XEED_Ventures_Login_Page")
@allure.title("TC001 - Login with Valid Credentials")
@allure.description("""
**Test Scenario:**  
Attempt to log in using a valid credentials
Username: Sk12@gmail.com  
Password: Sk@123

**Expected Result:**  
User should be able to log in.

**How it is evaluated:**  
This is verified by checking the URL change; if the login is successful, the URL changes to `/dashboard`.
""")

def test_site(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    with allure.step("Login Page is Opened"):
        driver.get("http://157.15.202.244:99/authentication/login")

    with allure.step("Waiting until the username field is displayed and it is clicked"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        element.click()

    with allure.step("Typing the valid Email"):
        element.send_keys("Sk12@gmail.com")

    with allure.step("Waiting until the password field is displayed"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.click()

    with allure.step("Typing the valid password"):
        element.send_keys("Sk@123")

    with allure.step("Clicking the login button"):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        element.click()

    with allure.step("Waiting for redirect and validating the URL ends with /dashboard"):
        wait.until(EC.url_contains("/dashboard"))
        current_url = driver.current_url
        assert current_url.endswith("/dashboard"), f"Login failed. Current URL is {current_url}"

    allure.attach("Test Passed Successfully", name="Test Result", attachment_type=allure.attachment_type.TEXT)

# Follow these

# Any change u make to the code follow the below commands it will overwrite the existing files in allure results folder
# and even if it is pushed to remote github it will overwrite there also hence any changes done run following commands
# to see on the allure


# pytest Xeed_Login_Page/Test_TC001.py --alluredir=allure-results
# if file outside directory use pytest Test_TC001.py --alluredir=allure-results
# allure generate allure-results --clean -o docs
# git add docs
# git commit -m "First Commit"
# git push origin main

# This is used to remove all the files in docs directory {Remove-Item -Path allure-results\* -Recurse -Force}
# whenever the organization or naming or anything is felt wrong run remove command to remove all files and then again run
# commands from start

# pytest Xeed_Login_Page/ --alluredir=allure-results  (Run this to run all the files in the directory)
# pytest Xeed_Login_Page/Test_TC001.py Xeed_Login_Page/Test_TC002.py --alluredir=allure-results (To run selected files in the directory use this)

# Run the Following command to run store results generate report and push it to github
# pytest Xeed_Login_Page/Test_TC001.py --alluredir=allure-results; allure generate allure-results --clean -o docs; git add docs; git commit -m "First Commit"; git push origin main

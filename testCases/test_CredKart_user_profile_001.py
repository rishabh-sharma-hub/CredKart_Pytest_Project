import time

import allure
import pytest
from faker import Faker
from pageObjects.Login import login_page_class
from pageObjects.Registration import registration_page_class #user definer class import
from utilities.Logger import Log_generation_class
from utilities.Read_Config import ReadConfigclass
from utilities.Logger import Log_generation_class

@pytest.mark.usefixtures("browser_setup") # new
class Test_User_Profile:
    driver=None #new
    email= ReadConfigclass.get_data_for_email()
    password = ReadConfigclass.get_data_for_password()
    home_page = ReadConfigclass.get_home_page_url()
    registration_page = ReadConfigclass.get_registration_url()
    login_page = ReadConfigclass.get_login_page_url()
    log=Log_generation_class.log_gen_method()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify application url")
    @allure.description("This test case is to validate CredKart title functionality")
    @allure.link(home_page)
    @allure.story("Story 1")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    #@pytest.mark.dependency(name="test_CredKart_URL_001")

    def test_CredKart_URL_001(self):
        # self.log.info("This is info")
        # self.log.info("This is Warning")
        # self.log.info("This is Error")
        # self.log.info("This is Critical")
        #self.driver.get("https://automation.credence.in")
        self.log.info("Testcase test_CredKart_URL_001 is started")
        self.driver.get(self.home_page) #implemented read_config via config.ini
        self.log.info(f"Opening browser and landing on {self.home_page}")
        self.log.info(f"Checking page title")
        if self.driver.title=='CredKart':
            self.log.info(f"Page title is correct and landed on correct url")
            self.log.info(f"Taking Screenshot")
            self.driver.save_screenshot('.\\Screenshots\\CredKart_Home_Page_Pass.png')
            allure.attach.file('.\\Screenshots\\CredKart_Home_Page_Pass.png',
                               name="CredKart_Home_Page_Pass",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("test_CredKart_URL_001 is pass")
        else:
            self.log.info(f"Page title is incorrect and landed on url -->{self.driver.title}")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot('.\\Screenshots\\CredKart_Home_Page_Fail.png')
            allure.attach.file('.\\Screenshots\\CredKart_Home_Page_Fail.png',
                               name="CredKart_Home_Page_Fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Testcase test_Credkart_URL_001 is completed")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify registration url")
    @allure.description("This test case is to validate CredKart user registration")
    @allure.link(registration_page)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    #@pytest.mark.dependency(depends=["test_CredKart_URL_001"])

    def test_CredKart_User_Registration_002(self):
        self.log.info("Testcase test_CredKart_User_Registration_002 is started")
        #self.driver.get("https://automation.credence.in/register")
        self.driver.get(self.registration_page)
        self.log.info(f"Opening Browser and landing on {self.registration_page}")
        self.rp = registration_page_class(self.driver) #Object

        # Enter name
        name_data = Faker().name()
        self.log.info(f"Entering name: {name_data}")
        print(f"name_data:{name_data}")
        self.rp.Enter_name(name_data)

        # Enter email
        email_data = Faker().email()
        self.log.info(f"Entering email: {email_data}")
        print(f"email_data:{email_data}")
        self.rp.Enter_email(email_data)

        # Enter Password
        self.log.info(f"Entering password")
        self.rp.Enter_password("Rishabh123")

        # Confirm Password
        self.log.info(f"Entering confirm password")
        self.rp.Enter_confirm_password("Rishabh123")

        # Click on register button
        self.log.info(f"Click on register button")
        self.rp.click_Submit()
        time.sleep(2)

        # Verify Registration
        self.log.info(f"Checking registration status")
        try:
            if self.rp.verify_Menu()=="Pass":
                self.log.info(f"Click Menu")
                self.rp.click_Menu()
                self.log.info(f"registration pass")
                time.sleep(2)
                self.driver.save_screenshot('.\\Screenshots\\UserRegistrationPass.png')
                allure.attach.file('.\\Screenshots\\UserRegistrationPass.png',
                                   name="CredKart_User_Registration_Pass",
                                   attachment_type=allure.attachment_type.PNG)
                self.log.info(f"Taking screenshot for registration pass")
                self.log.info(f"Click on logout button")
                self.rp.click_Logout()
                self.log.info("Testcase test_CredKart_User_Registration_002 is Passed")
        except:
            self.log.info(f"registration fail")
            self.log.info(f"Taking screenshot for registration fail")
            self.driver.save_screenshot('.\\Screenshots\\UserRegistrationFail.png')
            allure.attach.file('.\\Screenshots\\UserRegistrationFail.png',
                               name="CredKart_User_Registration_Fail",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("Testcase test_Credkart_Registration_003 is failed")
            assert False
        self.log.info("Testcase test_CredKart_User_Registration_002 is Completed")


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify login url")
    @allure.description("This test case is to validate CredKart user login")
    @allure.link(login_page)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    #@pytest.mark.dependency(depends=["test_CredKart_URL_001"])

    def test_CredKart_User_login_003(self):
        #self.driver.get("https://automation.credence.in/login")
        self.driver.get(self.login_page)
        self.lp = registration_page_class(self.driver)

        # Enter email
        #self.lp.Enter_email("millerbrent@example.org")
        self.lp.Enter_email(self.email)

        # Enter Password
        #self.lp.Enter_password("Rishabh123")
        self.lp.Enter_password(self.password)

        # Click on register button
        self.lp.click_Submit()
        time.sleep(2)

        # Verify login
        try:
            if self.lp.verify_Menu()=="Pass":
                self.lp.click_Menu()
                time.sleep(2)
                self.driver.save_screenshot('.\\Screenshots\\UserloginPass.png')
                allure.attach.file('.\\Screenshots\\UserloginPass.png',
                                   name="CredKart_User_Login_Pass",
                                   attachment_type=allure.attachment_type.PNG)
                self.lp.click_Logout()
        except:
            self.driver.save_screenshot('.\\Screenshots\\UserloginFail.png')
            allure.attach.file('.\\Screenshots\\UserloginFail.png',
                               name="CredKart_User_Login_Fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False


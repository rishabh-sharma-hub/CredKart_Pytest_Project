import time

import allure
import pytest
from faker import Faker
from pageObjects.Login import login_page_class #user definer class import
from pageObjects.Registration import registration_page_class #user definer class import
from utilities import Excel_Utilities #user definer class import
from utilities.Logger import Log_generation_class #user definer class import
from utilities.Read_Config import ReadConfigclass #user definer class import
from utilities.Logger import Log_generation_class #user definer class import


@pytest.mark.usefixtures("browser_setup") # new
class Test_User_Login_002:
    driver=None #new
    home_page = ReadConfigclass.get_home_page_url()
    registration_page = ReadConfigclass.get_registration_url()
    login_page = ReadConfigclass.get_login_page_url()
    log=Log_generation_class.log_gen_method()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify application url")
    @allure.description("This test case is to validate CredKart user login functionality with DDT param")
    @allure.link(login_page)
    @allure.story("Story 4")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    #@pytest.mark.dependency(name="test_user_login_param_004")

    def test_user_login_param_004(self,User_login_multidata_set):
        self.log.info(f" TestCase test_user_login_param_004 is started")
        self.driver.get(self.login_page)
        self.log.info(f"Opening browser and landing on {self.login_page}")
        self.lp=registration_page_class(self.driver) #Object

        #Below giving index to read param data from class User_Login_multidata_set
        self.email=User_login_multidata_set[0]
        self.password=User_login_multidata_set[1]
        self.expected_result=User_login_multidata_set[2]

        #Enter email
        self.log.info(f" Entering email {self.email}")
        self.lp.Enter_email(self.email)

        #Enter Password
        self.log.info(f" Entering password")
        self.lp.Enter_password(self.password)

        # Click on login button
        self.log.info(f" Clicking on login button")
        self.lp.click_Submit()

        self.log.info(f"Click on login button")
        if self.lp.verify_Menu()=='Pass':
            self.log.info(f"Login Pas")
            self.log.info(f"Clicking on menu button")
            self.lp.click_Menu()
            self.log.info(f"Clicking on logout button")
            self.lp.click_Logout()
            self.log.info(f"Taking screenshot for login pass")
            self.lp.driver.save_screenshot(f".\\Screenshots\\User_Login_DDT_Param_pass_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User_Login_DDT_Param_pass_{self.email}.png",
                               name="CredKart_User_Login_DDT_Param_Pass",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info(f"TestCase test_user_login_param_004 is passed")
            actual_result='Login Pass'

        else:
            self.log.info(f"Login Fail")
            self.log.info(f"Taking screenshot for login fail")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_DDT_Param_fail_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User_Login_DDT_Param_fail_{self.email}.png",
                               name="CredKart_User_Login_DDT_Param_Fail",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info(f"TestCase test_user_login_param_004 is failed")
            actual_result='Login Fail'

        assert actual_result == self.expected_result,f"{actual_result}!={self.expected_result}"
        self.log.info(f"TestCase test_user_login_param_004 is completed")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify application url")
    @allure.description("This test case is to validate CredKart user login functionality with DDT excel")
    @allure.link(login_page)
    @allure.story("Story 5")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    #@pytest.mark.dependency(depends=["test_user_login_param_004"])

    def test_user_login_by_excel_005(self):

        excel_path=".\\TestData\\Test_Data.xlsx"
        sheet_name="Login_Data"
        self.log.info(f" TestCase test_user_login_by_excel_005 is started")
        self.lp = registration_page_class(self.driver)  # Object
        self.rows=Excel_Utilities.get_row_count(excel_path,sheet_name)
        print(f"Number of rows in Excel File : {self.rows}")
        result_list=[]

        for i in range(2,self.rows+1):
            self.driver.get(self.login_page)
            self.log.info(f"Opening browser and landing on {self.login_page}")
            self.email=Excel_Utilities.read_data(excel_path,sheet_name,i,2)
            self.password=Excel_Utilities.read_data(excel_path,sheet_name,i,3)
            self.expected_result=Excel_Utilities.read_data(excel_path,sheet_name,i,4)

            # Enter email
            self.log.info(f" Entering email {self.email}")
            self.lp.Enter_email(self.email)

            # Enter Password
            self.log.info(f" Entering password")
            self.lp.Enter_password(self.password)

            # Click on login button
            self.log.info(f" Clicking on login button")
            self.lp.click_Submit()

            self.log.info(f"Click on login button")
            if self.lp.verify_Menu() == 'Pass':
                self.log.info(f"Login Pass")
                self.log.info(f"Clicking on menu button")
                self.lp.click_Menu()
                self.log.info(f"Taking screenshot for login pass")
                self.lp.driver.save_screenshot(f".\\Screenshots\\User_Login_DDT_Excel_pass_{self.email}.png")
                allure.attach.file(f".\\Screenshots\\User_Login_DDT_Excel_pass_{self.email}.png",
                                   name="CredKart_User_Login_DDT_excel_Pass",
                                   attachment_type=allure.attachment_type.PNG)
                self.log.info(f"Clicking on logout button")
                self.lp.click_Logout()
                self.log.info(f"TestCase test_user_login_param_005 is passed")
                actual_result = 'Login Pass'

            else:
                self.log.info(f"Login Fail")
                self.log.info(f"Taking screenshot for login fail")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_DDT_Excel_fail_{self.email}.png")
                allure.attach.file(f".\\Screenshots\\User_Login_DDT_Excel_fail_{self.email}.png",
                                   name="CredKart_User_Login_DDT_excel_Fail",
                                   attachment_type=allure.attachment_type.PNG)
                self.log.info(f"TestCase test_user_login_param_005 is failed")
                actual_result = 'Login Fail'

            self.log.info(f"Writing data into Excel File")

            Excel_Utilities.write_data(excel_path,sheet_name,i,5,actual_result)
            print(f"Written value at row {i}, col 5: {actual_result}")

            if self.expected_result == actual_result:
                test_case_status='Pass'
            else:
                test_case_status='Fail'
            result_list.append(test_case_status)
            Excel_Utilities.write_data(excel_path,sheet_name,i,6,test_case_status)
            print(f"Written value at row {i}, col 6: {test_case_status}")

        if 'Login Fail' not in result_list:
            self.log.info(f"All Test Cases Passed")
            self.log.info(f"TestCase test_user_login_param_005 is passed")
            assert True
        else:
            self.log.info(f"Some Test Cases Failed")
            self.log.info(f"TestCase test_user_login_param_005 is failed")
            assert False
        self.log.info(f"TestCase test_user_login_param_005 is completed")
#name
#email
#password
#confirm
#Click submit
#Click menu
#logout
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class registration_page_class:

    text_name_id="name"
    text_email_id="email"
    text_password_id="password"
    text_confirm_password_id="password-confirm"
    button_login_class_name="btn-primary"
    link_menu_xpath="//a[@role='button']"
    link_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver): #constructor
        self.driver = driver

    def Enter_name(self,name):
        self.driver.find_element(By.ID,self.text_name_id).send_keys(name)

    def Enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def Enter_password(self,password):
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def Enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,self.text_confirm_password_id).send_keys(confirm_password)

    def click_Submit(self):
        self.driver.find_element(By.CLASS_NAME,self.button_login_class_name).click()

    def click_Menu(self):
        self.driver.find_element(By.XPATH, self.link_menu_xpath).click()

    def click_Logout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()

    def verify_Menu(self):
        try: # wait tp load menu button
            WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[@role='button']")))
            return 'Pass'
        except:
            return 'Fail'





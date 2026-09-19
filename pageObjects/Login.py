#email
#password
#Click submit
#Click menu
#logout
from pageObjects.Registration import registration_page_class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class login_page_class(registration_page_class):

    def enter_email(self,email):
        self.driver.find_element(By.XPATH,'//*[@id="id_email"]').send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys(password)
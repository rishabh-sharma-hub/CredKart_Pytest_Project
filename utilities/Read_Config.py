import configparser
config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')
class ReadConfigclass:

    @staticmethod
    def get_data_for_email():
        email = config.get("login_data", "email")
        return email

    @staticmethod
    def get_data_for_password():
        password = config.get("login_data", "password")
        return password

    @staticmethod
    def get_home_page_url():
        home_page = config.get("app_urls", "home_page_url")
        return home_page

    @staticmethod
    def get_registration_url():
        registration_page = config.get("app_urls", "registration_page_url")
        return registration_page

    @staticmethod
    def get_login_page_url():
        login_page = config.get("app_urls", "login_page_url")
        return login_page



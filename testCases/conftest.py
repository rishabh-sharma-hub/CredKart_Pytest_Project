import pytest
from selenium import webdriver


@pytest.fixture
def demo_fixture():
    print(f"This is demo fixture, This will run first before test case")
    yield
    print(f"\n This is demo fixture, This will run after test case")


'''
@pytest.fixture
def browser_setup():
    print(f"\nThis is browser setup, this will run before test case")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print(f"\n This is browser teardown")

# in real time we dont use this 
'''


def pytest_addoption(parser):
    parser.addoption("--browser")


# Here we are going to add --browser is a command line argument which is user define or
# custom  argument u can say

# __browser
@pytest.fixture(scope="class")
def browser_setup(request):
    browser = request.config.getoption("--browser")
    # we are going to share --browser value at the time of execution(pytest command se value lega)
    if browser == "Chrome":
        print("Launching Chrome")
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        print("Launching Firefox")
        driver = webdriver.Firefox()
    elif browser == "Edge":
        print("Launching Edge")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    #attaching driver to class
    request.cls.driver = driver #new
    yield driver
    driver.quit()


# test_file_8 (login status fail or pass based on multiple data set define)
# user_name :ballardpeter@example.org
# Password: Rishabh123
@pytest.fixture(params=[
    ('ballardpeter@example.org', 'Rishabh123', 'Login Pass'),
    ('ballardpeter@example.org', 'Rahul123', 'Login Fail'),
    ('ballar@example.org', 'Rishabh123', 'Login Fail'),
    ('baldp@example.org', 'Rahul123', 'Login Fail')
])
def User_login_multidata_set(request):
    return request.param

def pytest_metadata(metadata):
    #To add metadata
    metadata["Project name"]="CredKart"
    metadata["Module name "] = "Login"
    metadata["Tester name"] = "Crednece"
    metadata["Url"] = "https://apps.credence.in"

    #To remove metadata
    del metadata["Platform"]

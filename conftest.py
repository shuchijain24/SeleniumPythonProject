import pytest


def pytest_addoption(parser):
        parser.addoption("--browser", action="store", default="chrome", help ="Type in browser for ex. Chrome or Firefox")

@pytest.fixture(scope="class")
def test_setup(request):
        from selenium import webdriver

        browser = request.config.getoption("--browser")
        if browser == "chrome":
                driver = webdriver.Chrome(executable_path="/home/shuchi/PycharmProjects/AutomationFramework/drivers/chromedriver")

        driver.implicitly_wait(4)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
        driver.quit()
        print("Test Completed")
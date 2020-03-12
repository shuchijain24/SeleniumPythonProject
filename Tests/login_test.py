from selenium import webdriver
import time
import pytest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    
    def test_login(self):               #object classes
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)                         #objects created
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        
    def test_logout(self):
        try:
            driver = self.driver

            homepage = HomePage(driver)          #objects created
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except:
            print("There was an exception")
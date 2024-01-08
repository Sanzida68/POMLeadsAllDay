import time
import pytest

from test.conftest import user1
from test.pages.Homepage import HomePage

from test.pages.SignInPage import SigninPage


@pytest.mark.usefixtures("driver")
class TestSignin:

    def test_signin(self, driver):
        HomePage(driver).for_signin_page(user1.Url)
        SigninPage(driver).for_login(user1.valid_email, user1.valid_password)
        time.sleep(3)

    def test_invalid_email_valid_pass(self, driver):
        HomePage(driver).for_signin_page(user1.Url)
        SigninPage(driver).for_login(user1.invalid_email, user1.valid_password)
        time.sleep(3)

    def test_valid_email_invalid_pass(self, driver):
        HomePage(driver).for_signin_page(user1.Url)
        SigninPage(driver).for_login(user1.valid_email, user1.invalid_password)
        time.sleep(3)

    def test_empty_field(self, driver):
        HomePage(driver).for_signin_page(user1.Url)
        SigninPage(driver).for_login("", "")
        time.sleep(3)

import time

import pytest

from test.conftest import user1
from test.pages.Homepage import HomePage
from test.pages.LogOutPage import LogoutPage
from test.pages.SignInPage import SigninPage


@pytest.mark.usefixtures("driver")
class TestLogout:
    def test_logout(self, driver):
        HomePage(driver).for_signin_page(url=user1.Url)
        signin = SigninPage(driver)
        signin.for_login(user1.valid_email, user1.valid_password)
        LogoutPage(driver).logout()

        time.sleep(3)


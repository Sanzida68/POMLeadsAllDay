import time

import pytest

from test.conftest import user1, set_task
from test.pages.CrmTaskPage import CrmTaskPage
from test.pages.Homepage import HomePage
from test.pages.SignInPage import SigninPage


@pytest.mark.usefixtures("driver")
class TestCrmTask:
    def test_task(self, driver):
        HomePage(driver).for_signin_page(user1.Url)
        SigninPage(driver).for_login(user1.valid_email, user1.valid_password)
        time.sleep(3)
        CrmTaskPage(driver).create_task(title=set_task.title, description=set_task.description)

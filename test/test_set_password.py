import time

import pytest

from test.conftest import set_pass
from test.pages.AccountActivationPage import AccountActivePage


@pytest.mark.usefixtures("driver")
class TestSetPassword:
    def test_set_password(self, driver):
        AccountActivePage(driver).for_activation(url=set_pass.url, ps=set_pass.password, cp=set_pass.confirm_password)

        time.sleep(3)

    def test_not_match_set(self, driver):
        AccountActivePage(driver).for_activation(url=set_pass.url, ps=set_pass.password, cp=set_pass.not_match)

        time.sleep(3)

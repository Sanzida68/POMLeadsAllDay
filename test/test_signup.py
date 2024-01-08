import pytest

from test.conftest import user2, user1
from test.pages.Homepage import HomePage
from test.pages.SignUpPage import SignupPage


@pytest.mark.usefixtures("driver")
class TestSignup:
    def test_signup(self, driver):
        HomePage(driver).for_signup_page(url=user1.Url)

        SignupPage(driver).for_signin(fn=user2.name, br=user2.brokerage, email_add=user2.email, m=user2.mobile,
                                      add=user2.address, city=user2.city, pc=user2.postal_code, ch=user2.card_name,
                                      cn=user2.card_number,
                                      ex=user2.exp_date, cv=user2.cvc)

    def test_with_mandatory_field(self, driver):
        HomePage(driver).for_signup_page(url=user1.Url)

        SignupPage(driver).for_signin(fn=user2.name, br="", email_add=user2.email, m=user2.mobile,
                                      add=user2.address, city=user2.city, pc=user2.postal_code, ch=user2.card_name,
                                      cn=user2.card_number,
                                      ex=user2.exp_date, cv=user2.cvc)

    def test_with_empty_field(self, driver):
        HomePage(driver).for_signup_page(url=user1.Url)

        SignupPage(driver).for_signin(fn="", br="", email_add="", m="", add="", city="", pc="", ch="", cn="", ex="",
                                      cv="")

    def test_with_same_email(self, driver):
        SignupPage(driver).for_signin(fn=user2.name, br=user2.brokerage, email_add=user2.same_mail, m=user2.mobile,
                                      add=user2.address, city=user2.city, pc=user2.postal_code, ch=user2.card_name,
                                      cn=user2.card_number,
                                      ex=user2.exp_date, cv=user2.cvc)


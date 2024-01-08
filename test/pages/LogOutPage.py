import time

from selenium.webdriver.common.by import By


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_xpath = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined "
                                       "MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium "
                                       "MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary "
                                       "MuiButton-sizeMedium MuiButton-outlinedSizeMedium mui-style-o5oxgn']")

    def logout(self):
        time.sleep(2)
        self.driver.find_element(*self.logout_xpath).click()


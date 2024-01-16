import time

from selenium.webdriver.common.by import By


class CrmTaskPage:
    def __init__(self, driver):
        self.driver = driver

        self.tasks_path = (By.XPATH, "//*[name()='path' and @d='M20 22H4C3.44772 22 3 21.5523 3 21V3C3 2.44772 "
                                     "3.44772 2 4 2H20C20.5523 2 21 2.44772 21 3V21C21 21.5523 20.5523 22 20 22ZM19 "
                                     "20V4H5V20H19ZM8 7H16V9H8V7ZM8 11H16V13H8V11ZM8 15H13V17H8V15Z']")
        self.task_button_path = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained "
                                           "MuiButton-containedPrimary MuiButton-sizeMedium "
                                           "MuiButton-containedSizeMedium MuiButton-root MuiButton-contained "
                                           "MuiButton-containedPrimary MuiButton-sizeMedium "
                                           "MuiButton-containedSizeMedium mui-style-1635xam']")
        self.title_name = (By.NAME, "title")
        self.date_path = (By.XPATH, "//div[@class='react-datepicker__input-container']")
        self.pick_date_path = (By.XPATH, "//div[@class='react-datepicker__tab-loop']//div["
                                         "@class='react-datepicker__month']//div[@class='react-datepicker__week']["
                                         "3]//div[@class='react-datepicker__day react-datepicker__day--016 "
                                         "react-datepicker__day--selected react-datepicker__day--today']")
        self.pick_time_path = (By.XPATH, "//div[@class='react-datepicker__time']//ul["
                                         "@class='react-datepicker__time-list']//li["
                                         "@class='react-datepicker__time-list-item  "
                                         "react-datepicker__time-list-item--disabled'][3]")
        self.description_name = (By.NAME, "description")

        self.save_button_xpath = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained "
                                            "MuiButton-containedPrimary MuiButton-sizeMedium "
                                            "MuiButton-containedSizeMedium MuiButton-root MuiButton-contained "
                                            "MuiButton-containedPrimary MuiButton-sizeMedium "
                                            "MuiButton-containedSizeMedium mui-style-1nm31qw']")

    def create_task(self, title, description):
        self.driver.find_element(*self.tasks_path).click()
        self.driver.find_element(*self.task_button_path).click()
        self.driver.find_element(*self.title_name).send_keys(title)
        self.driver.find_element(*self.date_path).click()
        time.sleep(2)
        self.driver.find_element(*self.pick_date_path).click()
        time.sleep(1)
        self.driver.find_element(*self.pick_time_path).click()
        time.sleep(2)
        self.driver.find_element(*self.description_name).send_keys(description)
        self.driver.find_element(*self.save_button_xpath).click()
        time.sleep(2)


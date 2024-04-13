import time
from typing import Tuple

import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, """#create-btn""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_USER_NAME = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_FORM_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_OUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_MESSAGE_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, """#contact > div.submit > button > span""")


class OperationHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def check_login_success(self):
        user_name = self.find_element(TestSearchLocators.LOCATOR_USER_NAME)
        if user_name.text:
            logging.info("Login successful")
            return True
        else:
            logging.info("Login failed")
            return False

    def create_post(self, title, content):
        logging.info("Creating a new post")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()
        title_input = self.find_element((By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input"""))
        title_input.clear()
        title_input.send_keys(title)

        content_input = self.find_element((By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""))
        content_input.clear()
        content_input.send_keys(content)

        save_btn = self.find_element((By.CSS_SELECTOR, "button > span"))
        save_btn.click()

        time.sleep(5)
        post_title = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        assert post_title.text == title, "Post title does not match"
        logging.info(f"Post created with title: {title}")

    def test_contact_us(self):
        logging.info("Testing Contact Us form")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        # После клика по кнопке "Contact Us"
        time.sleep(10)
        contact_form_title = self.find_element(TestSearchLocators.LOCATOR_CONTACT_FORM_TITLE)
        assert contact_form_title.text == "Contact us!", "Contact form did not open"

        self.find_element(TestSearchLocators.LOCATOR_OUR_NAME_FIELD).send_keys("Grisha")
        self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD).send_keys("hdrbv@jnjf.by")
        self.find_element(TestSearchLocators.LOCATOR_MESSAGE_FIELD).send_keys("Тестовый месендж")

        time.sleep(5)
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

        alert = self.driver.switch_to.alert
        assert alert.text == "Ваше сообщение отправлено!", "Alert text does not match"
        alert.accept()


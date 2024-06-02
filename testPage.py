import pytest
import requests
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):
@pytest.fixture()
def login():
    data = {
        "address": "https://test-stand.gb.ru",
        "username": "testuser",
        "password": "testpassword"
    }

    try:
        response = requests.post(data["address"] + "getway/login",
                                 data={"username": data["username"], "password": data["password"]})
        response.raise_for_status()
        logger.debug(f"Успешный вход: {response.content}")
        token = response.json()["token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка входа: {e}")

def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exeption while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exeption with clock")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text


#ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word, description="title form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], word, description="description form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content form")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description="name form")

    def enter_contact_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word, description="email form")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_MESSAGE_FIELD"], word, description="content form")

#CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new post")

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save")

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact")

    def click_contact_send_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SEND_BTN"], description="send")

#GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"])

    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RES_TEXT"], description="result")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
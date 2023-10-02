import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
from zeep import Client, Settings


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    # ENTER TEXT
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
            logging.exception(f"Exception while operation with {locator}")
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
            logging.exception("Exception with click")
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
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {element_name}")
        return text

    def speller(self, text, description=None):
        with open('testdata.yaml') as f:
            data = yaml.safe_load(f)
        if description:
            element_name = description
        else:
            element_name = __name__

        settings = Settings(strict=False)
        client = Client(wsdl=data['wsdl'], settings=settings)

        try:
            result = client.service.checkText(text)[0]['s']
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found list of words {result}")
        return result

    # Input text

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description="login")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description="password")

    def input_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE'], word, description="title")

    def input_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION'], word, description="description")

    def input_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT'], word, description="content")

    def input_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME_FIELD'], word, description="name")

    def input_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_MAIL_FIELD'], word, description="mail")

    def input_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_CONTACT'], word,
                                   description="content contact")

    # Clickers
    def click_save_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_BTN'], description="save")

    def click_delete_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_DELETE_BTN'], description="delete")

    def click_contact_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description="contact")

    def click_plus_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_PLUS_BTN'], description="plus")

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description="contact us")

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description="login btn")

    def click_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    # Get text

    def post_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_CREATED_TITLE'], description="created title")

    def success_delete(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_POSTS'], description="delete success")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description="error")

    def login_success(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SUCCESS'], description="login success")

    def spell_the_word(self, word):
        return self.speller(word, description="Spell the word")

    def short_pause(self):
        time.sleep(1)

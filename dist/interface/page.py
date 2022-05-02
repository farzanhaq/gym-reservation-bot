from locator import *
from element import InputElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import smtplib
from email.message import EmailMessage


class InputUsernameElement(InputElement):
    locator = LoginPageLocators.USERNAME_FIELD[1]


class InputPasswordElement(InputElement):
    locator = LoginPageLocators.PASSWORD_FIELD[1]


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    input_username_element = InputUsernameElement()
    input_password_element = InputPasswordElement()

    def is_title_matches(self):
        return "Sign-in" in self.driver.title

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


class HomePage(BasePage):
    def is_classes_found(self):
        return "My Classes" in self.driver.page_source

    def click_classes_button(self):
        self.driver.find_element(*HomePageLocators.CLASSES_BUTTON).click()


class ClassesPage(BasePage):
    def click_day_button(self, day):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(
                ClassesPageLocators.get_day_button(day)
            )
        ).click()

    def click_time_button(self, timeslot):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(
                ClassesPageLocators.get_time_button(timeslot)
            )
        ).click()

    def click_reserve_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                ClassesPageLocators.RESERVE_BUTTON
            )
        ).click()

    def is_cancel_found(self):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.CANCEL_BUTTON)
        )

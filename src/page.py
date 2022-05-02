from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from element import InputElement
from locator import *


class InputUsernameElement(InputElement):
    # Inherit setter and getter functionality from InputElement
    locator = LoginPageLocators.USERNAME_FIELD[1]


class InputPasswordElement(InputElement):
    # Inherit setter and getter functionality from InputElement
    locator = LoginPageLocators.PASSWORD_FIELD[1]


class BasePage(object):
    def __init__(self, driver):
        """
        Initialize the base page with properties inherited by sub-classes

        Keyword arguments:
        driver -- the Chrome driver
        """
        self.driver = driver


class LoginPage(BasePage):
    # Create descriptors for username and password to hide functionality
    input_username_element = InputUsernameElement()
    input_password_element = InputPasswordElement()

    def is_title_matches(self):
        """
        Check if sign-in is in the title of the webpage
        """

        return "Sign-in" in self.driver.title

    def click_login_button(self):
        """
        Click on the button to login
        """

        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


class HomePage(BasePage):
    def is_classes_found(self):
        """
        Check if my classes is in the page source of the webpage
        """

        return "My Classes" in self.driver.page_source

    def click_classes_button(self):
        """
        Click on the button for my classes
        """

        self.driver.find_element(*HomePageLocators.CLASSES_BUTTON).click()


class ClassesPage(BasePage):
    def click_day_button(self, day):
        """
        Click on the desired day when it appears

        Keyword arguments:
        day -- the desired day
        """

        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(
                ClassesPageLocators.get_day_button(day)
            )
        ).click()

    def click_time_button(self, timeslot):
        """
        Click on the desired timeslot when it appears

        Keyword arguments:
        timeslot -- the desired timeslot
        """

        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(
                ClassesPageLocators.get_time_button(timeslot)
            )
        ).click()

    def click_reserve_button(self):
        """
        Click on the reserve button when it appears
        """

        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(
                ClassesPageLocators.RESERVE_BUTTON
            )
        ).click()

    def is_cancel_found(self):
        """
        Check if the cancel reservation button exists 
        """

        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.CANCEL_BUTTON)
        )

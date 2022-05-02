from selenium.webdriver.common.by import By
import datetime


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, "login-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="new_member"]/div[4]/input')


class HomePageLocators(object):
    CLASSES_BUTTON = (By.CSS_SELECTOR, 'a[href="/my-classes"]')


class ClassesPageLocators(object):
    RESERVE_BUTTON = (By.XPATH, "//span[contains(text(),'reserve')]")
    CANCEL_BUTTON = (
        By.XPATH, "//span[contains(text(),'cancel Reservation')]"
    )

    def get_day_button(day):
        return (By.CSS_SELECTOR, f"li[data-dayname='{day}']")

    def get_time_button(time):
        return (By.XPATH, f"//p[contains(text(),'{time} EDT')]")

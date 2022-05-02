from selenium.webdriver.common.by import By


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
        """
        Locates the button for the desired day

        Keyword arguments:
        day -- the desired day
        """

        return (By.CSS_SELECTOR, f"li[data-dayname='{day}']")

    def get_time_button(time):
        """
        Locates the button for the desired time

        Keyword arguments:
        time -- the desired time
        """

        return (By.XPATH, f"//p[contains(text(),'{time} EDT')]")

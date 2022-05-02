from selenium.webdriver.support.ui import WebDriverWait


class InputElement(object):

    def __set__(self, obj, value):
        """
        Set the value of an input element
        """

        driver = obj.driver

        # Use anonymous function to perform search for custom locator
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )

        # Update the located field with the new value
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """
        Get the value of an input element
        """

        driver = obj.driver

        # Use anonymous function to perform search for custom locator
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )

        # Retrieve the value at the located field
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")

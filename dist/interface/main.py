#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page
import pause
from datetime import datetime, timedelta
import time
import schedule
from sys import argv
import json
import smtplib
from email.message import EmailMessage
from selenium.common.exceptions import TimeoutException
from chromedriver_py import binary_path


class CrunchFitnessBot:
    def __init__(self, email, email_password, crunch_password, timeslots):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--disable-gpu')
        self.prefs = {}
        self.options.experimental_options["prefs"] = self.prefs
        self.prefs["profile.default_content_settings"] = {"images": 2}

        self.email = email
        self.email_password = email_password
        self.crunch_password = crunch_password
        self.timeslots = timeslots

    def send_mail(self, message):
        msg = EmailMessage()
        msg['from'] = self.email
        msg['to'] = self.email
        msg['subject'] = "Your reservation status"
        msg.set_content(message)

        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.email, self.email_password)
        server.send_message(msg)
        server.quit()

    def login(self):
        login_page = page.LoginPage(self.driver)

        if login_page.is_title_matches():
            login_page.input_username_element = self.email
            login_page.input_password_element = self.crunch_password

            try:
                login_page.click_login_button()
            except NoSuchElementException:
                self.send_mail("ERROR: Could not click on login button")
                self.driver.close()
        else:
            self.send_mail("ERROR: Could not validate page title")
            self.driver.close()

    def find_reservation(self):
        home_page = page.HomePage(self.driver)

        if home_page.is_classes_found():
            home_page.click_classes_button()

            now = datetime.now()

            pause.until(datetime(
                now.year, now.month, now.day, now.hour + 1
            ))
            self.driver.refresh()
            time.sleep(5)

        else:
            self.send_mail("ERROR: Could not locate classes button")
            self.driver.close()

    def make_reservation(self, timeslot, day):
        classes_page = page.ClassesPage(self.driver)

        try:
            classes_page.click_day_button(day)
            try:
                classes_page.click_time_button(timeslot)
                try:
                    classes_page.click_reserve_button()
                except TimeoutException:
                    self.send_mail("ERROR: Could not find reserve button")
                    self.driver.close()
            except TimeoutException:
                self.send_mail("ERROR: Could not find desired time")
                self.driver.close()
        except TimeoutException:
            self.send_mail("ERROR: Could not find desired day")
            self.driver.close()

        time.sleep(120)
        self.driver.refresh()

        try:
            classes_page.is_cancel_found()
            self.send_mail(f"Your reservation at Crunch Fitness for {day} at {timeslot} was successful")
            self.driver.close()
        except TimeoutException:
            self.send_mail("ERROR: Timeslot is full")
            self.driver.close()

    def reserve(self, timeslot, day):
        '''self.driver = webdriver.Chrome(
            "/usr/local/bin/chromedriver", options=self.options
        )'''

        self.driver = webdriver.Chrome(
            executable_path=binary_path
        )

        self.driver.get("https://members.crunchfitness.ca/members/sign_in")

        CrunchFitnessBot.login(self)
        CrunchFitnessBot.find_reservation(self)
        CrunchFitnessBot.make_reservation(
            self, timeslot, day
        )

    def main(self):
        for day, timeslot in timeslots.items():
            if timeslot:
                booking_time = datetime.strptime(
                    timeslot, "%H:%M"
                ) - timedelta(hours=22, minutes=5)
                booking_time = booking_time.strftime("%H:%M")

                if day == "Monday":
                    schedule.every().sunday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Tuesday":
                    schedule.every().monday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Wednesday":
                    schedule.every().tuesday.at("12:29").do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Thursday":
                    schedule.every().wednesday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Friday":
                    schedule.every().thursday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Saturday":
                    schedule.every().friday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )
                elif day == "Sunday":
                    schedule.every().saturday.at(booking_time).do(
                        CrunchFitnessBot.reserve, self, timeslot, day
                    )

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    email = argv[1]
    email_password = argv[2]
    crunch_password = argv[3]
    timeslots = json.loads(argv[4])

    cfb = CrunchFitnessBot(email, email_password, crunch_password, timeslots)
    cfb.main()

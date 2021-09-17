import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import json
from datetime import datetime

options = Options()
options.headless = True

class Bot:
    def __init__(self, t, person):
        self.bot = webdriver.Firefox(options=options)
        self.type = t
        self.fullName = person['fullName']
        self.email = person["email"]
        self.mobile = person["mobile"]
        if self.type != "student" and self.type != "guest":
            raise ValueError("User type can only be {student} or {guest}")

    def next(self):
        next = self.bot.find_element_by_id("NextButton")
        next.click()

    def start(self):
        self.bot.get("https://uoguelph.eu.qualtrics.com/jfe/form/SV_4Ntfm8k1oXAPssm")
        time.sleep(1)
        yes = self.bot.find_element_by_id("QID3-1-label")
        yes.click()
        self.next()
        time.sleep(2)
        self.next()
        time.sleep(2)

    def fill(self):
        if self.type == "student":
            self.fill_student()
        elif self.type == "guest":
            self.fill_guest()

    def fill_student(self):
        student = self.bot.find_element_by_xpath("//span[.='University of Guelph Student']")
        student.click()
        self.next()
        time.sleep(2)
        self.bot.find_element_by_xpath("//span[.='No']").click()
        self.next()
        time.sleep(2)
        self.bot.find_element_by_id("QR~QID5").send_keys(self.fullName)
        self.bot.find_element_by_id("QR~QID7").send_keys(self.email)
        self.bot.find_element_by_id("QR~QID8").send_keys(self.mobile)
        self.next()
        time.sleep(2)
        self.bot.find_element_by_xpath("//span[.='I do not seem to have symptoms of COVID-19 and am not required to self-isolate']").click()
        self.next()

    def fill_guest(self):
        guest = self.bot.find_element_by_xpath("//span[.='Visitor']")
        guest.click()
        self.next()
        time.sleep(2)
        self.bot.find_element_by_xpath("//span[.='I attest that I am fully vaccinated']").click()
        self.next()
        time.sleep(2)
        self.bot.find_element_by_id("QR~QID5").send_keys(self.fullName)
        self.bot.find_element_by_id("QR~QID7").send_keys(self.email)
        self.bot.find_element_by_id("QR~QID8").send_keys(self.mobile)
        self.next()
        time.sleep(2)
        self.bot.find_element_by_xpath("//span[.='I do not seem to have symptoms of COVID-19 and am not required to self-isolate']").click()
        self.next()

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)
    for t in config.keys():
        for person in config[t]:
            bot = Bot(t, person)
            bot.start()
            bot.fill()
            print("Completed covid test form for {} on {}".format(person["fullName"], datetime.strftime(datetime.now(), "%B %d, %Y %H:%M:%S")))
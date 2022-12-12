import datetime
import undetected_chromedriver as uc
from requests import put
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random
import secrets
from logging import log  # import json file to write to

emails_liste = ['collectoradress999+FTest1-111@gmail.com',
                'collectoradress999+FTest2-111@gmail.com',
                'collectoradress999+FTest3-111@gmail.com',
                'collectoradress999+FTest4-111@ygmail.com',
                'collectoradress999+FTest5-111@gmail.com']


def getSecretRandomNumber(min, max):
    return secrets.randbelow(max - min) + min


wait_after_side_loaded_time = getSecretRandomNumber(4, 14)
wait_after_button_clicked_time = getSecretRandomNumber(2, 8)
wait_after_clicking_email_input_time = getSecretRandomNumber(2, 8)
wait_after_inputting_email_time = getSecretRandomNumber(2, 8)
wait_after_clicking_send_button_time = getSecretRandomNumber(8, 23)
wait_after_fetching_code_time = getSecretRandomNumber(12, 18)
interval_between_digits_input_time = getSecretRandomNumber(1, 3)
final_wait_time = getSecretRandomNumber(1, 100)

# random_number = getSecretRandomNumber(3, 21)


# inputs
driver = uc.Chrome()
link = "https://poll-maker.com/QDZ9LFGAP"
verification_email = "x"
# emails_liste[]

option_button = '//*[@id="qp_main14874138"]/div[2]/div/div[1]/div/span'
searchbar = "#verify-inp > div.qp_login_social.em > input.qp_verify_em"
send_mail_button = "#verify-inp > div.qp_login_social.em > div.qp_verify_emb"
input_code_field = "#verify-inp > div.qp_login_social.em > input.qp_verify_emc"


def chrome_options():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("proxy-server=socks5://")
    options.add_argument("--headless")
    options.add_argument("--user-data-dir=/Users/jimvincentwagner/Library/Application Support/Google/Chrome/Default")


chrome_options()  # instantiating the function


class Foo:
    def __init__(self, driver):
        self.driver = driver

    def get_link(self):
        self.driver.get(link)

    def click_option_and_enter_email(self):
        self.get_link()
        print("site loaded")
        time.sleep(wait_after_side_loaded_time)
        self.driver.find_element(By.XPATH, option_button).click()
        print("answer_clicked")  # click A
        time.sleep(wait_after_button_clicked_time)
        self.driver.find_element(By.CSS_SELECTOR, searchbar).click()
        print("email input clicked")  # click Email Input
        time.sleep(wait_after_clicking_email_input_time)
        self.driver.find_element(By.CSS_SELECTOR, searchbar).send_keys(verification_email)
        print("email put in")  # input Email
        time.sleep(wait_after_inputting_email_time)
        self.driver.find_element(By.CSS_SELECTOR, send_mail_button).click()
        print("answer and email submitted")  # click send

    @staticmethod
    def fetch_email():
        mail_caller()
        print(mail_caller())

    def input_code(self) -> object:
        for i in mail_caller():
            for char in i:
                self.driver.find_element(By.CSS_SELECTOR, input_code_field).send_keys(char)
                time.sleep(interval_between_digits_input_time)

        # self.driver.find_element(By.CSS_SELECTOR, input_code_field).send_keys(Keys.ENTER)


def mail_caller():
    import imaplib
    import email
    import re
    imap_server = "imap.gmail.com"
    imap_port = 993
    email_address = "collectoradress999@gmail.com"
    # password = "xobsab-2mepne-dyMzyf" #this is the original collector password
    password = "swuzhjqulexrzxah"  # collector adress app password
    # password = "txmtaqgrmirjgbqa" #blacklight
    # password = "hbwdtarewxmckvac"  # vincent.johanness

    imap = imaplib.IMAP4_SSL(imap_server)

    imap.login(email_address, password)

    imap.select("INBOX")
    value = "UNSEEN"

    key = "FROM"
    value = "noreply@poll-maker.com"
    _, data = imap.search(None, "ALL")

    mail_id_list = data[0].split()

    msgs = []

    for num in mail_id_list:
        typ, data = imap.fetch(num, '(RFC822)')
        msgs.append(data)

    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                original = email.message_from_bytes((response_part[1]))
                # print("-------MESSAGE----")
                # print(original['From'])
                # print("------------------")
                # print(original['Subject'])
                # print("------------------")
                # print(original['Date'])
                # print("------------------")
                # print(original.get_payload())
                # print("--------END-------")
                for part in original.walk():
                    if part.get_content_type() == "text/html":
                        # print(part.get_payload())
                        html_line = part.get_payload()
                        html_line = html_line.splitlines()
                        html_line = str(html_line)
                        code = re.findall("\d{6}", html_line)
                        return code  # returns the code as a list
                        return [code[0]]
                        return "FROM"
                        print(code[0])


## define function that writes the verification email an the correspoinding code to a file
def write_to_file():
    with open("verification_codes.txt", "a") as file:
        file.write(verification_email + " " + str(mail_caller()) + "\n")


def process1():
    foo = Foo(driver)
    Foo.click_option_and_enter_email(self=foo)


def process2() -> object:
    foo = Foo(driver)
    foo.input_code()
    print("code entered")


# email loop
while True:
    for email in emails_liste:
        if len(emails_liste) == 0:
            print("no more emails in list")
            driver.close()
        else:
            verification_email = random.choice(emails_liste)
            print("chose:", verification_email)
            emails_liste.remove(verification_email)
            process1()
            foo = Foo(driver)
            time.sleep(wait_after_clicking_send_button_time)
            mail_caller()
            print("code from mail" + str(mail_caller()))
            print("fetched from:  " + verification_email)
            time.sleep(wait_after_fetching_code_time)
            process2()
            time.sleep(final_wait_time)
            print("--------------------")
            #print("done with run with: " + str(run_number))
            print("--------------------")

            log_file = open("logs.txt", "a")
            log_file.write(f"{verification_email}, {mail_caller()}, {datetime.datetime.now()}\n")
            log_file.close()
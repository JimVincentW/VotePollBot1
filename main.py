import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import datetime
from datetime import date
import random
import secrets
today = date.today()


emails_liste = ['collectoradress999@gmail.com']
'''
if today.day % 2 == 0:
  # day is an even number
  emails_liste = []
else:
  # day is an uneven number
  emails_liste = []

'''


def getSecretRandomNumber(min, max):
    return secrets.randbelow(max - min) + min


wait_after_side_loaded_time = secrets.randbelow(10) + 4
wait_after_button_clicked_time = getSecretRandomNumber(2, 8)
wait_after_clicking_email_input_time = getSecretRandomNumber(2, 8)
wait_after_inputting_email_time = getSecretRandomNumber(2, 10)
wait_after_clicking_send_button_time = getSecretRandomNumber(8, 23)
wait_after_fetching_code_time = getSecretRandomNumber(12, 18) # 30, 300
interval_between_digits_input_time = getSecretRandomNumber(1, 3)
final_wait_time = getSecretRandomNumber(10, 100)
wait_after_run_time = getSecretRandomNumber(250, 3000)

# random_number = getSecretRandomNumber(3, 21)

def chrome_options():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    #options.add_argument("proxy-server=socks5://") #no proxy in place yet
    options.add_argument("--headless")
    options.add_argument("--user-data-dir=/Users/jimvincentwagner/Library/Application Support/Google/Chrome/Default")
chrome_options()  # instantiating the function



# inputs
driver = uc.Chrome(options=chrome_options())
link = "https://poll-maker.com/QS5246LR4"
verification_email = "x"

option_button = '//*[@id="qp_main14874138"]/div[2]/div/div[1]/div/span'
searchbar = "#verify-inp > div.qp_login_social.em > input.qp_verify_em"
send_mail_button = "#verify-inp > div.qp_login_social.em > div.qp_verify_emb"
input_code_field = "#verify-inp > div.qp_login_social.em > input.qp_verify_emc"


class Foo:
    def __init__(self, driver):
        self.driver = driver

    def get_link(self):
        self.driver.get(link)


    def brutkasten_clicker(self):

        choose_team_button = '//*[@id="qp_main14775033"]/div[2]/div/div[8]/div'
        click_email_input = '#verify-inp > div.qp_login_social.em > input.qp_verify_em'
        click_send_button = '#verify-inp > div.qp_login_social.em > div.qp_verify_emb'

        self.get_link()
        print("site loaded")
        time.sleep(wait_after_side_loaded_time)
        self.driver.find_element(By.XPATH, choose_team_button).click()
        print("team chosen")
        time.sleep(wait_after_button_clicked_time)
        #self.driver.find_element(By.CSS_SELECTOR, vote_for_team_button).click()
        #print("voted")
        time.sleep(wait_after_button_clicked_time)
        self.driver.find_element(By.CSS_SELECTOR, click_email_input).click()
        print("email input clicked")
        self.driver.find_element(By.CSS_SELECTOR, click_email_input).send_keys(verification_email)
        print("email inputted")
        self.driver.find_element(By.CSS_SELECTOR, click_send_button).click()
        print("send button clicked")


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
    Foo.brutkasten_clicker(self=foo)


def process2() -> object:
    foo = Foo(driver)
    foo.input_code()
    print("code entered")


# email loop
while True:
    for email in emails_liste:
        if len(emails_liste) == 0:
            break
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
            print("--------------------")

            log_file = open("logs.txt", "a")
            log_file.write(f"{verification_email}, {mail_caller()}, {datetime.datetime.now()}\n")
            log_file.close()
            if not emails_liste:
                print("All emails have been used, quitting script.")
                quit()
            else:
                time.sleep(wait_after_run_time)

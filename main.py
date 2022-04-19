from __future__ import annotations
from datetime import datetime
import paths
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


class User:
    def __init__(self, name: str, password: str, session: Session) -> None:
        self.name = name
        self.password = password
        self.session = session

    @property
    def schoolpass(self) -> int:
        previous_link = self.session.driver.current_url
        self.session.driver.get(paths.main_page_url)
        element = self.session.driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[5]/td[3]/a/div/div")
        schoolpass_ = int(element.text)
        self.session.driver.get(previous_link)
        return schoolpass_

    def __str__(self):
        return self.name


class Session:
    def __init__(self, user: str, password: str, chromedriver_path: str=r"C:\Chromedriver\chromedriver.exe") -> None:
        self.user = User(user, password, self)
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--log-level=3")
            self.driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)
        except WebDriverException:
            print("ChromeDriver not found. Please download it from https://chromedriver.chromium.org/downloads")

    def login(self) -> bool:
        self.driver.get(paths.login_url)
        self.driver.find_element_by_xpath(paths.code_input).send_keys(self.user.name)
        self.driver.find_element_by_xpath(paths.password_input).send_keys(self.user.password)
        self.driver.find_element_by_xpath(paths.login_button).click()
        self.start_time = datetime.now()
        print(self)

    @property
    def time_left(self) -> int:
        return (datetime.now() - self.start_time).seconds

    def __del__(self) -> None:
        self.driver.close()

    def __str__(self):
        return f"User: {self.user}\nTime-left: {self.time_left}s"
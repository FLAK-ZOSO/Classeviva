from __future__ import annotations
from datetime import datetime
import paths
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException
from variables import *


class User:
    def __init__(self, name: str, password: str, session: Session, role=Roles.STUDENT) -> None:
        self.name = name
        self.password = password
        self.session = session
        self.role = role

    @property
    def schoolpass(self) -> int:
        if (self.role): # If it's not a student
            return 0
        previous_link = self.session.driver.current_url
        self.session.driver.get(paths.main_page_url)
        element = self.session.driver.find_element(By.XPATH, paths.schoolpass_div)
        schoolpass_ = int(element.text)
        self.session.driver.get(previous_link)
        return schoolpass_

    def __str__(self) -> str:
        return f"{self.name} | {self.password} | {self.schoolpass}"


class Session:
    def __init__(self, user: str, password: str, chromedriver_path: str=r"C:\Chromedriver\chromedriver.exe", role: str=Roles.STUDENT, hidden: bool=False) -> None:
        self.user = User(user, password, self, role)
        try:
            chrome_options = Options()
            if (hidden):
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--log-level=3")
            self.driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)
        except WebDriverException:
            print("ChromeDriver not found. Please download it from https://chromedriver.chromium.org/downloads")

    def login(self) -> bool:
        self.driver.get(paths.login_url)
        self.driver.find_element(By.XPATH, paths.code_input).send_keys(self.user.name)
        self.driver.find_element(By.XPATH, paths.password_input).send_keys(self.user.password)
        self.driver.find_element(By.XPATH, paths.login_button).click()
        self.start_time = datetime.now()
        print(self)

    @property
    def time_left(self) -> int:
        return 60*60 - (datetime.now() - self.start_time).seconds

    def __str__(self) -> str:
        return f"User: {self.user}\nTime-left: {self.time_left}s"


class Valutazioni:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.driver = session.driver
        self.user = session.user

    def start(self) -> None:
        self.driver.get(paths.valutazioni_voti_url)

    @property
    def subjects(self) -> list[str]:
        self.driver.get(paths.valutazioni_note_url)
        return [element.text for element in self.driver.find_elements(By.XPATH, paths.subjects_tds)]

    def get_valutations_marks(self, first_period: bool=True, second_period: bool=True) -> list[float | str]:
        self.driver.get(paths.valutazioni_voti_url)
        result: list[float | str] = []
        if (first_period):
            for p in self.driver.find_elements(By.XPATH, paths.marks):
                mark: str = p.text
                if (not mark):
                    continue
                try:
                    result.append(float(mark.replace('½', '.5')))
                except ValueError:
                    result.append(mark)
        if (second_period):
            self.driver.get(f"{paths.valutazioni_note_url}#S3")
            for p in self.driver.find_elements(By.XPATH, paths.marks):
                mark: str = p.text
                if (not mark):
                    continue
                try:
                    result.append(float(mark.replace('½', '.5')))
                except ValueError:
                    result.append(mark)
        return result

    def get_valutations(self, opt_date: bool=True, opt_type: bool=True, opt_description: bool=True) -> list[tuple[str, str, float | str, str, str]]:
        self.driver.get(paths.valutazioni_note_url)
        result: list[tuple[str, str, float | str, str, str]] = []
        trs = self.driver.find_elements(By.XPATH, paths.trs)
        b = False # True if the current tr is after the first subject
        for tr in trs:
            if (tr.get_attribute("class") == "griglia"):
                b = True
                continue
            if (not b):
                continue
            if (tr.get_attribute("align") == "center"):
                last_subject = tr.find_element(By.TAG_NAME, "td").text
            else:
                tds: list[WebElement] = tr.find_elements(By.TAG_NAME, "td")
                mark: str = tds[2].find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "p").text
                if (not (any(sym in mark for sym in {'+', '-'}) or mark == 'g')):
                    mark = float(mark.replace('½', '.5'))
                res = [last_subject, mark]
                if (opt_date):
                    date: str = tds[1].find_element(By.TAG_NAME, "p").text
                    res.append(date)
                if (opt_type):
                    type_: str = tds[3].find_element(By.TAG_NAME, "p").get_attribute("title")
                    res.append(type_)
                if (opt_description):
                    description: str = tds[5].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "span").text
                    res.append(description)
                result.append(tuple(res))
        return result

    def get_valutations_by_subject(self, opt_date: bool=True, opt_type: bool=True, opt_description: bool=True) -> dict[str, list[tuple]]:
        self.driver.get(paths.valutazioni_note_url)
        result: dict[str, list[tuple[str, float | str, str, str]]] = {}
        trs = self.driver.find_elements(By.XPATH, paths.trs)
        b = False # True if the current tr is after the first subject
        for tr in trs:
            if (tr.get_attribute("class") == "griglia"):
                b = True
                continue
            if (not b):
                continue
            if (tr.get_attribute("align") == "center"):
                last_subject = tr.find_element(By.TAG_NAME, "td").text
                result[last_subject] = []
            else:
                mark: str = tds[2].find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "p").text
                if (not (any(sym in mark for sym in {'+', '-'}) or mark == 'g')):
                    mark = float(mark.replace('½', '.5'))
                res = [last_subject, mark]
                tds: list[WebElement] = tr.find_elements(By.TAG_NAME, "td")
                if (opt_date):
                    date: str = tds[1].find_element(By.TAG_NAME, "p").text
                    res.append(date)
                if (opt_type):
                    type_: str = tds[3].find_element(By.TAG_NAME, "p").get_attribute("title")
                    res.append(type_)
                if (opt_description):
                    description: str = tds[5].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "span").text
                    res.append(description)
                result[last_subject].append(tuple(res))
        return result
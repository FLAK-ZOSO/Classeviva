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
        self.session.driver.get(paths.main_page_url)
        element = self.session.driver.find_element(By.XPATH, paths.schoolpass_div)
        schoolpass_ = int(element.text)
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


class Finestra:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.driver: webdriver.Chrome = session.driver
        self.user = session.user


class Valutazioni(Finestra):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    @property
    def subjects(self) -> list[str]:
        if (self.driver.current_url != paths.valutazioni_note_url):
            self.driver.get(paths.valutazioni_note_url)
        return [element.text for element in self.driver.find_elements(By.XPATH, paths.subjects_tds)]

    def get_valutations_marks(self, first_period: bool=True, second_period: bool=True) -> list[float | str]:
        result: list[float | str] = []
        if (first_period):
            self.driver.get(f"{paths.valutazioni_voti_url}#S1")
            for p in self.driver.find_elements(By.XPATH, paths.marks):
                mark: str = p.text
                if (not mark):
                    continue
                try:
                    result.append(float(mark.replace('½', '.5')))
                except ValueError:
                    result.append(mark)
        if (second_period):
            self.driver.get(f"{paths.valutazioni_voti_url}#S3")
            for p in self.driver.find_elements(By.XPATH, paths.marks):
                mark: str = p.text
                if (not mark):
                    continue
                try:
                    result.append(float(mark.replace('½', '.5')))
                except ValueError:
                    result.append(mark)
        return result

    def get_valutations(self, date: bool=True, type_: bool=True, notes: bool=True) -> list[tuple[str, str, float | str, str, str]]:
        if (self.driver.current_url != paths.valutazioni_note_url):
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
                if (date):
                    res.append(tds[1].find_element(By.TAG_NAME, "p").text)
                if (type_):
                    res.append(tds[3].find_element(By.TAG_NAME, "p").get_attribute("title"))
                if (notes):
                    res.append(tds[5].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "span").text)
                result.append(tuple(res))
        return result

    def get_valutations_by_subject(self, date: bool=True, type_: bool=True, notes: bool=True) -> dict[str, list[tuple]]:
        if (self.driver.current_url != paths.valutazioni_note_url):
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
                if (date):
                    res.append(tds[1].find_element(By.TAG_NAME, "p").text)
                if (type_):
                    res.append(tds[3].find_element(By.TAG_NAME, "p").get_attribute("title"))
                if (notes):
                    res.append(tds[5].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "span").text)
                result[last_subject].append(tuple(res))
        return result


class Note(Finestra):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    @property
    def lenght(self) -> int:
        if (self.driver.current_url != paths.note_url):
            self.driver.get(paths.note_url)
        # Select 40 notes for page
        self.driver.find_element(By.XPATH, paths.note_option.format(4)).click()
        # Count the pages
        pages: str = self.driver.find_element(By.XPATH, paths.pages_input).get_attribute("value")
        pages = int(pages.split('/')[1])
        counter: int = (pages-1)*40
        # Go to the last page
        self.driver.find_element(By.XPATH, paths.last_img).click()
        # Coutn the notes of the last page
        counter += len(self.driver.find_elements(By.XPATH, paths.nota_trs))
        return counter

    def get_notes(self, sort: int=NoteSortBy.AUTHOR, teacher: bool=True, date: bool=True, type_: bool=True) -> list[tuple[str, str, str, str] | tuple[str, str, str] | tuple[str, str] | tuple[str]]:
        if (self.driver.current_url != paths.note_url):
            self.driver.get(paths.note_url)
        # Select the specified sorting
        tr: WebElement = self.driver.find_element(By.XPATH, paths.order_tr)
        tr.find_elements(By.TAG_NAME, "th")[sort].click()
        # Get the notes
        result: list[tuple[str, str, str, str] | tuple[str, str, str] | tuple[str, str] | tuple[str]] = []
        for tr in self.driver.find_elements(By.XPATH, paths.nota_trs):
            tds: list[WebElement] = tr.find_elements(By.TAG_NAME, "td")
            res = [tds[2].text]
            if (teacher):
                res.append(tds[0].text)
            if (date):
                res.append(tds[1].text)
            if (type_):
                res.append(tds[3].text)
            result.append(tuple(res))
        return result


class Registro(Finestra):
    def __init__(self, session: Session) -> None:
        super().__init__(session)


    class Date:
        week: tuple[str] = ('lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica')
        months: tuple[str] = ('gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre')

        def __init__(self, weekday: int | str, day: int | str, month: int | str, year: int | str) -> None:
            self.day = int(day)
            self.weekday = self.int_from_weekday(weekday)
            self.month = int(month)
            self.year = int(year)

        def int_from_weekday(weekday: str) -> int:
            try:
                return Registro.Date.week.index(weekday.lower()) + 1
            except ValueError:
                return 0

        @classmethod
        def from_str(cls, date: str) -> Registro.Date:
            # SABATO 23 APRILE 2022
            date = date.split()
            return cls(date[0], date[1], date[2], date[3])

    @property
    def day(self) -> str:
        if (self.driver.current_url != paths.registro_url):
            self.driver.get(paths.registro_url)
        return self.driver.find_element(By.XPATH, paths.data_a).text

    @property
    def day_date(self) -> Registro.Date:
        return Registro.Date.from_str(self.day)

    def _select_date(self, date: Registro.Date) -> None:
        if (self.driver.current_url != paths.registro_url):
            self.driver.get(paths.registro_url)
        # Click on the current date button
        date_button: WebElement = self.driver.find_element(By.XPATH, paths.data_a)
        date_button.click()
        # Scroll to the wanted date
    
    status_str: dict[str, int] = {
        'p': RegistroStatus.PRESENTE,
        'a': RegistroStatus.ASSENTE,
        'al': RegistroStatus.ASSENTE
    }

    def status_from_str(self, status: str) -> int:
        try:
            return Registro.status_str[status]
        except KeyError:
            return 0

    def get_status(self, date: Registro.Date, hour: int=0) -> int:
        if (self.driver.current_url != paths.registro_url):
            self.driver.get(paths.registro_url)
        # Select the specified date
        ...
        # Get the status from the date
        if (not hour): # They want the status of the day
            status: WebElement = self.driver.find_element(By.XPATH, paths.status_p)
            status_: str = status.text
            return self.status_from_str(status_.lower())
        else: # They want the status of a specific hour
            ... # TODO: Implement this
            # The problem is caused by the fact that some hours come with groups of two or three
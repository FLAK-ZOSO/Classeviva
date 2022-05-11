Intro
===========================

``ClassevivaAPI`` contiene al suo interno i seguenti moduli:

    - ``classeviva``: contiene le classi per la comunicazione con il sito di Classeviva;
    - ``classeviva.exceptions``: contiene le eccezioni che possono essere sollevate [1]_
    - ``classeviva.paths``: contiene gli xpath, i CSSselectors e i link per l'accesso al sito di Classeviva
    - ``classeviva.variables``: contiene le costanti [2]_


``classeviva``
===========================
Classeviva è il modulo che contiene le classi per la comunicazione con il sito di Classeviva.


``Session``
---------------------------

Costruttore

    .. code-block:: python

        def __init__(
            self, user: str, password: str, 
            chromedriver_path: str=r"C:\Chromedriver\chromedriver.exe", 
            hidden: bool=False
        ) -> None:

    Parametri:

    - ``user``: username dell'utente
    - ``password``: password dell'utente
    - ``chromedriver_path``: percorso del driver di Chrome
    - ``hidden``: se True, il browser non viene visualizzato


Attributi
    
    - ``.user: User`` - username dell'utente
    - ``.driver: webdriver.Chrome`` -  il driver di Chrome
    - ``.start_time: datetime.datetime`` - ora di inizio sessione

Proprietà

    - ``.time_left: int`` - tempo rimanente per la sessione

Metodi

    - ``.login()`` - effettua il login

    .. code-block:: python

        def login(self) -> None:
            self.driver.get(paths.login_url)
            self.driver.find_element(By.XPATH, paths.code_input).send_keys(self.user.name)
            self.driver.find_element(By.XPATH, paths.password_input).send_keys(self.user.password)
            self.driver.find_element(By.XPATH, paths.login_button).click()
            self.start_time = datetime.now()
            print(self)

Metodi magici

    .. code-block:: python

        def __str__(self) -> str:
            return f"User: {self.user}\nTime-left: {self.time_left}s"

``User``
===========================

Costruttore

    .. code-block:: python

        def __init__(
            self, name: str, password: str, 
            session: Session
        ) -> None:
    
    Parametri:

    - ``name``: username dell'utente
    - ``password``: password dell'utente
    - ``session``: sessione di Classeviva

Attributi

    - ``.name: str`` - username dell'utente
    - ``.password: str`` - password dell'utente
    - ``.session: Session`` - sessione di Classeviva
    - ``.role: int`` - ruolo [3]_

Proprietà

    - ``.schoolpass: int`` - schoolpass dell'utente

Metodi magici

    .. code-block:: python

        def __str__(self) -> str:
            return f"{self.name} | {self.password} | {self.schoolpass}"

Note
===========================

.. [1] Non ancora implementato nelle versioni <0.3
.. [2] Organizzate per classi a mo' di namespace
.. [3] Dalla classe ``classeviva.variables.variables.Roles``
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

        def __init__(self, user: str, password: str, chromedriver_path: str=r"C:\Chromedriver\chromedriver.exe", hidden: bool=False) -> None:

    Parametri:

    - ``user``: username dell'utente
    - ``password``: password dell'utente
    - ``chromedriver_path``: percorso del driver di Chrome
    - ``hidden``: se True, il browser non viene visualizzato


Attributi
    
    ``.user: User`` - username dell'utente
    ``.driver: webdriver.Chrome`` -  il driver di Chrome
    ``.start_time: datetime.datetime`` - ora di inizio sessione

Proprietà

    ``.time_left: int`` - tempo rimanente per la sessione

Metodi

    .. code-block:: python

        def login(self) -> None:

Metodi magici

    .. code-block:: python

        def __str__(self) -> str:
            return f"User: {self.user}\nTime-left: {self.time_left}s"


Note
===========================

.. [1] Non ancora implementato nelle versioni <0.3
.. [2] Organizzate per classi a mo' di namespace
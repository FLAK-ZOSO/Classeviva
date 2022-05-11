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

Segue l'elenco delle classi pubbliche del modulo classeviva:

- `Session <#id3>`_: classe che rappresenta una sessione di comunicazione con il sito di Classeviva
- `User <#id4>`_: classe che rappresenta un utente di Classeviva


``Session``
---------------------------

Rappresenta una sessione di comunicazione con il sito di Classeviva.
Genera un'istanza della classe ``User`` quando inizializzata.


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
---------------------------

Rappresenta un utente di Classeviva, ne contiene anche le informazioni necessarie per effettuare il login.
Le sue istanze vengono utilizzate principalmente per gestire i dati dell'utente.


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


``Finestra``
---------------------------

Classe che rappresenta una finestra di Classeviva.
Le sue sottoclassi rappresentano le diverse finestre di Classeviva, come ad esempio "Valutazioni" e "Note".


Costruttore
    
    .. code-block:: python

        def __init__(self, session: Session) -> None:
    
    Parametri:

    - ``session: Session``: sessione di Classeviva

Attributi

    - ``.session: Session`` - sessione di Classeviva
    - ``.driver: webdriver.Chrome`` - il driver di Chrome [4]_
    - ``.user: User`` - utente di Classeviva [4]_


``Valutazioni (Finestra)``
---------------------------

Rappresenta la finestra "Valutazioni" di Classeviva.


Costruttore

    .. code-block:: python

        def __init__(self, session: Session) -> None:
            super().__init__(session)
        
    Parametri:

    - ``session: Session``: sessione di Classeviva

Attributi
    
    - ``.session: Session`` - sessione di Classeviva [5]_

Proprietà

    - ``.subjects: list[str]`` - materie di Classeviva

Metodi

    ``.get_valutations_marks()`` fornisce le valutazioni dell'anno scolastico corrente.
    Le ritorna sottoforma di ``list``a di ``float`` e ``str``inghe. [6]_

    Parametri:

    - ``first_period: bool=True`` - includere le valutazioni del primo periodo?
    - ``second_period: bool=True`` - includere le valutazioni del secondo periodo?

    .. code-block:: python

        def get_valutations_marks(
            self, first_period: bool=True, 
            second_period: bool=True
        ) -> list[float | str]:


    ``.get_valutations()`` fornisce le valutazioni dell'anno scolastico corrente con le informazioni sui voti.
    Le ritorna sottoforma di ``list``a di ``tuple``, che contengono la data, il tipo ("orale", "scritto" o "pratico"), la descrizione, il voto e la materia.

    Parametri:

    - ``date: bool=True`` - includere le date?
    - ``type_: bool=True`` - includere i tipi?
    - ``notes: bool=True`` - includere le descrizioni?

    .. code-block:: python
        
        def get_valutations(
            self, date: bool=True, 
            type_: bool=True, notes: bool=True
        ) -> list[tuple[str, str, float | str, str, str]]:
    

    ``.get_valutations_by_subject()`` fornisce le valutazioni dell'anno scolastico corrente ordinate per materia specifica.
    Le ritorna sottoforma di ``dict[str, list[tuple[str, float | str, str, str]]]``, che ha come chiave il nome della materia e come valore una lista di tuple, che contengono la data, il voto, il tipo [7]_ e la descrizione.

    Parametri:

    - ``date: bool=True`` - includere le date?
    - ``type_: bool=True`` - includere i tipi?
    - ``notes: bool=True`` - includere le descrizioni?

    .. code-block:: python

        def get_valutations_by_subject(
            self, date: bool=True, 
            type_: bool=True, notes: bool=True
        ) -> dict[str, list[tuple]]:


Note
===========================

.. [1] Non ancora implementato nelle versioni <0.3
.. [2] Organizzate per classi a mo' di namespace
.. [3] Dalla classe ``classeviva.variables.variables.Roles``
.. [4] Ereditato dall'omonimo attributo della classe ``Session``
.. [5] Ereditato dall'omonimo attributo della classe ``Finestra``
.. [6] Le ``str``inghe non vengono restituite a meno di un errore di conversione a ``float``
.. [7] Il tipo di voto è una ``str``inga, che può essere "orale", "scritto" o "pratico"
class Roles:
    '''
    Class to define the roles of the users
    '''
    STUDENTE: int = 0
    GENITORE: int = 1
    INSEGNANTE: int = 2

    letter_roles = {
        'S': STUDENTE,
        'G': GENITORE,
        'V': INSEGNANTE
    }

    @classmethod
    def from_username(cls, username: str) -> int:
        try:
            return cls.letter_roles[username[0]]
        except KeyError:
            # If login was made by email and not by username...
            # ...we assume that the user is a student
            return cls.STUDENTE


class NoteSortBy:
    '''
    Class defined to represent the different ways to sort the notes
    '''
    AUTHOR = 0
    DATE = 1
    NOTE = 2
    TYPE = 3


class RegistroStatus:
    '''
    Class defined to represent the status of a day or of an hour in the registro
    '''
    NO_LEZIONE: float          = -1.0 # Negative value on absent lesson
    PRESENTE: float            = 0.0
    PRESENTE_FUORI_AULA: float = 0.1
    PRESENTE_A_DISTANZA: float = 0.2
    ASSENTE: float             = 1.0
    RITARDO: float             = 2.0
    RITARDO_BREVE: float       = 2.1
    USCITO: float              = 3.0
    
    hour_status: dict[str, float] = {
        'xg': NO_LEZIONE,
        'pd': PRESENTE,
        'px': PRESENTE_FUORI_AULA,
        'pd': PRESENTE_A_DISTANZA,
        'a': ASSENTE,
        'al': ASSENTE
    }

    day_status: dict[str, float] = {
        'XG': NO_LEZIONE,
        'PL': PRESENTE,
        'AP': ASSENTE,
        'RB': RITARDO_BREVE,
        'U': USCITO
    }
    
    name_from_status: dict[float, str] = {
        NO_LEZIONE: 'NO_LEZIONE',
        PRESENTE: 'PRESENTE',
        PRESENTE_FUORI_AULA: 'PRESENTE_FUORI_AULA',
        PRESENTE_A_DISTANZA: 'PRESENTE_A_DISTANZA',
        ASSENTE: 'ASSENTE',
        RITARDO: 'RITARDO',
        RITARDO_BREVE: 'RITARDO_BREVE',
        USCITO: 'USCITO'
    }
        

    @classmethod
    def from_upper_str(cls, s: str) -> float:
        try:
            return cls.day_status[s.upper()]
        except KeyError:
            return 0 # Better idea in the near future would be to raise an error

    @classmethod
    def from_lower_str(cls, s: str) -> float:
        try:
            return cls.hour_status[s.lower()]
        except KeyError:
            return 0 # Better idea in the near future would be to raise an error

    @classmethod
    def to_str(cls, status: float) -> str:
        try:
            return cls.name_from_status[status]
        except KeyError:
            return 'UNKNOWN' # Better idea in the near future would be to raise an error
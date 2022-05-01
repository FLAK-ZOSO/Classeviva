class Roles:
    STUDENT = 0
    PARENT = 1
    TEACHER = 2


class NoteSortBy:
    AUTHOR = 0
    DATE = 1
    NOTE = 2
    TYPE = 3


class RegistroStatus:
    PRESENTE = 0
    ASSENTE = 1
    
    @classmethod
    def from_str(cls, s: str) -> int:
        try:
            return {
                'PL': cls.PRESENTE,
                'AL': cls.ASSENTE
            }[s.upper()]
        except KeyError:
            return 0
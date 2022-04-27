# Classeviva
Slow `API` for `Classeviva` by `GruppoSpaggiariParma`

# Download
Since `Classeviva` still isn't available on `PyPI`, you must download the content of this repository file by file.

# Tree
```
YourProject/
            ├── YourFile.py
            ├── paths.py
            ├── variables.py
            └── main.py
```

# Usage
Your `YourFile.py` could be written as follows:

```python
#!\usr\bin\env python3
from main import *


if __name__ == "__main__":
    s = Session("MyUserCode", "MyPassword", hidden=False)
    s.login()
    print(s.user)

    v = Valutazioni(s)
    print(v.subjects)
    print(v.get_valutations_marks())
    print(v.get_valutations(False, False, False))

    n = Note(s)
    print(n.get_notes(NoteSortBy.TYPE))
    print(n.lenght)

    r = Registro(s)
    print(d := r.Date.from_str("SABATO 27 APRILE 2022"))
    print(r.get_day_status(d))
```

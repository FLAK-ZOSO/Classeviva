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
from classeviva import Session, Valutazioni, Note, NoteSortBy, Registro


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
    print(d := r.Date.from_str("SABATO 31 GENNAIO 2022"))
    print(r.get_day_status(d))
    print(r.get_status(d, 1))
    print(r.get_status(d, 2))
    print(r.get_status(d, 5))
```

A sample output may be the following:

```
DevTools listening on ws://127.0.0.1:57310/devtools/browser/9946a611-eeed-425c-b830-5cbc62779de2
User: MyUserCode | MyPassword | 58733881
Time-left: 3599s
MyUserCode | MyPassword | 58733881
['SCIENZE NATURALI', 'LINGUA E CULTURA STRANIERA (INGLESE)', 'LINGUA E LETTERATURA ITALIANA', 'SCIENZE MOTORIE E SPORTIVE', 'INFORMATICA', "DISEGNO E STORIA DELL'ARTE", 'FISICA', 'MATEMATICA', 'FILOSOFIA', 'STORIA', 'EDUCAZIONE CIVICA']
[8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5, 8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5]
[('SCIENZE NATURALI', 9.5), ('SCIENZE NATURALI', 10.0), ('SCIENZE NATURALI', 9.0), ('LINGUA E CULTURA STRANIERA (INGLESE)', 7.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E LETTERATURA ITALIANA', 8.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('LINGUA E LETTERATURA ITALIANA', 7.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('SCIENZE MOTORIE E SPORTIVE', 8.0), ('SCIENZE MOTORIE E SPORTIVE', 8.5), ('INFORMATICA', 10.0), ('INFORMATICA', 10.0), ("DISEGNO E STORIA DELL'ARTE", 10.0), ("DISEGNO E STORIA DELL'ARTE", 7.0), ('FISICA', 7.0), ('FISICA', 9.5), ('FISICA', 6.0), ('FISICA', 6.5), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('FILOSOFIA', 8.0), ('STORIA', 9.0), ('STORIA', 8.5), ('STORIA', 8.5), ('EDUCAZIONE CIVICA', 8.5), ('EDUCAZIONE CIVICA', 8.0)]
[('La classe oggi 2/04/22, esce alle 11.50.', 'Qualcuno', '02-04-2022', 'Annotazione del docente'), ('Compiti di Geometria non svolti', 'Qualcun altro', '12-02-2022', 'Richiamo (Compiti)')]
2
SABATO 27 APRILE 2022
0
```

The whole run should take around `9.8s`.

# Classeviva
Slow `API` for `Classeviva` by `GruppoSpaggiariParma`

# Download
`Classeviva` isn available on [`PyPI`](https://pypi.org/project/classevivaAPI/)

```cmd
$ python -m pip install classevivaAPI
```

# Usage
Your `YourFile.py` could be written as follows:

```python
#!\usr\bin\env python3
from classeviva import Session, Valutazioni, Note, Registro
from classeviva.variables import NoteSortBy


if __name__ == "__main__":
    s = Session("S<my-username>", "<my-password>", hidden=False)
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
DevTools listening on ws://127.0.0.1:63746/devtools/browser/25500ad4-68de-4f15-b52a-08068382f340
User: S<my-username> | <my-password> | 58733881
Time-left: 3598s
S<my-username> | <my-password> | 58733881
["RELIGIONE CATTOLICA O ATTIVITA' ALTERNATIVE", 'SCIENZE NATURALI', 'LINGUA E CULTURA STRANIERA (INGLESE)', 'LINGUA E LETTERATURA ITALIANA', 'SCIENZE MOTORIE E SPORTIVE', 'INFORMATICA', "DISEGNO E STORIA DELL'ARTE", 'FISICA', 'MATEMATICA', 'FILOSOFIA', 'STORIA', 'EDUCAZIONE CIVICA']
[8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5, 8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5]
[("RELIGIONE CATTOLICA O ATTIVITA' ALTERNATIVE", 10.0), ('SCIENZE NATURALI', 10.0), ('SCIENZE NATURALI', 9.5), ('SCIENZE NATURALI', 10.0), ('LINGUA E CULTURA STRANIERA (INGLESE)', 7.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E LETTERATURA ITALIANA', 8.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('LINGUA E LETTERATURA ITALIANA', 7.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('SCIENZE MOTORIE E SPORTIVE', 9.0), ('SCIENZE MOTORIE E SPORTIVE', 8.0), ('SCIENZE MOTORIE E SPORTIVE', 8.5), ('INFORMATICA', 10.0), ("DISEGNO E STORIA DELL'ARTE", 10.0), ("DISEGNO E STORIA DELL'ARTE", 7.0), ('FISICA', 7.0), ('FISICA', 9.5), ('FISICA', 6.0), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('FILOSOFIA', 8.0), ('STORIA', 9.0), ('STORIA', 8.5), ('STORIA', 8.5), ('EDUCAZIONE CIVICA', 10.0), ('EDUCAZIONE CIVICA', 8.5)]
[('La classe oggi 2/04/22, esce alle 11.50.', 'SOMEBODY', '02-04-2022', 'Annotazione del docente'), ("La classe esce alle ore 12:45 per l'assenza della prof.ssa SOMEBODY", 'SOMEBODY', '03-05-2022', 'Annotazione del docente'), ('Compiti di Geometria non svolti', 'SOMEBODY', '12-02-2022', 'Richiamo (Compiti)')]
3
SABATO 31 GENNAIO 2022
1.0
0.2
1.0
1.0
```

The whole run should take around `9.8s`.

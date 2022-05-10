Importazioni
===============

.. code-block:: python

    from classeviva import Session, Valutazioni, Note, Registro
    from classeviva.variables import NoteSortBy

Sessione
==============
L'username deve obbligatoriamente essere sottoforma di codice (es. ``S8733890I``, ``G8733890I``), e mai sottoforma di indirizzo email.

.. code-block:: python

    if __name__ == "__main__":
        s = Session("<my-username>", "<my-password>", hidden=False)
        s.login()

``ClassevivaAPI`` riconosce il tipo di account per via dell'iniziale del codice (es. ``G8733890I`` è un genitore, ``S8733890I`` è un alunno).


Esempio
==============
Il seguente programma riassume le principali funzionalità di ``ClassevivaAPI``.

.. code-block:: python

    #!\usr\bin\env python3
    from classeviva import Session, Valutazioni, Note, Registro
    from classeviva.variables import NoteSortBy


    if __name__ == "__main__":
        s = Session("<my-username>", "<my-password>", hidden=False)
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

Alla versione ``0.2.2`` il risultato del programma in esempio eseguito con le credenziali dell'utenza di esempio è il seguente.

.. code-block:: python

    DevTools listening on ws://127.0.0.1:63746/devtools/browser/25500ad4-68de-4f15-b52a-08068382f340
    User: <my-username> | <my-password> | 58733881
    Time-left: 3598s
    <my-username> | <my-password> | 58733881
    ["RELIGIONE CATTOLICA O ATTIVITA' ALTERNATIVE", 'SCIENZE NATURALI', 'LINGUA E CULTURA STRANIERA (INGLESE)', 'LINGUA E LETTERATURA ITALIANA', 'SCIENZE MOTORIE E SPORTIVE', 'INFORMATICA', "DISEGNO E STORIA DELL'ARTE", 'FISICA', 'MATEMATICA', 'FILOSOFIA', 'STORIA', 'EDUCAZIONE CIVICA']
    [8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5, 8.0, 9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 'g', 7.0, 8.5, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0, 9.0, 8.5, 8.0, 8.0, 10.0, 10.0, 10.0, 8.0, 9.5, 9.5, 8.0, 8.5]
    [("RELIGIONE CATTOLICA O ATTIVITA' ALTERNATIVE", 10.0), ('SCIENZE NATURALI', 10.0), ('SCIENZE NATURALI', 9.5), ('SCIENZE NATURALI', 10.0), ('LINGUA E CULTURA STRANIERA (INGLESE)', 7.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E CULTURA STRANIERA (INGLESE)', 8.5), ('LINGUA E LETTERATURA ITALIANA', 8.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('LINGUA E LETTERATURA ITALIANA', 7.0), ('LINGUA E LETTERATURA ITALIANA', 8.5), ('SCIENZE MOTORIE E SPORTIVE', 9.0), ('SCIENZE MOTORIE E SPORTIVE', 8.0), ('SCIENZE MOTORIE E SPORTIVE', 8.5), ('INFORMATICA', 10.0), ("DISEGNO E STORIA DELL'ARTE", 10.0), ("DISEGNO E STORIA DELL'ARTE", 7.0), ('FISICA', 7.0), ('FISICA', 9.5), ('FISICA', 6.0), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('MATEMATICA', 9.0), ('MATEMATICA', 8.0), ('FILOSOFIA', 8.0), ('STORIA', 9.0), ('STORIA', 8.5), ('STORIA', 8.5), ('EDUCAZIONE CIVICA', 10.0), ('EDUCAZIONE CIVICA', 8.5)]
    [('La classe oggi 2/04/22, esce alle 11.50.', 'QUALCUNO', '02-04-2022', 'Annotazione del docente'), ("La classe esce alle ore 12:45 per l'assenza della prof.ssa QUALCUNO", 'QUALCUNO', '03-05-2022', 'Annotazione del docente'), ('Compiti di Geometria non svolti', 'QUALCUNO', '12-02-2022', 'Richiamo (Compiti)')]
    3
    SABATO 31 GENNAIO 2022
    1.0
    0.2
    1.0
    1.0

I dati sono stati raccolti in circa ``21`` secondi.
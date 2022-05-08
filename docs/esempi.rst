Importazioni
===============

.. code-block:: python
    from classeviva import Session, Valutazioni, Note, Registro
    from classeviva.variables import NoteSortBy

Sessione
==============
L'username deve obbligatoriamente essere sottoforma di codice (es. S8733890I, G8733890I, Vils001), e mai sottoforma di indirizzo email.

.. code-block:: python
    if __name__ == "__main__":
        s = Session("<my-username>", "<my-password>", hidden=False)
        s.login()
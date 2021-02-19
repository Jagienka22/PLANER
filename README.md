#Planner

Co to jest PLANER?
-------------

Planer jest to aplikacja do planowania wydarzeń napisana w języku `Python`. 
Aplikacja ta bazuje na bibliotece `tkinter`.
Dane są zapisywane w bazie danych mySql.

W aplikacji mamy takie funkcjonalości jak:
* dodawanie nowych wydarzeń
* modyfikowanie wydarzeń
* usuwanie wydarzeń
* Powiadomienia o wydarzeniu

Aby uruchomić aplkację należy wpisać

```
python3 kalendarz.py
```

Wymagania
------------
aby uruchomić aplikację musimy:
* stworzyć pustą bazę danych o nazwie `kalendarz`
  
* w kodzie podać prawidłowe dane do połączenia z bazą danych
* mieć zainstalowane biblioteki takie jak 
  `MySQLdb`, `tkinter`, `tkcalendar ` oraz `threading`
  
Zasada działania
------------
###Wygląd aplikacji
W oknie aplikacji po lewej stronie mamy kalendarz w którym możemy wybrać dzień.
Poniżej kalendarza znajduje się formularz oraz odpowiednie przyciski do wykonywania akcji.
Po prawej stronie znajduje się lista wydarzeń z danego dnia.

###Powiadomienie
Wraz z uruchomieniem aplikacji uruchamia się nowy wątek który o każdej pełnej minucie
sprawdza czy jakieś wydarzenie się właśnie zaczyna.
Jeśli znajdzie takie wydarzenie zostaje wyświetlone stosowne powiadomienie.

Struktura kodu
------------
###kalendarz.py
Główny plik programu. Składa się z:
* `if __name__ == "__main__":` program rozpoczyna działanie od tego warunku.
  Umieszczamy tutaj wszystkie elementy w oknie programu.
  Ustawimy wyzwalacze oraz uruchamiamy wątek sprawdzający czy jest jakieś wydarzenie
  
* `add_data()` metoda dodaje wydarzenie do bazy
* `delete_data()` metoda usuwa wydarzenie z bazy
* `modify_data()` metoda modyfikuje wydarzenie w bazie
* `get_data_from_table()` metoda pobiera dane z bazy danych i wstawia je do listy wydarzeń
* `change_date()` metoda wyzwalana po zmianie wybranej daty w kalendarzu
* `change_listbox()` metoda wyzwalana po zmianie wybranegego wydarzenia na liście


###kalendarz_thread.py
W tym pliku jest metoda od powiadomień oraz metody do wyzwalania powiadomień o nowym wydarzeniu.

###db.py
Zawiera metody do łaczenia się z bazą danych.

###db_create_table.sql
Zawiera skrypt tworzący tabelę w bazie danych.
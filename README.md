# qa_python

В данном репозитории представлен класс `BooksCollector` и тесты для проверки его функциональности. Ниже описаны тесты, сгруппированные по методам, которые они проверяют.

## Описание класса BooksCollector

Класс `BooksCollector` предназначен для работы с книгами, их жанрами и списком избранного. 

## Тесты

### `add_new_book(name)`
- **`test_add_new_book_add_two_books`**  
  Проверяет, что при добавлении двух корректных книг обе сохраняются в словаре.
- **`test_add_new_book_invalid_name`**  
  Проверяет, что при попытке добавить книгу с некорректным названием книга не добавляется.
- **`test_add_new_book_no_genre`**  
  Проверяет, что при добавлении новой книги без явного указания жанра, ей по умолчанию устанавливается пустая строка.

### `set_book_genre(name, genre)`
- **`test_set_book_genre_valid_genre`**  
  Проверка, что жанр устанавливается только в том случае, если он находится в допустимом списке жанров класса.

### `get_book_genre(name)`
- **`test_get_book_genre_valid_genre`**  
  Проверяет, что возвращается корректный жанр для книги, если он был установлен.

### `get_books_with_specific_genre(genre)`
- **`test_get_books_with_specific_genre_two_fantasy_books`**  
  Проверяет корректность фильтра книг по заданному жанру.
- **`test_get_books_with_specific_genre_no_match`**  
  Проверяет корректность фильтра книг по отсутствующему жанру.

### `get_books_genre()`
- **`test_get_books_genre_correct_filling`**  
  Проверяет, что словарь книг (`books_genre`) корректно пополняется и хранит правильные жанры, если те были установлены.

### `get_books_for_children()`
- **`test_get_books_for_children_exclude_adult_genres`**  
  Проверяет, что метод возвращает только те книги, жанры которых не находятся в списке "взрослых" жанров `genre_age_rating`.

### `add_book_in_favorites(name)`
- **`test_add_book_in_favorites_correct_filling`**  
  Проверяет, что книга корректно добавляется в список избранных и не дублируется при повторном добавлении.

### `delete_book_from_favorites(name)`
- **`test_delete_book_from_favorites_correct_delete`**  
  Проверяет, что метод корректно удаляет книгу из избранного, если она там присутствует.

### `get_list_of_favorites_books()`
- **`test_get_list_of_favorites_books_сorrect_filling`**  
  Проверяет, что в список избранных попадают только добавленные туда книги и не содержатся те, которые не были туда добавлены.

---

Запустить тесты из терминала можно командой:
```bash
pytest -v tests.py

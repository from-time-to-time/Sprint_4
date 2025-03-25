import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'invalid_name',
        [
            '',
            'TestTestTestTestTestTestTestTestTestTestTest'
        ]
    )
    def test_add_new_book_invalid_name(self, invalid_name):
        collector = BooksCollector()

        collector.add_new_book(invalid_name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')

        assert collector.get_book_genre('Война и мир') == ''

    @pytest.mark.parametrize(
        'book_name, genre_to_set, is_valid_genre',
        [
            ('Гарри Поттер', 'Фантастика', True), 
            ('Колобок', 'Сказка', False),
        ]
    )
    def test_set_book_genre_valid_genre(self, book_name, genre_to_set, is_valid_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        collector.set_book_genre(book_name, genre_to_set)

        genre_is_saved = collector.get_book_genre(book_name) != ''
        assert genre_is_saved == is_valid_genre

    @pytest.mark.parametrize(
        'title, genre',
        [
            ('Алиса в стране чудес', 'Фантастика'),
            ('Ведьмак', 'Фантастика')
        ]
    )
    def test_get_book_genre_valid_genre(self, title, genre):
        collector = BooksCollector()
        
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)

        assert collector.get_book_genre(title) == genre

    def test_get_books_with_specific_genre_two_fantasy_books(self):
        collector = BooksCollector()

        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Фантастика")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        assert len(collector.get_books_with_specific_genre("Фантастика")) == 2
            
    def test_get_books_with_specific_genre_no_match(self):
        collector = BooksCollector()

        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")

        assert len(collector.get_books_with_specific_genre("Комедии")) == 0

    def test_get_books_genre_correct_filling(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        expected_result = {
            'Мастер и Маргарита': 'Фантастика',
            'Автостопом по галактике': '',
        }

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_exclude_adult_genres(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы') 

        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла', 'Ужасы')

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_correct_filling(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Автостопом по галактике')

        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']

        collector.add_book_in_favorites('Автостопом по галактике')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс', 'Автостопом по галактике']

    def test_delete_book_from_favorites_correct_delete(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')

        collector.add_new_book('Американский психопат')
        collector.add_book_in_favorites('Американский психопат')

        collector.delete_book_from_favorites('Сияние')

        assert collector.get_list_of_favorites_books() == ['Американский психопат']

    def test_get_list_of_favorites_books_correct_filling(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.add_new_book('Американский психопат')
        collector.add_new_book('Мгла')

        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Американский психопат')

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Сияние' in favorites
        assert 'Мгла' not in favorites

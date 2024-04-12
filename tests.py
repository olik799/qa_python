import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_book_name_less_40_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_no_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_add_new_book_not_add_two_book_same_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'name',
        [
            'Странная история доктора Джекила и мистера Хайда',
            ''
        ]
    )
    def test_add_new_book_negative_add_book_lenght_not_valid(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        books_genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert books_genre == 'Фантастика'

    def test_get_books_with_specific_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(books_with_specific_genre) == 1

    def test_get_books_with_specific_genre_real_book_and_not_real_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Ну погоди!')
        collector.set_book_genre('Ну погоди!', 'Мультфильмы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(books_with_specific_genre) == 0

    def test_get_books_genre_book_in_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        book_genre = collector.get_books_genre()
        assert 'Гордость и предубеждение и зомби' in book_genre

    def test_get_books_for_children_valid_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Ну погоди!')
        collector.set_book_genre('Ну погоди!', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert 'Ну погоди!' in books_for_children

    def test_get_books_for_children_not_valid_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Граф Монте-Кристо')
        collector.set_book_genre('Граф Монте-Кристо', 'Детектив')
        books_for_children = collector.get_books_for_children()
        assert 'Граф Монте-Кристо' not in books_for_children

    def test_add_book_in_favorites_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

    def test_delete_book_from_favorites_book_delete_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites

    def test_get_list_of_favorites_books_books_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Волшебник изумрудного города')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Волшебник изумрудного города')
        list_of_favorites_books = collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби', 'Волшебник изумрудного города' in list_of_favorites_books

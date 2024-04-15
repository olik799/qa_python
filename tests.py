import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_add_book_no_genre_true(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        book_genre = collector.get_books_genre()
        assert book_genre[name] == ''

    def test_add_new_book_not_add_two_book_same_name_true(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

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
        assert name not in collector.get_books_genre()

    def test_set_book_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        date = collector.get_book_genre(name)
        assert date is not None

    def test_get_books_with_specific_genre_real_book_and_genre_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(genre)
        assert name in books_with_specific_genre

    def test_get_books_with_specific_genre_real_book_and_not_real_genre_true(self):
        collector = BooksCollector()
        name = 'Ну погоди!'
        genre = 'Мультфильмы'
        genre_compare = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(genre_compare)
        assert name not in books_with_specific_genre

    def test_get_books_genre_book_in_genre_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        date = collector.get_books_genre()
        assert date is not None

    def test_get_books_for_children_valid_genre_true(self):
        collector = BooksCollector()
        name = 'Ну погоди!'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert name in books_for_children

    def test_get_books_for_children_not_valid_genre_true(self):
        collector = BooksCollector()
        name = 'Граф Монте-Кристо'
        genre = 'Детектив'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert name not in books_for_children

    def test_add_book_in_favorites_book_in_favorites_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_delete_book_from_favorites_book_delete_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books_books_in_favorites_true(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        name1 = 'Волшебник изумрудного города'
        collector.add_new_book(name)
        collector.add_new_book(name1)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name1)
        list_of_favorites_books = collector.get_list_of_favorites_books()
        assert name, name1 in list_of_favorites_books

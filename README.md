# Финальный проект 4 спринта автоматизации
## Юнит-тесты для приложения BooksCollector
### 1. Тесты метода add_new_book - добавление книги в словарь:
##### test_add_new_book_add_book_name_less_40_true
###### книга добавляеся при валидной длине названия
##### test_add_new_book_add_book_no_genre_true
###### у новой добавленной книги жанр не задан
##### test_add_new_book_not_add_two_book_same_name_true
###### книгу можно добавить только один раз
##### test_add_new_book_negative_add_book_lenght_not_valid
###### нельзя добавить книгу с названием больше 40 символов
###### нельзя добавить книгу с названием 0 символов
### 2. Тесты метода set_book_genre
##### test_set_book_genre_real_book_and_genre_true
###### книге из словаря books_genre можно задать жанр из списка genre
### 3. Тесты метода get_book_genre
##### test_get_book_genre_real_book_and_genre_true
###### просмотр жанра книги по ее имени
### 4. Тесты метода get_books_with_specific_genre
##### test_get_books_with_specific_genre_real_book_and_genre_true
###### просмотр списка книг по определенному жанру
##### test_get_books_with_specific_genre_real_book_and_not_real_genre_true
###### если книги с указанным жанром отсутствуют - список пустой
### 5. Тесты метода get_books_genre
##### test_get_books_genre_book_in_genre_true
###### просмотр текущего словаря books_genre
### 6. Тесты метода get_books_for_children
##### test_get_books_for_children_valid_genre_true
###### просмотр книг, которые подходят детям
##### test_get_books_for_children_not_valid_genre_true
###### в список не входят книги с возрастным рейтингом
### 7. Тесты метода add_book_in_favorites
##### test_add_book_in_favorites_book_in_favorites_true
###### добавление книги в избранное
### 8. Тесты метода delete_book_from_favorites
##### test_delete_book_from_favorites_book_delete_true
###### удаление книги из избранного
### 9. Тесты метода get_list_of_favorites_books
##### test_get_list_of_favorites_books_books_in_favorites_true
###### просмотр списка избранных книг


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
long_name = 'Очень длинное название книги, которое превышает 40 символов'

class TestBooksCollector:

    def test_add_new_book_success(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение')
        # проверяем, что добавилась книга
        assert 'Гордость и предубеждение' in collector.books_genre

    def test_add_new_book_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.books_genre) == 1

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Комедии'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Неизвестный жанр')
        assert collector.get_book_genre('Гордость и предубеждение') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == ['Гордость и предубеждение']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение', '1984']

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.favorites

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение', '1984']   

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Маска")
        collector.set_book_genre("Маска", "Комедии")
        assert collector.get_book_genre("Маска") == "Комедии"

    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_get_books_genre_with_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Ужасы")
        expected = {"Книга1": "Фантастика", "Книга2": "Ужасы"}
        assert collector.get_books_genre() == expected

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
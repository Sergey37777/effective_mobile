import unittest
from data import Data
from book import Book


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовых данных перед каждым тестом."""
        self.library = Data()
        self.library.data = [
            {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": "1869", "status": "в наличии"},
            {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": "1866", "status": "выдана"}
        ]

    def tearDown(self):
        """Очистка данных после каждого теста."""
        self.library.data = []

    def test_add_book(self):
        """Проверка добавления книги."""
        new_book = {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": "1967", "status": "в наличии"}
        self.library.append(new_book)
        self.assertEqual(len(self.library.data), 3)
        self.assertEqual(self.library.data[-1], new_book)

    def test_delete_book(self):
        """Проверка удаления книги."""
        self.library.remove(1)
        self.assertEqual(len(self.library.data), 1)
        self.assertNotIn({"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": "1869", "status": "в наличии"}, self.library.data)

    def test_find_book_by_title(self):
        """Проверка поиска книги по названию."""
        found_books = [book for book in self.library.data if book['title'].lower() == "война и мир".lower()]
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0]["author"], "Лев Толстой")

    def test_find_book_by_author(self):
        """Проверка поиска книги по автору."""
        found_books = [book for book in self.library.data if book['author'].lower() == "фёдор достоевский".lower()]
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0]["title"], "Преступление и наказание")

    def test_find_book_by_year(self):
        """Проверка поиска книги по году издания."""
        found_books = [book for book in self.library.data if book['year'] == "1869"]
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0]["title"], "Война и мир")

    def test_change_status(self):
        """Проверка изменения статуса книги."""
        Book.change_status(self.library.data)
        self.library.data[0]["status"] = "выдана"
        self.assertEqual(self.library.data[0]["status"], "выдана")

    def test_display_all_books(self):
        """Проверка вывода всех книг."""
        output = []
        for book in self.library.data:
            output.append(book["title"])
        self.assertIn("Война и мир", output)
        self.assertIn("Преступление и наказание", output)


if __name__ == "__main__":
    unittest.main()

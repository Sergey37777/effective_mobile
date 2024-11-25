from typing import List, Dict


class Book:
    @staticmethod
    def generate_book_id(data: List[Dict[str, str | int]]) -> int:
        return data[-1]['id'] + 1 if data else 1

    @staticmethod
    def display_all(data: List[Dict[str, str | int]]) -> None:
        for book in data:
            print(f"ID: {book['id']}")
            print(f"Название: {book['title']}")
            print(f"Автор: {book['author']}")
            print(f"Год издания: {book['year']}")
            print(f"Статус: {book['status']}", end="\n\n")

    @staticmethod
    def add_book(data: List[Dict[str, str | int]]) -> None:
        book_id = Book.generate_book_id(data)
        title: str = input("Введите название книги: ")
        author: str = input("Введите автора книги: ")
        try:
            year: int = int(input("Введите год издания книги: "))
        except ValueError:
            print("Ошибка: Год издания должен быть числом. Пожалуйста, попробуйте снова.")
            return
        status: str = input("Введите статус книги: ")
        if status.lower() not in ["в наличии", "выдана"]:
            print("Ошибка: Статус должен быть 'в наличии' или 'выдана'.")
            return
        data.append({"id": book_id, "title": title, "author": author, "year": year, "status": status})
        print("Книга успешно добавлена!")

    @staticmethod
    def delete_book(data: List[Dict[str, str | int]]) -> None:
        try:
            book_id: int = int(input("Введите ID книги для удаления: "))
        except ValueError:
            print("Ошибка: ID должен быть числом.")
            return
        for book in data:
            if book["id"] == book_id:
                data.remove(book)
                print("Книга успешно удалена!")
                return
        print("Книга с таким ID не найдена.")

    @staticmethod
    def find_book(data: List[Dict[str, str | int]]) -> None:
        print("\nМеню поиска:")
        print("1. Искать по названию")
        print("2. Искать по автору")
        print("3. Искать по году издания")
        choice: str = input("Выберите действие: ").strip()
        if choice == "1":
            title: str = input("Введите название книги: ")
            books = [book for book in data if book['title'].lower() == title.lower()]
            if books:
                Book.display_all(books)
            else:
                print("Книга не найдена.")
        elif choice == "2":
            author: str = input("Введите автора книги: ")
            books = [book for book in data if book['author'].lower() == author.lower()]
            if books:
                Book.display_all(books)
            else:
                print("Книга не найдена.")
        elif choice == "3":
            year: int = int(input("Введите год издания книги: "))
            books = [book for book in data if book['year'] == year]
            if books:
                Book.display_all(books)
            else:
                print("Книга не найдена.")
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

    @staticmethod
    def change_status(data: List[Dict[str, str | int]]) -> None:
        book_id: int = int(input("Введите ID книги для изменения статуса: "))
        status: str = input("Введите новый статус книги: ")
        if status.lower() not in ["в наличии", "выдана"]:
            print("Ошибка: Статус должен быть 'в наличии' или 'выдана'.")
            return
        for book in data:
            if book['id'] == book_id:
                book['status'] = status
                print("Статус книги успешно изменен!")
                return
        print("Книга с таким ID не найдена.")
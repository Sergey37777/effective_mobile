from data import Data
from book import Book


def main() -> None:
    library = Data()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice: str = input("Выберите действие: ").strip()
        if choice == "1":
            Book.add_book(data=library.data)
            library.save_data()
        elif choice == "2":
            Book.delete_book(data=library.data)
            library.save_data()
        elif choice == "3":
            Book.find_book(data=library.data)
        elif choice == "4":
            Book.display_all(data=library.data)
        elif choice == "5":
            Book.change_status(data=library.data)
            library.save_data()
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
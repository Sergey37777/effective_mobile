# Тестовое задание

## Задача
Разработать консольное приложение для управления библиотекой книг. Приложение должно позволять добавлять, удалять, искать и отображать книги. Каждая книга должна содержать следующие поля:
 • id (уникальный идентификатор, генерируется автоматически)
 • title (название книги)
 • author (автор книги)
 • year (год издания)
 • status (статус книги: “в наличии”, “выдана”)

## Требования
 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

## Дополнительные требования
- Реализовать хранение данных в текстовом или json формате.
- Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
- Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
- Не использовать сторонние библиотеки.

## Структура проекта
/
    |- book.py        # Логика работы с книгами
    |- data.py        # Управление данными (загрузка, сохранение, удаление)
    |- main.py        # Точка входа в приложение
    |- data.json      # Файл для хранения данных о книгах
    |- README.md      # Описание проекта


## Запуск приложения
Для запуска приложения необходимо выполнить команду:
```bash
python3 main.py
```

## Описание функционала
При запуске приложения пользователю предлагается выбрать действие:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Отобразить все книги
5. Изменить статус книги
6. Выход

После выбора действия пользователь вводит необходимые данные. Приложение обрабатывает ввод и выводит результат операции.
После выполнения операции пользователю снова предлагается выбрать действие.
При выборе пункта "Выход" приложение завершает работу.




import json
import os
from pathlib import Path
from typing import List, TypedDict, Dict

DATA_PATH = Path(__file__).parent / 'data.json'


class Book(TypedDict):
    id: int
    title: str
    author: str
    year: int
    status: str


class Data:
    def __init__(self) -> None:
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, str | int]]:
        if not DATA_PATH.exists() or not DATA_PATH.stat().st_size > 0:
            return []

        with open(DATA_PATH, 'r') as file:
            return json.load(file)

    def save_data(self) -> None:
        data = json.dumps(self.data, indent=4, ensure_ascii=False)
        with open(DATA_PATH, 'w') as file:
            file.write(data)

    def append(self, book: Book) -> None:
        self.data.append(book)
        self.save_data()

    def remove(self, book_id: int) -> None:
        for book in self.data:
            if book["id"] == book_id:
                self.data.remove(book)
                self.save_data()
                return
        print("Книга с таким ID не найдена.")



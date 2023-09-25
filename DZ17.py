from typing import Any
import os
from datetime import datetime, timedelta

class ListManipulator:
    def __init__(self, my_list: list):
        self._my_list = my_list

    def get_length(self) -> int:
        return len(self._my_list)

    def add_element(self, element: Any) -> None:
        self._my_list.append(element)

    def remove_element(self, element: Any) -> None:
        if element in self._my_list:
            self._my_list.remove(element)
        else:
            raise ValueError(f"{element} not found in the list")

    def get_element_at_index(self, index: int) -> Any:
        if index < 0 or index >= len(self._my_list):
            raise IndexError("Index out of range")
        return self._my_list[index]

    @staticmethod
    def merge_lists(list1: list, list2: list) -> list:
        return list1 + list2

class FileManager:
    def __init__(self, file_name: str):
        self._file_name = file_name

    def read_file(self) -> str:
        try:
            with open(self._file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"

    def write_to_file(self, content: str) -> None:
        with open(self._file_name, 'w') as file:
            file.write(content)

class DateTimeManager:
    def __init__(self):
        self._current_date_time = datetime.now()

    def add_days(self, days: int) -> None:
        self._current_date_time += timedelta(days=days)

    def subtract_days(self, days: int) -> None:
        self._current_date_time -= timedelta(days=days)

    def format_date(self, format_string: str) -> str:
        return self._current_date_time.strftime(format_string)

# Примеры использования классов
if __name__ == "__main__":
    # Пример использования ListManipulator
    my_list = [1, 2, 3, 4]
    list_manipulator = ListManipulator(my_list)
    list_manipulator.add_element(5)
    list_manipulator.remove_element(2)
    print(list_manipulator.get_element_at_index(2))
    merged_list = ListManipulator.merge_lists([1, 2, 3], [4, 5, 6])
    print(merged_list)

    # Пример использования FileManager
    file_manager = FileManager("sample.txt")
    file_manager.write_to_file("Hello, World!")
    content = file_manager.read_file()
    print(content)

    # Пример использования DateTimeManager
    date_manager = DateTimeManager()
    date_manager.add_days(7)
    formatted_date = date_manager.format_date("%Y-%m-%d")
    print(formatted_date)
    date_manager.subtract_days(3)
    formatted_date = date_manager.format_date("%Y-%m-%d")
    print(formatted_date)

from typing import Dict, List, Optional


class Table:
    """Таблица, представляющая данные из CSV-файла.

    Attributes:
        data: Список строк таблицы в виде словарей.
    """

    def __init__(self, data: List[Dict[str, str]]):
        """Создаёт объект Table на основе списка словарей."""
        self.data = data

    def filter_by(self, column: str, operator: str, value: str) -> None:
        """Фильтрует строки таблицы по заданному условию.

        Args:
            column: Название колонки для фильтрации.
            operator: Оператор сравнения ('>', '<', '=').
            value: Значение, с которым сравнивается значение колонки.

        Raises:
            ValueError: Если оператор не поддерживается для текстовых данных.
        """
        if not self.data:
            return

        try:
            float(value)
            is_numeric = all(self._is_number(row[column]) for row in self.data)
        except ValueError:
            is_numeric = False

        if is_numeric:
            numeric_value = float(value)
            if operator == ">":
                self.data = [
                    row for row in self.data if float(row[column]) > numeric_value
                ]
            elif operator == "<":
                self.data = [
                    row for row in self.data if float(row[column]) < numeric_value
                ]
            elif operator == "=":
                self.data = [
                    row for row in self.data if float(row[column]) == numeric_value
                ]
        else:
            if operator == "=":
                self.data = [row for row in self.data if row[column] == value]
            else:
                raise ValueError("Only '=' operator allowed for string columns")

    def aggregate(self, column: str, func: str) -> Optional[float]:
        """Выполняет агрегацию по указанной колонке.

        Args:
            column: Название колонки, по которой выполняется агрегация.
            func: Тип агрегации. Поддерживаемые значения: 'avg', 'min', 'max'.

        Returns:
            Результат агрегации или None, если таблица пустая.

        Raises:
            ValueError: Если указана неподдерживаемая функция агрегации.
        """
        if not self.data:
            return None

        values = [float(row[column]) for row in self.data]
        if func == "avg":
            return sum(values) / len(values)
        elif func == "min":
            return min(values)
        elif func == "max":
            return max(values)
        else:
            raise ValueError(f"Unsupported aggregation function: {func}")

    @staticmethod
    def _is_number(s: str) -> bool:
        """Проверяет, является ли строка числом."""
        try:
            float(s)
            return True
        except ValueError:
            return False

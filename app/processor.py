import csv

from app.table import Table


class CSVProcessor:
    """Процессор для чтения CSV-файлов и преобразования их в объекты Table."""

    def read_csv(self, file_path: str) -> Table:
        """Читает CSV-файл и возвращает данные в виде объекта Table.

        Args:
            file_path: Путь к CSV-файлу.

        Returns:
            Объект Table, содержащий данные из файла.

        Raises:
            FileNotFoundError: Если файл не найден.
            csv.Error: Если возникла ошибка при чтении CSV.
        """
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return Table(list(reader))

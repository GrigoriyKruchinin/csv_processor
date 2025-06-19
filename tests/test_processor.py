from app.processor import CSVProcessor


def test_read_csv(tmp_path):
    """Проверяет, что read_csv() корректно читает CSV-файл
    и возвращает объект Table.

    Тест:
        1. Создаёт временный CSV-файл с данными
        2. Читает файл через CSVProcessor.read_csv()
        3. Проверяет количество строк и значения в таблице
    """
    csv_content = """name,brand
item1,apple
item2,banana"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    processor = CSVProcessor()
    table = processor.read_csv(str(csv_file))

    assert len(table.data) == 2
    assert table.data[0]["name"] == "item1"
    assert table.data[1]["brand"] == "banana"

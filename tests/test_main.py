from unittest.mock import MagicMock, patch


@patch("app.cli.parse_args")
@patch("app.processor.CSVProcessor.read_csv")
def test_main_no_aggregate(mock_read, mock_args):
    """Проверяет, что main() выводит таблицу при отсутствии агрегации."""
    mock_args.return_value = MagicMock(file="fake.csv", where=None, aggregate=None)

    mock_table = MagicMock()
    mock_table.data = [{"name": "item1", "price": "100"}]
    mock_read.return_value = mock_table

    with patch("builtins.print") as mock_print:
        from app.main import main

        main()
        assert mock_print.called


@patch("app.cli.parse_args")
@patch("app.processor.CSVProcessor.read_csv")
def test_main_with_filter_and_output(mock_read, mock_args):
    """Проверяет, что main() выводит таблицу после фильтрации."""
    mock_args.return_value = MagicMock(
        file="fake.csv", where="price > 150", aggregate=None
    )

    mock_table = MagicMock()
    mock_table.data = [{"name": "item2", "price": "200"}]
    mock_read.return_value = mock_table

    with patch("builtins.print") as mock_print:
        from app.main import main

        main()
        assert mock_print.called

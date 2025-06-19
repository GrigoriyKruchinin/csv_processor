import pytest

from app.cli import parse_args


def test_full_args(monkeypatch):
    """Проверяет корректный парсинг всех аргументов командной строки."""
    monkeypatch.setattr(
        "sys.argv",
        [
            "prog",
            "--file",
            "examples/products.csv",
            "--where",
            "price > 200",
            "--aggregate",
            "price=avg",
        ],
    )
    args = parse_args()
    assert args.file == "examples/products.csv"
    assert args.where == "price > 200"
    assert args.aggregate == "price=avg"


def test_required_file_missing(monkeypatch):
    """
    Проверяет, что отсутствие обязательного аргумента '--file'
    вызывает SystemExit.
    """
    monkeypatch.setattr("sys.argv", ["prog"])
    with pytest.raises(SystemExit):
        parse_args()

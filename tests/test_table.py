import pytest

from app.table import Table


@pytest.fixture
def sample_data():
    """Фикстура с предзаполненной таблицей для тестирования."""
    return Table(
        [
            {"name": "item1", "price": "100", "rating": "4.5"},
            {"name": "item2", "price": "200", "rating": "4.7"},
            {"name": "item3", "price": "300", "rating": "4.3"},
        ]
    )


@pytest.fixture
def empty_table():
    """Фикстура с пустой таблицей для тестирования граничных случаев."""
    return Table([])


def test_filter_numeric_gt(sample_data):
    """Проверяет фильтрацию по числовому полю с оператором '>'."""
    sample_data.filter_by("price", ">", "150")
    assert len(sample_data.data) == 2


def test_filter_numeric_eq(sample_data):
    """Проверяет фильтрацию по числовому полю с оператором '='."""
    sample_data.filter_by("price", "=", "200")
    assert len(sample_data.data) == 1


def test_filter_string_eq(sample_data):
    """Проверяет фильтрацию по текстовому полю с оператором '='."""
    sample_data.filter_by("name", "=", "item2")
    assert len(sample_data.data) == 1


def test_filter_on_empty_table(empty_table):
    """Проверяет поведение filter_by() на пустой таблице."""
    empty_table.filter_by("price", ">", "100")
    assert len(empty_table.data) == 0


def test_filter_non_numeric_column_with_gt():
    """
    Проверяет, что попытка использовать '>' к текстовой колонке
    вызывает ValueError.
    """
    table = Table([{"name": "a"}, {"name": "b"}])
    with pytest.raises(ValueError):
        table.filter_by("name", ">", "x")


def test_aggregate_avg(sample_data):
    """Проверяет агрегацию avg (среднее значение)."""
    avg = sample_data.aggregate("price", "avg")
    assert avg == 200.0


def test_aggregate_min(sample_data):
    """Проверяет агрегацию min (минимальное значение)."""
    minimum = sample_data.aggregate("price", "min")
    assert minimum == 100.0


def test_aggregate_max(sample_data):
    """Проверяет агрегацию max (максимальное значение)."""
    maximum = sample_data.aggregate("price", "max")
    assert maximum == 300.0


def test_aggregate_empty_table(empty_table):
    """Проверяет агрегацию avg на пустой таблице — возвращает None."""
    result = empty_table.aggregate("price", "avg")
    assert result is None


def test_aggregate_unsupported_func(sample_data):
    """Проверяет, что неизвестная функция агрегации вызывает ValueError."""
    with pytest.raises(ValueError):
        sample_data.aggregate("price", "sum")

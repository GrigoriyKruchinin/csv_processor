# CSV Processor

CLI-утилита для фильтрации и агрегации данных из CSV-файлов.

## Что использовалось

- **Python 3.13** — современная версия Python с поддержкой аннотаций типов и улучшенной работой с модулями.
- **uv** — быстрый менеджер пакетов и зависимостей (альтернатива `pip` + `venv`).
- **pytest** — фреймворк для написания юнит-тестов.
- **tabulate** — красивый вывод таблиц в консоль.
- **ruff** — проверка стиля кода и линтера `pre-commit`.
- **GitHub Actions** — автоматический запуск линтера и тестов при пуше/PR.
- **pre-commit-config.yaml** — для автоматического форматирования и проверки кода до коммита.

## Установка

Убедитесь, что установлен [uv](https://github.com/astral-sh/uv):

```bash
# Установка uv (если не установлен)
pip install uv
```

Установите зависимости:

```bash
uv sync --no-install-project
```

## Как запустить

1. Сделайте скрипт исполняемым:

```bash
chmod +x run_tests.sh
```

2. Запустите скрипт:

```bash
./run_tests.sh
```

> Этот скрипт:
> - Установит зависимости
> - Запустит тесты
> - Выведет результаты работы программы

Вывод покажет результаты и покрытие тестами, а так же примеры использования программы (см. папку `screenshots/`):

```
Тестирование CLI интерфейса:
Все устройства дороже 500:
2025-06-19 20:52:46,443 - INFO - Чтение файла: examples/products.csv
2025-06-19 20:52:46,443 - INFO - Фильтрация: price > 500
2025-06-19 20:52:46,443 - INFO - Вывод данных в формате таблицы:
+------------------+---------+---------+----------+
| name             | brand   |   price |   rating |
|------------------+---------+---------+----------|
| iphone 15 pro    | apple   |     999 |      4.9 |
| galaxy s23 ultra | samsung |    1199 |      4.8 |
| iphone 14        | apple   |     799 |      4.7 |
| galaxy z flip 5  | samsung |     999 |      4.6 |
| iphone 13 mini   | apple   |     599 |      4.5 |
+------------------+---------+---------+----------+
Все устройства Xiaomi:
2025-06-19 20:52:46,580 - INFO - Чтение файла: examples/products.csv
2025-06-19 20:52:46,581 - INFO - Фильтрация: brand = xiaomi
2025-06-19 20:52:46,581 - INFO - Вывод данных в формате таблицы:
+---------------+---------+---------+----------+
| name          | brand   |   price |   rating |
|---------------+---------+---------+----------|
| redmi note 12 | xiaomi  |     199 |      4.6 |
| poco x5 pro   | xiaomi  |     299 |      4.4 |
| redmi 10c     | xiaomi  |     149 |      4.1 |
+---------------+---------+---------+----------+
Средняя цена всех устройств:
2025-06-19 20:52:46,738 - INFO - Чтение файла: examples/products.csv
2025-06-19 20:52:46,738 - INFO - Агрегация: AVG по колонке 'price'
2025-06-19 20:52:46,738 - INFO - AVG of price: 602.00
Средняя цена устройств Apple:
2025-06-19 20:52:46,900 - INFO - Чтение файла: examples/products.csv
2025-06-19 20:52:46,900 - INFO - Фильтрация: brand = apple
2025-06-19 20:52:46,901 - INFO - Агрегация: AVG по колонке 'price'
2025-06-19 20:52:46,901 - INFO - AVG of price: 706.50
```

## Ручной запуск тестов

Запуск всех тестов:

```bash
uv run pytest tests/
```

С отчётом о покрытии:

```bash
uv run pytest --cov=app tests/
```

## Примеры использования

Вот 10 примеров команд, которые можно использовать:

```bash
# 1. Фильтрация: все устройства дороже 500$
uv run python -m app.main --file examples/products.csv --where "price > 500"

# 2. Агрегация: средняя цена устройств Xiaomi
uv run python -m app.main --file examples/products.csv --where "brand = xiaomi" --aggregate "price=avg"

# 3. Фильтрация: все устройства Apple
uv run python -m app.main --file examples/products.csv --where "brand = apple"

# 4. Агрегация: максимальный рейтинг среди Samsung
uv run python -m app.main --file examples/products.csv --where "brand = samsung" --aggregate "rating=max"

# 5. Фильтрация: устройства с рейтингом выше 4.5
uv run python -m app.main --file examples/products.csv --where "rating > 4.5"

# 6. Фильтрация: устройства с названием "iphone se"
uv run python -m app.main --file examples/products.csv --where "name = iphone se"

# 7. Агрегация: самая дешёвая модель Xiaomi
uv run python -m app.main --file examples/products.csv --where "brand = xiaomi" --aggregate "price=min"

# 8. Фильтрация: все устройства дешевле 200$
uv run python -m app.main --file examples/products.csv --where "price < 200"
```

В том числе обработка ошибок:

```bash
# 9. Ошибка: попытка агрегировать строковое поле
uv run python -m app.main --file examples/products.csv --aggregate "brand=avg"

# 10. Ошибка: файл не найден
uv run python -m app.main --file nonexistent.csv`
```

## CI/CD

В проекте есть workflow `.github/workflows/ci.yml`, который:
- Запускает линтер и тесты при каждом `push` и `pull request`

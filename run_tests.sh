#!/bin/bash

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Запуск скрипта для тестирования CSV Processor${NC}"

# Проверяем, установлен ли uv
if ! command -v uv &> /dev/null
then
    echo "Ошибка: 'uv' не установлен. Установите его с https://github.com/astral-sh/uv"
    exit 1
fi

echo -e "${BLUE}Установка зависимостей...${NC}"
uv sync --no-install-project > /dev/null 2>&1

echo -e "${BLUE}Запуск юнит-тестов и генерация HTML-отчёта покрытия кода...${NC}"
uv run pytest --cov=app --cov-report=html tests/
echo -e "${GREEN}HTML-отчёт доступен в htmlcov/index.html${NC}"

echo -e "${BLUE}Тестирование CLI интерфейса:${NC}"

# Пример 1: Фильтрация по цене
echo -e "${GREEN}Все устройства дороже 500:${NC}"
uv run python -m app.main --file examples/products.csv --where "price > 500"

# Пример 2: Фильтр по бренду
echo -e "${GREEN}Все устройства Xiaomi:${NC}"
uv run python -m app.main --file examples/products.csv --where "brand = xiaomi"

# Пример 3: Агрегация — средняя цена
echo -e "${GREEN}Средняя цена всех устройств:${NC}"
uv run python -m app.main --file examples/products.csv --aggregate "price=avg"

# Пример 4: Фильтр + агрегация — средняя цена Apple
echo -e "${GREEN}Средняя цена устройств Apple:${NC}"
uv run python -m app.main --file examples/products.csv --where "brand = apple" --aggregate "price=avg"

echo -e "${BLUE}Все тесты и примеры выполнены!${NC}"

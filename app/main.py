import logging

from tabulate import tabulate

from app.cli import parse_args
from app.processor import CSVProcessor

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    """Основная функция приложения для обработки CSV-файлов.

    Поддерживает:
        - Фильтрацию (--where "column>value")
        - Агрегацию (--aggregate "column=avg|min|max")
    """
    args = parse_args()
    processor = CSVProcessor()

    try:
        logger.info(f"Чтение файла: {args.file}")
        table = processor.read_csv(args.file)

        if args.where:
            column, op, value = args.where.split()
            logger.info(f"Фильтрация: {column} {op} {value}")
            table.filter_by(column.strip(), op.strip(), value.strip())

        if args.aggregate:
            column, func = args.aggregate.split("=")
            logger.info(f"Агрегация: {func.upper()} по колонке '{column}'")
            result = table.aggregate(column.strip(), func.strip())
            if result is not None:
                logger.info(f"{func.upper()} of {column}: {result:.2f}")
        else:
            logger.info("Вывод данных в формате таблицы:")
            print(tabulate(table.data, headers="keys", tablefmt="psql"))

    except Exception as e:
        logger.error(f"Ошибка выполнения: {e}", exc_info=True)


if __name__ == "__main__":
    main()

import argparse


def parse_args(args=None):
    """Парсит аргументы командной строки.

    Args:
        args (Optional[List[str]]): Список аргументов для парсинга.
            Если None, используются sys.argv.

    Returns:
        argparse.Namespace: Объект с распарсенными аргументами.

    Пример:
        >>> parse_args(['--file', 'data.csv', '--where', 'price > 200'])
        Namespace(file='data.csv', where='price > 200', aggregate=None)
    """
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("--file", required=True, help="Path to CSV file")
    parser.add_argument("--where", help="Filter condition like 'column>value'")
    parser.add_argument("--aggregate", help="Aggregation like 'column=avg'")
    return parser.parse_args(args)

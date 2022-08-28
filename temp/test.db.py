import sqlite3

create_table = """
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
text TEXT NOT NULL
);
"""

create_quotes = """
INSERT INTO
quotes (author,text)
VALUES
('Rick Cook', 'Программирование сегодня — это гонка разработчиков программ...'),
('Waldi Ravens', 'Программирование на С похоже на быстрые танцы на только...');
"""

# Подключение в БД
connection = sqlite3.connect("test.db")

# Создаем cursor, он позволяет делать SQL-запросы
cursor = connection.cursor()

# Выполняем запрос:
cursor.execute(create_table)

# Фиксируем выполнение(транзакцию)
connection.commit()

# Закрыть курсор:
cursor.close()

# Закрыть соединение:
connection.close()

def get_all_quotes():
    # Подключение в БД
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    select_quotes = "SELECT * from quotes"
    cursor.execute(select_quotes)
    quotes_db = cursor.fetchall()
    cursor.close()
    quotes = []
    keys = ["id", "author", "text"]
    for quote_db in quotes_db:
        quote = dict(zip(keys, quote_db))
        quotes.append(quote)
    return quotes
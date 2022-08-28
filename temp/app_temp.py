import random
from flask import Flask, abort, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

quotes = [
    {
        "id": 1,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 2,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
    },
    {
        "id": 3,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
        "id": 4,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. На практике это не так."
    },
]


# Сериализация: list --> str
@app.route("/quotes")
def get_all_quotes():
    return quotes


@app.route("/quotes/filter")
def get_quotes_filter():
    args = request.args
    print(args)
    # TODO: закончить реализацию
    return {}


@app.route("/quotes/count")
def quote_counts():
    return {
        "count": len(quotes)
    }


# dict --> str
@app.route("/quotes/random")
def random_quote():
    return random.choice(quotes)


@app.route("/quotes/<int:id>")
def get_quote(id):
    for quote in quotes:
        if quote["id"] == id:
            return quote

    abort(404, f"Quote with id={id} not found")


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/about", methods=['GET'])
def about():
    author_info = {
        "name": "Евгений!",
        "surname": "Юрченко",
        "email": "yurchenko@spacialist.ru",
    }
    return author_info


# @app.route("/quotes", methods=['POST'])
# def create_quote():
#     new_quote = request.json
#     # print(type(new_quote))
#     last_id = quotes[-1]["id"]
#     new_quote["id"] = last_id + 1
#     quotes.append(new_quote)
#     return new_quote, 201
@app.post("/quotes")
def create_quote():
    new_quote = request.json
    last_id = quotes[-1]["id"]
    new_quote["id"] = last_id + 1
    new_quote["rating"] = 1
    quotes.append(new_quote)
    return new_quote, 201


@app.put("/quote/<int:quote_id>")
def edit_quote(quote_id):
    new_data = request.json
    for quote in quotes:
        if quote["id"] == quote_id:
            quote.update(new_data)
            return quote, 200
    abort(404, f"Указанного id= {quote_id}, не существует")


@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
    for quote in quotes:
        if id == quote['id']:
            quotes.remove(quote)
            return f"Quote with id {id} is deleted.", 200
    abort(404, f"Указанного id= {id}, не существует")


if __name__ == "__main__":
    app.run(debug=True)

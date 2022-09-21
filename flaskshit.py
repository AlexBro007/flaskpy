from flask import Flask, abort, request
from req import get_weather, city_id, apikey
from datetime import datetime
from news_list import all_news

app = Flask(__name__)

@app.route("/")
def index():
    weather = get_weather(city_id, apikey)
    cur_date = datetime.now().strftime("%d.%m.%Y")
    print(cur_date)

    response = '<p><b>temperature:</b> %s</p>' % weather['main']['temp']
    response += "<p><b>city:</b> %s</p>" % weather['name']
    response += "<p><b>date:</b> %s</p>" % cur_date
    return response


@app.route("/news")
def all_the_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get("limit"))
    except:
        limit = 10
    color = request.args.get("color") if request.args.get('color') in colors else "black"

    return "<h1 style='color: %s'>News: <small>%s</small></h1>" % (color, limit)


@app.route("/news/<int:news_id>")
def newd_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = "<h1>%(title)s</h1><p><i>current date time is: %(current_date_time)s</i></p><p>%(text)s</p>"
        result = result % news_to_show[0]
        return result
    else:
        abort(404)



if __name__ == "__main__":
    app.run(port=5001)


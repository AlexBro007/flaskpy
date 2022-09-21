from datetime import datetime

cur_date = datetime.now().strftime("%d.%m.%Y")

all_news = [
    {
        'id': 1,
        'title': 'putin xyecoc obyavil mobilizaciyu',
        'text': 'ne nu a che, u nego matb sdohla',
        'date': '2022-09-21',
    },
    {
        'id': 2,
        'title': 'putin ebanaya shavka',
        'text': 'ne nu a che, ebuchiy sumashedshiy ded',
        'date': '2022-09-2122',
    },
    {
        'id': 3,
        'title': 'putler - eblan',
        'text': 'ne nu a che epta blyat3333',
        'date': '2022-09-21333',
    },
]

for aboba in all_news:
    counter = aboba.get("date")
    aboba.update({"current_date_time": cur_date})
    print(f'{aboba.get("current_date_time")}')

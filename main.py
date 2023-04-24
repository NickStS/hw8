import datetime


def get_birthdays_per_week(users):
    weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    today = datetime.date.today()

    start = today - datetime.timedelta(days=today.weekday())
    end = start + datetime.timedelta(days=6)

    birthday_week = {day: [] for day in weekdays.values()}

    for user in users:
        if start <= user['birthday'].date().replace(year=today.year) <= end:
            if user['birthday'].weekday() in (5, 6):
                birthday_week['Monday'].append(user['name'])
            else:
                day_week = weekdays[user['birthday'].weekday()]
                birthday_week[day_week].append(user['name'])

    for day, names in birthday_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {'name': 'usr1', 'birthday': datetime.datetime(2000, 4, 24)},
    {'name': 'usr2', 'birthday': datetime.datetime(2000, 4, 25)},
    {'name': 'usr3', 'birthday': datetime.datetime(2000, 4, 26)},
    {'name': 'usr4', 'birthday': datetime.datetime(2000, 4, 27)},
    {'name': 'usr5', 'birthday': datetime.datetime(2000, 4, 28)},
    {'name': 'usr6', 'birthday': datetime.datetime(2000, 4, 29)},
    {'name': 'usr7', 'birthday': datetime.datetime(2000, 4, 30)},
    {'name': 'usr8', 'birthday': datetime.datetime(2000, 5, 1)},
    {'name': 'usr9', 'birthday': datetime.datetime(2000, 5, 2)},
    {'name': 'usr10', 'birthday': datetime.datetime(2000, 5, 3)},
    {'name': 'usr11', 'birthday': datetime.datetime(2000, 5, 4)},
    {'name': 'usr12', 'birthday': datetime.datetime(2000, 5, 5)},
    {'name': 'usr14', 'birthday': datetime.datetime(2000, 5, 7)},
    {'name': 'usr15', 'birthday': datetime.datetime(2000, 5, 8)},
]

get_birthdays_per_week(users)

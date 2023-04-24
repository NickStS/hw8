import datetime


def get_birthdays_per_week(users):
    today = datetime.date.today()

    if today.weekday() == 0:
        smallest_diff = -2
    else:
        smallest_diff = 0

    largest_diff = 4

    birthday_week = {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}

    if today.weekday() == 0:
        saturday = today - datetime.timedelta(days=2)
        sunday = today - datetime.timedelta(days=1)
        for user in users:
            if user['birthday'].month == sunday.month and user['birthday'].day == sunday.day:
                birthday_week['Monday'].append(user['name'])
            elif user['birthday'].month == saturday.month and user['birthday'].day == saturday.day:
                birthday_week['Monday'].append(user['name'])

    for user in users:
        bday = user['birthday'].replace(year=today.year)

        if bday < today:
            bday = bday.replace(year=today.year + 1)

        diff = (bday - today).days

        if smallest_diff <= diff <= largest_diff:
            day = bday.strftime('%A')
            if day in birthday_week:
                birthday_week[day].append(user['name'])

    for day, names in birthday_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {'name': 'usr1', 'birthday': datetime.date(2023, 4, 21)},
    {'name': 'usr2', 'birthday': datetime.date(2023, 4, 22)},
    {'name': 'usr3', 'birthday': datetime.date(2023, 4, 23)},
    {'name': 'usr4', 'birthday': datetime.date(2023, 4, 24)},
    {'name': 'usr5', 'birthday': datetime.date(2023, 4, 25)},
    {'name': 'usr6', 'birthday': datetime.date(2023, 4, 26)},
    {'name': 'usr7', 'birthday': datetime.date(2023, 4, 27)},
    {'name': 'usr8', 'birthday': datetime.date(2023, 4, 28)},
    {'name': 'usr9', 'birthday': datetime.date(2023, 4, 29)},
    {'name': 'usr10', 'birthday': datetime.date(2023, 4, 30)},
    {'name': 'usr11', 'birthday': datetime.date(2023, 5, 1)},
    {'name': 'usr12', 'birthday': datetime.date(2023, 5, 2)},
    {'name': 'usr13', 'birthday': datetime.date(2023, 5, 3)},
    {'name': 'usr14', 'birthday': datetime.date(2023, 5, 4)},
    {'name': 'usr15', 'birthday': datetime.date(2023, 5, 5)},
]

get_birthdays_per_week(users)

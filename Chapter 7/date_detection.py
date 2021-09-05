import re

def date_detector(text):
    date_pattern = re.compile('''
    ([12][0-9]|3[0-1]|0?[1-9])
    ([./-])
    (1[0-2]|0?[1-9])
    ([./-])
    (2?1?[0-9][0-9][0-9])
    ''', re.VERBOSE)

    days = []
    months = []
    years = []
    dates = []
    for date in date_pattern.findall(text):
        days.append(int(date[0]))
        months.append(int(date[2]))
        years.append(int(date[4]))

    for num in range(len(days)):
        if months[num] not in (2, 4, 6, 9, 11):
            dates.append([days[num], months[num], years[num]])

        elif days[num] < 31 and months[num] in (4, 6, 9, 11):
            dates.append([days[num], months[num], years[num]])

        elif months[num] == 2 and days[num] == 29:
            if years[num] % 4 == 0:
                if years[num] % 100 == 0:
                    if years[num] % 400 == 0:
                        dates.append([days[num], months[num], years[num]])

        elif months[num] == 2 and days[num] < 29:
            dates.append([days[num], months[num], years[num]])

        if len(dates) > 0:
            for date in dates:
                print(date)

data = '30-06-2012, 31-12-2012, 15-02-2002, 29-02-2004, 29-02-2002, 31-02-2004, 31-06-2012'

date_detector(data)
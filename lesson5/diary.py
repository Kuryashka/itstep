tasks = {
    'Monday': ['meeting at 5', 'meeting at 6'],
    'Tuesday': ['meeting at 4', 'meeting at 7'],
    'Wednesday': ['meeting at 6', 'meeting at 9'],
    'Thursday': ['meeting at 5', 'meeting at 7'],
    'Friday': ['meeting at 4', 'meeting at 6'],
    'Saturday': ['meeting at 7', 'meeting at 8'],
    'Sunday': ['meeting at 6', 'meeting at 9'],
}
days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}


def update(day, task):
    return tasks.update({day: task})


def get_task(day):
    return tasks.get(day)


while True:
    try:
        try:
            a = int(input('Enter the day (e.g Monday): '))
        except ValueError:
            a = str(input('Enter the day (e.g Monday): '))
        if isinstance(a, int):
            if a in days.keys():
                a = days.get(a)
                if a in tasks:
                    break
        elif isinstance(a, str):
            a = a.capitalize()
            if a in tasks:
                break
    except:
        pass

print(str(get_task(a)))
from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)
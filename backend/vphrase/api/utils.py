import datetime

def years_range():
    return [(year,year) for year in range(1984,datetime.date.today().year + 1)]
def current_year(): 
    return datetime.date.today().year
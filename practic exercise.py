import datetime

def check_day_of_week(day):

    if day == 1:
        return "понеділок"

    elif day == 2:
        return"вівторок"

    elif day == 3:
        return"середа"

    elif day == 4:
        return"четверг"

    elif day == 5:
        return"пятниця"

    elif day == 6:
        return"субота"

    elif day == 7:
        return"неділя"

    else:
        return"невірна дата тижня"

    day_now = datetime.date.today()
    day = day_now.isoweekday()

    print(f"дата: {day_now} - день: {check_day_of_week(day)}")

check_day_of_week()

#Завдання 1
def days_until_new_year(new_year_date):
    today = datetime.date.today()
    next_new_year = new_year_date.replace( year = today.year +1 , mounth = 1  ,day = 1)

    return (next_new_year - today).days

new_year_date = datetime.date(2025,1,1)
print(f"до нового року залишилось{days_until_new_year(new_year_date)}днів")

days_until_new_year()

#Завдання 2

def calculate_lived_time(birth_date):


        birth_date = datetime.strptime(birth_date, )

        current_date = datetime.now()

        time_difference = current_date - birth_date

        days = time_difference.days

        total_seconds = time_difference.total_seconds()

        hours = int(total_seconds // 3600)

        minutes = int(total_seconds // 60)

        seconds = int(total_seconds)

        return {"days": days,"hours": hours,"minutes": minutes,"seconds": seconds}

birth_date_input = input("Введіть вашу дату народження (у форматі YYYY-MM-DD): ")
result = calculate_lived_time(birth_date_input)
if isinstance(result, dict):
    print(
        f"Ви прожили: {result['days']} днів, {result['hours']} годин, {result['minutes']} хвилин, {result['seconds']} секунд.")
else:
    print(result)

calculate_lived_time()

#Завдання 3

def calculate_age(birth_date):


    current_date = datetime.now().date()


    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day


    if days < 0:
        months -= 1
        previous_month = (current_date.month - 1) % 12 or 12
        previous_year = current_date.year if previous_month != 12 else current_date.year - 1
        days += (datetime(previous_year, previous_month + 1, 1) - datetime(previous_year, previous_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days



birth_date = datetime(1990, 5, 15).date()
age = calculate_age(birth_date)
print("Вік:", age[0], "років,", age[1], "місяців,", age[2], "днів.")

calculate_age()































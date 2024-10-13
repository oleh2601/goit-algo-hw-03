import datetime


def get_days_from_today(date):
    try:
        #converting user's string to datetime class as YYYY-MM-DD 
        #and eliminating time since we don't need it as per task
        user_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        #getting the current date
        current_date = datetime.date.today()

        #subtracting the user's date from the current date
        #and returning the timedelta object's attribute "days"
    
        return (current_date - user_date).days
    
    #handling wrong format of input as per task
    except ValueError as e:
        return "Invalid date format"



#data entry, example from the task
date= '2020-10-09'

#using the function 
result = get_days_from_today(date)

#output test
#print(result)


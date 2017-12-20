""" Give a user date of Birth, this app will calculate the amount of days that
 remain untill the user's next birthday"""
import datetime

def title():
    """
        Function used to build the title of the app
    """
    print("--------------------------------------")
    print("            BIRTHDAY APP              ")
    print("--------------------------------------\n")

def get_bday():
    """
    Returns the obtained birth date from the user input in day/month/year
    """
    return input("Please enter your birth date in the following format (DD/MM/YYYY): ").split("/")

def get_this_year_bday(bday):
    """
    Returns the date of the birthday based on the current year
        :param bday: the birth date of the user
    """
    return datetime.date(datetime.date.today().year, int(bday[1]), int(bday[0]))

def display_bday_msg(days):
    """
    Displays a birthday message based on the days between the user birth date and today's date
        :param days: difference between the birthday and the current day
    """
    if days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        if days == 0:
            print("Happy birthday!!!")
        else:
            print("Your birthday was {} days ago this year.".format(-days))

def birthday_calculator():
    """
    Main script that runs the secuense for the application functionality
    """
    title()
    bday = get_bday()
    current_bday = get_this_year_bday(bday)
    remaining_days = current_bday - datetime.date.today()
    display_bday_msg(remaining_days.days)

birthday_calculator()

#Armin Darabi Mahboub

from datetime import date

def main():
    """Required variables"""
    current_time = date.today()

    """Input"""
    userDate = list(input().split("/"))
    #Cheking if the userDate is valid or not, if it's not valid, stop progress
    if not (Validation_Check(userDate, current_time)):
        return

    """Class"""
    class person:
        def __init__(self, year, month, day):
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
        def birthday(self):
            current_age = current_time.year - self.year - 1
            if (current_time.month <= self.month):
                if (current_time.day <= self.day):
                    current_age += 1
            return current_age

    """calculation"""
    user = person(userDate[0], userDate[1], userDate[2])

    """Output"""
    print(user.birthday())

#This func, checks the user's input date to see if it's valid or not
def Validation_Check(userDate, current_time):
    #Year
    if (int(userDate[0]) > current_time.year):
        #user's birth year cannot be more than current year
        print("WRONG")
        return False
    if (int(userDate[0]) < 0):
        #uesr's birth year cannot be less than zero
        print("WRONG")
        return False

    #Month
    if (int(userDate[1]) > 12 or int(userDate[1]) <= 0):
        #user's birth month cannot be more than 12 or less than zero
        print("WRONG")
        return False

    #Day
    if (int(userDate[2]) > 31 or int(userDate[2]) <= 0):
        #user's birth day cannot be less than 1 or more than 31
        print("WRONG")
        return False
    
    return True

if __name__ == "__main__":
    main()
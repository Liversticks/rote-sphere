from datetime import datetime
from pytz import timezone
import operator 

class dataStruct():  
  def __init__(self, uid, username, password, dayscore, monthscore, yearscore):
    self.uid = uid
    self.username = username
    self.password = password
    self.dayscore = dayscore
    self.monthscore = monthscore
    self.yearscore = yearscore
    self.daywater = []
    self.monthwater = []
    self.yearwater = []
    self.daypower = []
    self.monthpower = []
    self.yearpower = []
    self.day = 0
    self.month = 0
    self.year = 0

def updateStruct(userid, userstruct, dailywater, dailypower):
  if userstruct.uid != userid:
    return 

  # Storing current date into variables
  # https://stackoverflow.com/a/32490661
  timeNow = datetime.now(timezone('America/Vancouver'))
  currentDay = int(timeNow.strftime('%d'))
  currentMonth = int(timeNow.strftime('%m'))
  currentYear = int(timeNow.strftime('%Y'))

  # If the month has changed, clear previous month's daily data list
  if (userstruct.month != currentMonth):
    userstruct.month = currentMonth
    userstruct.daywater.clear()
    userstruct.daypower.clear()
  
  # If the year has changed, clear previous year's monthly data list
  if (userstruct.year != currentYear):
    userstruct.year = currentYear
    userstruct.monthwater.clear()
    userstruct.monthpower.clear()

  # Update current day, append first daily item
  if (userstruct.day != currentDay):
    userstruct.day = currentDay
    userstruct.daywater.append(dailywater) #imagine that we have real data
    userstruct.daypower.append(dailypower) #see notes above on daywater

    # Special Case: No elements to remove on the first day of each month
    if (currentDay != 1):
      userstruct.monthwater.pop()
      userstruct.monthpower.pop()

    userstruct.monthwater.append(monthlywater)
    userstruct.monthpower.append(monthlypower)

    # Yearly usage appended to on a daily basis, remove previous count and update with new one
    if (currentDay != 1 or currentMonth != 1):
      userstruct.yearwater.pop()
      userstruct.yearpower.pop()
      
    userstruct.yearwater.append(yearlywater)
    userstruct.yearpower.append(yearlypower)

  # Daily usage may be updated several times a day, remove previous count
  # and update with new one if a value is updated within the same day
  else:
    userstruct.daywater.pop()
    userstruct.daywater.append(dailywater)

    # Will pop previous value regardless of the date (even if it's the 1st of the month)
    # because going into this portion of code implies that the struct has already been
    # updated earlier in the day, so data must be popped regardless
    userstruct.monthwater.pop()
    userstruct.monthwater.append(monthlywater)

    # Same logic as above; pops yearly value and replaces with new data.
    userstruct.yearwater.pop()
    userstruct.yearwater.append(yearlywater)

  monthlywater = sum(userstruct.daywater) #sum up all the daywater values we have to get monthly water usage so far
  yearlywater = sum(userstruct.monthwater) #sum up all monthly values to get yearly values
  monthlypower = sum(userstruct.daypower)
  yearlypower = sum(userstruct.monthpower) 
  
  tempdayscore = dailywater + dailypower #may change formula later
  userstruct.dayscore = tempdayscore
  tempmonthscore = monthlywater + monthlypower 
  userstruct.monthscore = tempmonthscore
  tempyearscore = yearlywater + yearlypower 
  userstruct.yearscore = tempyearscore
  return

def main():
  dayscoreboard = []
  monthscoreboard = []
  yearscoreboard = []
  #simplified users for development, change for production 
  userx = dataStruct(1, 'user1', 'pw1', None, None, None)
  usery = dataStruct(2, 'user2', 'pw2', None, None, None)
  userz = dataStruct(3, 'user3', 'pw3', None, None, None)
  
  #assume that we have sensor data 
  dailywaterx = 1 
  dailypowerx = 1
  
  dailywatery = 2
  dailypowery = 2

  dailywaterz = 3 
  dailypowerz = 3

  #assume that there is a trigger for when to update data and who to update
  updateStruct(1, userx, dailywaterx, dailypowerx)
  updateStruct(2, usery, dailywatery, dailypowery)
  updateStruct(3, userz, dailywaterz, dailypowerz)
  
  #create + sort leaderboards
  userslist = [userx, usery, userz]
  dayscoreboard = sorted(userslist, key=operator.attrgetter('dayscore'))
  monthcoreboard = sorted(userslist, key=operator.attrgetter('monthscore'))
  yearscoreboard = sorted(userslist, key=operator.attrgetter('yearscore'))
  
  #print dayscoreboard[0].username, dayscoreboard[0].dayscore

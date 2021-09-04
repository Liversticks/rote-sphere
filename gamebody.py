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

  userstruct.daywater.append(dailywater) #imagine that we have real data
  monthlywater = sum(userstruct.daywater) #sum up all the daywater values we have to get monthly water usage so far
  # If the data is updated daily, then the monthly usage would also be appended daily, so pop the last element
  # of the monthly list before adding the new, currently updated value
  if (currentDay != 1):
    userstruct.monthwater.pop()
  userstruct.monthwater.append(monthlywater)
  yearlywater = sum(userstruct.monthwater) #sum up all monthly values to get yearly values
  # Yearly usage appended to on a daily basis, remove previous count and update with new one
  if (currentDay != 1 and currentMonth != 1):
    userstruct.yearwater.pop()
  userstruct.yearwater.append(yearlywater)
  
  userstruct.daypower.append(dailypower) #see notes above on daywater
  monthlypower = sum(userstruct.daypower)
  if (currentDay != 1):
    userstruct.monthpower.pop()
  userstruct.monthpower.append(monthlypower)
  yearlypower = sum(userstruct.monthpower) 
  if (currentDay != 1 and currentMonth != 1):
    userstruct.yearpower.pop()
  userstruct.yearpower.append(yearlypower)
  
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

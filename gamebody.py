from datetime import datetime
from pytz import timezone

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

def updateStruct(userid, userstruct, dailywater, dailypower):
  if userstruct.uid != userid:
    return 
  
  userstruct.daywater.append(dailywater) #imagine that we have real data 
  monthlywater = sum(userstruct.daywater) #sum up all the daywater values we have to get monthly water usage so far
  userstruct.monthwater.append(monthlywater)
  yearlywater = sum(monthwater) #sum up all monthly values to get yearly values
  userstruct.yearwater.append(yearlywater)
  
  userstruct.daypower.append(dailypower) #see notes above on daywater
  monthlypower = sum(userstruct.daypower)
  userstruct.monthpower.append(monthlypower)
  yearlypower = sum(userstruct.monthpower) 
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
  userx = dataStruct(1, user1, pw1, None, None, None)
  usery = dataStruct(2, user2, pw2, None, None, None)
  userz = dataStruct(3, user3, pw3, None, None, None)
  
  #assume that there is a trigger for when to update data and who to update
  dailywater = 1 
  dailypower = 1
  updateStruct(1, userx, dailywater, dailypower)
  
  

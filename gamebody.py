from datetime import datetime
from pytz import timezone

class dataStruct():  
  def __init__(self, uid, dayscore, monthscore, yearscore):
    self.uid = uid
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
  yearlywater = sum(monthwater) 
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
  

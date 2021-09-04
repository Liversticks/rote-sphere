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
  yearlywater = sum(monthwater)
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
  

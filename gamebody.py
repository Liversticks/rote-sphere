from datetime import datetime
from pytz import timezone

class dataStruct():  
  def __init__(self, uid, dayscore, monthscore, yearscore, daywater, monthwater, yearwater, daypower, monthpower, yearpower):
    self.uid = uid
    self.dayscore = dayscore 
    self.monthscore = monthscore
    self.yearscore = yearscore
    self.daywater = daywater
    self.monthwater = monthwater
    self.yearwater = yearwater
    self.daypower = daypower
    self.monthpower = monthpower
    self.yearpower = yearpower

def assigntostruct(userid,userstruct):
  if userstruct.uid != userid:
    return 
  dailywater = 1 #imagine that we have real data
  userstruct.daywater = dailywater
  monthlywater = 2 #if we had real data, we would sum up all the days' data up until now
  userstruct.monthwater = monthlywater
  yearlywater = 3 #if we had real data, we would sum up all the months' data up until now
  userstruct.yearwater = yearlywater
  
  dailypower = 1 #see above notes on dailywater
  userstruct.daypower = dailypower
  monthlypower = 2 
  userstruct.monthpower = monthlypower
  yearlypower = 3 
  userstruct.yearpower = yearlypower
  
  tempdayscore = dailywater + dailypower #may change formula later
  userstruct.dayscore = tempdayscore
  tempmonthscore = monthlywater + monthlypower 
  userstruct.monthscore = tempmonthscore
  tempyearscore = yearlywater + yearlypower 
  userstruct.yearscore = tempyearscore
  return
    
def main():
  

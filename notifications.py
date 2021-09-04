import gamebody

def checkUsage(userid, userstruct, dailyWater, dailyPower):
    if userstruct.uid != userid:
        return

    # Storing current date into variables
    # https://stackoverflow.com/a/32490661
    timeNow = datetime.now(timezone('America/Vancouver'))
    currentDay = int(timeNow.strftime('%d'))

    # Sum daily values from the beginning of the month until the day before the
    # current day to find the average usage of previous days for comparison
    averageDayWater = int(sum(userstruct.daywater[0:currentDay-1])/(currentDay-1))
    averageDayPower = int(sum(userstruct.daypower[0:currentDay-1])/(currentDay-1))

    # Water Usage
    waterPercentDiff = int((float(dailyWater/averageDayWater) - 1)*100)

    # Case 1: Significant drop in water usage (e.g. over 20% less)
    # Energy usage is dropping significantly, congratulate the user!
    if (waterPercentDiff <= -20):
        print("Congrats! Your water usage today has decreased by ", (-1)*waterPercentDiff, "%",
        " compared to your daily average this month.")

    # Case 2: Significant rise in water usage (e.g. over 20% more)
    # Energy usage is rising significantly, inform them to check appliances!
    elif (waterPercentDiff >= 20):
        print("Yikes! Your water usage today has increased by ", waterPercentDiff, "%",
        "compared to your daily average this month. Check your toilet and sink sensors!")

    # Case 3: Consistent energy usage
    # Energy usage is consistent, tell the user to keep up the good work!
    else:
        print("Nice work! Your water usage has been consistent today compared to your daily average this month.")

    # Power Usage
    powerPercentDiff = int((float(dailyPower/averageDayPower) - 1)*100)

    # Case 1: Significant drop in water usage (e.g. over 20% less)
    # Energy usage is dropping significantly, congratulate the user!
    if (powerPercentDiff <= -20):
        print("Congrats! Your power usage today has decreased by ", (-1)*powerPercentDiff, "%",
        " compared to your daily average this month.")

    # Case 2: Significant rise in water usage (e.g. over 20% more)
    # Energy usage is rising significantly, inform them to check appliances!
    elif (powerPercentDiff >= 20):
        print("Yikes! Your power usage today has increased by ", powerPercentDiff, "%",
        "compared to your daily average this month. Check your stove and computer sensors!")

    # Case 3: Consistent energy usage
    # Energy usage is consistent, tell the user to keep up the good work!
    else:
        print("Nice work! Your power usage has been consistent today compared to your daily average this month.")


def main():
    # Taken from gamebody.py
    userx = dataStruct(1, 'user1', 'pw1', None, None, None)
    usery = dataStruct(2, 'user2', 'pw2', None, None, None)
    userz = dataStruct(3, 'user3', 'pw3', None, None, None)

    timeNow = datetime.now(timezone('America/Vancouver'))
    currentDay = int(timeNow.strftime('%d'))
    
    # Use arbitrary values for now
    # User X: Significant decrease in energy usage
    dailywaterx = 246
    dailypowerx = 232

    # User Y: Consistent usage
    dailywatery = 296
    dailypowery = 254

    # User Z: Significant increase in energy usage
    dailywaterz = 634
    dailypowerz = 304

    updateStruct(1, userx, dailywaterx, dailypowerx)
    updateStruct(2, usery, dailywatery, dailypowery)
    updateStruct(3, userz, dailywaterz, dailypowerz)

    checkUsage(1, userx, dailywaterx, dailypowerx)
    checkUsage(2, usery, dailywatery, dailypowery)
    checkUsage(3, userz, dailywaterz, dailypowerz)
import gamebody
import time
import random

def checkUsage(userid, userstruct):
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

    random.seed()
    index = random.randint(0,4)

    # Water Usage
    waterPercentDiff = int((float(userstruct.dailywatertotal/averageDayWater) - 1)*100)

    # Dictionary to store appliances as keys with tips/suggestions as values
    waterApps = {
        "sink": "Check your sink pipes for potential leaks!",
        "toilet": "Check your toilet pipes for potential leaks!",
        "bath": "You can cut down on your water usage by taking a shower instead!",
        "hose": "Did you know that watering in the morning is a more effective use of your water?",
        "washing machine": "You can cut down on your water usage by using cooler water. Wash less frequently, but with fuller loads!"
    }

    # Access key of the dictionary - https://stackoverflow.com/a/53311468
    waterAppliance = [key for key in waterApps.keys()][index]

    # Case 1: Significant drop in water usage (e.g. over 20% less)
    # Energy usage is dropping significantly, congratulate the user!
    if (waterPercentDiff <= -20):
        print("Congrats! Your water usage today has decreased by", (-1)*waterPercentDiff, "%",
        "compared to your daily average this month. Keep up the awesome work!")

    # Case 2: Significant rise in water usage (e.g. over 20% more)
    # Energy usage is rising significantly, inform them to check appliances!
    elif (waterPercentDiff >= 20):
        print("Yikes! Your water usage today has increased by", waterPercentDiff, "%",
        "compared to your daily average this month.")
        print("During this period, your", waterAppliance, "usage skyrocketed!")
        print("POWERUP!", waterApps[waterAppliance]) 

    # Case 3: Consistent energy usage
    # Energy usage is consistent, tell the user to keep up the good work!
    else:
        print("Nice work! Your water usage has been consistent today compared to your daily average this month.")

    # Power Usage
    powerPercentDiff = int((float(userstruct.dailypowertotal/averageDayPower) - 1)*100)

    # Dictionary to store appliances as keys with tips/suggestions as values
    powerApps = {
        "oven": "You can save energy by using your oven less frequently, but in larger batches! A good alternative would be a microwave.",
        "stove": "Did you know that you can improve your energy score by using a pressure cooker or slow cooker instead?",
        "lights": "Seems like you're turning the lights on during the day! Natural light is good for you, so get on opening your curtains or blinds!",
        "thermostat": "Your temperature is currently set near the extremes! You can reduce your energy use by gradually adjusting your thermostat towards the middle.",
        "electronics": "Are you leaving your electronics plugged in when not in use? Save energy by unplugging them, and curb phantom power use!"
    }

    # Access key of the dictionary - https://stackoverflow.com/a/53311468
    powerAppliance = [key for key in powerApps.keys()][index]

    # Case 1: Significant drop in water usage (e.g. over 20% less)
    # Energy usage is dropping significantly, congratulate the user!
    if (powerPercentDiff <= -20):
        print("Congrats! Your power usage today has decreased by", (-1)*powerPercentDiff, "%",
        "compared to your daily average this month. Keep up the awesome work!")

    # Case 2: Significant rise in water usage (e.g. over 20% more)
    # Energy usage is rising significantly, inform them to check appliances!
    elif (powerPercentDiff >= 20):
        print("Yikes! Your power usage today has increased by", powerPercentDiff, "%",
        "compared to your daily average this month.")
        print("During this period, your", powerAppliance, "usage skyrocketed!")
        print("POWERUP!", powerApps[powerAppliance]) 

    # Case 3: Consistent energy usage
    # Energy usage is consistent, tell the user to keep up the good work!
    else:
        print("Nice work! Your power usage has been consistent today compared to your daily average this month.")


def municipalAlerts():
    # Format based on outage alerts from:
    # https://www.bchydro.com/power-outages/app/outage-map.html
    # https://outages.fortisbc.com/Outages

    # Random selection of cities as a sample
    cities = ["Kelowna, BC", "Hope, BC", "Coldstream, BC", "Lumby, BC", "Prince George, BC"]
    causes = ["wildfires", "thunderstorms", "heavy winds"]

    random.seed()

    # Used code idea from sensors file to determine whether a theoretical power outage occurs
    outage = random.randint(0,1)

    if outage:
        outCity = cities[random.randint(0,4)]
        outCause = causes[random.randint(0,2)]
        hours = random.randint(1, 24)
        print("POWER OUTAGE ALERT: A power outage is currrently affecting certain residential areas of", outCity, "as a result of", outCause)
        print("Outage expected to last for", hours, "more hours. Please exercise caution!")    


def main():
    # Taken from gamebody.py
    userx = dataStruct(1, 'user1', 'pw1', None, None, None)
    usery = dataStruct(2, 'user2', 'pw2', None, None, None)
    userz = dataStruct(3, 'user3', 'pw3', None, None, None)

    timeNow = datetime.now(timezone('America/Vancouver'))
    currentDay = int(timeNow.strftime('%d'))

    # Assume structs have already been updated with data
    # updateStruct(1, userx, dailywaterx, dailypowerx)
    # updateStruct(2, usery, dailywatery, dailypowery)
    # updateStruct(3, userz, dailywaterz, dailypowerz)
    
    # Use arbitrary values for now
    # User X: Significant decrease in energy usage
    userx.dailywatertotal = 246
    userx.dailypowertotal = 232

    # User Y: Consistent usage
    usery.dailywatertotal = 296
    usery.dailypowertotal = 254

    # User Z: Significant increase in energy usage
    userz.dailywatertotal = 634
    userz.dailypowertotal = 304

    # Checks are assumed to be made daily; should add an option
    # to grab data and sleep for a day after each notification/summary message
    checkUsage(1, userx)
    checkUsage(2, usery)
    checkUsage(3, userz)

    municipalAlerts()
    municipalAlerts()
import uuid
import random
import time
from datetime import datetime
from pytz import timezone
import json

class sensor():  
  def __init__(self, uid, type_, resource, address, unit, street, city, country, zippostcode):
    self.uid = uid
    self.type = type_
    self.resource = resource
    self.address = address
    self.unit = unit
    self.street = street
    self.city = city
    self.country = country 
    self.zippostcode = zippostcode
    
class sensorData():
  def __init__(self, uid, datetime, water, power):
  self.uid = uid
  self.datetime = datetime
  self.water = water
  self.power = power
    
    
tester1 = sensor(uuid.uuid4(), 'Computer', 'Power', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()

while True: 
  #avg computer wattage is 60 - 250 watts, so ill pick 200 as a rounder number, meaning it uses at most 0.2 kWh per hour. unfortunate choice of value. 
  hoursused = random.randint(0, 16) / 2
  powerused = hoursused * 0.2
  waterused = 0
  package = sensorData(tester1.uid, datetime.now(timezone('America/Vancouver')), waterused, powerused)
  jsonStr = json.dumps(package.__dict__)
  time.sleep(28800) #8 hours

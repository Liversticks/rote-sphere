import uuid
import random
import time
from datetime import datetime
from pytz import timezone
import json
import requests

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
  def __init__(self, linked_sensor, day, water, power):
    self.linked_sensor = linked_sensor
    self.day = day
    self.water = water
    self.power = power
    
    
tester1 = sensor(str(uuid.uuid4()), 'Computer', 'Power', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()
endpt = 'localhost:8000/game/usage/'

while True: 
  #avg computer wattage is 60 - 250 watts, so ill pick 200 as a rounder number, meaning it uses at most 0.2 kWh per hour. unfortunate choice of value. 
  hoursused = random.randint(0, 16) / 2
  powerused = hoursused * 0.2
  waterused = 0
  package = sensorData(tester1.uid, str(datetime.now(timezone('America/Vancouver'))), waterused, powerused)
  jsonStr = json.dumps(package.__dict__)
  requests.post(url = endpt, data = jsonStr)
  time.sleep(28800) #8 hours

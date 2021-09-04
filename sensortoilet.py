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
    
    
tester1 = sensor(str(uuid.uuid4()), 'Toilet', 'Water', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()
endpt = 'localhost:8000/game/usage/'

while True: 
  isused = random.randint(0,1)
  if isused: 
    #avg toilet is about 9.8 L/flush, i put lower bound a bit lower to account for low water use toilets
    #then i set the upper bound at 10 flushes/hour bc i think thats about the most you could expect for a reasonable household per toilet
    waterused = random.randint(1,10) * 9
  else: 
    waterused = 0
  powerused = 0
  package = sensorData(tester1.uid, str(datetime.now(timezone('America/Vancouver'))), waterused, powerused)
  jsonStr = json.dumps(package.__dict__)
  requests.post(url = endpt, data = jsonStr)
  time.sleep(3600)

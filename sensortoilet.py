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
  def __init__(self, uid, datetime_, water, power):
  self.uid = uid
  self.datetime = datetime
  self.water = water
  self.power = power
    
    
tester1 = sensor(uuid.uuid4(), 'Toilet', 'Water', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()

while True: 
  isused = random.randint(0,1)
  if isused: 
    #avg toilet is about 9.8 L/flush, i put lower bound a bit lower to account for low water use toilets
    #then i set the upper bound at 10 flushes/hour bc i think thats about the most you could expect for a reasonable household per toilet
    waterused = random.randint(1,10) * 9
  else: 
    waterused = 0
  powerused = 0
  package = sensorData(tester1.uid, datetime.now(timezone('America/Vancouver')), waterused, powerused)
  jsonStr = json.dumps(package.__dict__)
  time.sleep(3600)
